# Penn Treebank Tagset

> Source: http://web.mit.edu/6.863/www/PennTreebankTags.html

$ Clause Level
    `S                             {{Simple declarative clause.}} 
    `SBAR                          {{Clause introduced by a (possibly empty) subordinating conjunction.}} 
    `SBARQ                         {{ Direct question introduced by a wh-word or a wh-phrase. Indirect questions and relative clauses should be bracketed as SBAR, not SBARQ.}} 
    `SINV                          {{Inverted declarative sentence, i.e. one in which the subject follows the tensed verb or modal.}} 
    `SQ                            {{Inverted yes/no question, or main clause of a wh-question, following the wh-phrase in SBARQ.}} 

$ Phrase Level
    `ADJP                          {{Adjective Phrase}} 
    `ADVP                          {{Adverb Phrase}} 
    `CONJP                         {{Conjunction Phrase}} 
    `FRAG                          {{Fragment}} 
    `INTJ                          {{Interjection. Corresponds approximately to the part-of-speech tag UH}} 
    `LST                           {{List marker. Includes surrounding punctuation}} 
    `NAC                           {{Not a Constituent; used to show the scope of certain prenominal modifiers within an NP}} 
    `NP                            {{Noun Phrase}} 
    `NX                            {{Used within certain complex NPs to mark the head of the NP}} 
    `PP                            {{Prepositional Phrase}} 
    `PRN                           {{Parenthetical}} 
    `PRT                           {{Particle. Category for words that should be tagged RP}} 
    `QP                            {{Quantifier Phrase (i.e. complex measure/amount phrase); used within NP}} 
    `RRC                           {{Reduced Relative Clause}} 
    `UCP                           {{Unlike Coordinated Phrase}} 
    `VP                            {{Verb Phrase}} 
    `WHADJP                        {{Wh-adjective Phrase}} 
    `WHAVP                         {{Wh-adverb Phrase}} 
    `WHNP                          {{Wh-noun Phrase}} 
    `WHPP                          {{Wh-prepositional Phrase}} 
    `X                             {{Unknown, uncertain, or unbracketable}} 

$ Word Level
    `CC                            {{Coordinating conjunction}} 
    `CD                            {{Cardinal number}} 
    `DT                            {{Determiner}} 
    `EX                            {{Existential there}} 
    `FW                            {{Foreign word}} 
    `IN                            {{Preposition or subordinating conjunction}} 
    `JJ                            {{Adjective}} 
    `JJR                           {{Adjective, comparative}} 
    `JJS                           {{Adjective, superlative}} 
    `LS                            {{List item marker}} 
    `MD                            {{Modal}} 
    `NN                            {{Noun, singular or mass}} 
    `NNS                           {{Noun, plural}} 
    `NNP                           {{Proper noun, singular}} 
    `NNPS                          {{Proper noun, plural}} 
    `PDT                           {{Predeterminer}} 
    `POS                           {{Possessive ending}} 
    `PRP                           {{Personal pronoun}} 

$ Word Level (Cont.)
    `PRP$                          {{Possessive pronoun (prolog version PRP-S)}} 
    `RB                            {{Adverb}} 
    `RBR                           {{Adverb, comparative}} 
    `RBS                           {{Adverb, superlative}} 
    `RB                            {{Particle}} 
    `SYM                           {{Symbol}} 
    `TO                            {{to}} 
    `UH                            {{Interjection}} 
    `VB                            {{Verb, base form}} 
    `VBD                           {{Verb, past tense}} 
    `VBG                           {{Verb, gerund or present participle}} 
    `VBN                           {{Verb, past participle}} 
    `VBP                           {{Verb, non-3rd person singular present}} 
    `VBZ                           {{Verb, 3rd person singular present}} 
    `WDT                           {{Wh-determiner}} 
    `WP                            {{Wh-pronoun}} 
    `WP$                           {{Possessive wh-pronoun}} 
    `WRB                           {{Wh-adverb}} 

