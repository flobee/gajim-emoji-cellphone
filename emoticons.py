# encoding=utf-8
import os
import struct
from collections import OrderedDict

DIR = os.path.join(os.path.dirname(__file__), 'images')

special = {
    0x260e: ['(T)'],
    0x2615: ['(C)'],
    0x2639: [':-(', ':('],
    0x263a: [':-)', ':)'],
    0x2764: ['<3', '(L)', '*IN LOVE*'],
    0x2b50: ['(*)'],
    0x1f308: ['(R)'],
    0x1f315: ['(S)'],
    0x1f339: ['@}-<--', '(F)'],
    0x1f378: ['(D)'],
    0x1f37a: ['(B)', '*DRINK*'],
    0x1f3b5: ['(8)'],
    0x1f44d: ['(Y)', '*THUMBS UP*'],
    0x1f44e: ['(N)'],
    0x1f48b: [':-*', ':*', ':-{}', '(K)'],
    0x1f494: ['</3', '(U)'],
    0x1f4a1: ['(I)'],
    0x1f4e7: ['(E)'],
    0x1f4f7: ['(P)'],
    0x1f603: [':-D', ':D'],
    0x1f606: ['XD'],
    0x1f608: [']:->', '>:-)', '>:)', '(6)'],
    0x1f609: [';-)', ';)'],
    0x1f60e: ['8-)', 'B-)', '(H)'],
    0x1f60f: [':3', '>:3'],
    0x1f610: [':-|', ':|'],
    0x1f615: [':-/', ':/', ':-\\', ':\\', ':-S', ':S'],
    0x1f618: [';-*', ';*'],
    0x1f61b: [':-P', ':P', ':-þ', ':þ'],
    0x1f61c: [';-P', ';P'],
    0x1f620: ['>:-(', '>:(', ':-@', ':@'],
    0x1f622: [":'-(", ":'(", ';-(', ';(', ";'-("],
    0x1f632: ['=-O', ':-O', ':O'],
    0x1f638: ['(@)', '=^.^='],
    0x1f940: ['(W)'],
    0x1f987: [':-[', ':['],
}

def unichar(i):
    """
    Return a Unicode string of one character with ordinal i

    Supports ordinals bigger than 0x10000 on narrow Python builds.

    (Source: http://stackoverflow.com/a/28326717)
    """
    try:
        return unichr(i)
    except ValueError:
        return struct.pack('i', i).decode('utf-32')
#    except NameError:
#        return struct.pack('i', i).decode('utf-32')


emoticons = {}
for filename in os.listdir(DIR):
    name, ext = filename.rsplit('.', 1)

    if ext != 'png' or name.startswith('00'):
        continue

    filename = os.path.join(DIR, filename)
    codes = [int(x, 16) for x in name.split('-')]
    string = "".join(map(unichar, codes)).encode('utf-8')

    emoticons[filename] = [string]
    if len(codes) == 1 and codes[0] in special:
        emoticons[filename].extend(special[codes[0]])

emoticons = OrderedDict(sorted(emoticons.items(), key=lambda x: x[0]))
