# NthWords
A python 3.10 program that reads every Nth word of an Ao3-download-formatted HTML file and puts them into an oup.txt. It removes all non-body words, including A/N's, summaries, and other various non-body words.

Usage: `python nthWords.py [-h] [-o OUTPUT] [-mc] file n`

Make sure to use the `-mc` flag if a fic has multiple chapters.

Note: Any text between <>'s will not be counted.

---
## Example
`python nthWords.py -o 'example/Mermaid.txt' 'example/mermaid.html' 500`