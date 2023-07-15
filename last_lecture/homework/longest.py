def find_word(text: str) -> str:
    longest_word = ""

    for word in text.split():
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


def test_find_word():
    text = "The quick brown fox jumped over the lazy dog"
    result = find_word(text)
    assert result == "jumped"
