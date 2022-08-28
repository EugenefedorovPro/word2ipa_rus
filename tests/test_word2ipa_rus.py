from word2ipa_rus.word2ipa import word2ipa


def test_word2ipa():
    assert "ˈkoʂkə" == word2ipa("ко'шка")
