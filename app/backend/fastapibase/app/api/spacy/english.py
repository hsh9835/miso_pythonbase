import spacy
from spacy import displacy


def example1():
    nlp = spacy.load("en_core_web_sm")
    doc = nlp('''Did you know? NASA has proved that distance from 
              The Sun to The Earth is equal to the distance from 
              The Earth to The Sun. 
              ...What??''')

    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)

    return displacy.render(doc, style='ent')


def example2():
    nlp = spacy.load("en_core_web_sm")
    doc = nlp('''
        그거 아시나요?
        나사는 태양과 지구사이의 거리가
        지구와 태양사이의 거리와 일치한다는 것을
        증명했습니다.
        
        ... 뭐라고요?
    ''')

    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)

    return displacy.render(doc, style='ent')
