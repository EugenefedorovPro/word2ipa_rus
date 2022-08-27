import pytest
from word2ipa_rus.utils.word_processing import WordsProcessing


def test_word_processing():
    output = [
        7,
        17,
        1,
        15,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]
    word_stressed = "до'м"
    assert output == WordsProcessing.word2numbers(word_stressed)
