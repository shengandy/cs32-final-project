from helpers import (
    get_text_stats,
    find_repeated_words,
    find_long_sentences,
    find_weak_words,
    find_weak_phrases,
    suggest_synonyms,
    suggest_phrase_replacements,
    generate_summary,
    count_occurrences,
    get_readability_label,
)


def test_get_text_stats():
    text = "This is a test. It works."
    stats = get_text_stats(text)
    assert stats["word_count"] == 6
    assert stats["sentence_count"] == 2
    assert stats["unique_word_count"] == 6
    assert stats["readability"] in {"Easy to read", "Moderate", "Dense"}


def test_find_repeated_words():
    text = "This is is a test."
    assert find_repeated_words(text) == ["is"]


def test_find_long_sentences():
    text = (
        "This is short. "
        "This sentence has way too many words and should probably be flagged by the program."
    )
    results = find_long_sentences(text, max_words=8)
    assert len(results) == 1


def test_find_weak_words():
    text = "This is a very good thing and a very nice one."
    assert find_weak_words(text) == ["very", "good", "thing", "very", "nice"]


def test_find_weak_phrases():
    text = "I kind of think this matters a lot, and at the end of the day it does."
    assert find_weak_phrases(text) == ["a lot", "kind of", "at the end of the day"]


def test_suggest_synonyms():
    assert "excellent" in suggest_synonyms("good")


def test_suggest_phrase_replacements():
    assert "many" in suggest_phrase_replacements("a lot")


def test_count_occurrences():
    items = ["very", "good", "very", "nice", "good"]
    assert count_occurrences(items) == [("very", 2), ("good", 2), ("nice", 1)]


def test_get_readability_label():
    assert get_readability_label(10, 4.5) == "Easy to read"
    assert get_readability_label(16, 5.0) == "Moderate"
    assert get_readability_label(22, 5.8) == "Dense"


def test_generate_summary():
    text = (
        "This is is a very good thing. "
        "I kind of like it a lot because it is really nice."
    )
    summary = generate_summary(text, max_words=10)

    assert "stats" in summary
    assert summary["repeated_words"] == ["is"]
    assert "very" in summary["weak_words"]
    assert "a lot" in summary["weak_phrases"]
    assert ("very", 1) in summary["weak_word_counts"]
    assert ("a lot", 1) in summary["weak_phrase_counts"]
