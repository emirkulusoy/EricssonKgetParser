# kgetParserLib/utils.py
import os
from os.path import isfile, join

def get_input_output_files(directory):
    return [f for f in os.listdir(directory) if isfile(join(directory, f))]

