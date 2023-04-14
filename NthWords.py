import string
import re
import sys
import argparse
import coreUtils

def nthWords(path, writeTo, n):
    contents = coreUtils.FileTools.read_data(path) # Reading in the data
    contents = coreUtils.ChapterTools.split_and_clean_chapters(contents) # Splitting into chapters and cleaning into plaintext
    contents = ' '.join(contents) # Combining these all into a single file
    wordsList = coreUtils.WordCountTools.words_list(contents) # Turning into just a list of all the words
    # A catch to make sure it's long enough
    if len(wordsList) < n:
        print("There are not %i words in the fic!" % n)
        exit()
    ous = ' '.join(wordsList[n-1::n]) # Getting every nth word
    coreUtils.FileTools.write_data(ous, writeTo) # Writing our output to the file

# Setting up command line options
parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='The html file to process')
parser.add_argument('n', type=int, help='How many words between each word in the output. Must be >=1')
parser.add_argument('-o', '--output', type=str, default='oup.txt', required=False, help='The output file to write to. Default=oup.txt')

args = parser.parse_args()
if (args.n < 1):
    print("n must be a positive integer") 
else:
    nthWords(args.file, args.output, args.n)


