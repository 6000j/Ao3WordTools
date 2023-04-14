# Ao3WordTools

A collection of Tools for Ao3 that analyse Ao3-download-formatted HTML files and can perform various basic analyses on them regarding calculating word counts. Word counts will not 100% match up to Ao3, but they will get close.

---

# NthWords
A python 3.10 program that reads every Nth word of an Ao3-download-formatted HTML file and puts them into an oup.txt. It removes all non-body words, including A/N's, summaries, and other various non-body words.

Usage: `python nthWords.py [-h] [-o OUTPUT] file n`



## Example
`python nthWords.py -o 'example/Mermaid.txt' 'example/mermaid.html' 500`


---

# ChapterWords
A python 3.10 program that calculates the word counts of the chapters an Ao3-download-formatted HTML file and puts them into an oup.txt, along with a cumulative total. It removes all non-body words, including A/N's, summaries, and other various non-body words.

Usage: `python chapterWords.py [-h] [-o OUTPUT] file`




## Example
`python ChapterWords.py -o 'example/UUD.txt' 'example/Untap Upkeep Draw.html'`