from pathlib import Path
import os
import numpy as np
from word2ipa_rus.utils.ipa_processing import IpaProcessing
from word2ipa_rus.utils.word_processing import WordsProcessing

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
from tensorflow.keras.models import load_model

# import trained model
path_model = Path(__file__).parent / "model_word2ipa_rus.h5"
model_ipa = load_model(path_model)
print("Trained Model 'word2ipa' uploaded successfully")


def make_array_from_word_for_model(word_stressed):
    no_classes = 90
    n_columns_labels = 34
    word_as_array = WordsProcessing.word2numbers(word_stressed)
    word_as_array = np.array(word_as_array)
    word_as_array = word_as_array.reshape(1, word_as_array.shape[0])
    predicted_array = model_ipa.predict(word_as_array, verbose=0)
    predicted_array = predicted_array.reshape(n_columns_labels, no_classes)
    return predicted_array


def turn_predicted_array_to_transcription(predicted_array):
    number2sign = IpaProcessing.get_number2sign()
    ipa_predicted = []
    for position in predicted_array:
        number = np.argmax(position)
        if number != 0:
            sign = number2sign[number]
            ipa_predicted.append(str(sign))
    ipa_predicted = "".join(ipa_predicted)
    return ipa_predicted


def word2ipa(word_stressed):
    predicted_array = make_array_from_word_for_model(word_stressed)
    ipa_predicted = turn_predicted_array_to_transcription(predicted_array)
    return ipa_predicted
