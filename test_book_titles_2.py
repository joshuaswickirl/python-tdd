
import book_titles
import pytest

#This is a Pramaterized list
@pytest.mark.parametrize("test_input,expected", 
    [
        ("Harry Potter", "H12"), 
        ("Some book", "S9"), 
        ("Another book", "A12"), 
        ("The Hunger Games", "T16"), 
        ("Pride and Prejudice", "P19"), 
        ("Gone with the wind", "G18")
    ])
def test_eval(test_input, expected):
    assert book_titles.calculate(test_input) == expected

