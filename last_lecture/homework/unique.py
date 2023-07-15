def first_uniq_char(s: str) -> int:
    letters = {}

    for letter in s:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    for i in range(len(s)):
        if letters[s[i]] == 1:
            return i

    return -1len
print(first_uniq_char("loveleetcode"))
