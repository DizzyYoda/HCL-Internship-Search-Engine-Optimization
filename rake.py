# install required pyhton libraries like rake_nltk

# import nltk
# nltk.download('stopwords')
# >>> nltk.download('punkt')
from rake_nltk import Rake


r = Rake()
text="Machine learning is good"
r.extract_keywords_from_text(text)
r.get_ranked_phrases()
list=r.get_ranked_phrases_with_scores()
print(list)
l2=[]
l=len(r.get_ranked_phrases())
for i in range(0,l):
    if(r.get_ranked_phrases_with_scores()[i][0]>1):
        print(r.get_ranked_phrases_with_scores()[i][1])
        
