import ply.yacc as yacc
import pykakasi
from lexer import tokens

kakasi = pykakasi.Kakasi()

# Dictionary - Hiragana into Romaji
hiragana_to_romaji = {
    'あ': "a", 'い': "i", 'う': "u", 'え': "e", 'お': "o",
    'か': "ka", 'き': "ki", 'く': "ku", 'け': "ke", 'こ': "ko",
    'さ': "sa", 'し': "shi", 'す': "su", 'せ': "se", 'そ': "so",
    'た': "ta", 'ち': "chi", 'つ': "tsu", 'て': "te", 'と': "to",
    'な': "na", 'に': "ni", 'ぬ': "nu", 'ね': "ne", 'の': "no",
    'は': "ha", 'ひ': "hi", 'ふ': "fu", 'へ': "he", 'ほ': "ho",
    'ま': "ma", 'み': "mi", 'む': "mu", 'め': "me", 'も': "mo",
    'や': "ya", 'ゆ': "yu", 'よ': "yo",
    'ら': "ra", 'り': "ri", 'る': "ru", 'れ': "re", 'ろ': "ro",
    'わ': "wa", 'を': "wo", 'ん': "n",
    'が': "ga", 'ぎ': "gi", 'ぐ': "gu", 'げ': "ge", 'ご': "go",
    'ざ': "za", 'じ': "ji", 'ず': "zu", 'ぜ': "ze", 'ぞ': "zo",
    'だ': "da", 'ぢ': "ji", 'づ': "zu", 'で': "de", 'ど': "do",
    'ば': "ba", 'び': "bi", 'ぶ': "bu", 'べ': "be", 'ぼ': "bo",
    'ぱ': "pa", 'ぴ': "pi", 'ぷ': "pu", 'ぺ': "pe", 'ぽ': "po",
    # Small characters
    'ぁ': "a", 'ぃ': "i", 'ぅ': "u", 'ぇ': "e", 'ぉ': "o",
    'ゃ': "ya", 'ゅ': "yu", 'ょ': "yo", 'っ': "",
}

# Dictionary - Katakana into Romaji
katakana_to_romaji = {
    'ア': "a", 'イ': "i", 'ウ': "u", 'エ': "e", 'オ': "o",
    'カ': "ka", 'キ': "ki", 'ク': "ku", 'ケ': "ke", 'コ': "ko",
    'サ': "sa", 'シ': "shi", 'ス': "su", 'セ': "se", 'ソ': "so",
    'タ': "ta", 'チ': "chi", 'ツ': "tsu", 'テ': "te", 'ト': "to",
    'ナ': "na", 'ニ': "ni", 'ヌ': "nu", 'ネ': "ne", 'ノ': "no",
    'ハ': "ha", 'ヒ': "hi", 'フ': "fu", 'ヘ': "he", 'ホ': "ho",
    'マ': "ma", 'ミ': "mi", 'ム': "mu", 'メ': "me", 'モ': "mo",
    'ヤ': "ya", 'ユ': "yu", 'ヨ': "yo",
    'ラ': "ra", 'リ': "ri", 'ル': "ru", 'レ': "re", 'ロ': "ro",
    'ワ': "wa", 'ヲ': "wo", 'ン': "n",
    'ガ': "ga", 'ギ': "gi", 'グ': "gu", 'ゲ': "ge", 'ゴ': "go",
    'ザ': "za", 'ジ': "ji", 'ズ': "zu", 'ゼ': "ze", 'ゾ': "zo",
    'ダ': "da", 'ヂ': "ji", 'ヅ': "zu", 'デ': "de", 'ド': "do",
    'バ': "ba", 'ビ': "bi", 'ブ': "bu", 'ベ': "be", 'ボ': "bo",
    'パ': "pa", 'ピ': "pi", 'プ': "pu", 'ペ': "pe", 'ポ': "po",
    # Small characters
    'ァ': "a", 'ィ': "i", 'ゥ': "u", 'ェ': "e", 'ォ': "o",
    'ャ': "ya", 'ュ': "yu", 'ョ': "yo", 'ッ': "",
    # Prolonged sound
    'ー': "",
}

def p_sentence(p):
    '''sentence : sentence element
                | element'''
    if len(p) == 3:
        p[0] = p[1] + ' ' + p[2]
    else:
        p[0] = p[1]

# Old version - convert all kana and kanji to romaji using kakasi library
# def p_element(p):
#     '''element : HIRAGANA
#                | KATAKANA
#                | KANJI
#                | PUNCTUATION'''
#     p[0] = convert_to_romaji(p[1])

# Convert Hiragana into Romaji
def p_hiragana(p):
    '''element : HIRAGANA'''
    result =""
    previous_char=''
    for char in p[1]:
        if char == 'っ':
            previous_char = char
            continue
        if previous_char == 'っ':
            temp = hiragana_to_romaji[char]
            result += temp[0]
        if char in ['ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ','ゃ', 'ゅ', 'ょ']  :
            result = result[:-1]
        result += hiragana_to_romaji[char]
        previous_char = char
    p[0] = result

# Convert Katakana into Romaji
def p_katakana(p):
    '''element : KATAKANA'''
    result = ""
    previous_char = ''
    for char in p[1]:
        if char == 'ー':
            previous_char = char
            result += result[-1]
        if char == 'ッ':
            previous_char = char
            continue
        if previous_char == 'ッ':
            temp = katakana_to_romaji[char]
            result += temp[0]
        if char in ['ァ', 'ィ', 'ゥ', 'ェ', 'ォ','ャ', 'ュ', 'ョ']:
            result = result[:-1]
        result += katakana_to_romaji[char]
        previous_char = char
    p[0] = result

# Convert Kanji into Romaji using kakasi library
def p_kanji(p):
    '''element : KANJI'''
    result = kakasi.convert(p[1])
    p[0] = " ".join([item['hepburn'] for item in result])

# Copy punctuation with no modifications
def p_punctuation(p):
    '''element : PUNCTUATION'''
    p[0] = p[1]

def p_error(p):
    print("Syntax error in input")

# Method to convert all kana and kanji into romaji using kakasi
# def convert_to_romaji(text):
#     result = kakasi.convert(text)
#     return " ".join([item['hepburn'] for item in result])

parser = yacc.yacc()