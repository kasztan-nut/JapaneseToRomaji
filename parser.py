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
                | element
                | sentence H_first
                | H_first
                | sentence K_first
                | K_first'''
    if len(p) == 3:
        p[0] = p[1] + ' ' + p[2]
    else:
        p[0] = p[1]

# Sentence containing words with more than one hiragana/katakana symbol
def p_sentence_kana(p):
    '''sentence : sentence H_first H_word
                | H_first H_word
                | sentence K_first K_word
                | K_first K_word'''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1] + ' ' + p[2] + p[3]

# Convert Hiragana into Romaji
def p_first_hiragana(p):
    '''H_first  : HIRAGANA
                | HIRAGANA SMALL_HIRAGANA '''
    if len(p) == 2:
        p[0] = hiragana_to_romaji.get(p[1])
    else:
        if p[1] not in ['\u304D', '\u304E', '\u3057','\u3058','\u3061','\u3062','\u306B','\u3072','\u3073','\u3074','\u307F']:
            print(f"Invalid HIRAGANA combination {p[1]} {p[2]}")
            raise SyntaxError(f"Invalid HIRAGANA combination {p[1]} {p[2]}")
        if p[1] in ['\u3057','\u3061']:
            p[0] = hiragana_to_romaji.get(p[1])[:-1] + hiragana_to_romaji.get(p[2])[1]
        else:
            p[0] = hiragana_to_romaji.get(p[1])[0] + hiragana_to_romaji.get(p[2])

def p_word_hiragana(p):
    '''H_word   : H_element
                | H_element H_word'''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_element_hiragana(p):
    '''H_element    : HIRAGANA
                    | TSU_HIRAGANA HIRAGANA'''
    if len(p) == 2:
        p[0] = hiragana_to_romaji.get(p[1])
    else:
        if p[2] in ['\u306A','\u306B','\u306C','\u306D','\u306E']:
            print(f"Invalid HIRAGANA combination {p[1]} {p[2]}")
            raise SyntaxError(f"Invalid HIRAGANA combination {p[1]} {p[2]}")
        else:
            p[0] = hiragana_to_romaji.get(p[2])[0] + hiragana_to_romaji.get(p[2])

def p_small_hiragana(p):
    '''H_element    : HIRAGANA SMALL_HIRAGANA
                    | TSU_HIRAGANA HIRAGANA SMALL_HIRAGANA'''
    i = 1 if len(p) == 3 else 2
    if p[i] not in ['\u304D', '\u304E', '\u3057', '\u3058', '\u3061', '\u3062', '\u306B', '\u3072', '\u3073', '\u3074',
                    '\u307F']:
        print(f"Invalid HIRAGANA combination {"".join(p[0:])}")
        raise SyntaxError(f"Invalid HIRAGANA combination {"".join(p[0:])}")
    if p[i] in ['\u3057', '\u3061']:
       result = hiragana_to_romaji.get(p[i])[:-1] + hiragana_to_romaji.get(p[i+1])[1]
    else:
        result = hiragana_to_romaji.get(p[i])[0] + hiragana_to_romaji.get(p[i+1])
    # Check for Small TSU
    if len(p) == 3:
        p[0] = result
    else:
        if p[2] in ['\u306A', '\u306B', '\u306C', '\u306D', '\u306E']:
            print(f"Invalid HIRAGANA combination {"".join(p[0:])}")
            raise SyntaxError(f"Invalid HIRAGANA combination {"".join(p[0:])}")
        else:
            p[0] = result[0] + result

# Convert Katakana into Romaji
def p_first_katakana(p):
    '''K_first  : KATAKANA
                | KATAKANA  LONG_KATAKANA'''
    result = katakana_to_romaji.get(p[1])
    # Check for Long Katakana
    if len(p) == 3:
        p[0] = result + result[-1]
    else:
        p[0] = result

def p_first_small_katakana(p):
    '''K_first  : KATAKANA SMALL_KATAKANA
                | KATAKANA SMALL_KATAKANA LONG_KATAKANA'''
    if p[1] not in ['\u30C7', '\u30AD', '\u30AE', '\u30B7', '\u30B8', '\u30C1', '\u30C2', '\u30CB', '\u30D2', '\u30D3', '\u30D4',
                    '\u30DF']:
        print(f"Invalid KATAKANA combination {p[1]} {p[2]}")
        raise SyntaxError(f"Invalid KATAKANA combination {p[1]} {p[2]}")
    if p[1] in ['\u30B7', '\u30B8', '\u30C1', '\u30C2']:
        result = katakana_to_romaji.get(p[1])[:-1] + katakana_to_romaji.get(p[2])[1]
    elif p[1] in ['\u30C7']:
        if p[2] == '\u30E5':
            result = katakana_to_romaji.get(p[1])[0] + katakana_to_romaji.get(p[2])
        else:
            print(f"Invalid KATAKANA combination {p[1]} {p[2]}")
            raise SyntaxError(f"Invalid KATAKANA combination {p[1]} {p[2]}")
    else:
        result = katakana_to_romaji.get(p[1])[0] + katakana_to_romaji.get(p[2])
    # Check for Long Katakana
    if len(p) == 4:
        p[0] = result + result[-1]
    else:
        p[0] = result

def p_first_s_vowel_katakana(p):
    '''K_first  : KATAKANA SMALL_K_VOWEL
                | KATAKANA SMALL_K_VOWEL LONG_KATAKANA'''
    if p[1] not in ['\u30B7', '\u30B8', '\u30C1', '\u30C4', '\u30C6', '\u30C7', '\u30D5']:
        print(f"Invalid KATAKANA combination {p[1]} {p[2]}")
        raise SyntaxError(f"Invalid KATAKANA combination {p[1]} {p[2]}")
    # fa, fi, fe, fo
    if p[1] == '\u30D5':
        result = katakana_to_romaji.get(p[1])[0] + katakana_to_romaji.get(p[2])
    else:
        # she, je, che, tse
        if p[2] == '\u30A7':
            result = katakana_to_romaji.get(p[:-1])[0] + katakana_to_romaji.get(p[2])
        # tsa,tso,
        elif p[1] == '\u30C4':
            if p[2] not in ['\u30A1', '\u30A9']:
                print(f"Invalid KATAKANA combination {p[1]} {p[2]}")
                raise SyntaxError(f"Invalid KATAKANA combination {p[1]} {p[2]}")
            else:
                result = katakana_to_romaji.get(p[1])[0] + katakana_to_romaji.get(p[2])
        # ti, di
        elif p[2] == '\u30A3':
            if p[1] not in ['\u30C6', '\u30C7']:
                print(f"Invalid KATAKANA combination {p[1]} {p[2]}")
                raise SyntaxError(f"Invalid KATAKANA combination {p[1]} {p[2]}")
            else:
                result = katakana_to_romaji.get(p[1])[0] + katakana_to_romaji.get(p[2])
        else:
            print(f"Invalid KATAKANA combination {p[1]} {p[2]}")
            raise SyntaxError(f"Invalid KATAKANA combination {p[1]} {p[2]}")
    # Check for Long Katakana
    if len(p) == 4:
        p[0] = result + result[-1]
    else:
        p[0] = result

def p_word_katakana(p):
    '''K_word   : K_element
                | K_element K_word'''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_element_katakana(p):
    '''K_element    : KATAKANA
                    | TSU_KATAKANA KATAKANA '''
    if len(p) == 2:
        p[0] = katakana_to_romaji.get(p[1])
    else:
        if p[2] in ['\u30CA','\u30CB','\u30CC','\u30CD','\u30CE']:
            print(f"Invalid KATAKANA combination {p[1]} {p[2]}")
            raise SyntaxError(f"Invalid KATAKANA combination {p[1]} {p[2]}")
        else:
            p[0] = katakana_to_romaji.get(p[2])[0] + katakana_to_romaji.get(p[2])

def p_small_katakana(p):
    '''K_element    : KATAKANA SMALL_KATAKANA
                    | TSU_KATAKANA KATAKANA SMALL_KATAKANA'''
    i = 1 if len(p) == 3 else 2
    if p[i] not in ['\u30C7', '\u30AD', '\u30AE', '\u30B7', '\u30B8', '\u30C1', '\u30C2', '\u30CB', '\u30D2', '\u30D3',
                    '\u30D4', '\u30DF']:
        print(f"Invalid KATAKANA combination {"".join(p[0:])}")
        raise SyntaxError(f"Invalid KATAKANA combination {"".join(p[0:])}")
    if p[i] in ['\u30B7', '\u30B8', '\u30C1', '\u30C2']:
        result = katakana_to_romaji.get(p[i])[:-1] + katakana_to_romaji.get(p[i+1])[1]
    elif p[i] == '\u30C7':
        if p[i+1] == '\u30E5':
            result = katakana_to_romaji.get(p[i])[0] + katakana_to_romaji.get(p[i+1])
        else:
            print(f"Invalid KATAKANA combination {"".join(p[0:])}")
            raise SyntaxError(f"Invalid KATAKANA combination {"".join(p[0:])}")
    else:
        result = katakana_to_romaji.get(p[i])[0] + katakana_to_romaji.get(p[i+1])
    # Check for Small TSU
    if len(p) == 3:
        p[0] = result
    else:
        if p[2] in ['\u30CA', '\u30CB', '\u30CC', '\u30CD', '\u30CE']:
            print(f"Invalid KATAKANA combination {"".join(p[0:])}")
            raise SyntaxError(f"Invalid KATAKANA combination {"".join(p[0:])}")
        else:
            p[0] = result[0] + result

def p_s_vowel_katakana(p):
    '''K_element    : KATAKANA SMALL_K_VOWEL
                    | TSU_KATAKANA KATAKANA SMALL_K_VOWEL'''
    i = 1 if len(p) == 3 else 2
    if p[i] not in ['\u30B7', '\u30B8', '\u30C1', '\u30C4', '\u30C6', '\u30C7', '\u30D5']:
        print(f"Invalid KATAKANA combination {"".join(p[0:])}")
        raise SyntaxError(f"Invalid KATAKANA combination {"".join(p[0:])}")
    # fa, fi, fe, fo
    if p[i] == '\u30D5':
        result = katakana_to_romaji.get(p[i])[0] + katakana_to_romaji.get(p[i+1])
    else:
        # she, je, che, tse
        if p[i+1] == '\u30A7':
            result = katakana_to_romaji.get(p[i])[:-1] + katakana_to_romaji.get(p[i+1])
        # tsa,tso,
        elif p[i] == '\u30C4':
            if p[i+1] not in ['\u30A1', '\u30A9']:
                print(f"Invalid KATAKANA combination {"".join(p[0:])}")
                raise SyntaxError(f"Invalid KATAKANA combination {"".join(p[0:])}")
            else:
                result = katakana_to_romaji.get(p[i])[0] + katakana_to_romaji.get(p[i+1])
        # ti, di
        elif p[i+1] == '\u30A3':
            if p[i] not in ['\u30C6', '\u30C7']:
                print(f"Invalid KATAKANA combination {"".join(p[0:])}")
                raise SyntaxError(f"Invalid KATAKANA combination {"".join(p[0:])}")
            else:
               result = katakana_to_romaji.get(p[i])[0] + katakana_to_romaji.get(p[i+1])
        else:
            print(f"Invalid KATAKANA combination {"".join(p[0:])}")
            raise SyntaxError(f"Invalid KATAKANA combination {"".join(p[0:])}")
    # Check for Small TSU
    if len(p) == 3:
        p[0] = result
    else:
        if p[2] in ['\u30CA', '\u30CB', '\u30CC', '\u30CD', '\u30CE']:
            print(f"Invalid KATAKANA combination {"".join(p[0:])}")
            raise SyntaxError(f"Invalid KATAKANA combination {"".join(p[0:])}")
        else:
            p[0] = result[0] + result

def p_long_katakana(p):
    '''K_element    : KATAKANA LONG_KATAKANA
                    | TSU_KATAKANA KATAKANA  LONG_KATAKANA'''
    if len(p) == 3:
        p[0] = katakana_to_romaji.get(p[1]) + katakana_to_romaji.get(p[1])[-1]
    else:
        if p[2] in ['\u30CA', '\u30CB', '\u30CC', '\u30CD', '\u30CE']:
            print(f"Invalid KATAKANA combination {p[1]} {p[2]} {p[3]}")
            raise SyntaxError(f"Invalid KATAKANA combination {p[1]} {p[2]} {p[3]}")
        else:
            p[0] = katakana_to_romaji.get(p[2])[0] + katakana_to_romaji.get(p[2]) + katakana_to_romaji.get(p[2])[-1]

def p_small_long_katakana(p):
    '''K_element    : KATAKANA SMALL_KATAKANA LONG_KATAKANA
                    | TSU_KATAKANA KATAKANA SMALL_KATAKANA LONG_KATAKANA'''
    i = 1 if len(p) == 4 else 2
    if p[i] not in ['\u30C7', '\u30AD', '\u30AE', '\u30B7', '\u30B8', '\u30C1', '\u30C2', '\u30CB', '\u30D2', '\u30D3',
                    '\u30D4', '\u30DF']:
        print(f"Invalid KATAKANA combination {"".join(p[0:])}")
        raise SyntaxError(f"Invalid KATAKANA combination {"".join(p[0:])}")
    if p[i] in ['\u30B7', '\u30B8', '\u30C1', '\u30C2']:
        result = katakana_to_romaji.get(p[i])[:-1] + katakana_to_romaji.get(p[i+1])[-1] + katakana_to_romaji.get(p[i+1])[-1]
    elif p[i] in ['\u30C7']:
        if p[i+1] == '\u30E5':
            result = katakana_to_romaji.get(p[i])[0] + katakana_to_romaji.get(p[i+1]) + katakana_to_romaji.get(p[i+1])[-1]
        else:
            print(f"Invalid KATAKANA combination {"".join(p[0:])}")
            raise SyntaxError(f"Invalid KATAKANA combination {"".join(p[0:])}")
    else:
        result = katakana_to_romaji.get(p[i])[0] + katakana_to_romaji.get(p[i+1]) + katakana_to_romaji.get(p[i+1])[-1]
    # Check for Small TSU
    if len(p) == 4:
        p[0] = result
    else:
        if p[2] in ['\u30CA', '\u30CB', '\u30CC', '\u30CD', '\u30CE']:
            print(f"Invalid KATAKANA combination {"".join(p[0:])}")
            raise SyntaxError(f"Invalid KATAKANA combination {"".join(p[0:])}")
        else:
            p[0] = result[0] + result

def p_s_vowel_long_katakana(p):
    '''K_element    : KATAKANA SMALL_K_VOWEL LONG_KATAKANA
                    | TSU_KATAKANA KATAKANA SMALL_K_VOWEL LONG_KATAKANA'''
    i = 1 if len(p) == 4 else 2
    if p[i] not in ['\u30B7', '\u30B8', '\u30C1', '\u30C4', '\u30C6', '\u30C7', '\u30D5']:
        print(f"Invalid KATAKANA combination {"".join(p[0:])}")
        raise SyntaxError(f"Invalid KATAKANA combination {"".join(p[0:])}")
    # fa, fi, fe, fo
    if p[i] == '\u30D5':
        result = katakana_to_romaji.get(p[i])[0] + katakana_to_romaji.get(p[i+1]) + katakana_to_romaji.get(p[i+1])
    else:
        # she, je, che, tse
        if p[i+1] == '\u30A7':
            result = katakana_to_romaji.get(p[i])[:-1] + katakana_to_romaji.get(p[i+1]) + katakana_to_romaji.get(p[i+1])
        # tsa,tso
        elif p[i] == '\u30C4':
            if p[i+1] not in ['\u30A1', '\u30A9']:
                print(f"Invalid KATAKANA combination {"".join(p[0:])}")
                raise SyntaxError(f"Invalid KATAKANA combination {"".join(p[0:])}")
            else:
                result = katakana_to_romaji.get(p[i])[0] + katakana_to_romaji.get(p[i+1]) + katakana_to_romaji.get(p[i+1])
        # ti, di
        elif p[i+1] == '\u30A3':
            if p[i] not in ['\u30C6', '\u30C7']:
                print(f"Invalid KATAKANA combination {"".join(p[0:])}")
                raise SyntaxError(f"Invalid KATAKANA combination {"".join(p[0:])}")
            else:
                result = katakana_to_romaji.get(p[i])[0] + katakana_to_romaji.get(p[i+1]) + katakana_to_romaji.get(p[i+1])
        else:
            print(f"Invalid KATAKANA combination {"".join(p[0:])}")
            raise SyntaxError(f"Invalid KATAKANA combination {"".join(p[0:])}")
    # Check for Small TSU
    if len(p) == 4:
        p[0] = result
    else:
        if p[2] in ['\u30CA', '\u30CB', '\u30CC', '\u30CD', '\u30CE']:
            print(f"Invalid KATAKANA combination {"".join(p[0:])}")
            raise SyntaxError(f"Invalid KATAKANA combination {"".join(p[0:])}")
        else:
            p[0] = result[0] + result

# Convert Kanji into Romaji using kakasi library
def p_kanji(p):
    '''element : KANJI'''
    result = kakasi.convert(p[1])
    p[0] = " ".join([item['hepburn'] for item in result])

# Copy punctuation/numbers with no modifications
def p_special(p):
    '''element : SPECIAL'''
    p[0] = p[1]

def p_error(p):
    print("Syntax error in input")

# Ensures that a word in hiragana doesn't start with small tsu - accent mark
def p_h_small_tsu_error(p):
    '''H_first  : TSU_HIRAGANA'''
    print(f"Word cannot start with small tsu ({p[1]})")
    raise SyntaxError(f"Word cannot start with small tsu ({p[1]})")

# Ensures that a word in katakana doesn't start with small tsu - accent mark
def p_k_small_tsu_error(p):
    '''K_first  : TSU_KATAKANA'''
    print(f"Word cannot start with small tsu ({p[1]})")
    raise SyntaxError(f"Word cannot start with small tsu ({p[1]})")

parser = yacc.yacc()