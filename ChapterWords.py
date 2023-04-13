import string
import re
import sys
import argparse

# a handy useful writing data function helper thing
def write_data(oup, loc):
    f = open(loc, 'w', encoding='utf-8')
    f.write(oup)
    f.close()
    
def chapterWordCounts(path, writeTo):

    # Reading in the chapter
    f = open(path, 'r', encoding='utf8')
    contents = f.read()
    f.close()
    chapters = [] # This is our chapters array
    chapterWords = []

    # Catch for single-chapter
    if len(contents.split("<!--chapter content-->")) == 1:
        print("ChapterWords only works on multi-chapter fics!")
        exit()

    # Splitting up into individual chapters
    chapters = contents.split("<!--chapter content-->")[1:]
    # Iterating 
    for k in range(len(chapters)):
        chapter = chapters[k]
        chapter = chapter.strip()
        chapter = chapter.split("<!--/chapter content-->")[0]
        # chapter = re.sub("<!--/chapter content-->(.*?)", "", chapter, flags=re.DOTALL)

        # cleaning up the rest of it
        
        chapter = re.sub("<(.*?)>", "", chapter)
        chapter = re.sub("&#(.+?);", "", chapter)
        # This part is an approximation of the Ao3 word counter, which can be found here
        # https://github.com/otwcode/otwarchive/blob/master/lib/word_counter.rb 
        chapter = re.sub("[--]", "—", chapter)
        chapter = re.sub("['’‘-]", "", chapter)

        # Making sure our chapter is cleansed
        chapters[k] = chapter
        # Finding the words
        poggers = re.findall(r'\w+', chapter)

        # Setting the wordcount:
        chapterWords.append(len(poggers))

    # Debugging:
    # for k in chapters:
    #    print(k)
    # 
    
    # Creating our chapter output formatting
    ous = chWCFormatting(chapterWords).strip()
    write_data(ous,writeTo)

# Our output formatting
def chWCFormatting(chapterCounts):
    total = 0
    oup = ""
    for k in range(len(chapterCounts)):
        currCount = chapterCounts[k]
        total = total + currCount
        oup = oup + "\nChapter " + str(k) + " has " + str(currCount) + " words. So far there have been a total of " + str(total) + " words."
    return oup

# Setting up command line options
parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='The html file to process')
parser.add_argument('-o', '--output', type=str, default='oup.txt', required=False, help='The output file to write to. Default=oup.txt')

args = parser.parse_args()
chapterWordCounts(args.file, args.output)


