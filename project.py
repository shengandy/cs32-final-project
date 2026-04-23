from helpers import (
    get_text_stats,
    find_repeated_words,
    find_long_sentences,
    find_weak_words,
    suggest_synonyms,
)

def main():
    print("Welcome to the Writing Assistant!")
    text = input("Enter a paragraph:\n> ").strip()

    if not text:
        print("No text entered.")
        return

    stats = get_text_stats(text)
    repeated = find_repeated_words(text)
    long_sentences = find_long_sentences(text, max_words=20)
    weak_words = find_weak_words(text)

    print("\n--- TEXT STATS ---")
    print(f"Words: {stats['word_count']}")
    print(f"Sentences: {stats['sentence_count']}")
    print(f"Characters: {stats['char_count']}")
    print(f"Average word length: {stats['avg_word_length']:.2f}")
    print(f"Average sentence length: {stats['avg_sentence_length']:.2f}")

    print("\n--- FLAGS ---")
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

    print("\n--- SYNONYM SUGGESTIONS ---")
    shown = set()
    for word in weak_words:
        if word not in shown:
            suggestions = suggest_synonyms(word)
            if suggestions:
                print(f"{word}: {', '.join(suggestions)}")
                shown.add(word)

if __name__ == "__main__":
    main()
