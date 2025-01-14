from parser import parser

if __name__ == '__main__':
    input_data = "今日は学校に行きます。 かっこいい。 やきゅう。 ハンバーガー。 しゃ。 しや。 きゃ。 きや。 ティ。 ファ "
    # incorrect_data = "focus"
    incorrect_data = "っね"

    romaji = parser.parse(input_data)
    print(f"Japanese: {input_data}\nRomaji: {romaji}")

    wrong_romaji = parser.parse(incorrect_data)
    print(f"Japanese: {incorrect_data}\nRomaji: {wrong_romaji}")