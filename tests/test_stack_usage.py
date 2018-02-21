from stack_usage import brackets_balanced
from stack_usage import to_binary
from stack_usage import convert
from stack_usage import infix_to_postfix
from stack_usage import eval_postfix_expr


def test_brackets_balanced():
    assert brackets_balanced('{{([][])}()}')
    assert not brackets_balanced('{{]}')


def test_to_binary():
    assert to_binary(5) == "0b101"
    assert to_binary(15) == "0b1111"
    assert to_binary(16) == "0b10000"


def test_convert():
    assert convert(10, 2) == "1010"
    assert convert(2, 3) == "2"
    assert convert(13, 8) == "15"
    assert convert(13, 10) == "13"
    assert convert(28, 16) == "1C"
    assert convert(28, 13) == "22"


def test_infix_to_postfix():
    assert infix_to_postfix("A * B + C * D") == "A B * C D * +"
    assert infix_to_postfix(
        "( A + B ) * C - ( D - E ) * ( F + G )") == "A B + C * D E - F G + * -"


def test_eval_postfix_expr():
    assert eval_postfix_expr("7 8 + 3 2 + /") == 3.0
    assert eval_postfix_expr("3 5 * 8 *") == 120
