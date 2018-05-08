#import regex
import re
import csv
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#start process_tweet
def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

#Read the tweets one by one and process it
#fp = open('J_tsar_tweets.csv', 'r')
#line = fp.readline()

#while line:
   # processedTweet = processTweet(line)
#    lemmatizer = WordNetLemmatizer(processedTweet)
  #  print (processedTweet)
#    line = fp.readline()
#end loop
#fp.close()

#initialize stopWords
stopWord = []

#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end

#start getStopWordList
def getStopWordList(stopWordListFileName):
    #read the stopwords file and build a list
    stopWord = []
    stopWord.append('AT_USER')
    stopWord.append('URL')

    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWord.append(word)
        line = fp.readline()
    fp.close()
    return stopWord
#end

#start getfeatureVector
def getFeatureVector(tweet):
    featureVector = []
    #split tweet into words
    words = tweet.split()
    for w in words:
        #replace two or more with two occurrences
        w = replaceTwoOrMore(w)
        #strip punctuation
        w = w.strip('\'"?,.')
        #check if the word stats with an alphabet
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        #ignore if it is a stop word
        if(w in stopWord or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector
#end

#Read the tweets one by one and process it
#fp = open('J_tsar_tweets.csv', 'r')
#line = fp.readline()
lemmatizer = WordNetLemmatizer()
#st = open('stopwords.txt', 'r')
stopWord = set(stopwords.words('english'))
# getStopWordList('stopwords.txt')

fp = open('J_tsar_tweets.csv', 'r')
line = fp.readline()
while line:
    processedTweet = processTweet(line)
   # print(processedTweet)
    lemmatiz = " "
  #  words1 = processedTweet.split()
    #for word in words1:
      #  lemma = WordNetLemmatizer(word)
       # lemmatizer = lemmatizer.append(lemma)
    featureVector = getFeatureVector(processedTweet)
#    lemmatize
    #fp = open('J_tsar_tweets.csv', 'r')
#line = fp.readline()
    for i in range(0,len(featureVector)):
        lemma = lemmatizer.lemmatize(featureVector[i])
        lemmatiz = lemmatiz + " " + lemma
       
       # lemmatiz = lemmatiz.append(lemma)
        
    #print (featureVector)
    print(lemmatiz)
#    with open('outputtweet.csv','w') as csvfile:
#        csvwriter = csv.writer(csvfile)
#        csvwriter.writerow(lemmatiz)
#    
    line = fp.readline()
    
    
#end loop  
fp.close() 