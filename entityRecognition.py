import spacy
nlp = spacy.load("en_core_web_sm")
from spacy.scorer import Scorer

# Default scoring pipeline
scorer = Scorer()

# Provided scoring pipeline
nlp = spacy.load("en_core_web_sm")
scorer = Scorer(nlp)
text=nlp("Mr.Varun Kumar works in HCL Enterprice which in in India")
for word in text.ents:
    print(word.text,word.label_)
    # print(scorer)