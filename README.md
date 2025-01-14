# Project for AUG classes
Converts an input in mixed kana and kanji notation into romaji (latin notation)

### The project utilizes:
- Python, PLY (Python Lex-Yacc) library and Kakasi library

### The lexer splits the input into tokens: 
HIRAGANA, KATAKANA, KANJI (based on the japanese notation)\
and PUNCTUATION (which includes punctuation and numbers)

### The parser is a top-down parser checks the tokens and for:
- Hiragana and Katakana is converted via a map of kana to romaji and performs additional operations when dealing with small characters  (eg. small tsu, sylable accenting; small ya yu yo, replaces the vowel sound of the kana into ya; small vowels, used in words of foreign origin)
- Kanji is converted to romaji using the kakasi library since each kanji has multiple spellings and sounds, which change based on factors like the appearing next to other kanji
- Punctuation is copied with no modifications

## Update 
_smaller_ - Tokens contain singular hiragana/katakana
### Changes:
 - Lexer
   - Tokens now contain only one kana
   - Added separate token for small kana  (ゃ, ゅ, ょ) for both Hiragana & Katakana
   - Added separate token for small tsu (っ)
   - Added separate token for long sound in Katakana (ー)
- Parser (Due to changes in tokenization)
  -  Added methods for parsing each type of kana, using small tsu (syllable accenting), using small kana, long sound
  -  Modified the starting method sentence - consisting of 1 or many elements (words, punctuation, numbers)
