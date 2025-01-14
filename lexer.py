import ply.lex as lex
tokens = (
    'HIRAGANA',
    'KATAKANA',
    'KANJI',
    'SMALL_HIRAGANA',
    'SMALL_KATAKANA',
    'SMALL_K_VOWEL',
    'TSU_HIRAGANA',
    'TSU_KATAKANA',
    'LONG_KATAKANA',
    'PUNCTUATION'
)

t_HIRAGANA = r'[\u3042|\u3044|\u3046|\u3048|\u304A-\u3062|\u3064-\u3082|\u3084|\u3086|\u3088-\u308D|\u308F-\u309F]'
t_KATAKANA = r'[\u30A2|\u30A4|\u30A6|\u30A8|\u30AA-\u30C2|\u30C4-\u30E2|\u30E4|\u30E6|\u30E8-\u30ED|\u30EF-\u30FB|\u30FD-\u30FF]'
t_KANJI = r'[\u4E00-\u9FAF]+'
t_SMALL_HIRAGANA = r'[\u3083|\u3085|\u3087]'
t_SMALL_KATAKANA = r'[\u30E3|\u30E5|\u30E7]'
t_SMALL_K_VOWEL = r'[\u30A1|\u30A3|\u30A5|\u30A7|\u30A9]'
t_TSU_HIRAGANA = r'\u3063'
t_TSU_KATAKANA = r'\u30C3'
t_LONG_KATAKANA = r'\u30FC'

# Numbers & Punctuation
t_PUNCTUATION = r'[\u3000-\u303f|\uff00-\uff1f|\uff61|\uffee]+'


t_ignore = ' \t\n'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()