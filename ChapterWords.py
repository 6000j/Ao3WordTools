import string
import re
import sys
import argparse
import coreUtils


def chapterWordCounts(path, writeTo):
    contents = coreUtils.FileTools.read_data(path)
    chapters = coreUtils.ChapterTools.split_and_clean_chapters(contents)
    chapterWords = []
    for chp in chapters:
        chapterWords.append(coreUtils.WordCountTools.simplified_word_count(chp))
    ous = chWCFormatting(chapterWords).strip()
    coreUtils.FileTools.write_data(ous, writeTo)

# Our output formatting
def chWCFormatting(chapterCounts):
    total = 0
    oup = ""
    for k in range(len(chapterCounts)):
        currCount = chapterCounts[k]
        total = total + currCount
        oup = oup + "\nChapter " + str(k+1) + " has " + str(currCount) + " words. So far there have been a total of " + str(total) + " words."
    return oup

# Setting up command line options
parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='The html file to process')
parser.add_argument('-o', '--output', type=str, default='oup.txt', required=False, help='The output file to write to. Default=oup.txt')

args = parser.parse_args()
chapterWordCounts(args.file, args.output)


