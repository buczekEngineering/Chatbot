import re

class TokenEncoder:
    def __init__(self, max_token_count):
        self.token2int = {}
        self.int2token = {}
        self.token_count = 1
        self.max_token_count = max_token_count

    # creating token2int dictionary, converting tokens into integers
    def encode_token(self, token):
        if token not in self.token2int:
            if self.token_count == self.max_token_count:
                return 0
            self.token2int[token] = self.token_count
            self.int2token[self.token_count] = token
            self.token_count += 1
        return self.token2int[token]

    # creating int2token dictionary for converting prediction into text
    def decode(self, prediction):
        return self.int2token[prediction]
