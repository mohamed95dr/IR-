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
import re, collections

porter = PorterStemmer()

lmtzr = WordNetLemmatizer()


# delete duplicate
def remove_duplicate_from_list(temp_list):
    if temp_list:
        my_list_temp = []
        for word in temp_list:
            if word not in my_list_temp:
                my_list_temp.append(word)
        return my_list_temp
    else:
        return []


def del_stop_words(list):
    f = open('stop words.txt', "r")
    line = f.read()
    stop_words = re.findall("\S+", line)
    f.close()
    list_w = []
    for w in list:
        if w not in stop_words:
            list_w.append(w)

    return list_w

    # function dates


def convert_to_regular_date(s):
    # s is output ==>   re.findall("regEx",str)
    _date = []
    s1 = ""
    for d in s:
        print(d[0])
        s1 = d[0]
        s1 += "-"
        if d[1] == "01" or d[1] == "January":
            s1 += "Jan"
        elif d[1] == "02" or d[1] == "February":
            s1 += "Feb"
        elif d[1] == "03" or d[1] == "March":
            s1 += "Mar"
        elif d[1] == "04" or d[1] == "April":
            s1 += "Apr"
        elif d[1] == "05" or d[1] == "May":
            s1 += "May"
        elif d[1] == "06" or d[1] == "June":
            s1 += "Jun"
        elif d[1] == "07" or d[1] == "July":
            s1 += "Jul"
        elif d[1] == "08" or d[1] == "August":
            s1 += "Aug"
        elif d[1] == "09" or d[1] == "September":
            s1 += "Sep"
        elif d[1] == "10" or d[1] == "October":
            s1 += "Oct"
        elif d[1] == "11" or d[1] == "November":
            s1 += "Nov"
        elif d[1] == "12" or d[1] == "December":
            s1 += "Dec"
        else:
            s1 += d[1]

        s1 += "-{}".format(d[2])
    _date.append(s1)
    return _date


# ----------------------------------------------------------------------
# words means verb or noun:


def wordsVorN(s):
    train = state_union.raw("2005-GWBush.txt")
    # sample_text = open("corpus/1.txt", "r").read()
    cust = PunktSentenceTokenizer(train)
    tok = cust.tokenize(s)

    # tokenized_word = word_tokenize(sample_text)
    # print(len(tokenized_word))
    # print(tokenized_word)
    verbs = []
    nouns = []
    for i in tok:
        words = nltk.word_tokenize(i)
        tag = nltk.pos_tag(words)
        for c in tag:
            # print(c[0])
            if c[1] == "VBD" or c[1] == "VBG" or c[1] == "VBN" or c[1] == "VBN" or c[1] == "VBP" or c[1] == "VBZ" or \
                    c[
                        1] == "VP":
                verbs.append(c[0])
            else:
                nouns.append(c[0])

    return [verbs, nouns]


def porter_word(tokens):
    # the words porte and lemmatize
    # clean_corpus=remove_duplicate_from_list(clean_corpus)
    porte = []
    # for i in clean_corpus:
    for i in tokens:
        porte.append(porter.stem(i))

    return porte


def lemmatize_word(tokens):
    lemmatize = []
    for i in tokens:
        lemmatize.append(WordNetLemmatizer().lemmatize(i, 'v'))

    lem = []
    for i in lemmatize:
        lem.append(WordNetLemmatizer().lemmatize(i, 'a'))

    return lem


# spelling correct -----------
# -*- coding: utf-8 -*-
def spelling_correct(l):
    from textblob import TextBlob

    # incorrect spelling
    correct_w = []
    for j in l:
        correct_w.append(j)
    temp = []
    print("original text: " + str(l))
    word = nltk.word_tokenize(l)

    for i in word:
        b = TextBlob(i)
        print("corrected text: " + str(b.correct()))
        temp.append(str(b.correct()))
    print(temp)
    return temp
    # prints the corrected spelling
    #  print("corrected text: " + str(b.correct()))


# --------------------------------------------------------------------
def create_indexfile():
    # read stop words
    f = open("stop words.txt", "r")
    content = f.read()
    f.close()
    stop_words = re.findall("\S+", content)

    tokines = []
    clean_corpus = []
    diction = {}
    f1 = open("result.txt", "w")
    for x in range(1, 424):
        f = open("corpus/{}.txt".format(x), "r")
        contentAFile = f.read()
        f.close()
        ## processing dates
        # extract dates from string
        dates = re.findall("(0[1-9]|[12]\d|3[01])[/.-]"
                           "(0[1-9]|1[012])"
                           "[/.-](\d{4})", contentAFile)
        dates.extend(re.findall("(0[1-9]|[12]\d|3[01])[/.-]"
                                "(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
                                "[/.-](\d{4})", contentAFile))
        dates.extend(re.findall("(0[1-9]|[12]\d|3[01])[/.-]"
                                "(January|February|March|April|May|June|July|August|September|October|November|December)"
                                "[/.-](\d{4})", contentAFile))
        years = re.findall("\d{4}", contentAFile)

        # remove dates from string
        contentAFile = re.sub("(0[1-9]|[12]\d|3[01])[/.-]"
                              "(0[1-9]|1[012])"
                              "[/.-](\d{4})", "", contentAFile)
        contentAFile = re.sub("(0[1-9]|[12]\d|3[01])[/.-]"
                              "(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
                              "[/.-](\d{4})", "", contentAFile)
        contentAFile = re.sub("(0[1-9]|[12]\d|3[01])[/.-]"
                              "(January|February|March|April|May|June|July|August|September|October|November|December)"
                              "[/.-](\d{4})", "", contentAFile)
        contentAFile = re.sub("\d{4}", "", contentAFile)
        # convert dates to regular form 01-Mar-2020
        dates = convert_to_regular_date(dates)

        ## processing emails
        # extract emails from string in contentAFile
        emails = re.findall("\w+@\w+[.]\w+", contentAFile)
        # remove emails from string
        contentAFile = re.sub("\w+@\w+[.]\w+", "", contentAFile)

        ## processing phones
        # extract phones from string in contentAFile
        phones = re.findall("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4} | "
                            "\(\d{3}\)\s *\d{3}[-\.\s]??\d{4} |"
                            "\d{3}[-\.\s]??\d{4})", contentAFile)
        # remove phones from string
        contentAFile = re.sub("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4} | "
                              "\(\d{3}\)\s *\d{3}[-\.\s]??\d{4} |"
                              "\d{3}[-\.\s]??\d{4})", "", contentAFile)

        verbs_nounes = wordsVorN(contentAFile)
        verbs = del_stop_words(verbs_nounes[0])
        nounes = del_stop_words(verbs_nounes[1])

        #######################################################################

        lmtzr = WordNetLemmatizer()
        lemmatizedVerbs = []
        for v in verbs:
            lemmatizedVerbs.append(WordNetLemmatizer().lemmatize(v, 'v'))

        verbs = lemmatizedVerbs

        porter = PorterStemmer()
        porteredNouns = []
        for n in nounes:
            porteredNouns.append(porter.stem(n))

        nounes = porteredNouns

        ################################################################

        clean_corpus.extend(verbs)
        clean_corpus.extend(nounes)
        clean_corpus.extend(years)
        clean_corpus.extend(phones)
        clean_corpus.extend(dates)
        clean_corpus.extend(emails)

        for w in clean_corpus:
            if w not in tokines:
                tokines.append(w)

        temp_dic = {}  # dictionary for each term
        for y in clean_corpus:
            temp_dic.update({y: (1 + math.log(clean_corpus.count(y), 10)).__round__(5)})

        diction.update({x: temp_dic})
        print("document number : {} process".format(x))
        clean_corpus.clear()

    # Extension of the previous diction in order to contain all terms
    # and show their repetition within the document
    for a in range(1, 424):
        temp_dic2 = diction.get(a).copy()
        diction.get(a).clear()
        # print(temp_dic2)
        # for y in list(dict.fromkeys(tokines)):
        for y in tokines:
            if y not in temp_dic2.keys():
                diction.get(a).update({y: 0.0})
            else:
                diction.get(a).update({y: temp_dic2[y]})

    f1.write(str(diction))
    f1.close()
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tokines)
    f2 = open("tokines.txt", "w")
    f2.write(str(tokines))
    f2.close()
    return diction


#     ------------------
def create_indexquery(q, x):
    ## processing the query
    # read stop words
    f = open("stop words.txt", "r")
    content = f.read()
    f.close()
    stop_words = re.findall("\S+", content)

    termsInQuery = []  # this contain all terms in query without stop words
    terms = []  #
    ########################################################################
    # extract dates from query
    dates = re.findall("(0[1-9]|[12]\d|3[01])[/.-]"
                       "(0[1-9]|1[012])"
                       "[/.-](\d{4})", q)
    dates.extend(re.findall("(0[1-9]|[12]\d|3[01])[/.-]"
                            "(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
                            "[/.-](\d{4})", q))
    dates.extend(re.findall("(0[1-9]|[12]\d|3[01])[/.-]"
                            "(January|February|March|April|May|June|July|August|September|October|November|December)"
                            "[/.-](\d{4})", q))
    years = re.findall("\d{4}", q)

    # remove dates from string
    q = re.sub("(0[1-9]|[12]\d|3[01])[/.-]"
               "(0[1-9]|1[012])"
               "[/.-](\d{4})", "", q)
    q = re.sub("(0[1-9]|[12]\d|3[01])[/.-]"
               "(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
               "[/.-](\d{4})", "", q)
    q = re.sub("(0[1-9]|[12]\d|3[01])[/.-]"
               "(January|February|March|April|May|June|July|August|September|October|November|December)"
               "[/.-](\d{4})", "", q)
    q = re.sub("\d{4}", "", q)
    # convert dates to regular form 01-Mar-2020
    dates = convert_to_regular_date(dates)

    ## processing emails
    # extract emails from string in contentAFile
    emails = re.findall("\w+@\w+[.]\w+", q)
    # remove emails from string
    q = re.sub("\w+@\w+[.]\w+", "", q)

    ## processing phones
    # extract phones from string in contentAFile
    phones = re.findall("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4} | "
                        "\(\d{3}\)\s *\d{3}[-\.\s]??\d{4} |"
                        "\d{3}[-\.\s]??\d{4})", q)
    # remove phones from string
    q = re.sub("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4} | "
               "\(\d{3}\)\s *\d{3}[-\.\s]??\d{4} |"
               "\d{3}[-\.\s]??\d{4})", "", q)

    verbs_nounes = wordsVorN(q)
    verbs = del_stop_words(verbs_nounes[0])
    nounes = del_stop_words(verbs_nounes[1])

    #######################################################################

    lmtzr = WordNetLemmatizer()
    lemmatizedVerbs = []
    for v in verbs:
        lemmatizedVerbs.append(WordNetLemmatizer().lemmatize(v, 'v'))

    verbs = lemmatizedVerbs

    porter = PorterStemmer()
    porteredNouns = []
    for n in nounes:
        porteredNouns.append(porter.stem(n))

    nounes = porteredNouns

    ################################################################
    termsInQuery.extend(verbs)
    termsInQuery.extend(nounes)
    termsInQuery.extend(years)
    termsInQuery.extend(phones)
    termsInQuery.extend(dates)
    termsInQuery.extend(emails)

    diction_query = {}  # dictionary for terms and its frequencies
    for y in termsInQuery:
        diction_query.update({y: (1 + math.log(termsInQuery.count(y), 10)).__round__(5)})

    # remove duplication from termsInQuery
    tempTerms = []
    for w in termsInQuery:
        if w not in tempTerms:
            tempTerms.append(w)

    termsInQuery = tempTerms
    # print(termsInQuery)
    # print(diction_query)

    # # Extension of the previous diction in order to contain all terms
    # # and show their repetition within the query
    temp_dic2 = diction_query.copy()
    diction_query.clear()
    save_term = []
    f3 = open("tokines.txt", "r")
    y = f3.read()
    for i in y:
        save_term.append(i)

    for term in save_term:
        if term not in temp_dic2.keys():
            diction_query.update({term: 0.0})
        else:
            diction_query.update({term: temp_dic2[term]})
            # diction_query.update({y: 505})

    # for x, y in diction_query.items():
    # print(x," ====> ", y)

    print(matching(list(diction_query.values()), x))


# --------------------------create matching-----------------------
def matching(queryVector, diction):
    result = {}
    for key_dic in diction:
        value_dic = diction[key_dic]
        vector = list(value_dic.values())
        result.update({key_dic: angle_between_two_vector(queryVector, vector)})
    return result


# -------------------------


# to calculate inner product between to vectors
def inner_product(v1, v2):
    elNum = len(v1)
    result = 0
    for i in range(elNum):
        result += v1[i] * v2[i]
    return result


#################################################
# calculate a length of vector
# v is a list like that : [1,3,4,-9] .....
def length_vector(v):
    result = 0
    for i in range(len(v)):
        result += math.pow(v[i], 2)
    return math.sqrt(result)


#####################################################
# calculate angle between two vector
def angle_between_two_vector(v1, v2):
    cos_theta = inner_product(v1, v2) / (length_vector(v1) * length_vector(v2))
    theta = math.acos(cos_theta)
    # theta by Radian so we will convert it to Degrees
    theta = 180 * theta / math.pi
    return theta
