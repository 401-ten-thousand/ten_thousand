import pytest
from ten_thousand.game_logic import GameLogic
from ten_thousand.game import Game


def extract_elements(lines, prefix, transform=lambda x: x):
    """"""
    elements = []
    for line in lines:
        if line.startswith(prefix):
            element = line[len(prefix):].strip()
            elements.append(transform(element))
    return elements


def get_inputs(lines):
    return extract_elements(lines, "> ")


def get_mock_rolls(lines):
    # TODO: Change the "You rolled " to "*** "
    return extract_elements(lines, "You rolled ", lambda x: tuple(int(num) for num in x if num.isnumeric()))


def compare_output_and_expected(captured_output, lines):
    captured_output = captured_output.split("\n")

    for actual_line, expected_line in zip(captured_output, lines):
        assert actual_line.strip() == expected_line.strip()


@pytest.mark.parametrize(
    "test_input",
    [
        "tests/sims/fireball_sword_then_win.sim.txt",
    ],
)
def test_all(monkeypatch, capsys, test_input):
    with open(test_input, "r") as f:
        lines = f.readlines()

        # follows a pattern to capture a list of inputs
        inputs = get_inputs(lines)

        # follows a pattern to capture the mock rolls to be used in the mock roller
        mock_rolls = get_mock_rolls(lines)

    def mock_input(prompt):
        response = inputs.pop(0)
        print(prompt, response, sep="")
        return response

    monkeypatch.setattr("builtins.input", mock_input)

    test_instance = GameLogic(mock_rolls)

    # TODO: Maybe change, depends on how your game exits
    # for games that use a `exit()` call
    with pytest.raises(SystemExit):
        play(test_instance.mock_roller)

    captured_output = capsys.readouterr().out  # everything that's printed to the terminal
    compare_output_and_expected(captured_output, lines)
