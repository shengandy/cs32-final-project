# Writing Assistant

This is Andy Sheng's final project for CS32.

## Project Description
Writing Assistant is a command-line Python program that analyzes a piece of writing and gives revision-oriented feedback.

The program helps users identify:
- repeated words
- overly long sentences
- weak words
- weak phrases
- possible stronger replacements

It also calculates basic text statistics, including word count, sentence count, average word length, average sentence length, lexical diversity, and a simple readability label.

The goal of the project is to help a user quickly review a paragraph and notice places where the writing may be repetitive, vague, or weaker than it could be.

## Files
- `project.py` - main program and user interaction
- `helpers.py` - helper functions for text analysis
- `dictionary.py` - weak-word lists and replacement suggestions
- `test_project.py` - tests for the helper functions

## How to Run
Run the program with:

```bash
python project.py
