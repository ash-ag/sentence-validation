import unittest

from src import is_sentence_valid

class TestSentenceValidator(unittest.TestCase):
    def test_correct_sentences(self):
        """
        Test Correct sentences based on rules
        """
        sentence = [ "The quick brown fox said “hello Mr lazy dog”.",
                    "The quick brown fox said hello Mr lazy dog.",
                    "One lazy dog is too few, 13 is too many.",
                    "One lazy dog is too few, thirteen is too many.",
                    "How many \"lazy dogs\" are there?",
                    ]
        string_size = len(sentence)
        for i in range(string_size):
            self.assertTrue(is_sentence_valid(sentence[i]))

    def test_incorrect_sentences(self):
        """
        Test in-correct sentences based on rules
        """
        sentence = [ "The quick brown fox said \"hello Mr. lazy dog\".",
				"the quick brown fox said “hello Mr lazy dog\".",
				"\"The quick brown fox said “hello Mr lazy dog.\"",
				"One lazy dog is too few, 12 is too many.",
				"Are there 11, 12, or 13 lazy dogs?",
				"There is no punctuation in this sentence",
				""
                ]
        string_size = len(sentence)
        for i in range(string_size):
            self.assertFalse(is_sentence_valid(sentence[i]))

if __name__ == '__main__':
    unittest.main()
