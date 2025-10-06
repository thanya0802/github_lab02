# test/test_pytest.py
import pytest
from src.string_processor import count_vowels, reverse_string, capitalize_words, combined_summary

def test_count_vowels():
    assert count_vowels("Hello World") == 3
    assert count_vowels("AI") == 2

def test_reverse_string():
    assert reverse_string("abcd") == "dcba"

def test_capitalize_words():
    assert capitalize_words("machine learning lab") == "Machine Learning Lab"

def test_combined_summary():
    result = combined_summary("hello")
    assert result["vowel_count"] == 2
    assert result["reversed"] == "olleh"
    assert result["capitalized"] == "Hello"
