from helpers import (
    get_text_stats,
    find_repeated_words,
    find_long_sentences,
    find_weak_words,
    suggest_synonyms,
)


def test_get_text_stats():
    text = "This is a test. It works."
    stats = get_text_stats(text)
    assert stats["word_count"] == 6
    assert stats["sentence_count"] == 2


def test_find_repeated_words():
    text = "This is is a test."
    assert find_repeated_words(text) == ["is"]


def test_find_long_sentences():
    text = "This is short. This sentence has way too many words and should probably be flagged by the program."
    results = find_long_sentences(text, max_words=8)
    assert len(results) == 1


def test_find_weak_words():
    text = "This is a very good thing."
    assert find_weak_words(text) == ["very", "good", "thing"]


def test_suggest_synonyms():
    assert "excellent" in suggest_synonyms("good")
