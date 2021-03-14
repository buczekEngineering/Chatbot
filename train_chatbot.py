import json
import pickle

from ChatbotClassifier import ChatbotClassifier

if __name__ == "__main__":
    with open("../data/chatbot_dialog.json") as file:
        data = json.load(file)


    num_classes = 50
    # all possible cases / tags
    num_labels = len(data["intents"]) + 1
    sequence_length = 8

    training_user_input = []
    training_labels = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            training_labels.append(intent["tag"])
            training_user_input.append(pattern)

    classifier = ChatbotClassifier(num_classes, num_labels, sequence_length)
    classifier.train(training_user_input, training_labels, 32, 200)

    with open("../data/chatbot_data.pickle", "wb") as file:
        pickle.dump(classifier, file)



