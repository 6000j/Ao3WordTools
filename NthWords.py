import string
import re
import sys
import argparse

def write_data(oup, loc):
    f = open(loc, 'w', encoding='utf-8')
    f.write(oup)
    f.close()
    
def nthWords(path, n):
    # Reading in the chapter
    f = open(path, 'r', encoding='utf8')
    contents = f.read()
    f.close()
    # Cleaning up the string to only include the chapter
    mc = contents.split("<!--chapter content-->", 1)[1]
    mc = mc.strip()
    mc = mc.rsplit("<!--/chapter content-->", 1)[0]
    mc = re.sub("<!--/chapter content-->(.*?)<!--chapter content-->", "", mc, flags=re.DOTALL)
    mc = re.sub("<(.*?)>", "", mc)
    mc = re.sub("&#(.+?);", "", mc)
    # https://github.com/otwcode/otwarchive/blob/master/lib/word_counter.rb
    mc = re.sub("[--]", "—", mc)
    mc = re.sub("['’‘-]", "", mc)
    result = len(re.findall(r'\w+', mc))
    poggers = re.findall(r'\w+', mc)
    ous = ' '.join(poggers[::n])
    write_data(ous,'oup.txt')

    return result

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='The html file to process')
parser.add_argument('n', type=int, help='How many words between each word in the output. Must be >=1')
args = parser.parse_args()
if (args.n < 1):
    print("n must be a positive integer")
else:
    nthWords(args.file, args.n)


