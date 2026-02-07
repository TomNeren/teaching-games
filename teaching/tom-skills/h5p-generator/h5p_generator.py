#!/usr/bin/env python3
"""
H5P Content Generator

A Python library for programmatically creating H5P content packages.
Supports: Multiple Choice, Fill in the Blanks, Flashcards, True/False, Quiz (Question Set)

Usage:
    from h5p_generator import H5PGenerator, MultipleChoice, FillInBlanks, Flashcard

    # Create a multiple choice question
    mc = MultipleChoice(
        question="What is the capital of France?",
        answers=["Paris", "London", "Berlin", "Madrid"],
        correct=0  # Index of correct answer
    )

    # Generate H5P file
    generator = H5PGenerator()
    generator.create_multichoice("capitals_quiz", mc)

Author: Claude Code Session 2026-01-24
License: MIT
"""

import json
import os
import zipfile
import tempfile
import shutil
from dataclasses import dataclass, field
from typing import List, Optional, Union
from pathlib import Path
from datetime import datetime
import uuid


# =============================================================================
# Data Classes for Content Types
# =============================================================================

@dataclass
class MultipleChoice:
    """A multiple choice question."""
    question: str
    answers: List[str]
    correct: Union[int, List[int]]  # Index(es) of correct answer(s)
    tip: Optional[str] = None
    feedback_correct: str = "Richtig!"
    feedback_incorrect: str = "Leider falsch."
    single_answer: bool = True  # True = radio buttons, False = checkboxes

    def to_h5p_content(self) -> dict:
        """Convert to H5P content.json format for H5P.MultiChoice."""
        answers = []
        correct_indices = [self.correct] if isinstance(self.correct, int) else self.correct

        for i, answer_text in enumerate(self.answers):
            answers.append({
                "correct": i in correct_indices,
                "text": f"<div>{answer_text}</div>\n",
                "tpiAndFeedback": {
                    "tip": "",
                    "chosenFeedback": "",
                    "notChosenFeedback": ""
                }
            })

        return {
            "media": {"type": {"params": {}}, "disableImageZooming": False},
            "answers": answers,
            "overallFeedback": [
                {"from": 0, "to": 100, "feedback": ""}
            ],
            "behaviour": {
                "enableRetry": True,
                "enableSolutionsButton": True,
                "enableCheckButton": True,
                "type": "auto",
                "singlePoint": False,
                "randomAnswers": True,
                "showSolutionsRequiresInput": True,
                "confirmCheckDialog": False,
                "confirmRetryDialog": False,
                "autoCheck": False,
                "passPercentage": 100,
                "showScorePoints": True
            },
            "UI": {
                "checkAnswerButton": "Überprüfen",
                "submitAnswerButton": "Absenden",
                "showSolutionButton": "Lösung anzeigen",
                "tryAgainButton": "Nochmal versuchen",
                "tipsLabel": "Hinweis anzeigen",
                "scoreBarLabel": "Du hast :num von :total Punkten erreicht.",
                "tipAvailable": "Hinweis verfügbar",
                "feedbackAvailable": "Feedback verfügbar",
                "readFeedback": "Feedback lesen",
                "wrongAnswer": "Falsche Antwort",
                "correctAnswer": "Richtige Antwort",
                "shouldCheck": "Hätte ausgewählt werden sollen",
                "shouldNotCheck": "Hätte nicht ausgewählt werden sollen",
                "noInput": "Bitte antworte, bevor du die Lösung ansiehst",
                "a11yCheck": "Die Antworten überprüfen. Die Auswahl wird als richtig, falsch oder zu wählen markiert.",
                "a11yShowSolution": "Die Lösung anzeigen. Die Aufgabe wird mit der korrekten Lösung markiert.",
                "a11yRetry": "Die Aufgabe wiederholen. Alle Versuche werden zurückgesetzt und die Aufgabe startet erneut."
            },
            "confirmCheck": {
                "header": "Beenden?",
                "body": "Ganz sicher beenden?",
                "cancelLabel": "Abbrechen",
                "confirmLabel": "Beenden"
            },
            "confirmRetry": {
                "header": "Nochmal versuchen?",
                "body": "Ganz sicher nochmal versuchen?",
                "cancelLabel": "Abbrechen",
                "confirmLabel": "Bestätigen"
            },
            "question": f"<p>{self.question}</p>\n"
        }


@dataclass
class FillInBlanks:
    """A fill in the blanks exercise."""
    task_description: str
    text_with_blanks: str  # Use *correct answer* or *answer1/answer2* for alternatives
    case_sensitive: bool = False
    feedback_correct: str = "Richtig!"
    feedback_incorrect: str = "Leider falsch."

    def to_h5p_content(self) -> dict:
        """Convert to H5P content.json format for H5P.Blanks."""
        return {
            "media": {"type": {"params": {}}, "disableImageZooming": False},
            "text": f"<p>{self.text_with_blanks}</p>\n",
            "overallFeedback": [
                {"from": 0, "to": 100, "feedback": ""}
            ],
            "showSolutions": "Lösung anzeigen",
            "tryAgain": "Nochmal versuchen",
            "checkAnswer": "Überprüfen",
            "submitAnswer": "Absenden",
            "notFilledOut": "Bitte fülle alle Lücken aus, um die Lösung zu sehen",
            "answerIsCorrect": "':ans' ist richtig",
            "answerIsWrong": "':ans' ist falsch",
            "answeredCorrectly": "Richtig beantwortet",
            "answeredIncorrectly": "Falsch beantwortet",
            "solutionLabel": "Richtige Antwort:",
            "inputLabel": "Lücke @num von @total",
            "inputHasTipLabel": "Hinweis verfügbar",
            "tipLabel": "Hinweis",
            "behaviour": {
                "enableRetry": True,
                "enableSolutionsButton": True,
                "enableCheckButton": True,
                "caseSensitive": self.case_sensitive,
                "showSolutionsRequiresInput": True,
                "autoCheck": False,
                "separateLines": False,
                "confirmCheckDialog": False,
                "confirmRetryDialog": False,
                "acceptSpellingErrors": False
            },
            "scoreBarLabel": "Du hast :num von :total Punkten erreicht.",
            "a11yCheck": "Prüfe die Antworten. Die Eingaben werden als richtig oder falsch markiert.",
            "a11yShowSolution": "Zeige die Lösung. Die Aufgabe wird mit den korrekten Antworten gefüllt.",
            "a11yRetry": "Wiederhole die Aufgabe. Alle Eingaben werden zurückgesetzt.",
            "a11yCheckingModeHeader": "Überprüfungsmodus",
            "confirmCheck": {
                "header": "Beenden?",
                "body": "Ganz sicher beenden?",
                "cancelLabel": "Abbrechen",
                "confirmLabel": "Beenden"
            },
            "confirmRetry": {
                "header": "Nochmal versuchen?",
                "body": "Ganz sicher nochmal versuchen?",
                "cancelLabel": "Abbrechen",
                "confirmLabel": "Bestätigen"
            }
        }


@dataclass
class Flashcard:
    """A single flashcard with front and back."""
    front: str  # Question/prompt
    back: str   # Answer
    image_path: Optional[str] = None  # Optional image for front

    def to_h5p_card(self) -> dict:
        """Convert to H5P card format."""
        card = {
            "text": self.front,
            "answer": self.back,
        }
        # Image handling would go here if needed
        return card


@dataclass
class FlashcardSet:
    """A set of flashcards."""
    title: str
    cards: List[Flashcard]
    description: str = ""

    def to_h5p_content(self) -> dict:
        """Convert to H5P content.json format for H5P.Flashcards."""
        return {
            "title": f"<p>{self.title}</p>",
            "description": self.description,
            "cards": [card.to_h5p_card() for card in self.cards],
            "showSolutions": "Lösung anzeigen",
            "showFront": "Vorderseite zeigen",
            "checkAnswerText": "Überprüfen",
            "submitAnswerText": "Absenden",
            "answeredCorrectly": "Richtig!",
            "answeredIncorrectly": "Falsch",
            "notFilledOut": "Bitte gib eine Antwort ein",
            "progressText": "Karte @card von @total",
            "a11yShowSolution": "Zeige die Lösung",
            "a11yCardPrefix": "Karteikarte. ",
            "a11yShowCardFront": "Zeige die Vorderseite",
            "a11yFlipCardSuffix": "Drehe die Karte um",
            "a11yAnswerModeSuffix": "Antworte auf diese Karte"
        }


@dataclass
class TrueFalse:
    """A true/false question."""
    question: str
    correct: bool  # True if the statement is true
    feedback_correct: str = "Richtig!"
    feedback_incorrect: str = "Leider falsch."

    def to_h5p_content(self) -> dict:
        """Convert to H5P content.json format for H5P.TrueFalse."""
        return {
            "media": {"type": {"params": {}}, "disableImageZooming": False},
            "correct": "true" if self.correct else "false",
            "behaviour": {
                "enableRetry": True,
                "enableSolutionsButton": True,
                "enableCheckButton": True,
                "confirmCheckDialog": False,
                "confirmRetryDialog": False,
                "autoCheck": False
            },
            "l10n": {
                "trueText": "Wahr",
                "falseText": "Falsch",
                "score": "Du hast @score von @total Punkten erreicht",
                "checkAnswer": "Überprüfen",
                "submitAnswer": "Absenden",
                "showSolutionButton": "Lösung anzeigen",
                "tryAgain": "Nochmal versuchen",
                "wrongAnswerMessage": "Falsche Antwort",
                "correctAnswerMessage": "Richtige Antwort",
                "scoreBarLabel": "Du hast :num von :total Punkten erreicht.",
                "a11yCheck": "Prüfe die Antwort. Sie wird als richtig oder falsch markiert.",
                "a11yShowSolution": "Zeige die Lösung. Die Aufgabe wird mit der korrekten Lösung angezeigt.",
                "a11yRetry": "Wiederhole die Aufgabe. Die Eingabe wird zurückgesetzt."
            },
            "confirmCheck": {
                "header": "Beenden?",
                "body": "Ganz sicher beenden?",
                "cancelLabel": "Abbrechen",
                "confirmLabel": "Beenden"
            },
            "confirmRetry": {
                "header": "Nochmal versuchen?",
                "body": "Ganz sicher nochmal versuchen?",
                "cancelLabel": "Abbrechen",
                "confirmLabel": "Bestätigen"
            },
            "question": f"<p>{self.question}</p>\n",
            "feedbacks": {
                "correct": self.feedback_correct,
                "wrong": self.feedback_incorrect
            }
        }


@dataclass
class QuizQuestion:
    """A question for a Quiz (Question Set)."""
    content: Union[MultipleChoice, TrueFalse, FillInBlanks]
    library: str = ""  # Auto-detected if empty

    def get_library(self) -> str:
        if self.library:
            return self.library
        if isinstance(self.content, MultipleChoice):
            return "H5P.MultiChoice 1.16"
        elif isinstance(self.content, TrueFalse):
            return "H5P.TrueFalse 1.8"
        elif isinstance(self.content, FillInBlanks):
            return "H5P.Blanks 1.14"
        return "H5P.MultiChoice 1.16"


@dataclass
class Quiz:
    """A quiz (question set) containing multiple questions."""
    title: str
    questions: List[QuizQuestion]
    pass_percentage: int = 50
    randomize: bool = True

    def to_h5p_content(self) -> dict:
        """Convert to H5P content.json format for H5P.QuestionSet."""
        question_list = []
        for q in self.questions:
            question_list.append({
                "params": q.content.to_h5p_content(),
                "library": q.get_library(),
                "metadata": {"contentType": q.get_library().split()[0]},
                "subContentId": str(uuid.uuid4())
            })

        return {
            "introPage": {
                "showIntroPage": True,
                "startButtonText": "Quiz starten",
                "title": self.title,
                "introduction": ""
            },
            "progressType": "dots",
            "passPercentage": self.pass_percentage,
            "disableBackwardsNavigation": False,
            "randomQuestions": self.randomize,
            "endGame": {
                "showResultPage": True,
                "showSolutionButton": True,
                "showRetryButton": True,
                "noResultMessage": "Quiz beendet",
                "message": "Dein Ergebnis:",
                "overallFeedback": [
                    {"from": 0, "to": 50, "feedback": "Versuch es noch einmal!"},
                    {"from": 51, "to": 80, "feedback": "Gut gemacht!"},
                    {"from": 81, "to": 100, "feedback": "Ausgezeichnet!"}
                ],
                "solutionButtonText": "Lösung anzeigen",
                "retryButtonText": "Nochmal versuchen",
                "finishButtonText": "Beenden",
                "submitButtonText": "Absenden",
                "showAnimations": True,
                "skippable": False,
                "skipButtonText": "Video überspringen"
            },
            "override": {
                "checkButton": True,
                "showSolutionButton": "on",
                "retryButton": "on"
            },
            "texts": {
                "prevButton": "Zurück",
                "nextButton": "Weiter",
                "finishButton": "Beenden",
                "submitButton": "Absenden",
                "textualProgress": "Frage @current von @total",
                "jumpToQuestion": "Frage %d von %total",
                "questionLabel": "Frage",
                "readSpeakerProgress": "Frage @current von @total",
                "unansweredText": "Unbeantwortet",
                "answeredText": "Beantwortet",
                "currentQuestionText": "Aktuelle Frage",
                "navigationLabel": "Fragen"
            },
            "questions": question_list
        }


# =============================================================================
# H5P Generator Class
# =============================================================================

class H5PGenerator:
    """Generator for H5P content packages."""

    # Library versions (these should match your H5P installation)
    LIBRARY_VERSIONS = {
        "H5P.MultiChoice": "1.16",
        "H5P.Blanks": "1.14",
        "H5P.Flashcards": "1.7",
        "H5P.TrueFalse": "1.8",
        "H5P.QuestionSet": "1.20"
    }

    def __init__(self, output_dir: str = "."):
        """Initialize the generator with an output directory."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _create_h5p_json(self, title: str, main_library: str) -> dict:
        """Create the h5p.json metadata file."""
        lib_name, lib_version = main_library.split()
        major, minor = lib_version.split(".")[:2]

        return {
            "title": title,
            "language": "de",
            "mainLibrary": lib_name,
            "embedTypes": ["div"],
            "license": "U",
            "defaultLanguage": "de",
            "preloadedDependencies": [
                {
                    "machineName": lib_name,
                    "majorVersion": int(major),
                    "minorVersion": int(minor)
                }
            ]
        }

    def _create_h5p_package(
        self,
        filename: str,
        title: str,
        main_library: str,
        content: dict
    ) -> Path:
        """Create an H5P package file."""
        # Create temporary directory for building the package
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Create content directory
            content_dir = temp_path / "content"
            content_dir.mkdir()

            # Write content.json
            with open(content_dir / "content.json", "w", encoding="utf-8") as f:
                json.dump(content, f, ensure_ascii=False, indent=2)

            # Write h5p.json
            h5p_meta = self._create_h5p_json(title, main_library)
            with open(temp_path / "h5p.json", "w", encoding="utf-8") as f:
                json.dump(h5p_meta, f, ensure_ascii=False, indent=2)

            # Create the .h5p file (which is just a zip)
            output_path = self.output_dir / f"{filename}.h5p"

            with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
                for file_path in temp_path.rglob("*"):
                    if file_path.is_file():
                        arcname = file_path.relative_to(temp_path)
                        zf.write(file_path, arcname)

            return output_path

    def create_multichoice(
        self,
        filename: str,
        question: MultipleChoice,
        title: Optional[str] = None
    ) -> Path:
        """Create a Multiple Choice H5P package."""
        title = title or question.question[:50]
        content = question.to_h5p_content()
        library = f"H5P.MultiChoice {self.LIBRARY_VERSIONS['H5P.MultiChoice']}"
        return self._create_h5p_package(filename, title, library, content)

    def create_fill_in_blanks(
        self,
        filename: str,
        exercise: FillInBlanks,
        title: Optional[str] = None
    ) -> Path:
        """Create a Fill in the Blanks H5P package."""
        title = title or exercise.task_description[:50]
        content = exercise.to_h5p_content()
        library = f"H5P.Blanks {self.LIBRARY_VERSIONS['H5P.Blanks']}"
        return self._create_h5p_package(filename, title, library, content)

    def create_flashcards(
        self,
        filename: str,
        flashcard_set: FlashcardSet
    ) -> Path:
        """Create a Flashcards H5P package."""
        content = flashcard_set.to_h5p_content()
        library = f"H5P.Flashcards {self.LIBRARY_VERSIONS['H5P.Flashcards']}"
        return self._create_h5p_package(filename, flashcard_set.title, library, content)

    def create_true_false(
        self,
        filename: str,
        question: TrueFalse,
        title: Optional[str] = None
    ) -> Path:
        """Create a True/False H5P package."""
        title = title or question.question[:50]
        content = question.to_h5p_content()
        library = f"H5P.TrueFalse {self.LIBRARY_VERSIONS['H5P.TrueFalse']}"
        return self._create_h5p_package(filename, title, library, content)

    def create_quiz(
        self,
        filename: str,
        quiz: Quiz
    ) -> Path:
        """Create a Quiz (Question Set) H5P package."""
        content = quiz.to_h5p_content()
        library = f"H5P.QuestionSet {self.LIBRARY_VERSIONS['H5P.QuestionSet']}"
        return self._create_h5p_package(filename, quiz.title, library, content)


# =============================================================================
# Convenience Functions
# =============================================================================

def create_quick_quiz(
    filename: str,
    questions: List[dict],
    title: str = "Quiz",
    output_dir: str = "."
) -> Path:
    """
    Create a quiz from a simple list of question dictionaries.

    Args:
        filename: Output filename (without .h5p extension)
        questions: List of question dicts with keys:
            - question: The question text
            - answers: List of answer options
            - correct: Index of correct answer (0-based)
            - type: "mc" (default), "tf", or "blanks"
        title: Quiz title
        output_dir: Output directory

    Returns:
        Path to created .h5p file

    Example:
        create_quick_quiz("my_quiz", [
            {"question": "2+2=?", "answers": ["3", "4", "5"], "correct": 1},
            {"question": "The sky is blue", "correct": True, "type": "tf"}
        ])
    """
    quiz_questions = []

    for q in questions:
        q_type = q.get("type", "mc")

        if q_type == "mc":
            content = MultipleChoice(
                question=q["question"],
                answers=q["answers"],
                correct=q["correct"]
            )
        elif q_type == "tf":
            content = TrueFalse(
                question=q["question"],
                correct=q["correct"]
            )
        elif q_type == "blanks":
            content = FillInBlanks(
                task_description=q.get("description", "Fülle die Lücken aus"),
                text_with_blanks=q["text"]
            )
        else:
            raise ValueError(f"Unknown question type: {q_type}")

        quiz_questions.append(QuizQuestion(content=content))

    quiz = Quiz(title=title, questions=quiz_questions)
    generator = H5PGenerator(output_dir)
    return generator.create_quiz(filename, quiz)


def create_vocabulary_flashcards(
    filename: str,
    vocabulary: List[tuple],
    title: str = "Vokabeln",
    output_dir: str = "."
) -> Path:
    """
    Create flashcards from vocabulary pairs.

    Args:
        filename: Output filename (without .h5p extension)
        vocabulary: List of (front, back) tuples
        title: Flashcard set title
        output_dir: Output directory

    Returns:
        Path to created .h5p file

    Example:
        create_vocabulary_flashcards("german_english", [
            ("Hund", "dog"),
            ("Katze", "cat"),
            ("Vogel", "bird")
        ])
    """
    cards = [Flashcard(front=front, back=back) for front, back in vocabulary]
    flashcard_set = FlashcardSet(title=title, cards=cards)
    generator = H5PGenerator(output_dir)
    return generator.create_flashcards(filename, flashcard_set)


# =============================================================================
# CLI Interface
# =============================================================================

def main():
    """Command-line interface for the H5P generator."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate H5P content packages from JSON files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create from JSON file
  python h5p_generator.py quiz input.json -o output_dir

  # Create sample quiz
  python h5p_generator.py sample -o output_dir

JSON Format for Quiz:
{
    "title": "My Quiz",
    "questions": [
        {
            "question": "What is 2+2?",
            "answers": ["3", "4", "5", "6"],
            "correct": 1,
            "type": "mc"
        },
        {
            "question": "The Earth is flat.",
            "correct": false,
            "type": "tf"
        }
    ]
}

JSON Format for Flashcards:
{
    "title": "Vocabulary",
    "cards": [
        {"front": "Hello", "back": "Hallo"},
        {"front": "Goodbye", "back": "Auf Wiedersehen"}
    ]
}
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Quiz command
    quiz_parser = subparsers.add_parser("quiz", help="Create a quiz from JSON")
    quiz_parser.add_argument("input", help="Input JSON file")
    quiz_parser.add_argument("-o", "--output", default=".", help="Output directory")
    quiz_parser.add_argument("-n", "--name", help="Output filename (without .h5p)")

    # Flashcards command
    flash_parser = subparsers.add_parser("flashcards", help="Create flashcards from JSON")
    flash_parser.add_argument("input", help="Input JSON file")
    flash_parser.add_argument("-o", "--output", default=".", help="Output directory")
    flash_parser.add_argument("-n", "--name", help="Output filename (without .h5p)")

    # Sample command
    sample_parser = subparsers.add_parser("sample", help="Create sample H5P files")
    sample_parser.add_argument("-o", "--output", default=".", help="Output directory")

    args = parser.parse_args()

    if args.command == "quiz":
        with open(args.input, "r", encoding="utf-8") as f:
            data = json.load(f)

        filename = args.name or Path(args.input).stem
        path = create_quick_quiz(
            filename=filename,
            questions=data["questions"],
            title=data.get("title", "Quiz"),
            output_dir=args.output
        )
        print(f"Created: {path}")

    elif args.command == "flashcards":
        with open(args.input, "r", encoding="utf-8") as f:
            data = json.load(f)

        filename = args.name or Path(args.input).stem
        cards = [(c["front"], c["back"]) for c in data["cards"]]
        path = create_vocabulary_flashcards(
            filename=filename,
            vocabulary=cards,
            title=data.get("title", "Flashcards"),
            output_dir=args.output
        )
        print(f"Created: {path}")

    elif args.command == "sample":
        generator = H5PGenerator(args.output)

        # Sample Multiple Choice
        mc = MultipleChoice(
            question="Was ist die Hauptstadt von Deutschland?",
            answers=["München", "Berlin", "Hamburg", "Frankfurt"],
            correct=1
        )
        path = generator.create_multichoice("sample_multichoice", mc)
        print(f"Created: {path}")

        # Sample Fill in the Blanks
        blanks = FillInBlanks(
            task_description="Fülle die Lücken mit den richtigen Wörtern",
            text_with_blanks="Die Sonne geht im *Osten* auf und im *Westen* unter."
        )
        path = generator.create_fill_in_blanks("sample_blanks", blanks)
        print(f"Created: {path}")

        # Sample Flashcards
        flashcards = FlashcardSet(
            title="Deutsche Vokabeln",
            cards=[
                Flashcard("apple", "der Apfel"),
                Flashcard("house", "das Haus"),
                Flashcard("car", "das Auto"),
            ]
        )
        path = generator.create_flashcards("sample_flashcards", flashcards)
        print(f"Created: {path}")

        # Sample True/False
        tf = TrueFalse(
            question="Berlin ist die Hauptstadt von Deutschland.",
            correct=True
        )
        path = generator.create_true_false("sample_truefalse", tf)
        print(f"Created: {path}")

        # Sample Quiz
        quiz = Quiz(
            title="Beispiel-Quiz",
            questions=[
                QuizQuestion(MultipleChoice(
                    question="Wie viele Bundesländer hat Deutschland?",
                    answers=["14", "15", "16", "17"],
                    correct=2
                )),
                QuizQuestion(TrueFalse(
                    question="Der Rhein ist der längste Fluss Deutschlands.",
                    correct=True
                )),
                QuizQuestion(MultipleChoice(
                    question="Welche Farben hat die deutsche Flagge?",
                    answers=[
                        "Schwarz, Rot, Gold",
                        "Rot, Weiß, Blau",
                        "Schwarz, Weiß, Rot",
                        "Grün, Weiß, Rot"
                    ],
                    correct=0
                ))
            ]
        )
        path = generator.create_quiz("sample_quiz", quiz)
        print(f"Created: {path}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
