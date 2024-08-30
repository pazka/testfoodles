import math
from typing import List


def get_word_count(words: List[str]) -> dict:
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 0

        counts[word] += 1

    return counts


def get_ranks_with_associated_words(sorted_list: List[tuple]) -> dict:
    """
        return a list of words with the same counts in a dict
        the dict keys(occurrences) preserve the order of first_appearing occurrences in the list
    """
    ranks = {}

    for word, rank in sorted_list:
        if str(rank) not in ranks:
            ranks[str(rank)] = []

        ranks[str(rank)].append(word)
        ranks[str(rank)].sort()

    return ranks


def count_words(sentence: str, limit: int) -> List[tuple]:
    words = sentence.split(' ')

    all_word_count = get_word_count(words)

    sorted_list = sorted(all_word_count.items(),
                         key=lambda x: x[1], reverse=True)

    words_per_count = get_ranks_with_associated_words(sorted_list)
    words_per_count_keys = list(words_per_count)
    res = []

    # Now we browse the resulting counts and the possible words with same count
    for count in words_per_count_keys:
        if len(res) >= limit:
            break
        
        words_for_count = words_per_count[str(count)]

        for word in words_for_count:
            if len(res) >= limit:
                break
            res.append((word, count))

    return res


if __name__ == "__main__":
    count_words("bar baz foo foo zblah zblah zblah baz toto bar", 3)
