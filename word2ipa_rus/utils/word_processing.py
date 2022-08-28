class WordsProcessing:

    @classmethod
    def word2numbers(cls, accent):
        character2number_for_stressed_words = {
            "'": 1,
            "-": 2,
            "а": 3,
            "б": 4,
            "в": 5,
            "г": 6,
            "д": 7,
            "е": 8,
            "ж": 9,
            "з": 10,
            "и": 11,
            "й": 12,
            "к": 13,
            "л": 14,
            "м": 15,
            "н": 16,
            "о": 17,
            "п": 18,
            "р": 19,
            "с": 20,
            "т": 21,
            "у": 22,
            "ф": 23,
            "х": 24,
            "ц": 25,
            "ч": 26,
            "ш": 27,
            "щ": 28,
            "ъ": 29,
            "ы": 30,
            "ь": 31,
            "э": 32,
            "ю": 33,
            "я": 34,
            "ё": 35,
        }
        max_length_of_stressed_word = 34
        numbers = []
        for ch in accent:
            n = character2number_for_stressed_words[ch]
            numbers.append(n)
        n_of_zeros_to_add = max_length_of_stressed_word - len(numbers)
        numbers.extend([0 for i in range(n_of_zeros_to_add)])
        return numbers
