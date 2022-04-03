#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

class Folder(defaultdict):
    def __init__(self):
        super().__init__(Folder)
        self.files = []

    def render_lines(self, name):
        yield name + '/'
        total_len = len(self.files) + len(self)
        i = 0
        for subname, subfolder in sorted(self.items()):
            prefix = '  ' if (i+1 == total_len) else '| '
            first = True
            for line in subfolder.render_lines(subname):
                if first:
                    yield '+-' + line
                    first = False 
                else:
                    yield prefix + line
            i += 1
        for subfile in sorted(self.files):
            yield '+-' + subfile

#
# Complete the 'draw_tree_layout' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY files as parameter.
#

def draw_tree_layout(files):
    root_name = files[0].split('/')[0]
    root = Folder()
    for file in files:
        *folders, name = file.split('/')
        f = root
        for part in folders[1:]:
            f = f[part]
        f.files.append(name)
    # print(root)
    # Write your code here
    return (root.render_lines(root_name))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    files_input = []

    for _ in range(N):
        files_input_item = input()
        files_input.append(files_input_item)

    result = draw_tree_layout(files_input)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
