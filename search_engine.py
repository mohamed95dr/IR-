import sys
import re
import os
import nltk
from nltk import tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from collections import defaultdict
from array import array
import gc
import math
from nltk import pos_tag, sent_tokenize, ne_chunk
from nltk.corpus import wordnet as wn
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize
from nltk.util import pr
import function

porter = PorterStemmer()
lmtzr = WordNetLemmatizer()
clean_corpus = []
temp_cleandata = []


class search_engine(object):
    # f = open('stop words.txt', "r")
    # line = f.read()
    # stop_words = re.findall("\S+", line)
    # f.close()
    # tokines = []
    # clean_corpus = []
    # diction = {}
    # temp_dic2 = {}
    # temp_dic = {}
    # verbs = []
    # nouns = []
    # # -------------
    #
    # # start
    # f2 = open("result.txt", "w")
    # for r in range(1, 424):
    #     f1 = open("corpus/{}.txt".format(r), 'r')
    #     x = f1.read()
    #     f1.close()
    #     # process date
    #     dates = re.findall("(0[1-9]|[12]\d|3[01])[/.-]"
    #                        "(0[1-9]|1[012])"
    #                        "[/.-](\d{4})", x)
    #     dates.extend(re.findall("(0[1-9]|[12]\d|3[01])[/.-]"
    #                             "(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
    #                             "[/.-](\d{4})", x))
    #     dates.extend(re.findall("(0[1-9]|[12]\d|3[01])[/.-]"
    #                             "(January|February|March|April|May|June|July|August|September|October|November|December)"
    #                             "[/.-](\d{4})", x))
    #     years = re.findall("\d{4}", x)
    #
    #     # remove dates from string
    #     x = re.sub("(0[1-9]|[12]\d|3[01])[/.-]"
    #                "(0[1-9]|1[012])"
    #                "[/.-](\d{4})", "", x)
    #     x = re.sub("(0[1-9]|[12]\d|3[01])[/.-]"
    #                "(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
    #                "[/.-](\d{4})", "", x)
    #     x = re.sub("(0[1-9]|[12]\d|3[01])[/.-]"
    #                "(January|February|March|April|May|June|July|August|September|October|November|December)"
    #                "[/.-](\d{4})", "", x)
    #     x = re.sub("\d{4}", "", x)
    #     # convert dates to regular form 01-Mar-2020
    #     dates = function.convert_to_regular_date(dates)
    #
    #     ## processing emails
    #     # extract emails from string in contentAFile
    #     emails = re.findall("\w+@\w+[.]\w+", x)
    #     # remove emails from string
    #     contentAFile = re.sub("\w+@\w+[.]\w+", "", x)
    #
    #     ## processing phones
    #     phones = re.findall("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4} | "
    #                         "\(\d{3}\)\s *\d{3}[-\.\s]??\d{4} |"
    #                         "\d{3}[-\.\s]??\d{4})", x)
    #
    #     filter_vn = function.wordsVorN(x)
    #     verbs = filter_vn[0]
    #     nouns = filter_vn[1]
    #     clean_corpusverbs = function.del_stop_words(verbs)
    #     clean_corpusnouns = function.del_stop_words(nouns)
    #     porte_w = function.porter_word(clean_corpusnouns)
    #     lem_w = function.lemmatize_word(verbs)
    #     # store word process
    #     temp_cleandata.extend(dates)
    #     temp_cleandata.extend(emails)
    #     temp_cleandata.extend(porte_w)
    #     temp_cleandata.extend(lem_w)
    #     clean_corpus.extend(dates)
    #     clean_corpus.extend(porte_w)
    #     clean_corpus.extend(lem_w)
    #
    #     for y in temp_cleandata:
    #         temp_dic.update({y: (1 + math.log(temp_cleandata.count(y), 10)).__round__(5)})
    #         diction.update({x: temp_dic})
    #     # temp_dic2.update({x: temp_dic2})
    #     # print("document number : {} Done".format(x))
    #
    #     temp_cleandata.clear()
    # f2.write(str(diction))
    # f2.close()

    #      Extension of the previous diction in order to contain all terms
    #     and show their repetition within the document
    # for y in range(1, 424):
    #     #     temp_dic2 = diction.get(y).copy()
    #     #     diction.get(y).clear()
    #     # print(temp_dic2)
    #     for z in list(dict.fromkeys(clean_corpus)):
    #         if z not in temp_dic2.keys():
    #             diction.get(y).update({z: 0.0})
    #         else:
    #             diction.get(y).update({z: temp_dic2[y]})
    #
    # f2.write(str(diction))
    # f2.close()

    #     # print irreguler verbs
    # for s in tokines:
    #     if  s[0][1]=="VBD" :
    #         if re.findall(r"\bed\w*?T\b",s[0][0]) :
    #                 print(" ")
    #         else:
    #             print(s[0][0])
    # -----------------------------------------
    # read stop words

    x = function.create_indexfile()
    print(x)
    print("enter query:---------------------------------------")
    q = input()
    corect_word = function.spelling_correct(q)
    function.create_indexquery(corect_word, x)
