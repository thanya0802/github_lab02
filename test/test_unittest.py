# test/test_unittest.py
import unittest
from src.string_processor import count_vowels, reverse_string, capitalize_words, combined_summary

class TestStringProcessor(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(count_vowels("OpenAI"), 4)

    def test_reverse_string(self):
        self.assertEqual(reverse_string("ChatGPT"), "TPGtahC")

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("data science"), "Data Science")

    def test_combined_summary(self):
        result = combined_summary("mlops")
        self.assertEqual(result["vowel_count"], 1)
        self.assertEqual(result["reversed"], "spolm")
        self.assertEqual(result["capitalized"], "Mlops")

if __name__ == '__main__':
    unittest.main()
