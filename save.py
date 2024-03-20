def save_conversation(convo):
    f = open("conversation.txt", "w+")
    for i, con in enumerate(convo, start=2):
        if i % 2 == 0:
            f.write("Super Mario : " + con['content'] + "\n")
        else:
            f.write("User : " + con['content'] + "\n")
    f.close()

    print("Conversation saved!")
