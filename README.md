# JapaneseToRomaji - Project for AUG classes
This project utilizes Python, PLY (Python Lex-Yacc) and PyKakasi library

The goal of the project is to create a parser and grammar that is close to representing all input in mixed hiragana and katakana as well as kanji into romaji (latin notation - converted into the latin alphabet)

## Foreword
In order to understand what the program does it is necessary to understand the basic rules of the Japanese alphabets.
In Japanese:
- Each Kana (Hiragana & Katakana) represents a syllable
- Katakana is used for writing words of foreign origin and for this reason it has additional kana which aren't present in Hiragana
- The sound of a kana can be modified in different ways
    - Using the small tsu denotes which syllable should be emphasized
        - this is denoted by repeating the first letter of the syllable
        - any word cannot start with this character
    - Using the small kana i.e. ya, yu, yo the sound of every syllable ending in i is modified
        - this is denoted by replacing the i with the corresponding small kana
        - there are exceptions such as shi and chi which when a small kana is placed in front of them the i sound only takes the vowel sound a, u or o
        - Katakana has an additional: dyu
    - In Katakana there also exist small vowels a, i, u, e, o
        - these serve a similar purpose as small ya, yu, yo but there only exist these combinations:
            - fa, fi, fe, fo
            - she, je, che
            - tse, tsa, tso
            - ti, di
    - Katakana also has a special symbol (--) which describes that the syllable will be extended i.e. (ha-) is read as haa
- Kanji has multiple readings depending on whether the Kanji is by itself or written beside another Kanji
    - Due to the high complexity of Kanji readings, in order to obtain the latin notation of a Kanji phrase, the PyKakasi library is used

## How the Program works
### Lexer
The lexer splits the input into tokens:
- ```HIRAGANA``` - All full sized Hiragana
- ```KATAKANA``` - All full sized Katakana
- ```KANJI``` - All Kanji
- ```SMALL_HIRAGANA``` - Small Hiragana: (ya), (yu), (yo)
- ```SMALL_KATAKANA``` - Small Katakana: (ya), (yu), (yo)
- ```SMALL_K_VOWEL``` - Small Katakana vowels: (a), (i) , (u), (e), (o)
- ```TSU_HIRAGANA``` - Small Tsu Hiragana: (tsu)
- ```TSU_KATAKANA``` - Small Tsu Hiragana: (tsu)
- ```LONG_KATAKANA```- Long Symbol Katakana: --
- ```SPECIAL``` - Numbers and Punctuation

### Parser
The parser checks the tokens and processes them:
- The ```p_sentence``` and ```p_sentence_kana``` describe how the words are created and ensures that they do not start with a small tsu tokens: ```TSU_HIRAGANA``` and ```SMALL_KATAKANA```
    - if either ```TSU_HIRAGANA``` or ```SMALL_KATAKANA``` tokens are found at the start of the word then the corresponding error method is called: ```p_h_small_tsu_error``` and ```p_k_small_tsu_error```
- The ```p_sentence``` and ```p_sentence_kana``` ensure that the words written in Hiragana and Katakana do not start with the small tsu by using ```H_first``` and ```K_first```, which describe all possible combinations of kana that do not start with the small tsu
- If the word consists of more than one kana then ```p_word_hiragana``` or ```p_word_katakana``` method is called, which can invoke: 
    - For Hiragana:
        - ```p_element_hiragana``` - Describing Hiragana, with or without preceding small tsu
        - ```p_small_hiragana``` - Describing Hiragana followed by small kana, with or without a preceding small tsu
    - For Katakana:
        - ```p_element_katakana``` - Describing Katakana, with or without preceding small tsu
        - ```p_small_katakana``` - Describing Katakana followed by small kana, with or without a preceding small tsu
        - ```p_s_vowel_katakana``` -Describing Katakana followed by small vowel, with or without a preceding small tsu
        - ```p_long_katakana``` - similar to ```p_element_katakana``` but also followed by the Long Symbol
        - ```p_small_long_katakana``` - similar to ```p_small_katakana``` but also followed by the Long Symbol
        - ```p_s_vowel_long_katakana``` - similar to ```p_s_vowel_katakana``` but also followed by the Long Symbol
- Kanji is converted into romaji using the pykakasi library due to the complexity of reading Kanji
    - it is converted into romaji using the Hepburn notation, which is the most common latin notation of japanese words
- ```SPECIAL``` characters are copied from the input without modifications 
