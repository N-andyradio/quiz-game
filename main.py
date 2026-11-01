class Quiz:
    """퀴즈 한 문제를 나타내는 클래스."""

    def __init__(self, question, choices, answer):
        if len(choices) != 4:
            raise ValueError("선택지는 4개여야 합니다.")
        if answer not in (1, 2, 3, 4):
            raise ValueError("정답은 1~4 중 하나여야 합니다.")
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self, number=None):
        """문제와 선택지를 화면에 출력한다."""
        if number is not None:
            print(f"[문제 {number}]")
        print(self.question)
        print()
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")
        print()

    def check(self, user_answer):
        """사용자가 입력한 번호가 정답이면 True를 반환한다."""
        return user_answer == self.answer

    def to_dict(self):
        """JSON으로 저장하기 위해 딕셔너리로 변환한다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        """저장된 딕셔너리로부터 Quiz 객체를 만든다."""
        return cls(data["question"], data["choices"], data["answer"])
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
