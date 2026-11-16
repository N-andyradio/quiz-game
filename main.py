import json
from pathlib import Path

STATE_FILE = Path(__file__).parent / "state.json"


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


def read_text(prompt):
    """비어 있지 않은 문자열을 입력받아 반환한다."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("⚠️ 입력이 비어 있습니다. 내용을 입력하세요.")


class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스."""

    def __init__(self):
        self.quizzes = []
        self.best_score = None  # 아직 퀴즈를 풀지 않았으면 None
        self.load_state()

    def reset_to_default(self):
        """기본 퀴즈와 빈 점수로 초기화한다."""
        self.quizzes = create_default_quizzes()
        self.best_score = None

    def load_state(self):
        """state.json에서 퀴즈와 최고 점수를 불러온다."""
        if not STATE_FILE.exists():
            print("📂 저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
            self.reset_to_default()
            self.save_state()
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.quizzes = [Quiz.from_dict(item) for item in data["quizzes"]]
            self.best_score = data.get("best_score")
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("⚠️ 데이터 파일이 손상되어 기본 퀴즈로 복구합니다.")
            self.reset_to_default()
            self.save_state()
        except OSError:
            print("⚠️ 데이터 파일을 읽을 수 없어 기본 퀴즈로 시작합니다.")
            self.reset_to_default()
        else:
            score_text = "없음" if self.best_score is None else f"{self.best_score}점"
            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고 점수 {score_text})")

    def save_state(self):
        """퀴즈와 최고 점수를 state.json에 저장한다."""
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }
        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except OSError:
            print("⚠️ 데이터를 저장하지 못했습니다.")

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
        """저장된 퀴즈를 순서대로 출제하고 결과를 보여 준다."""
        if not self.quizzes:
            print("📭 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        total = len(self.quizzes)
        correct = 0
        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)\n")

        for number, quiz in enumerate(self.quizzes, start=1):
            print("-" * 40)
            quiz.display(number)
            user_answer = read_int("정답 입력: ", 1, 4)

            if quiz.check(user_answer):
                print("✅ 정답입니다!\n")
                correct += 1
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.\n")

        score = correct * 100 // total
        print("=" * 40)
        print(f"🏆 결과: {total}문제 중 {correct}문제 정답! ({score}점)")
        print("=" * 40)

    def add_quiz(self):
        """새 퀴즈를 입력받아 목록에 추가하고 저장한다."""
        print("\n📌 새로운 퀴즈를 추가합니다.\n")
        question = read_text("문제를 입력하세요: ")

        choices = []
        for i in range(1, 5):
            choice = read_text(f"선택지 {i}: ")
            choices.append(choice)

        answer = read_int("정답 번호 (1-4): ", 1, 4)

        self.quizzes.append(Quiz(question, choices, answer))
        self.save_state()
        print("\n✅ 퀴즈가 추가되었습니다!\n")

    def list_quizzes(self):
        """등록된 퀴즈의 문제 목록을 보여 준다."""
        if not self.quizzes:
            print("📭 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n")
        print("-" * 40)
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")
        print("-" * 40)

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
                self.save_state()
                print("💾 저장 완료! 게임을 종료합니다. 안녕히 가세요!")
                break


def main():
    game = QuizGame()
    game.run()


if __name__ == "__main__":
    main()