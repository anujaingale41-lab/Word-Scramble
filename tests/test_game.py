import sys
import os
import pytest

# Add the parent directory to sys.path so we can import word_scramble
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from word_scramble import scramble  # Assuming scramble is defined in word_scramble.py

def test_scramble_changes_word():
    original = "python"
    scrambled = scramble(original)
    assert scrambled != original

def test_scramble_preserves_characters():
    original = "pytest"
    scrambled = scramble(original)
    assert sorted(scrambled) == sorted(original)

def test_scramble_empty_string():
    assert scramble("") == ""

def test_scramble_single_character():
    assert scramble("a") == "a"
