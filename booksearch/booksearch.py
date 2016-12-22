import argparse

DEFAULT_FILE = 'bookdata.json'
bookfile = DEFAULT_FILE

def create_parser():
  parser = argparse.ArgumentParser()
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
