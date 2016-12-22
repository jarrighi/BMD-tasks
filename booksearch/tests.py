import unittest
from booksearch import *
import sys


class RunCommandTest(unittest.TestCase):

  def setUp(self):
    self.parser = create_parser()

  def tearDown(self):
    pass

  def test_returns_help_with_help_arg(self):
    with self.assertRaises(SystemExit) as cm:
      self.parser.parse_args(['-h'])
    output = sys.stdout.getvalue().strip()
    expected = "usage: tests.py [-h]"
    self.assertIn(expected, output)

  def test_command_takes_one_or_more_of_word_args(self):
    args = self.parser.parse_args(['hello', 'world'])

  def test_takes_optional_data_file(self):
    args = self.parser.parse_args(['-f', 'bookdata_small.json', 'word'])
    self.assertEqual(args.file[0], 'bookdata_small.json')
    bookfile = set_data_file(args)
    self.assertEqual(bookfile, 'bookdata_small.json')

  def test_returns_help_with_no_args(self):
    with self.assertRaises(SystemExit) as x:
      self.parser.parse_args()

    output = sys.stdout.getvalue().strip()
    expected = "usage: tests.py [-h]"
    self.assertIn(expected, output)


  def test_returns_help_with_invalid_args(self):
    with self.assertRaises(SystemExit) as x:
      self.parser.parse_args(["-u"])

    output = sys.stdout.getvalue().strip()
    expected = "usage: tests.py [-h]"
    self.assertIn(expected, output)
    pass


class CreateIndexTest(unittest.TestCase):

  def setUp(self):
    parser = create_parser()
    args = parser.parse_args([
      '-f', 'bookdata_small.json', 'hello', 'world'])
    bookfile = set_data_file(args)
    self.index = create_index(bookfile)
    self.words = self.index.keys()

  def tearDown(self):
    pass

  def test_no_punctuation_in_index_words(self):
    self.assertIn('sandwich', self.words)
    self.assertNotIn('sandwich.', self.words)

  def test_index_words_are_lowercase(self):
    self.assertIn('guide', self.words)
    self.assertNotIn('Guide', self.words)

  def test_index_includes_title_and_description_only(self):
    self.assertIn('guide', self.words)
    self.assertNotIn('Gambardella', self.words)

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