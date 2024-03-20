import save


def exitChat(s, full) -> bool:
    if s.lower() == 'exit':
        save_file = input("Do you want to save the conversation? (yes/no): ")
        if save_file.lower() == "yes" or save_file.lower() == 'y':
            save.save_conversation(full)
        print("Goodbye!")
        return False

    else:
        return True


def add_user_message(s):
    temp = {"role": "user",
            "content": s}
    return temp


def add_assistant_message(s):
    temp = {"role": "assistant",
            "content": s}
    return temp
