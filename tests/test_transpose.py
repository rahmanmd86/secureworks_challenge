import unittest, sys, pytest
from transpose import read_file, find_larget, transpose_word, init
from io import StringIO
from unittest.mock import patch

class TestTransposeLargest(unittest.TestCase):

    pytest.TEST_DATA_FOLDER = 'tests/test_data'

    """
    Positive Cases
    """
    def test_transpose_largest(self):
        word = 'abcde'
        actual = transpose_word(word)
        expected = 'edcba'
        self.assertEqual(expected, actual)

    def test_find_largest(self):
        wordlist = ['a','ab','abc']
        actual = find_larget(wordlist)
        expected = 'abc'
        self.assertEqual(expected, actual)

    def test_read_file(self):
        filepath = f'{pytest.TEST_DATA_FOLDER}/example_file.txt'
        actual = read_file(filepath)
        expected = ['a','ab','abc','abcd','abcde']
        self.assertEqual(expected, actual)

    def test_init(self):
        sys.argv = ['transpose.py', f'{pytest.TEST_DATA_FOLDER}/example_file.txt']
        expected = 'abcde\nedcba'
        with patch('sys.stdout', new=StringIO()) as output:
            init()
        self.assertEqual(output.getvalue().strip(), expected)

    def test_init_numbers(self):
        sys.argv = ['transpose.py', f'{pytest.TEST_DATA_FOLDER}/numbers_file.txt']
        expected = '12345\n54321'
        with patch('sys.stdout', new=StringIO()) as output:
            init()
        self.assertEqual(output.getvalue().strip(), expected)

    def test_init_spaced_words(self):
        sys.argv = ['transpose.py', f'{pytest.TEST_DATA_FOLDER}/spaced_words.txt']
        expected = 'jumps over the\neht revo spmuj'
        with patch('sys.stdout', new=StringIO()) as output:
            init()
        self.assertEqual(output.getvalue().strip(), expected)

    def test_init_special_chars(self):
        sys.argv = ['transpose.py', f'{pytest.TEST_DATA_FOLDER}/special_chars.txt']
        expected = '@#$^&\n&^$#@'
        with patch('sys.stdout', new=StringIO()) as output:
            init()
        self.assertEqual(output.getvalue().strip(), expected)

    """
    Negative Cases
    """
    def test_read_file_empty(self):
        filepath = f'{pytest.TEST_DATA_FOLDER}/empty_file.txt'
        actual = read_file(filepath)
        expected = []
        self.assertEqual(expected, actual)

    def test_find_largest_dup(self):
        wordlist = ['a','ab','abc', 'abc']
        result = find_larget(wordlist)
        self.assertEqual(result, 'abc')

    def test_find_largest_non_dup_same_length(self):
        wordlist = ['a','ab','abc', 'def']
        result = find_larget(wordlist)
        self.assertEqual(result, 'abc')

    def test_init_file_not_found(self):
        sys.argv = ['transpose.py', f'{pytest.TEST_DATA_FOLDER}/test_data.txt']
        with self.assertRaises(FileNotFoundError):
            init()

    def test_init_invalid_args(self):
        sys.argv = ['transpose.py']
        with self.assertRaises(IndexError):
            init()


if __name__ == '__main__':
    unittest.main()