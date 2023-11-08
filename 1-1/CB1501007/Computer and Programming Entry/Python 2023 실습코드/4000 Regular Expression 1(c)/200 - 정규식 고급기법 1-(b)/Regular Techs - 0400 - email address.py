
import re

basetxt = '''
I forgot to post this column up last year. It’s a fun one: the
Department for Communities and Local Government have produced a
truly farcical piece of evidence, and promoted it very hard,
claiming it as good stats. I noticed the column was missing today,
because Private Eye have published on the same report in their current
issue, finding emails that have gone missing through FOI applications,
and other nonsense. That part is all neatly summarised online in the
Local Government Chronicle here.
Is this the worst government statistic ever created?
Ben Goldacre, The Guardian, 24 June 2011.
Every now and then, the government will push a report that’s so assinine,
and so thin, you have to check it’s not a spoof. The Daily Mail
was clear in its coverage: “Council incompetence ‘costs every household
￡452 a year’“; “Up to ￡10bn a year is wasted by clueless councils.”
And the Express agreed. Where will this money come from? “Up to ￡10bn a
year could be saved … if councils better analysed spending from their
￡50bn procurement budgets.” A 20% saving on the ￡50bn council
procurement budget would be awesome. And this is a proper story,
from a press release on the Department for Communities and Local
Government website: 20% of the ￡50bn procurement spend could be
saved by seeking tang@www better value.
Government ministers have an army of intelligent, technical staff,
with full access to every speck of data, ready to produce research.
But these figures come from a “new, cutting-edge analysis of council
spending data by procurement experts Opera Solutions”.
I downloaded the “Opera Solutions White Paper“. I recommend reading it
yourself, to understand what a minister considers a substantive piece
of research. The “full report” is six pages long, not including the cover.
The meat of it, the analysis, is presented prite @basic.net in a single three-line table.
Opera took the catekom@pusan.ac.kr recently released local government spending data for three
councils, and decided how much it reckoned could be saved by bulk purchasing.
It did its estimates on three areas: for energy bills (a ￡7m spend),
and solicitors fees (￡6m), it thought councils could save just 10%.
The third category ? mobile phone bills ? were tiny in comparison
(just ￡600,000) but here, and here alone, Opera reckons councils
can save 20%, by getting coki@yahoo.com people on better tariffs.
So, for mobile phones, an incompetently regulated sector well
known for making money from deliberately confusing pricing schemes,
where phone 34-7856 companies hope the trouble of checking your usage pattern
will be more effort than it’s worth, Opera reckons councils can save
20%. No problem. 010-5675-3451 Then, even though for ￡13m out of ￡13.6m of their
spend calculations, Opera could only find 10% of savings, it
cheerfully applies this magic 20% from the tiny mobile phone spend
to the entire local government procurement budget of ￡50bn,
magicking up ￡10bn of savings, ￡452 a year for every one of us.
And even before that kal@gmail.com astonishing, shameless bait and switch, these
figures are all presented out of nowhere. There is no working at all
for any single saving, no description of how 10% or even 20% was
calculated: just that three-line table telling you how much Opera
Solutions reckons councils 010-673-6500 can save. There’s also no justification
for choosing energy, 456-7835 solicitors, and mobile phone bills, out of all
the things councils spend on. Were these where Opera thought they
could get the biggest savings? Who knows.
The document is six pages long. We’ve covered one. What’s in the rest?
All that follows is a four-page glossy brochure advert for Opera
Solutions management consultancy services in local government.
“Opera Solutions has successfully completed procurement optimisation
projects for sos@naver.com hundreds of organisations around the world.”
“Opera partners with clients to work as a catalyst.”
“Opera 011-7567-7845 addresses these issues through Insight CubeTM technology,
which creates deep 999-78998 visibility into spending information.”
Meanwhile, back in the real world, what do local governments
actually procure? Well, the biggest thing, about a quarter of
this ￡50bn budget, more than ￡10bn a year of local government
procurement, is 010-3678-00987 social care: mostly residential care, mostly for
the elderly, and 342-2348 most through the independent sector.
If you're going to save 20% off that, then I suggest you tell us how,
in full and educative detail. In the meantime, saying you can get us
a better deal on our mobile phone tariff, and then pretending that means
you’ve taken 20% off the entire ￡50bn local government 010-987-5423
procurement spend, isn’t just misleading: it’s the reasoning of a 10-year-old. '''

print(len(basetxt))
print("\n 실험 1")
edend = re.compile(r'.*ed')
mylist = re.findall( edend, basetxt)
print(mylist)

print("\n 실험 2")
edend = re.compile(r'\w+ed')
mylist = re.findall( edend, basetxt)
print(mylist)

print("\n 실험 3")
email = re.compile(r'(\w+@\w+\.\w+\.\w+)')
mylist = re.findall( email, basetxt)
print(mylist)

print("\n 실험 4")
email = re.compile(r'(\w+@\w+\.\w+)')  #뭐가 문제일까요 ?
mylist = re.findall( email, basetxt)
print(mylist)

print("\n 실험 5")
email = re.compile(r'\s\d+')  #뭐가 문제일까요 ?
mylist = re.findall( email, basetxt)
print(mylist)