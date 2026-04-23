from helpers import (
    generate_summary,
    suggest_synonyms,
    suggest_phrase_replacements,
)


def print_header(title):
    print(f"\n--- {title} ---")


def print_stats(stats):
    print_header("TEXT STATS")
    print(f"Words: {stats['word_count']}")
    print(f"Unique words: {stats['unique_word_count']}")
    print(f"Sentences: {stats['sentence_count']}")
    print(f"Characters: {stats['char_count']}")
    print(f"Average word length: {stats['avg_word_length']:.2f}")
    print(f"Average sentence length: {stats['avg_sentence_length']:.2f}")
    print(f"Lexical diversity: {stats['lexical_diversity']:.2f}")


def print_flags(summary):
    print_header("FLAGS")

    repeated = summary["repeated_words"]
    long_sentences = summary["long_sentences"]
    weak_words = summary["weak_words"]
    weak_phrases = summary["weak_phrases"]

    if repeated:
        print("Repeated words found:")
        for word in repeated:
            print(f"- {word}")
    else:
        print("No repeated words found.")

    if long_sentences:
        print("\nLong sentences found:")
        for sentence in long_sentences:
            print(f"- {sentence}")
    else:
        print("\nNo long sentences found.")

    if weak_words:
        print("\nWeak words found:")
        for word in weak_words:
            print(f"- {word}")
    else:
        print("\nNo weak words found.")

    if weak_phrases:
        print("\nWeak phrases found:")
        for phrase in weak_phrases:
            print(f"- {phrase}")
    else:
        print("\nNo weak phrases found.")


def print_suggestions(summary):
    print_header("SUGGESTIONS")

    weak_words = summary["weak_words"]
    weak_phrases = summary["weak_phrases"]

    shown_words = set()
    shown_phrases = set()
    printed_any = False

    for word in weak_words:
        if word not in shown_words:
            suggestions = suggest_synonyms(word)
            if suggestions:
                print(f"{word}: {', '.join(suggestions)}")
                shown_words.add(word)
                printed_any = True

    for phrase in weak_phrases:
        if phrase not in shown_phrases:
            suggestions = suggest_phrase_replacements(phrase)
            if suggestions:
                print(f"{phrase}: {', '.join(suggestions)}")
                shown_phrases.add(phrase)
                printed_any = True

    if not printed_any:
        print("No replacement suggestions needed.")


def get_user_text():
    print("Choose an input method:")
    print("1. Type or paste text directly")
    print("2. Load text from a file")
    choice = input("> ").strip()

    if choice == "1":
        print("\nEnter a paragraph. Press Enter when finished:")
        return input("> ").strip()

    if choice == "2":
        filename = input("Enter the file name or path: ").strip()
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return file.read().strip()
        except FileNotFoundError:
            print("File not found.")
            return ""
        except OSError:
            print("Could not read that file.")
            return ""

    print("Invalid choice.")
    return ""


def main():
    print("Welcome to the Writing Assistant!")
    text = get_user_text()

    if not text:
        print("No text entered.")
        return

    summary = generate_summary(text, max_words=20)

    print_stats(summary["stats"])
    print_flags(summary)
    print_suggestions(summary)

    print_header("STATUS NOTE")
    print("This is a prototype version of the assistant.")
    print("The current version focuses on core analysis features,")
    print("while future work will improve revision quality and usability.")


if __name__ == "__main__":
    main()
