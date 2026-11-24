"""A simple multiple-choice quiz for Stage 1."""

from collections.abc import Callable, Iterable, Sequence
from typing import TypedDict, Union, Callable, Iterable, Sequence, Dict
from typing import Union
from typing import Optional
class Question(TypedDict):
    question: str
    options: Dict[str, str]
    correct_answer: str


QUESTIONS: tuple[Question, ...] = (
    {
        "question": "Which Python keyword defines a function?",
        "options": {
            "A": "func",
            "B": "def",
            "C": "function",
            "D": "define",
        },
        "correct_answer": "B",
    },
    {
        "question": "Which data type stores key-value pairs in Python?",
        "options": {
            "A": "list",
            "B": "tuple",
            "C": "dictionary",
            "D": "string",
        },
        "correct_answer": "C",
    },
    {
        "question": "Which operator checks whether two values are equal?",
        "options": {
            "A": "=",
            "B": "!=",
            "C": "is",
            "D": "==",
        },
        "correct_answer": "D",
    },
    {
        "question": "Which list method adds an item to the end of a list?",
        "options": {
            "A": "append()",
            "B": "add()",
            "C": "push()",
            "D": "insert_end()",
        },
        "correct_answer": "A",
    },
    {
        "question": "What does len('quiz') return?",
        "options": {
            "A": "3",
            "B": "4",
            "C": "5",
            "D": "An error",
        },
        "correct_answer": "B",
    },
)


def is_correct_answer(answer: str, correct_answer: str) -> bool:
    """Return whether an A-D answer matches, ignoring case and outer spaces."""
    return answer.strip().upper() == correct_answer


def calculate_score(results: Iterable[bool]) -> tuple[int, int]:
    """Return the number of correct answers and the number of questions."""
    results = tuple(results)
    return sum(results), len(results)


def play_quiz(
     questions: Sequence[Question] = QUESTIONS,
    input_fn: Union[Callable[[str], str], None] = None,
    output_fn: Union[Callable[[str], None], None] = None,) -> tuple[int, int]:
    """Run one quiz round and return the correct and total question counts."""
    if input_fn is None:
        input_fn = input
    if output_fn is None:
        output_fn = print

    output_fn("Welcome to the quiz!")
    results = []

    for number, question in enumerate(questions, start=1):
        output_fn(f"\nQuestion {number}: {question['question']}")
        for label, choice in question["options"].items():
            output_fn(f"{label}) {choice}")

        answer = input_fn("Your answer: ")
        correct = is_correct_answer(answer, question["correct_answer"])
        results.append(correct)

        if correct:
            output_fn("Correct!")
        else:
            correct_label = question["correct_answer"]
            correct_choice = question["options"][correct_label]
            output_fn(f"Not quite. The correct answer is {correct_label}) {correct_choice}.")

    score, total = calculate_score(results)
    output_fn(f"\nYou scored {score} out of {total}.")
    return score, total


if __name__ == "__main__":
    play_quiz()
