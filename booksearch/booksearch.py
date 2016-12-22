import argparse
import sys

DEFAULT_FILE = 'bookdata.json'
bookfile = DEFAULT_FILE

class BookSearchParser(argparse.ArgumentParser):
  def error(self, message):
    sys.stderr.write('error: %s\n' % message)
    self.print_help()
    sys.exit(2)

def create_parser():
  parser = BookSearchParser()
  # Add arguments here

  return parser

def create_index(file):
  pass

def search(word, index):
  pass

def main():
  # Create parser
  parser = create_parser()

  # Parse Args
  args = parser.parse_args()

  # Create Index

  # Run Searches

  # Print Results

if __name__ == '__main__':
  main()
