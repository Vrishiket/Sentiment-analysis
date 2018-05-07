import csv
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
filter= set(stopwords.words('english'))
from clean_tweet import pre
infile = 'J_tsar_tweets.csv'
rw=[]
with open(infile, 'r+') as csvfile:
    rows = csv.reader(csvfile)
   
    
    for row in rows:
        sentence = row
        
        blob = TextBlob(pre(sentence[2]))
        sent=""
        if blob.polarity <0:
           sent="negative"
           print(blob.polarity,sent)
        elif blob.polarity >0:
            sent="Positive"
            print(blob.polarity,sent)
        else:
            sent="Neutral"
            print(blob.polarity,sent)
        row=row+[blob.polarity,sent]
        rw.append(row)
with open("J_tsar_tweets_sent).csv", 'w') as csvfile:
    csvWriter = csv.writer(csvfile)
    for r in rw:     
        csvWriter.writerow(r)
    #outfile="vrishi.csv"
    #with open(infile, 'w') as csvfile:
        
    