import pytest
from game import scramble

def test_scramble_changes_word():
    original = "python"
    scrambled = scramble(original)
    assert scrambled != original, "Scrambled word should differ from original"

def test_scramble_preserves_characters():
    original = "pytest"
    scrambled = scramble(original)
    assert sorted(scrambled) == sorted(original), "Scrambled word should contain same characters"

def test_scramble_empty_string():
    assert scramble("") == "", "Scrambling empty string should return empty string"

def test_scramble_single_character():
    assert scramble("a") == "a", "Scrambling single character should return same character"
