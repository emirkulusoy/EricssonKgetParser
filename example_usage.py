# example_usage.py
import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from kgetParserLib import FileParser

input_directory = 'input'
output_directory = 'output'

parser = FileParser(input_directory, output_directory)
parser.parse_files()
