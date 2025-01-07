import ply.lex as lex
tokens = (
    'HIRAGANA',
    'KATAKANA',
    'KANJI',
    'PUNCTUATION'
)

t_HIRAGANA = r'[\u3040-\u309F]+'
t_KATAKANA = r'[\u30A0-\u30FF]+'
t_KANJI = r'[\u4E00-\u9FAF]+'
t_PUNCTUATION = r'[\u3000-\u303f|\uff00-\uff1f]'

t_ignore = ' \t\n'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()