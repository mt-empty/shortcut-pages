# NLTK

> Source: http://www.nltk.org/

$ Set Up
    `pip install nltk              {{installs NLTK}} 
    `import nltk                   {{import everything from nltk}} 

$ Tagging
    `nltk.pos_tag(token_list)      {{part of speech annotation (pennbank)}} 

$ Normalization
    `[w for w in text1 if w.isalpha()]
>                                  {{remove punctutation}} 
    `[w.lower() for w in text]     {{convert each token to lowercase}} 
    `set(text1)                    {{remove duplicate tokens}} 

$ Tokenization
    `nltk.word_tokenize(string)    {{tokenize a string}} 

$ Stopwords
    `from nltk.corpus import stopwords
>                                  {{imports stopwords}} 
    `stopwords.words('english')    {{list english stopwords}} 
    `stopwords.words('spanish')    {{list spanish stopwords}} 
    `[w for w in sentence if w not in stopwords.words('english')]
>                                  {{remove stopwords from sentence}} 

$ Counting
    `len('this is a sentence')     {{count number of codepoints (letters)}} 
    `len(['a', 'tokenized', 'sentence'])
>                                  {{count number of tokens}} 
    `len(set([tokenized', 'sentence']))
>                                  {{count unique number of tokens}} 
    `nltk.FreqDist([tokenized', 'sentence'])
>                                  {{get unigram frequency distribution}} 
    `document.count('goose')       {{count occurrences of 'goose' within text}} 

