import nltk
from nltk.tokenize import word_tokenize
from nltk.parse.generate import generate

def cfg_parse(sentence):
    sent_tk = nltk.pos_tag(word_tokenize(sentence))
    for one in sent_tk:
        if one[1] == 'NNP':
            s_NP = "\'" + one[0] + "\'"
        if one[1] == 'VBD' or one[1]=='VBN':
            s_V = "\'" + one[0] + "\'"
        if one[1] == 'NN':
            s_N = "\'" + one[0] + "\'"
        else:
            pass
    cfg_grammar2 = nltk.CFG.fromstring("""
    S -> NP VP 
    VP -> V N 
    NP -> {} 
    V -> {} 
    N -> {}
    """.format(s_NP,s_V,s_N))
    for sentence in generate(cfg_grammar2):
        print(" ".join(sentence))
    return