
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
    #  1. STRING_ARRAY strings
    #  2. STRING_ARRAY queries
    #

def matchingStrings(strings, queries):
    # Write your code here
    result = []
    for query in queries:
        #sum(1 for y in x if y > 2)
        count = sum(1 for string in strings if  string == query)
        #count = sum(map(lambda val: val == query, strings))
        print(list(map(lambda val: val == query, strings)))
        result.append(count)
    return result

if __name__ == '__main__':

    strings_count = int(input().strip())
    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    print(res)
