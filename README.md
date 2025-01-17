# Updated JapanaeseToRomaji 
This project utilizes Python, PLY (Python Lex-Yacc) and PyKakasi library

The goal of the project is to create a parser and grammar that is close to representing all input in mixed hiragana and katakana as well as kanji into romaji (latin notation - converted into the latin alphabet)

## Changes from previous version
- Reduced the amount of code by changing the structure of ```H_word``` and ```K_word``` which consist of a ```H_element```/```K_element``` or ```TSU_HIRAGANA H_element```/```TSU_KATAKANA K_element```
- ```H_element```/```K_element``` now consist of only ```H_first```/```K_first```

## Foreword
In order to understand what the program does it is necessary to understand the basic rules of the Japanese alphabets.
In Japanese:
- Each Kana (Hiragana & Katakana) represents a syllable
- Katakana is used for writing words of foreign origin and for this reason it has additional kana which aren't present in Hiragana
- The sound of a kana can be modified in different ways
    - Using the small tsu denotes which syllable should be emphasized - っき or ッキ becomes kki
        - this is denoted by repeating the first letter of the syllable
        - any word cannot start with this character
    - Using the small kana i.e. ゃ(ya), ゅ(yu), ょ(yo), ャ(ya), ュ(yu), ョ(yo) the sound of every syllable ending in i is modified
        - this is denoted by replacing the i with the corresponding small kana
        - there are exceptions such as shi and chi which when a small kana is placed in front of them the i sound only takes the vowel sound a, u or o
        - Katakana has an additional: デュ(dyu)
    - In Katakana there also exist small vowels ァ(a), ィ(i) , ゥ(u), ェ(e), ォ(o)
        - these serve a similar purpose as small ya, yu, yo but there only exist these combinations:
            - fa, fi, fe, fo - ファ, フィ, フェ, フォ
            - she, je, che - シェ, ジェ, チェ
            - tse, tsa, tso - ツェ, ツァ, ツォ
            - ti, di - ティ, ディ
    - Katakana also has a special symbol (ー) which describes that the syllable will be extended i.e. ハー is read as haa
- Kanji has multiple readings depending on whether the Kanji is by itself or written beside another Kanji
    - Due to the high complexity of Kanji readings, in order to obtain the latin notation of a Kanji phrase, the PyKakasi library is used

## How the Program works
### Lexer
The lexer splits the input into tokens:
- ```HIRAGANA``` - All full sized Hiragana
- ```KATAKANA``` - All full sized Katakana
- ```KANJI``` - All Kanji
- ```SMALL_HIRAGANA``` - Small Hiragana: ゃ(ya), ゅ(yu), ょ(yo)
- ```SMALL_KATAKANA``` - Small Katakana: ャ(ya), ュ(yu), ョ(yo)
- ```SMALL_K_VOWEL``` - Small Katakana vowels: ァ(a), ィ(i) , ゥ(u), ェ(e), ォ(o)
- ```TSU_HIRAGANA``` - Small Tsu Hiragana: っ(tsu)
- ```TSU_KATAKANA``` - Small Tsu Hiragana: ッ(tsu)
- ```LONG_KATAKANA```- Long Symbol Katakana: ー
- ```SPECIAL``` - Numbers and Punctuation

### Parser
The parser checks the tokens and processes them:
- The ```p_sentence``` and ```p_sentence_kana``` describe how the words are created and ensures that they do not start with a small tsu tokens: ```TSU_HIRAGANA``` and ```SMALL_KATAKANA``` by using ```H_first``` and ```K_first```
    - if either ```TSU_HIRAGANA``` or ```SMALL_KATAKANA``` tokens are found at the start of the word then the corresponding error method is called: ```p_h_small_tsu_error``` and ```p_k_small_tsu_error```
- The ```p_sentence``` and ```p_sentence_kana``` ensure that the words written in Hiragana and Katakana do not start with the small tsu by using ```H_first``` and ```K_first```, which describe all possible combinations of kana that do not start with the small tsu
- If the word consists of more than one kana then ```p_word_hiragana``` or ```p_word_katakana``` method is called, which can invoke: 
    - For Hiragana:
        - ```p_first_hiragana``` - Describing single Hiragana, which may be followed by small kana
    - For Katakana:
        - ```p_first_katakana``` - Describing single Katakana, that may be followed by a Long Symbol
        - ```p_first_small_katakana``` - Describing single Katakana followed by small kana, that may also be followed by a Long Symbol
        - ```p_first_s_vowel_katakana``` - Describing single Katakana followed by small vowel, that may also be followed by a Long Symbol
- If the word consists of more than one kana and this kana is to be emphasized then ```p_word_tsu_hiragana``` or ```p_word_tsu_katakana``` is called:
    - These methods perform the same function as ```p_word_hiragana``` or ```p_word_katakana``` but with a preceding small tsu: っ or ッ
- Kanji is converted into romaji using the pykakasi library due to the complexity of reading Kanji
    - it is converted into romaji using the Hepburn notation, which is the most common latin notation of japanese words
- ```SPECIAL``` characters are copied from the input without modifications 
