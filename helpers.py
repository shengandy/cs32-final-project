import re
from dictionary import WEAK_WORDS, THESAURUS


def tokenize_words(text):
    return re.findall(r"[A-Za-z']+", text.lower())


def split_sentences(text):
    sentences = re.split(r"[.!?]+", text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]


def get_text_stats(text):
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

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "char_count": char_count,
        "avg_word_length": avg_word_length,
        "avg_sentence_length": avg_sentence_length,
    }


def find_repeated_words(text):
    words = tokenize_words(text)
    repeated = []

    for i in range(len(words) - 1):
        if words[i] == words[i + 1] and words[i] not in repeated:
            repeated.append(words[i])

    return repeated


def find_long_sentences(text, max_words=20):
    sentences = split_sentences(text)
    results = []

    for sentence in sentences:
        words = tokenize_words(sentence)
        if len(words) > max_words:
            results.append(sentence)

    return results


def find_weak_words(text):
    words = tokenize_words(text)
    found = []

    for word in words:
        if word in WEAK_WORDS and word not in found:
            found.append(word)

    return found


def suggest_synonyms(word):
    return THESAURUS.get(word, [])
