from parser import parser

if __name__ == '__main__':
    input_data = "今日は学校に行きます。 かっこいい。 やきゅう。 ハンバーガー。 しゃ。 しや。 きゃ。 きや。 ティ。 ファ。  デュ"
    incorrect_data = "focus"
    incorrect_data_1 = "っね"
    incorrect_data_2 = "ねゅ"
    incorrect_data_3 = "ッフ"
    incorrect_data_4 = "ねっにゅ"

    print(f"Japanese: {input_data}")
    romaji = parser.parse(input_data)
    print(f"Romaji: {romaji}")

    print(f"Japanese: {incorrect_data}")
    wrong_romaji = parser.parse(incorrect_data)
    print(f"Romaji: {wrong_romaji}")

    print(f"Japanese: {incorrect_data_1}")
    wrong_romaji = parser.parse(incorrect_data_1)
    print(f"Romaji: {wrong_romaji}")

    print(f"Japanese: {incorrect_data_2}")
    wrong_romaji = parser.parse(incorrect_data_2)
    print(f"Romaji: {wrong_romaji}")

    print(f"Japanese: {incorrect_data_3}")
    wrong_romaji = parser.parse(incorrect_data_3)
    print(f"Romaji: {wrong_romaji}")

    print(f"Japanese: {incorrect_data_4}")
    wrong_romaji = parser.parse(incorrect_data_4)
    print(f"Romaji: {wrong_romaji}")