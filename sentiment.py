from textblob import TextBlob


Feedback1 = " The farts at Anil's home were awesome"
Feedback2 = " The farts at Anil's home were lentil based"
blob1 = TextBlob(Feedback1)
blob2 = TextBlob(Feedback2)
print(blob1.sentiment)
print(blob2.sentiment)
