####-------Feature____Extraction-----------###
#The mapping from textual data to real valued vectors is called feature extraction

#---Some Terms---#
#Bag of Words(BOW): list of unique words in the text corpus(collection of words)

#Term Frequency-Inverse Document Frequency(TF-IDF):
#to count the number of times each words appear in a document


#------Tf-idf Vectorizer-----#

#Tf = no of times term t appears in a document/no. of terms in the document

#IDF = log(N/n), N= number of documents, n= no of documents a term t has apperaed in

#IDF of rare word is high and frequent word is low

# TF-IDF = TF * IDF
