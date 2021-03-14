import numpy as np

# sequences = array of array of numbers
def encode_sequences(sequences, num_classes):
    return np.array([encode_sequence(sequence, num_classes) for sequence in sequences])

def encode_sequences2(sequences, num_classes):
    result = np.zeros((len(sequences), len(sequences[0]), num_classes))
    for x, sequence in enumerate(sequences):
        for y, z in enumerate(sequence):
            result[x, y, z] = 1

def encode_sequence(sequence, num_classes):
    return np.array([encode_number(number, num_classes) for number in sequence])

def encode_number(number, num_classes):
    result = np.zeros(num_classes)
    result[number] = 1

    return result
