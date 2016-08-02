#! /usr/bin/env python3
import os

emoticons = {}
for filename in os.listdir('.'):
    name, ext = filename.rsplit('.', 1)

    if ext != 'svg' or name.startswith('00'):
        continue

    string = "".join(chr(int(x, 16)) for x in name.split('-'))

    emoticons[string] = filename

with open('emoticons.py', 'w') as f:
    f.write("# coding=utf8\nemoticons = {\n")
    for string, filename in sorted(emoticons.items(), key=lambda x: x[0]):
        f.write("    '{}': ['{}'],\n".format(filename, string))
    f.write("}\n")
