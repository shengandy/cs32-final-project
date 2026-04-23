import re
from dictionary import WEAK_WORDS, THESAURUS, PHRASE_SUGGESTIONS


def tokenize_words(text):
    """
    Return a lowercase list of word tokens.
    Apostrophes are allowed so contractions like "don't" stay together.
    """
    return re.findall(r"[A-Za-z']+", text.lower())


def split_sentences(text):
    """
    Split text into sentences based on ., !, or ?.
    Empty results are removed.
    """
    sentences = re.split(r"[.!?]+", text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]


def get_text_stats(text):
    """
    Compute basic statistics about the text.
    """
    words = tokenize_words(text)
    sentences = split_sentences(text)

    word_count = len(words)
    sentence_count = len(sentences)
    char_count = len(text)

    avg_word_length = (
        sum(len(word) for word in words) / word_count if word_count > 0 else 0
    )

    avg_sentence_length = (
        word_count / sentence_count if sentence_count > 0 else 0
    )

    unique_word_count = len(set(words))
    lexical_diversity = (
        unique_word_count / word_count if word_count > 0 else 0
    )

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "char_count": char_count,
        "avg_word_length": avg_word_length,
        "avg_sentence_length": avg_sentence_length,
        "unique_word_count": unique_word_count,
        "lexical_diversity": lexical_diversity,
    }


def find_repeated_words(text):
    """
    Find consecutive repeated words, like 'is is' or 'the the'.
    Returns each repeated word only once.
    """
    words = tokenize_words(text)
    repeated = []

    for i in range(len(words) - 1):
        if words[i] == words[i + 1] and words[i] not in repeated:
            repeated.append(words[i])

    return repeated


def find_long_sentences(text, max_words=20):
    """
    Return sentences whose word counts exceed max_words.
    """
    sentences = split_sentences(text)
    results = []

    for sentence in sentences:
        words = tokenize_words(sentence)
        if len(words) > max_words:
            results.append(sentence)

    return results


def find_weak_words(text):
    """
    Return weak single-word matches found in the text, preserving
    the order of first appearance and avoiding duplicates.
    """
    words = tokenize_words(text)
    found = []

    for word in words:
        if word in WEAK_WORDS and word not in found:
            found.append(word)

    return found


def find_weak_phrases(text):
    """
    Detect weak multi-word phrases that should be revised.
    """
    lowered = text.lower()
    found = []

    for phrase in PHRASE_SUGGESTIONS:
        if phrase in lowered:
            found.append(phrase)

    return found


def suggest_synonyms(word):
    """
    Return synonym suggestions for a weak word.
    """
    return THESAURUS.get(word.lower(), [])


def suggest_phrase_replacements(phrase):
    """
    Return suggested replacements for weak phrases.
    """
    return PHRASE_SUGGESTIONS.get(phrase.lower(), [])


def generate_summary(text, max_words=20):
    """
    Run the main analysis pipeline and return results in one dictionary.
    This keeps project.py cleaner and makes the design easier to test.
    """
    stats = get_text_stats(text)
    repeated = find_repeated_words(text)
    long_sentences = find_long_sentences(text, max_words=max_words)
    weak_words = find_weak_words(text)
    weak_phrases = find_weak_phrases(text)

    return {
        "stats": stats,
        "repeated_words": repeated,
        "long_sentences": long_sentences,
        "weak_words": weak_words,
        "weak_phrases": weak_phrases,
    }
