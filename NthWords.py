import string
import re
import sys
import argparse

# a handy useful writing data function helper thing
def write_data(oup, loc):
    f = open(loc, 'w', encoding='utf-8')
    f.write(oup)
    f.close()
    
def nthWords(path, n, writeTo, multiChapter):

    # Reading in the chapter
    f = open(path, 'r', encoding='utf8')
    contents = f.read()
    f.close()
    mc = []
    # Due to Ao3 jank, multiple chapter fics have to be handled in a different way to single chapter ones
    if multiChapter:
        # Cleaning up the string to only include the chapter
        mc = contents.split("<!--chapter content-->", 1)[1]
        mc = mc.rsplit("<!--/chapter content-->", 1)[0]
        mc = mc.strip()
        mc = re.sub("<!--/chapter content-->(.*?)<!--chapter content-->", "", mc, flags=re.DOTALL)
    else:
        # Cleaning up the string to only include the chapter
        mc = contents.split("<div id=\"chapters\" class=\"userstuff\">", 1)[1]
        mc = mc.rsplit("<div id=\"afterword\">", 1)[0]
        mc = mc.strip()
        mc = re.sub("<h2 class=\"toc-heading\">(.+?)</h2>", "", mc)

    # cleaning up the rest of it
    
    mc = re.sub("<(.*?)>", "", mc)
    mc = re.sub("&#(.+?);", "", mc)
    # This part is an approximation of the Ao3 word counter, which can be found here
    # https://github.com/otwcode/otwarchive/blob/master/lib/word_counter.rb 
    mc = re.sub("[--]", "—", mc)
    mc = re.sub("['’‘-]", "", mc)
    # Finding the words
    poggers = re.findall(r'\w+', mc)
    # Joining together every nth word
    ous = ' '.join(poggers[n::n])
    write_data(ous,writeTo)

# Setting up command line options
parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='The html file to process')
parser.add_argument('n', type=int, help='How many words between each word in the output. Must be >=1')

parser.add_argument('-o', '--output', type=str, default='oup.txt', required=False, help='The output file to write to. Default=oup.txt')
parser.add_argument('-mc', '--multichapter', action='store_true', default=False, help='Whether or not the fic is multi-chapter. Default=False.')

args = parser.parse_args()
if (args.n < 1):
    print("n must be a positive integer") 
else:
    nthWords(args.file, args.n, args.output, args.multichapter)


