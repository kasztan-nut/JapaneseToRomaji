# Project for AUG classes
Converts an input in mixed kana and kanji notation into romaji (latin notation)

### The project utilizes Python, PLY (Python Lex-Yacc) library and Kakasi library

### The lexer splits the input into tokens: 
HIRAGANA, KATAKANA, KANJI (based on the japanese notation)\
and PUNCTUATION (which includes punctuation and numbers)

### The parser is a top-down parser checks the tokens and for:
- Hiragana and Katakana is converted via a map of kana to romaji and performs additional operations when dealing with small characters  (eg. small tsu, which puts emphasis on the next kana; small ya, replaces the vowel sound of the kana into ya)
- Kanji is converted to romaji using the kakasi library since each kanji has multiple spellings and sounds, which change based on factors like the appearing next to other kanji
- Punctuation is copied with no modifications
