from bye import say_bye
from check_question import check_question
from date import today_is


def ask_question():
    return input("Ask me a question: ")


def main():
    question = ask_question()
    if check_question(question):
        print(f"Hello Git, today is {today_is()} and your question is: {question}")
    say_bye()

    print("Es bromita")
    print("Tell me whyyyyyy")


if __name__ == "__main__":
    main()
