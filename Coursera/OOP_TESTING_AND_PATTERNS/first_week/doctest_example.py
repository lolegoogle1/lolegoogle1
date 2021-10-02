from stack import Stack


def is_braces_sequence_correct(seq: str) -> bool:
    """
    Check correctness of braces sequence in statement
    >>> is_braces_sequence_correct("()(())")
    True
    >>> is_braces_sequence_correct("()[()]")
    True
    >>> is_braces_sequence_correct(")")
    False
    >>> is_braces_sequence_correct("[()")
    False
    >>> is_braces_sequence_correct("[(])")
    False
    """
    stack = Stack(len(seq))
    correspondent = dict(zip("([{", ")]}"))
    for brace in seq:
        if brace in "([{":
            stack.put(brace)
            continue
        elif brace in ")]}":
            if stack.empty:
                return False
            left = stack.get()
            if correspondent[left] != brace:
                return False
    return stack.empty


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())