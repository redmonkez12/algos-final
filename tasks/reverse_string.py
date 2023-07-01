def reverse_string(text: str):
    # return text[::-1]

    result = ""
    for char in text:
        result = char + result  # L + "

    return result

# L + "" = L
# i + L = iL
# s + iL = siL
# ...
