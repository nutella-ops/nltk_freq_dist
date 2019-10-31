#!/usr/bin/python3
import nltk, os
nltk.download("punkt")

################################
#                              #
#    LIST WORD OCCURENCES      #
#    IN YOUR CRAPPY DOCUMENT   # 
#                              #
################################

#current working directory
current_dir = os.getcwd()

#output formatting
print("")

#list avaliable files 
for root, dirs, files in os.walk(current_dir):
    for name in files:
        print(name)

#output formatting
print("")

#user selects file to tokenize 
selected_file = input("open_file: ")

#path to file
doc = os.path.join(current_dir + "/" + str(selected_file))

#display path to user
print("file_path = "+doc)

#load file into NLTK 
doc_loaded = open(doc).read()

#tokenize file
doc_tokenized = nltk.word_tokenize(doc_loaded)

#perform frequency distribution of words
doc_freq = nltk.FreqDist(doc_tokenized)

#length of word distribution list
print(doc_freq.most_common(int(input("list_length: "))))
