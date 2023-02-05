from pytest import mark
from src.jogo import brincadeira


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "env(name): mark test to run only on named environment"
    )


def test_should_be_one():
    input = 1  # Given
    expected = 1  # Given
    result = brincadeira(input)  # When input
    assert result == expected  # Then result


def test_should_be_two():
    assert brincadeira(2) == 2  # When input


def test_should_be_queijo():
    assert brincadeira(3) == "Queijo"  # When input


@mark.parametrize(
    "input",
    [5, 10, 20, 25, 35]
)
def test_should_be_goiabada_with_multiples_of_5(input):
    assert brincadeira(input) == "Goiabada"  # When input


@mark.parametrize(
    "input",
    [3, 6, 9, 12, 18]
)
def test_should_be_goiabada_with_multiples_of_5(input):
    assert brincadeira(input) == "Queijo"  # When input

@mark.parametrize(
    "input, expected",
    [(1, 1), (2, 2), (3, "Queijo"), (4, 4), (5, "Goiabada")]
)
def test_should_be_goiabada_with_multiples_of_5(input, expected):
    assert brincadeira(input) == expected  # When input


@mark.xfail
def test_must_fail():
    assert brincadeira(20) != "Goiabada"  # When input
