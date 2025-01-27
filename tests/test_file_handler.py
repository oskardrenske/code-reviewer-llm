from file_handler import convert_path_to_dash


def test_convert_to_dash():
    test_string = r"/path/to/something\on\Windows/"
    expected = "path-to-something-on-Windows"
    result = convert_path_to_dash(test_string)
    assert result == expected
