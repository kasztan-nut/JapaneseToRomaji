from parser import parser

if __name__ == '__main__':
    input_data = "今日は学校に行きます。 かっこいい。 やきゅう。 ハンバーガー。"
    incorrect_data = "focus"

    romaji = parser.parse(input_data)
    print(f"Japanese: {input_data}\nRomaji: {romaji}")

    # wrong_romaji = parser.parse(incorrect_data)
    # print(f"Japanese: {incorrect_data}\nRomaji: {wrong_romaji}")