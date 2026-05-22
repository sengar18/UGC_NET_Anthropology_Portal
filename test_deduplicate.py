import pytest
from deduplicate import normalize_text

def test_normalize_text_basic():
    assert normalize_text("Hello World") == "hello world"

def test_normalize_text_html():
    assert normalize_text("<p>Hello World</p>") == "hello world"
    assert normalize_text("<div><b>Bold</b> and <i>Italic</i></div>") == "bold and italic"

def test_normalize_text_punctuation():
    assert normalize_text("Hello, World!") == "hello world"
    assert normalize_text("Testing... 1, 2, 3.") == "testing 1 2 3"

def test_normalize_text_spaces():
    assert normalize_text("  Hello   World  ") == "hello world"
    assert normalize_text("Hello\tWorld\n\nNew\rLine") == "hello world new line"

def test_normalize_text_complex():
    complex_text = "  <p>Hello,   <b>World!</b></p> \n\n Testing... 1, 2, 3.  "
    assert normalize_text(complex_text) == "hello world testing 1 2 3"

def test_normalize_text_edge_cases():
    assert normalize_text("") == ""
    assert normalize_text("<p></p>") == ""
    assert normalize_text("!@#$%^&*()") == ""
    assert normalize_text("   \n\t   ") == ""
