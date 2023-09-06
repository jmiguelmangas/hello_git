from bye import say_bye
from check_question import check_question


def ask_question():
    return input("Ask me a question: ")


def main():
    question = ask_question()
    if check_question(question):
        print("hello git", question)
    say_bye()


main()
