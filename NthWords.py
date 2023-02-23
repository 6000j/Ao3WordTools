import string
import re
import sys

def write_data(oup, loc):
    f = open(loc, 'w', encoding='utf-8')
    f.write(oup)
    f.close()
    
def thousandthWords(path):
    # Reading in the chapter
    f = open(path, 'r', encoding='utf8')
    contents = f.read()

    # Cleaning up the string to only include the chapter
    # print(len(contents.split("<!--chapter content-->", 1)))
    mc = contents.split("<!--chapter content-->", 1)[1]
    mc = mc.strip()
    mc = mc.rsplit("<!--/chapter content-->", 1)[0]
    mc = re.sub("<!--/chapter content-->(.*?)<!--chapter content-->", "", mc, flags=re.DOTALL)
    mc = re.sub("<(.*?)>", "", mc)
    mc = re.sub("&#(.+?);", "", mc)
    # https://github.com/otwcode/otwarchive/blob/master/lib/word_counter.rb
    mc = re.sub("[--]", "—", mc)
    mc = re.sub("['’‘-]", "", mc)
    # print(type(mc))
    # write_data(mc,'contents.txt')
    result = len(re.findall(r'\w+', mc))
    poggers = re.findall(r'\w+', mc)
    # print(poggers[:1000])
    ous = ' '.join(poggers[::1000])
    write_data(ous,'oup.txt')
    # print(result)
    # print(mc)
    
    f.close()
    return result


thousandthWords('Run at the Cup.html')


