## Hardcoded Boulder Bot to answer questions of the bouldergym (climbinggym) customers
based on simple multiclass classification with LSTM

# Dataset 
The data are hand written in the json format: chabot_dialog.json.
The file contains Tag(Class Label), Patterns(Possible customer question), Responses (Hardcoded Chatbot Response).

# Training the model 
To train the model run train_chatbot.py
The implementation of the neural network, train and predict method is in the ChatbotClassifier.py.

# Talk to the bot
Afer the training is finished, you can run_chatbot.py and talk with the Boulder Bot through your terminal
