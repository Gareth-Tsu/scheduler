import pytest
from DSA.SandQ import *

def test_valid_parentheses():
    assert is_valid("()[]{}") == True,  "Failed: all valid pairs"
    assert is_valid("([{}])") == True,  "Failed: nested valid"
    assert is_valid("([)]")   == False, "Failed: wrong order"
    assert is_valid("(((")    == False, "Failed: unclosed brackets"
    assert is_valid("")        == True,  "Failed: empty string"
    assert is_valid("}")       == False, "Failed: close with no open"
    print("All parentheses tests passed!")
