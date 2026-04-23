from helpers import (
    get_text_stats,
    find_repeated_words,
    find_long_sentences,
    find_weak_words,
    find_weak_phrases,
    suggest_synonyms,
    suggest_phrase_replacements,
    generate_summary,
)


def test_get_text_stats():
    text = "This is a test. It works."
    stats = get_text_stats(text)
    assert stats["word_count"] == 6
    assert stats["sentence_count"] == 2
    assert stats["unique_word_count"] == 6


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
    text = "This is a very good thing."
    assert find_weak_words(text) == ["very", "good", "thing"]


def test_find_weak_phrases():
    text = "I kind of think this matters a lot."
    assert find_weak_phrases(text) == ["a lot", "kind of"]


def test_suggest_synonyms():
    assert "excellent" in suggest_synonyms("good")


def test_suggest_phrase_replacements():
    assert "many" in suggest_phrase_replacements("a lot")


def test_generate_summary():
    text = "This is is a very good thing. I kind of like it a lot."
    summary = generate_summary(text, max_words=10)

    assert "stats" in summary
    assert summary["repeated_words"] == ["is"]
    assert "very" in summary["weak_words"]
    assert "a lot" in summary["weak_phrases"]
    
