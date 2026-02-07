# H5P Content Generator

A Python library and CLI tool for programmatically creating H5P interactive content packages.

## Supported Content Types

| Type | Description | Class |
|------|-------------|-------|
| Multiple Choice | Single or multiple answer questions | `MultipleChoice` |
| Fill in the Blanks | Text with gaps to fill | `FillInBlanks` |
| True/False | Binary choice questions | `TrueFalse` |
| Flashcards | Learning cards with front/back | `FlashcardSet` |
| Quiz (Question Set) | Combines multiple question types | `Quiz` |

## Installation

No dependencies required - uses Python standard library only.

```bash
# Just copy the script
cp h5p_generator.py /your/project/
```

## Quick Start

### Command Line

```bash
# Create sample files to see the format
python h5p_generator.py sample -o ./output

# Create quiz from JSON
python h5p_generator.py quiz my_quiz.json -o ./output

# Create flashcards from JSON
python h5p_generator.py flashcards vocab.json -o ./output
```

### Python API

```python
from h5p_generator import (
    H5PGenerator,
    MultipleChoice,
    FillInBlanks,
    TrueFalse,
    Flashcard,
    FlashcardSet,
    Quiz,
    QuizQuestion
)

# Initialize generator
generator = H5PGenerator(output_dir="./output")

# Create a multiple choice question
mc = MultipleChoice(
    question="Was ist die Hauptstadt von Frankreich?",
    answers=["London", "Paris", "Berlin", "Madrid"],
    correct=1  # Index of correct answer (0-based)
)
generator.create_multichoice("france_capital", mc)

# Create fill in the blanks
blanks = FillInBlanks(
    task_description="Ergänze die fehlenden Wörter",
    text_with_blanks="Die Erde dreht sich um die *Sonne*."
)
generator.create_fill_in_blanks("solar_system", blanks)

# Create flashcards
flashcards = FlashcardSet(
    title="English-German Vocabulary",
    cards=[
        Flashcard("hello", "hallo"),
        Flashcard("goodbye", "auf Wiedersehen"),
        Flashcard("thank you", "danke"),
    ]
)
generator.create_flashcards("english_german", flashcards)

# Create a quiz with mixed question types
quiz = Quiz(
    title="Geographie Quiz",
    questions=[
        QuizQuestion(MultipleChoice(
            question="Wie viele Kontinente gibt es?",
            answers=["5", "6", "7", "8"],
            correct=2
        )),
        QuizQuestion(TrueFalse(
            question="Australien ist sowohl ein Land als auch ein Kontinent.",
            correct=True
        )),
    ]
)
generator.create_quiz("geography_quiz", quiz)
```

### Convenience Functions

```python
from h5p_generator import create_quick_quiz, create_vocabulary_flashcards

# Quick quiz from simple data
create_quick_quiz("math_quiz", [
    {"question": "2 + 2 = ?", "answers": ["3", "4", "5"], "correct": 1},
    {"question": "10 ist größer als 5", "correct": True, "type": "tf"},
], title="Mathe Quiz")

# Flashcards from word pairs
create_vocabulary_flashcards("animals", [
    ("dog", "der Hund"),
    ("cat", "die Katze"),
    ("bird", "der Vogel"),
], title="Tiere")
```

## JSON Format

### Quiz JSON

```json
{
    "title": "Mein Quiz",
    "questions": [
        {
            "question": "Frage hier?",
            "answers": ["Antwort A", "Antwort B", "Antwort C"],
            "correct": 0,
            "type": "mc"
        },
        {
            "question": "Wahr oder Falsch Aussage",
            "correct": true,
            "type": "tf"
        },
        {
            "description": "Fülle die Lücken",
            "text": "Der Himmel ist *blau* und das Gras ist *grün*.",
            "type": "blanks"
        }
    ]
}
```

### Flashcards JSON

```json
{
    "title": "Vokabeln",
    "cards": [
        {"front": "Hello", "back": "Hallo"},
        {"front": "World", "back": "Welt"}
    ]
}
```

## Fill in the Blanks Syntax

Use asterisks to mark blanks:
- `*answer*` - Single correct answer
- `*answer1/answer2*` - Multiple acceptable answers

Example:
```
"Die Hauptstadt von Deutschland ist *Berlin*."
"Wasser besteht aus *H2O/Wasserstoff und Sauerstoff*."
```

## Output

The generator creates `.h5p` files which are ZIP archives containing:
```
my_content.h5p
├── h5p.json          # Metadata
└── content/
    └── content.json  # Actual content
```

These files can be imported into:
- Moodle (with H5P plugin)
- WordPress (with H5P plugin)
- Drupal (with H5P module)
- H5P.com
- Lumi Desktop App

## Language

All UI strings are in German by default. To customize, modify the `to_h5p_content()` methods in the respective classes.

## Limitations

- Images are not yet supported (planned)
- Audio/Video content types not implemented
- Library files are not included (H5P platform provides these)

## Integration with Claude / LLMs

This generator works well with LLM-generated content:

```python
# Example: Generate quiz from Claude output
quiz_data = {
    "title": "Von Claude generiertes Quiz",
    "questions": claude_generated_questions  # List of question dicts
}

create_quick_quiz("ai_quiz", quiz_data["questions"], quiz_data["title"])
```

## License

MIT License - feel free to use and modify.

---

Created: 2026-01-24
