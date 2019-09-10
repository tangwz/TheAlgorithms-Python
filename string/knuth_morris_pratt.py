def kmp(pattern: str, text: str):
    """
    The Knuth-Morris-Pratt Algorithm for finding a pattern within a piece of text
    with complexity O(n + m)
    1) Preprocess pattern to identify any suffixes that are identical to prefixes
        This tells us where to continue from if we get a mismatch between a character in our pattern
        and the text.
    2) Step through the text one character at a time and compare it to a character in the pattern
        updating our location within the pattern if necessary
    """
    next_array = get_next_array(pattern)
    i, j = 0, 0
    while i < len(text):
        if pattern[j] == text[i]:
            if j == len(pattern)-1:
                return True
            j += 1
        # if this is a prefix in our pattern
        # just go back far enough to continue
        elif j > 0:
            j = next_array[j-1]
            continue
        i += 1
    return False


def get_next_array(pattern: str) -> [int]:
    """ Calculate partial match table"""
    res = [0]
    i, j = 0, 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
        elif i > 0:
            i = res[i-1]
            continue
        j += 1
        res.append(i)
    return res


if __name__ == '__main__':
    # Test 1)
    pattern = "abc1abc12"
    text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    text2 = "alskfjaldsk23adsfabcabc"
    assert kmp(pattern, text1) and not kmp(pattern, text2)

    # Test 2)
    pattern = "ABABX"
    text = "ABABZABABYABABX"
    assert kmp(pattern, text)

    # Test 3)
    pattern = "AAAB"
    text = "ABAAAAAB"
    assert kmp(pattern, text)

    # Test 4)
    pattern = "abcdabcy"
    text = "abcxabcdabxabcdabcdabcy"
    assert kmp(pattern, text)

    # Test 5)
    pattern = "aabaabaaa"
    assert get_next_array(pattern) == [0, 1, 0, 1, 2, 3, 4, 5, 2]
