def read_int(prompt, min_value, max_value):
    """min_value~max_value 사이의 정수를 입력받아 반환한다."""
    while True:
        text = input(prompt).strip()

        if text == "":
            print("⚠️ 입력이 비어 있습니다. 숫자를 입력하세요.")
            continue

        try:
            number = int(text)
        except ValueError:
            print(f"⚠️ 잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        if number < min_value or number > max_value:
            print(f"⚠️ 잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        return number


def show_menu():
    print("=" * 40)
    print("        🎯 클래식 기타 퀴즈 게임 🎯")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)


def main():
    while True:
        show_menu()
        choice = read_int("선택: ", 1, 5)

        if choice == 1:
            print("퀴즈 풀기는 준비 중입니다.")
        elif choice == 2:
            print("퀴즈 추가는 준비 중입니다.")
        elif choice == 3:
            print("퀴즈 목록은 준비 중입니다.")
        elif choice == 4:
            print("점수 확인은 준비 중입니다.")
        elif choice == 5:
            print("게임을 종료합니다. 안녕히 가세요!")
            break


if __name__ == "__main__":
    main()