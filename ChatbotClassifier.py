import re
from string import punctuation

import numpy as np
from keras.layers import Dense, LSTM, Dropout
from keras.models import Sequential

import one_hot
import utils
from TokenEncoder import TokenEncoder


class ChatbotClassifier:
    def __init__(self, num_classes, num_labels, sequence_length):
        self.sequence_length = sequence_length

        self.text_encoder = TokenEncoder(num_classes)
        self.label_encoder = TokenEncoder(num_labels)
        # self.tokenizer = Tokenizer(num_words=self.num_classes)

        self.num_classes = num_classes
        self.num_labels = num_labels

        self.model = Sequential()
        self.model.add(LSTM(256, input_shape=(sequence_length, self.num_classes)))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(self.num_labels, activation="softmax"))
        self.model.compile(optimizer="adam", loss="categorical_crossentropy")

    def train(self, texts, labels, batch_size, epochs):

        sequences = [[self.text_encoder.encode_token(t) for t in utils.tokenize(text.lower())] for text in texts]

        sequences = [utils.pad_sequence(s, self.sequence_length) for s in sequences]
        labels = [self.label_encoder.encode_token(label) for label in labels]

        sequences = one_hot.encode_sequences(sequences, self.num_classes)
        labels = one_hot.encode_sequence(labels, self.num_labels)

        self.model.fit(x=sequences,
                       y=labels,
                       batch_size=batch_size,
                       epochs=epochs)

    def predict(self, sequence):
        sequence = [self.text_encoder.encode_token(t) for t in utils.tokenize(sequence.lower())]
        sequence = utils.pad_sequence(sequence, self.sequence_length)
        sequences = one_hot.encode_sequences([sequence], self.num_classes)
        prediction = self.model.predict(sequences)[0]
        best_prediction = np.argmax(prediction)

        return self.label_encoder.decode(best_prediction)
