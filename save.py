def save_conversation(convo):
    f = open("conversation.txt", "w+")
    for i, con in enumerate(convo, start=2):
        if i % 2 == 0:
            f.write("Super Mario : " + con + "\n")
        else:
            f.write("User : " + con + "\n")
    f.close()
    print("Conversation saved!")
