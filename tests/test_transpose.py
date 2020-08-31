import unittest, sys, pytest
from transpose import read_file, find_larget, transpose_word, init


class TestTransposeLargest(unittest.TestCase):

    pytest.TEST_DATA_FOLDER = 'tests/test_data'

    # @pytest.fixture(autouse=True)
    # def _pass_fixtures(self, capsys):
    #     self.capsys = capsys
    
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
        filepath = f'{pytest.TEST_DATA_FOLDER}/test_data_1.txt'
        actual = read_file(filepath)
        expected = ['a','ab','abc']
        self.assertEqual(expected, actual)

    def test_init(self):
        sys.argv = ['transpose.py', f'{pytest.TEST_DATA_FOLDER}/test_data_0.txt']
        actual = init()
        #print(self.capsys.readouterr())

    """
    Negative Cases
    """
    def test_read_file_empty(self):
        filepath = f'{pytest.TEST_DATA_FOLDER}/test_data_2.txt'
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