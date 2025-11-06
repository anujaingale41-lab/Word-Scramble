import sys
import os
import pytest

# Add the parent directory to sys.path so we can import word_scramble
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from word_scramble import scramble_word

def test_scramble_changes_word():
    original = "python"
    scrambled = scramble_word(original)
    assert scrambled != original, "Scrambled word should differ from original"

def test_scramble_preserves_characters():
    original = "syntax"
    scrambled = scramble_word(original)
    assert sorted(scrambled) == sorted(original), "Scrambled word should contain same characters"

def test_scramble_empty_string():
    assert scramble_word("") == "", "Scrambling empty string should return empty string"

def test_scramble_single_character():
    assert scramble_word("a") == "a", "Scrambling single character should return same character"
