from codeforge import count_lines, todo_items


def test_count_lines():
    assert count_lines("a\n\nb\n") == {"total": 3, "blank": 1, "non_blank": 2}


def test_todos():
    assert todo_items("# TODO: fix\npass") == ["# TODO: fix"]
