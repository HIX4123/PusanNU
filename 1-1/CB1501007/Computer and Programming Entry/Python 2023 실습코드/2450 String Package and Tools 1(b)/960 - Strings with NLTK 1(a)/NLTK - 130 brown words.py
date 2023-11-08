#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-14
#-------------------------------------------------------------------------------

from nltk.tokenize import sent_tokenize,word_tokenize

from nltk.corpus import brown

Lwords = brown.words()
print(" Length= ", len( Lwords ))

for (i,w) in enumerate( Lwords ):
    print(i,w)
    if i >= 100 : break


