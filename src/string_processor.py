
def count_vowels(s: str) -> int:
    """Count vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def reverse_string(s: str) -> str:
    """Return the reversed version of the string."""
    return s[::-1]

def capitalize_words(s: str) -> str:
    """Capitalize each word in the string."""
    return " ".join(word.capitalize() for word in s.split())

def combined_summary(s: str) -> dict:
    """
    Combine results of all functions.
    Returns dictionary with:
      - vowel_count
      - reversed
      - capitalized
    """
    return {
        "vowel_count": count_vowels(s),
        "reversed": reverse_string(s),
        "capitalized": capitalize_words(s)
    }


