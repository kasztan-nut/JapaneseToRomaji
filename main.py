from parser import parser

if __name__ == '__main__':
    input_data = "今日は学校に行きます。 かっこいい。 やきゅう。 ハンバーガー。 しゃ。 しや。 きゃ。 きや。 ティ。 ファ。  デュ"
    # incorrect_data = "focus"
    incorrect_data = "っね"

    print(f"Japanese: {input_data}")
    romaji = parser.parse(input_data)
    print(f"Romaji: {romaji}")

    print(f"Japanese: {incorrect_data}")
    wrong_romaji = parser.parse(incorrect_data)
    print(f"Romaji: {wrong_romaji}")