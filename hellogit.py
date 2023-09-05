from bye import say_bye


def ask_question():
    return input("Ask me a question: ")


def main():
    question = ask_question()
    print("hello git", question)
    say_bye()


main()
