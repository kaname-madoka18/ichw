#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Songzetian"
__pkuid__  = "1800011835"
__email__  = "1800011835@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
from collections import defaultdict
import string


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    dcount = defaultdict(int)
    for line in lines.splitlines():
        lst = [i.strip(string.punctuation) for i in line.split()]
        for word in lst:
            word = word.lower()
            dcount[word] += 1
    sor = sorted(dcount.items(), key=lambda t:t[1], reverse=True)
    if len(sor)>=topn:
        top = sor[:topn]
    else:
        top = sor
    for u in top:
        print("{}\t{}".format(*u))

    
def openbook(url):
    try:
        with urlopen(url) as book:
            doc = book.read()
            book.close()
            docstr = doc.decode('UTF-8')
            return docstr
    except ValueError:
        print("Invalid format of URL")
        return False
    except UnicodeDecodeError:
        print("decode error we decode your input via UTF-8")
        return False
    except:
        print("Unprospective error")
        return False


def main():
    paras = sys.argv[1:]
    if len(paras) == 1:
        url = paras[0]
        book = openbook(url)
        if book:
            wcount(book)
    elif len(paras) == 2:
        url, topn = paras
        topn = int(topn)
        book = openbook(url)
        if book:
            wcount(book, topn)
    else:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    
if __name__ == '__main__':
    main()
