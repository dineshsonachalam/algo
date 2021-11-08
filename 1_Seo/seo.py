class Seo:
    def __init__(self, words):
        self.words = words

    @staticmethod
    def get_sorted_words(words):
        """Get Sorted Word
        Args:
            words (list): Given Input Strings
        Returns:
            dict: sorted_words
        """
        sorted_words = {}
        for word in words:
            sorted_word = "".join(sorted(word))
            if sorted_words.get(sorted_word):
                result = sorted_words[sorted_word]
                result.append(word)
                sorted_words[sorted_word] = result
            else:
                sorted_words[sorted_word] = [word]
        return sorted_words

    def find(self, word):
        """Find's matching string from the list of given strings
        Args:
            word (string): Word to be searched
        Returns:
            list: Matched strings
        """
        sorted_words = self.get_sorted_words(self.words)
        sorted_word = "".join(sorted(word))
        return sorted_words.get(sorted_word)