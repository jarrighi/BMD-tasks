import argparse
import sys

DEFAULT_FILE = 'bookdata.json'

class BookSearchParser(argparse.ArgumentParser):
  def error(self, message):
    sys.stderr.write('error: %s\n' % message)
    self.print_help()
    sys.exit(2)

def create_parser():
  parser = BookSearchParser()
  parser.add_argument('-f', '--file', nargs=1, help="JSON File to be searched.")
  parser.add_argument('words', nargs='+')
  return parser

def create_index(file):
  pass

def search(word, index):
  pass

def print_output(bookfile):
  print('Using "{}" as book data source.'.format(bookfile))

def set_data_file(args):
  bookfile = DEFAULT_FILE
  if args.file:
    bookfile = args.file[0]
  return bookfile

def main():
  # Create parser
  parser = create_parser()

  # Parse Args
  args = parser.parse_args()

  bookfile = set_data_file(args)

  # Create Index

  # Run Searches

  # Print Results
  print_output(bookfile)

if __name__ == '__main__':
  main()
