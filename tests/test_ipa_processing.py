from word2ipa_rus.utils.ipa_processing import IpaProcessing


def test_ipa_processing():
    assert 89 == len(IpaProcessing.get_number2sign())
