def reverse(filename: str) -> str:
    contents = None
    with (open(filename) as file):
        contents = file.read()

    contents = contents.replace(' ', '') \
            .replace('\r', '') \
            .replace('\n', '') \
            .replace('\t', '')

    reversed_contents = ""
    for idx in range(len(contents) - 1, -1, -1):
        reversed_contents += contents[idx]

    print(reversed_contents)
    return reversed_contents


def test_reverse():
    assert reverse('test.txt') == 'gfedcba'


test_reverse()
