#! /usr/bin/env python3

import sys
from argparse import ArgumentParser, FileType

def main():
    parser = ArgumentParser(description='Merge timestamped data in CSV format into one data stream');
    parser.add_argument('primary-file', help='The primary data file', type=FileType('r'))
    parser.add_argument('auxiliary-file', help='The auxiliary data file', type=FileType('r'))
    parser.add_argument('--verbose', help='Emit additional diagnostic data', action='store_true')
    parser.add_argument('--skip-lines', help='Number of lines to skip before starting to read data', type=int)

    args = parser.parse_args()
    
main()