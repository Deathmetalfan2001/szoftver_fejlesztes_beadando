# Project: Build a Quiz Game with TDD

## Goal

Build a small, command-line quiz game in Python. You will practice breaking a
problem into testable pieces and using the **red-green-refactor** cycle:

1. **Red:** write a test for one small behavior and run it. Confirm that it
   fails for the expected reason.
2. **Green:** write the simplest code that makes the test pass.
3. **Refactor:** improve the code without changing its behavior, then run the
   tests again.

Do not write the whole program first and add tests afterward. Keep the tests
passing as you build the game one behavior at a time.

## Stage 1: Build the basic quiz

Create a terminal game that asks the player a series of questions, checks their
answers, keeps track of their score, and displays the final result.

The first version of the game must:

- Include at least **five** questions, each with one correct answer.
- Give each question exactly four possible answers, labeled `A`, `B`, `C`, and
  `D`, with only one correct answer.
- Display one question and its four choices at a time, then ask the player to
  select an answer by entering its label.
- Accept lowercase labels and surrounding whitespace (for example, ` b ` is
  accepted as `B`). An empty or other invalid selection is incorrect.
- Tell the player whether each answer was correct. If it was incorrect, show
  the correct choice after the player has answered.
- Ask each question only once and calculate the final score correctly.
- Display the final score as both a number correct and a total, for example,
  `You scored 3 out of 5.`
- Run from the terminal without requiring any third-party packages.

For this stage, you may choose the questions and their topics. Keep the
questions, four choices, and correct choice in a form that is easy to review
and update. The questions may be stored in the Python code; loading them from a
file is part of Stage 2.

## Example interaction

The wording and layout are up to you, but the game should behave roughly like
this:

```text
Welcome to the quiz!

Question 1: What is the capital of France?
A) Berlin
B) Paris
C) Rome
D) Madrid
Your answer:  b
Correct!

Question 2: How many sides does a triangle have?
A) 2
B) 3
C) 4
D) 5
Your answer: C
Not quite. The correct answer is B) 3.

...
You scored 1 out of 5.
```

## Suggested structure

You can organize the program differently, but keep the game logic separate
from terminal input and output where practical. In particular, make answer
checking and score calculation testable without playing the interactive game.

For example, you might use:

- `quiz.py` for the questions and game code.
- `test_quiz.py` for automated tests.
- Small functions for checking a selected option, calculating a score, and
  running the interaction.

These are suggestions, not required function names or a required design.

## Stage 1 TDD milestones

Work through small steps. For each step, write and run a test before adding the
corresponding implementation.

1. **Question data:** each question has four labeled choices and one correct
   choice.
2. **Answer checking:** selecting the correct label is correct; selecting a
   different label is incorrect.
3. **Input normalization:** lowercase labels and surrounding whitespace are
   accepted; blank or invalid input is incorrect.
4. **Scoring:** calculate the number of correct answers and the total.
5. **Question flow:** present every question and its choices once, in order,
   and check the selected labels.
6. **Feedback and final result:** provide per-question feedback and display the
   final score.

After each small change, run the tests. Refactor only when the tests are
passing, and run them again after refactoring.

## Stage 1 testing

Use Python's built-in `unittest` framework; no test dependency needs to be
installed. From the project directory, run:

```bash
python -m unittest -v
```

Write focused tests for correct and incorrect choices, blank and invalid
selections, case/whitespace normalization, score calculation, and the complete
question flow. For tests of terminal interaction, use the standard library's
`unittest.mock` tools to provide input and capture output instead of requiring
a person to play the game.

## Stage 1 definition of done

- The game can be started from the terminal and completes a full quiz.
- All the requirements above are satisfied.
- Automated tests cover the important game rules and pass.
- The tests were developed using the red-green-refactor cycle.
- The code uses clear names and avoids unnecessary duplication.

## Stage 2: Load multiple-choice questions from a file

Extend the game so that it reads its questions from a data file when the game
starts, instead of keeping the questions in the Python source code. Add a
separate module for loading and validating the question data. Use either JSON
or XML; choose one format for your implementation.

The Stage 2 game must:

- Load at least five questions from the data file at startup.
- Give each question exactly four possible answers, labeled `A`, `B`, `C`, and
  `D`.
- Store the correct option's label in a dedicated `correct_answer` field,
  separate from the question text and options.
- Give each question a `difficulty` of `easy`, `medium`, or `hard`.
- Show all four options and ask the player to enter a label. Accept lowercase
  labels and surrounding whitespace (for example, ` b ` is accepted as `B`).
- Count a question as correct only when the selected label matches its
  `correct_answer`. An empty or other invalid selection is incorrect; do not
  ask that question again.
- Continue to show whether the answer was correct and reveal the correct
  option after the player has answered.
- Display the number of correct answers and the weighted score at the end.

Use the following weights:

| Difficulty | Weight |
| --- | ---: |
| easy | 1 |
| medium | 2 |
| hard | 3 |

For each correctly answered question, add that question's weight to the earned
score. Incorrect answers earn zero points. The maximum score is the sum of the
weights of all questions in the loaded quiz. Show the weighted result as earned
points out of the maximum and as a percentage. For example, if the quiz has a
maximum of 10 points and the player earns 7, display `7 out of 10 (70%)`.
Calculate the percentage as earned points divided by the maximum points,
multiplied by 100, and round it to the nearest whole number.

### Question file format

The following example shows the required data in JSON. If you choose XML,
represent the same fields: question text, four labeled options, the correct
option label, and difficulty.

```json
{
  "questions": [
    {
      "question": "What is the capital of France?",
      "options": {
        "A": "Berlin",
        "B": "Paris",
        "C": "Rome",
        "D": "Madrid"
      },
      "correct_answer": "B",
      "difficulty": "easy"
    }
  ]
}
```

The example shows one question; your data file must contain at least five.
Keep the correct answer in the `correct_answer` field rather than encoding it
in the option text or relying on its position.

The loader should report a clear error if the file cannot be read or its
contents are invalid. At minimum, validate that the quiz has at least five
questions, each question has text, exactly four options labeled `A` through
`D`, a `correct_answer` that refers to one of those labels, and a supported
difficulty. Do not silently skip malformed questions or substitute default
values.

### Stage 2 TDD milestones

Continue using red-green-refactor. Add tests before implementing each behavior:

1. **Load valid data:** load a quiz with questions, options, correct-answer
   labels, and difficulty levels from the chosen file format.
2. **Reject invalid data:** cover a missing/unreadable file and malformed
   question data, including missing fields, an incorrect number of options,
   an invalid correct-answer label, and an unsupported difficulty.
3. **Present choices:** show all four options and accept a normalized `A`-`D`
   selection.
4. **Calculate weighted score:** check each difficulty weight, ensure incorrect
   answers earn no points, and calculate the maximum and percentage correctly.
5. **Complete a file-backed game:** verify that loaded questions are presented
   once and the final correct-answer count and weighted score are displayed.

Keep file loading, quiz rules, and terminal interaction separate enough to test
them independently. Use temporary files in loader tests so tests do not depend
on the working directory or a student's personal question file.

### Stage 2 definition of done

- The game loads its questions from the selected JSON or XML file at startup.
- Invalid or unreadable question data produces a clear error.
- The game meets the multiple-choice and difficulty-weighting requirements.
- Automated tests cover the loader, validation, game behavior, and weighted
  score, and pass using `python -m unittest -v`.
- Tests were developed using the red-green-refactor cycle.

## Stage 3: Improve the quiz engine

Update the game engine to support multiple rounds, randomized question order,
per-question timing, and adaptive question weights. Continue to load questions
from the Stage 2 data file.

The Stage 3 game must:

- Shuffle the available questions at the start of every round.
- Measure how long the player takes to answer each question, starting when the
  question and choices are displayed and ending when the player submits a
  selection. Use elapsed time in seconds.
- Keep the elapsed time and whether the answer was correct for each question
  in the current round.
- At the end of each round, ask whether the player wants to play again. If the
  player declines, finish the game. If the player agrees, start another round
  using the available questions.
- Calculate the average response time for the round using all questions
  answered in that round, including incorrect answers.
- Mark a question as eligible to be left out of the next round when the player
  answered it correctly in less time than the round's average response time.
  An answer equal to the average is not "faster than average."
- Leave an eligible question out of the next round only if at least five other
  questions will remain. Never start a round with fewer than five questions.
  If removing an eligible question would leave fewer than five, keep it in the
  question pool.
- For the first round, use the Stage 2 difficulty weights: easy = 1, medium =
  2, hard = 3. For each later round, determine a question's weight from its
  result in the immediately previous round: increase its difficulty weight by
  one if the player missed it or took at least 10 seconds to answer it;
  otherwise use its normal difficulty weight. A missed and slow answer still
  increases the weight by only one.
- Calculate the earned and maximum weighted scores for each round using that
  round's question weights. A correct answer earns its question's weight; an
  incorrect answer earns zero. Continue to display the number correct and the
  weighted score.

Use the average response time from each round to decide which correctly and
quickly answered questions can be left out of future rounds. Retire an eligible
question from the question pool only when at least five questions will remain;
retired questions do not return in later rounds. The timing and correctness
from the previous round also determine the weights in the next round for
questions still in the pool.

### Stage 3 TDD milestones

Write tests before implementing each behavior:

1. **Question order:** each round contains the available questions once, in a
   shuffled order.
2. **Response timing:** record elapsed time for each question, including
   incorrect and invalid selections.
3. **Average and fast answers:** calculate the round average and identify only
   correct answers strictly faster than that average.
4. **Question pool:** leave eligible questions out only when at least five
   other questions remain; otherwise keep enough questions for the next round.
5. **Dynamic weights:** increase the next-round weight by one for a previous
   miss or an answer taking at least 10 seconds; otherwise preserve the
   difficulty weight.
6. **Replay flow:** ask to play again after each round, then either start a new
   round with the updated pool and weights or exit.
7. **Round results:** verify the correct-answer count and weighted score use
   the questions and weights for that round.

Test timing without real delays by controlling or substituting the clock used
by the game. Also test the minimum-question rule with pools where excluding
fast, correct answers would leave either five or fewer than five questions.
