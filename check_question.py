forbidden_word_list: list = ["fuck", "silly", "asshole", "stupid"]


def check_question(question):
    for word in forbidden_word_list:
        if word in question:
            return False
    return True
