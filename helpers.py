from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    a_lines = a.splitlines()
    b_lines = b.splitlines()
    shared_lines = set()

    # Keeps track if each line in string a is also in string b
    for line in a_lines:
        if line in b_lines:
            shared_lines.add(line)

    return list(shared_lines)


def sentences(a, b):
    """Return sentences in both a and b"""

    a_sentences = sent_tokenize(a)
    b_sentences = sent_tokenize(b)

    shared_sentences = set()

    # Keeps track if each sentence in string a is also in string b
    for sentence in a_sentences:
        if sentence in b_sentences:
            shared_sentences.add(sentence)

    return list(shared_sentences)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    a_substring = set()
    b_substring = set()

    shared_substring = set()

    # Finds all substrings of length n for both strings a and b
    for i in range(len(a)):
        if i < len(a) - n + 1:
            a_substring.add(a[i:i + n])
    for i in range(len(b)):
        if i < len(b) - n + 1:
            b_substring.add(b[i:i + n])

    # Keeps track if each substrings in string a is also in string b
    for substr in a_substring:
        if substr in b_substring:
            shared_substring.add(substr)

    return list(shared_substring)
