import pytest
from tokenizer import Tokenizer

@pytest.fixture
def tokenizer():
    return Tokenizer()

def test_basic_tokenization(tokenizer):
    text = "Hello, world!"
    expected = ["Hello", ",", "world", "!"]
    assert tokenizer.tokenize(text) == expected

def test_abbreviations(tokenizer):
    assert tokenizer.tokenize("U.S.A. is big.") == ["U.S.A.", "is", "big", "."]

def test_currency_and_percentages(tokenizer):
    assert tokenizer.tokenize("$5.99 is 20% off.") == ["$5.99", "is", "20%", "off", "."]

def test_hyphenated_words(tokenizer):
    assert tokenizer.tokenize("This is state-of-the-art.") == ["This", "is", "state-of-the-art", "."]
