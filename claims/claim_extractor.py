import spacy

nlp = spacy.load("en_core_web_sm")

def extract_claims(answer):

    doc = nlp(answer)

    claims = []

    for sent in doc.sents:
        claims.append(sent.text)

    return claims