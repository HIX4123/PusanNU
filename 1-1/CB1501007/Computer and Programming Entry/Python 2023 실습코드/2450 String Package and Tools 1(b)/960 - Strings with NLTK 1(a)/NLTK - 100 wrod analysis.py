#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-14
#-------------------------------------------------------------------------------

from nltk.tokenize import sent_tokenize,word_tokenize

data="Hey! Are you okay? Hey! Are you okay?"
CNN="""
Shanghai reported three Covid-19 deaths Monday, the first officially announced fatalities from a raging Omicron outbreak that has infected hundreds of thousands of people despite a government-enforced city-wide lockdown.
Three elderly people aged between 89 and 91 died from Covid on Sunday, after their condition deteriorated in hospital, the Shanghai Municipal Health Commission said in a statement Monday.
All three were unvaccinated and had underlying health conditions such as coronary heart disease, diabetes and high blood pressure, according to officials.

The city reported 2,417 symptomatic cases and 19,831 asymptomatic infections Monday, slightly down from the previous day, according to the health commission.

The death toll appears strikingly low against the vast number of cases -- since March 1, more than 370,000 people in Shanghai have been infected, and by the official count, no one had died of Covid until Sunday.
In comparison, the region's other financial hub Hong Kong has recorded nearly 9,000 Covid deaths out of 1.18 million total cases as of January this year.
Experts have attributed Hong Kong's high death toll to its high proportion of unvaccinated elderly. As of early March, just 48% of people aged 70 or older had received two doses. And at the start of this year, just 25% of residents aged 80 or over had been vaccinated.

Shanghai's low official death toll has raised questions among some experts outside mainland China, especially given the vaccination coverage among the elderly in Shanghai is not that much higher than that of Hong Kong.
On Monday, Shanghai officials said 62% of the city's residents aged over 60 had been fully vaccinated, and 38% had received a booster shot. The number of fully vaccinated people aged over 80 was even lower, at just 15%, according to the Communist Party mouthpiece the People's Daily.
Jin Dongyan, a virologist at the University of Hong Kong, said Shanghai's low death toll is partly a result of how Covid deaths are counted in mainland China.
"The methods used by Hong Kong and the mainland to calculate deaths are completely different. Over 90% of the Covid deaths reported in Hong Kong will not be counted on the mainland," he said.
In Hong Kong, a person is counted as having died of Covid if they were confirmed to have contracted the coronavirus less than 28 days before their death -- even if they died of suicide or road accidents, Jin said.
"On the mainland, if the deceased had underlying ailments, most of them would be categorized as having died of other diseases instead of Covid," Jin said.
In Shanghai, the number of officially designated severe cases is also low. According to Wu Jinglei, director of the Shanghai health commission, only 16 severe cases were being treated in hospital as of Saturday. "One of them has been fully vaccinated, the rest were not vaccinated against Covid-19," he said.
Chinese health officials have noted the high proportion of asymptomatic and mild cases in the country's Omicron outbreak. Wang Guiqiang, an infectious disease doctor in Beijing, said at a government news conference on April 6 that that was because the Omicron variant is less virulent, people are vaccinated, and that active testing has detected many cases early, during the incubation period. But Wang cautioned that Omicron is still dangerous for the elderly, especially those who haven't received full vaccination.
"""

sen=sent_tokenize(CNN)
words=word_tokenize(CNN)

for i,w in enumerate(sen) :
    print(f"\n sentense{i:2} = \n {w}")


allword= sorted ( set( words) )

for i,w in enumerate(allword) :
    print( f"{i:3} words = {w}")