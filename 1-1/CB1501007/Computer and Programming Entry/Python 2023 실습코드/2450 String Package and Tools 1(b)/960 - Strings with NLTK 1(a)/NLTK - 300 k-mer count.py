#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:
# 설치방법 > pip install nltk
#          python> nltk.download( )
#-------------------------------------------------------------------------------

etext="""
Alexey Fyodorovitch Karamazov was the third son of Fyodor Pavlovitch
Karamazov, a land owner well known in our district in his own day, and
still remembered among us owing to his gloomy and tragic death, which
happened thirteen years ago, and which I shall describe in its proper
place. For the present I will only say that this “landowner”?for so we
used to call him, although he hardly spent a day of his life on his own
estate?was a strange type, yet one pretty frequently to be met with, a
type abject and vicious and at the same time senseless. But he was one of
those senseless persons who are very well capable of looking after their
worldly affairs, and, apparently, after nothing else. Fyodor Pavlovitch,
for instance, began with next to nothing; his estate was of the smallest;
he ran to dine at other men’s tables, and fastened on them as a toady, yet
at his death it appeared that he had a hundred thousand roubles in hard
cash. At the same time, he was all his life one of the most senseless,
fantastical fellows in the whole district. I repeat, it was not
stupidity?the majority of these fantastical fellows are shrewd and
intelligent enough?but just senselessness, and a peculiar national form of
it.
"""

ktext="""
구글 뉴스(Google News)는 구글이 제공하고 운영하는 무료 뉴스 애그리게이터이다.
자동 집계 알고리즘에 의해 수천 곳의 발행사로부터 최신의 정보를 선별한다.
현 총괄자는 리처드 징그러스이다.
2002년 9월 출범한 이 서비스는 2006년 1월까지 3년에 걸쳐 베타 테스트로 표기되었다.[1]
초기의 아이디어는 크리시나 브하라트(Krishna Bharat)에 의해 개발되었다.[2][3]
구글 뉴스는 2014년 12월 16일부로 스페인에서 구글 뉴스 서비스를 중단한다고 밝혔다.
이는 스페인 저작권의 개정으로 2015년 1월부터 뉴스 인용문에도 저작권료를 지불해야 하기 때문이다.[4]
이 서비스는 대한민국을 비롯한 수십개 국가에서 이용할 수 있다.                [출처 필요]
"""

import nltk
from nltk.util import ngrams
from collections import OrderedDict
from collections import Counter
import collections

def ngram_counts( T, n ):
    ngrm = ngrams( T, n )
    ngrm = [ ''.join(w) for w in ngrm ]
    mydic = collections.Counter(ngrm)
    odic = OrderedDict( sorted( mydic.items(), key=lambda t: t[1], reverse=True ) )
    print( '|'+str(n)+'-mer dict|:', len(odic) )
    for w in odic.keys():
        if odic[w] >= 3 :
            print(f'{w:}:{odic[w]:2} 번 나타남')
    return odic

def text_preproc( T ) :
    # white space --> _
    # new line --> $
    mT = T.replace(" ", "_")
    mT = mT.replace("\n", "$")
    return mT

ndict = ngram_counts( text_preproc(ktext), 3 )
ndict = ngram_counts( text_preproc(etext), 2 )