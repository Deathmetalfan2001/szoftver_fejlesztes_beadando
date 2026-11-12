from unittest.mock import Mock

import pytest

from quiz import QUESTIONS, calculate_score, is_correct_answer, play_quiz


@pytest.mark.parametrize(
    ("answer", "correct_answer"),
    [
        ("A", "A"),
    ],
)
def test_correct_answer_ignores_case_and_surrounding_spaces(answer, correct_answer):
    assert is_correct_answer(answer, correct_answer)


@pytest.mark.parametrize("answer", ["", " "])
def test_empty_or_invalid_answer_is_incorrect(answer):
    assert not is_correct_answer(answer, "B")


def test_calculate_score_returns_correct_and_total_counts():
    assert calculate_score([True, False, True, False, True]) == (3, 5)


def test_calculate_score_handles_no_questions():
    assert calculate_score([]) == (0, 0)


def test_play_quiz_shows_choices_gives_feedback_and_asks_once_per_question():
    answers = Mock(side_effect=[" b ", "X", "", "A", " b "])
    output = []

    result = play_quiz(input_fn=answers, output_fn=output.append)

    assert result == (3, 5)
    assert answers.call_count == len(QUESTIONS)
    displayed = "\n".join(output)
    assert "A) func" in displayed
    assert "B) def" in displayed
    assert "Correct!" in displayed
    assert "Not quite. The correct answer is C) dictionary." in displayed
    assert "You scored 3 out of 5." in displayed
