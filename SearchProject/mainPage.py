import re
import numpy as np
import pandas as pd


my_file = open("albert.txt", "r")
content = my_file.read()
content = content.casefold()
content_list1 = re.split(', |\s', content)
my_file.close()
my_file = open("english3.txt", "r")
content = my_file.read()
content = content.casefold()
content_list2 = re.split(', |\s', content)
my_file.close()
my_file = open("stopwords.txt", "r")
content = my_file.read()
content = content.casefold()
content_list3 = re.split(', |\s', content)
my_file.close()
my_file = open("stephen.txt", "r")
content = my_file.read()
content = content.casefold()
content_list4 = re.split(', |\s', content)
my_file.close()
my_file = open("thomas.txt", "r")
content = my_file.read()
content = content.casefold()
content_list5 = re.split(', |\s', content)
my_file.close()



def wordExist(word):
    string =[]
    existDoc1 = False
    existDoc2 = False
    existDoc3 = False
    stopWord = False
    englishWord = False
    cntFile = 0
    cntword = 0
    for x in content_list1:
        if word == x:
            existDoc1 = True
            cntword = cntword + 1
    if existDoc1:
        cntFile = cntFile + 1
    for x in content_list4:
        if word == x:
            existDoc2 = True
            cntword = cntword + 1
    if existDoc2:
        cntFile = cntFile + 1
    for x in content_list2:
        if word == x:
            englishWord = True
    for x in content_list5:
        if word == x:
            existDoc3 = True
            cntword = cntword + 1
    for x in content_list3:
        if word == x:
            stopWord = True
    if existDoc3:
        cntFile = cntFile + 1




    if existDoc1==True or existDoc2==True or existDoc3==True:
        string += ["the word:", word, "exist\n"]
        if stopWord:
            string += ["the word:", word, "is stop word"]
        return string
    elif englishWord and not existDoc1 and not existDoc2 and not existDoc3:
        string = ["the word:", word, "is english word but not exist in the database"]
        return string
    elif not englishWord:
        string = ["not english word"]
        return string


def apperance_of_word(word):
    string = []
    existDoc1 = False
    existDoc2 = False
    existDoc3 = False
    stopWord = False
    englishWord = False
    names_of_files_word_in = []
    cntFile = 0
    cntword = 0
    for x in content_list1:
        if word == x:
            existDoc1 = True
            cntword = cntword + 1
    if existDoc1:
        cntFile = cntFile+1
        names_of_files_word_in.append("albert.txt")
    for x in content_list4:
        if word == x:
            existDoc2=True
            cntword = cntword + 1
    if existDoc2:
        cntFile = cntFile + 1
        names_of_files_word_in.append("stephen.txt")
    for x in content_list5:
        if word == x:
            existDoc3 = True
            cntword = cntword + 1
    if existDoc3:
        cntFile = cntFile + 1
        names_of_files_word_in.append("thomas.txt")

    for x in content_list2:
        if word == x:
            englishWord = True
    for x in content_list3:
        if word == x:
            stopWord = True

    # if cntFile> 0 and not stopWord:
    string += [f' the word:", {word}, ",exist", {cntFile}, "number of files\n']


    # if cntword > 0 and not stopWord:
    string += [f'the word:", {word}, ",exist", {cntword}, "number of times\n']

    if len(names_of_files_word_in) > 0:
        string += [f'the files the word exist in are: , {names_of_files_word_in}']
    return string

#check apperance of n_Gram words
def n_gram(word,number):
    list = []
    for i in range(0, len(word), number):
        list.append(word[i:i + number])
    for turn in list:
        if turn == ' ':
            list.remove(turn)
    return list



def count_occurrence(words, word_to_count):
    count = 0
    for word in words:
        if word == word_to_count:
          # update counter variable
            count = count + 1
    return count

#show in each doc the number of apperance of a choosen word
def count_apperance_of_word_in_doc(word):
    string = []
    string += [f'{word} appears in thomas.txt document {count_occurrence(content_list5, word)} time(s)\n']
    string += [f'{word} appears stephen.txt document {count_occurrence(content_list4, word)} time(s)\n']
    string += [f'{word} appears albert.txt document {count_occurrence(content_list1, word)} time(s)\n']
    return string





# switcher = {
#     1:wordExist,
#     2:apperance_of_word,
#     3:n_gram,
#     4:count_apperance_of_word_in_doc,
# }
#
# def switch_demo(argument=int(input("press 1 for wordExist\npress 2 for apperance_of_word in all files\npress 3 for n-gram method\npress 4 to show in each Doc the number of apperance of the choosen word:\npress 5 for exist: "))):
#     while(argument!=5):
#         switcher[argument]()
#         argument = int(input("\npress 1 for wordExist\npress 2 for apperance_of_word in all files\npress 3 for n-gram method\npress 4 to show in each Doc the number of apperance of the choosen word:\npress 5 for exist:  "))
#
# switch_demo()



# wordExist()
# apperance_of_word()
# n_gram()
# count_apperance_of_word_in_doc()