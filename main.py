import openai
import os
from data import message
from dotenv import load_dotenv
import func

load_dotenv()


def main():
    openai_key = os.getenv("OPEN_AI_KEY")
    myclient = openai.OpenAI(api_key=openai_key)
    check = True
    print("------------------------------------")
    print("Loading! Please wait :D")
    print("------------------------------------")

    while check:

        response = myclient.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=message,
            temperature=0.3,
        )

        reply = response.choices[0].message.content
        print("Super Mario : ", reply)
        message.append(func.add_assistant_message(reply))

        print("------------------------------------")
        statement = input("User : ")

        if not func.exitChat(statement,message):
            check = False
            break
        message.append(func.add_user_message(statement))


if __name__ == "__main__":
    main()
