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


def create_default_quizzes():
    """처음 실행할 때 쓰는 기본 퀴즈 5개를 만들어 반환한다."""
    return [
        Quiz(
            "클래식 기타의 표준 튜닝을 6번줄(가장 굵은 줄)부터 1번줄 순서로 나열한 것은?",
            ["E-B-G-D-A-E", "E-A-D-G-B-E", "D-A-D-G-B-E", "D-G-C-F-A-D"],
            2,
        ),
        Quiz(
            "일반적인 클래식 기타의 줄은 모두 몇 개일까요?",
            ["4개", "5개", "6개", "12개"],
            3,
        ),
        Quiz(
            "클래식 기타의 대표곡 '알함브라 궁전의 추억'을 작곡한 사람은?",
            ["프란시스코 타레가", "안드레스 세고비아", "페르난도 소르", "이삭 알베니스"],
            1,
        ),
        Quiz(
            "클래식 기타 줄의 기본 재질은 무엇일까요?",
            ["철(스틸)", "가죽", "실크", "나일론"],
            4,
        ),
        Quiz(
            "클래식 기타 오른손 지법에서 'a'로 표기하는 손가락은?",
            ["엄지", "검지", "중지", "약지"],
            4,
        ),
    ]


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


class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스."""

    def __init__(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None  # 아직 퀴즈를 풀지 않았으면 None

    def show_menu(self):
        print("=" * 40)
        print("        🎯 클래식 기타 퀴즈 게임 🎯")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def play(self):
        print("퀴즈 풀기는 준비 중입니다.")

    def add_quiz(self):
        print("퀴즈 추가는 준비 중입니다.")

    def list_quizzes(self):
        print("퀴즈 목록은 준비 중입니다.")

    def show_score(self):
        print("점수 확인은 준비 중입니다.")

    def run(self):
        while True:
            self.show_menu()
            choice = read_int("선택: ", 1, 5)

            if choice == 1:
                self.play()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                print("게임을 종료합니다. 안녕히 가세요!")
                break


def main():
    game = QuizGame()
    game.run()


if __name__ == "__main__":
    main()