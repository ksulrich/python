#!/usr/bin/env python3
# $Id$
#
# Usage: ./telefon.py $HOME/Wissen/telefon.txt <pattern>
# This code comes from ChatGPT asking the question in
# https://github.com/ksulrich/knowledgeDB

import re
import sys

def read_know_file(file_path):
    with open(file_path, 'r') as f:
        contents = f.read()
    blocks = re.split('-{3,}\n', contents)
    return [block.strip() for block in blocks if block.strip()]

def search_block(query, block):
    # Split the query into individual words/expressions
    #search_terms = query.split()
    search_terms = query
    # Check if all search terms are found in the block
    if all(re.search(term, block, re.IGNORECASE) for term in search_terms):
        return block

def search_know_file(query, file_path):
    print("query=", query, " file_path=", file_path)
    blocks = read_know_file(file_path)
    matching_blocks = [search_block(query, block) for block in blocks]
    return [block for block in matching_blocks if block]

if __name__ == '__main__':
    # we need at least the file and one pattern
    print(sys.argv)
    if len(sys.argv) <= 2:
        print("""
           Usage: telefon2.py <file> <pattern_1> <pattern_2> ...  <pattern_n>
           where <pattern_i> is a regular expression like "ul.*"
           The patterns are ANDed, so you can search for that:
           ./telefon2.py telefon.txt klaus "ul.*"
           and you are searching for klaus (case does not matter) AND 
           any word starting with ul 
        """)
        sys.exit(1)

    # The file is the first argument
    # All the next arguments are the search patterns
    query = sys.argv[2:]
    matching_blocks = search_know_file(query, sys.argv[1])
    for block in matching_blocks:
        print('-' * 80)
        print(block)
        print('-' * 80)
