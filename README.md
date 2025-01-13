# Updated version of the JapaneseToRomaji program
_smaller_ - Tokens contain singular hiragana/katakana
## Changes compared to original
 - Lexer
   - Tokens now contain only one kana
   - Added separate token for small kana  (ゃ, ゅ, ょ) for both Hiragana & Katakana
   - Added separate token for small tsu (っ)
   - Added separate token for long sound in Katakana (ー)
- Parser (Due to changes in tokenization)
  -  Added methods for parsing each type of kana, using small tsu (syllable accenting), using small kana, long sound
  -  Modified the starting method sentence - consisting of 1 or many elements (words, punctuation, numbers)
