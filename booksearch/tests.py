import unittest
from booksearch import *
import sys


class RunCommandTest(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_returns_help_with_help_arg(self):
    parser = create_parser()
    with self.assertRaises(SystemExit) as cm:
      parser.parse_args(['-h'])
      
    output = sys.stdout.getvalue().strip()
    expected = "usage: tests.py [-h]"
    self.assertIn(expected, output)

  def test_command_takes_any_number_of_word_args(self):
    pass

  def test_takes_optional_data_file(self):
    parser = create_parser()
    args = parser.parse_args(['-f', 'bookdata.json'])
    self.assertIsInstance(args.file, list)
    self.assertEqual(args.file[0], 'bookdata.json')
    pass

  def test_returns_help_with_no_args(self):
    parser = create_parser()
    with self.assertRaises(SystemExit) as x:
      parser.parse_args()

    output = sys.stdout.getvalue().strip()
    expected = "usage: tests.py [-h]"
    self.assertIn(expected, output)


  def test_returns_help_with_invalid_args(self):
    parser = create_parser()
    with self.assertRaises(SystemExit) as x:
      parser.parse_args(["-u"])

    output = sys.stdout.getvalue().strip()
    expected = "usage: tests.py [-h]"
    self.assertIn(expected, output)
    pass


class CreateIndexTest(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_no_punctuation_in_index_words(self):
    pass

  def test_index_words_are_lowercase(self):
    pass

  def test_index_includes_title_and_description_only(self):
    pass

  def test_all_books_in_index(self):
    pass

  def test_handle_errors_loading_json_file(self):
    pass


class SearchTest(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_find_word_returns_id_and_title(self):
    pass

if __name__ == "__main__":
  unittest.main(buffer=True) 