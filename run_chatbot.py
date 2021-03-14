from Chatbot import Chatbot

if __name__ == "__main__":
    chatbot = Chatbot("../data/chatbot_dialog.json", "../data/chatbot_data.pickle")
    while(True):
        user_input = input("> ")
        if user_input == "quit":
            break

        else:
            print(chatbot.get_response(user_input))

