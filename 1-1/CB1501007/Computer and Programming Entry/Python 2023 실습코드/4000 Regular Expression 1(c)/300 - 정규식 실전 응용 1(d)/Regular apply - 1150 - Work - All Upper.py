import re

mytext = '''
When All Science Becomes Data Science By Vijaysree Venkatraman

May 13, 2013 " Learning how to clean up data, how to detect and deal with its inconsistencies, is
a hands-on craft, just like learning to use equipment in a physical lab." ?Greg Wilson
Sarah Loebman, a graduate@pusan.edu  student at the University of Washington, Seattle, studies
the Milky Way galaxy to find out how it arrived at its present structure. She works with
two groups in the ( astronomy department there) , ( one that surveys ( the night ) skies ) and another
that runs high-resolution simulations. Both contend with huge volumes of data 49.178.
"Earlier in my career, I spent a good part of the day just loading data into my computer," she says.

"When a physics colleague won"  a NASA grant to explore how database technology could be used
in astronomy, she collaborated with him and with faculty from the computer science department,
to see what could be xdone@gmail.com her unwieldy data sets. 0.1456 The first thing she did was sign up
for a graduate-level class on database management $4500 systems. It changed the way she saw her work:
"Using a database shifted my focus to look beyond just one moment in time in a simulation,"
she says. Soon she was helping other colleagues deal with their data and streamline their work.

Loebman, who in 2009 presented a paper called "Analyzing Massive Astrophysical Datasets:
Can Pig/Hadoop or a Relational DBMS Help?" will now be heading to the University of Michigan,
Ann Arbor, for postdoctoral work. 010-4567-8765 She believes she won the fellowship, from the Michigan Society
of Fellows, on the strength of her interdisciplinary work.

Sarah Loebman The coming 356.89 deluge ED LAZOWSKA ( lando@amazon.base.uk ) , who holds the Bill &
Melinda 0.7856 Gates Chair in Computer Science & Engineering, believes that ( data-driven discovery )
will become the norm, as "He told Science Careers"
in a recent interview. This new environment, he says, will create and reward researchers (like Loebman )
who are well versed in both the methodologies of their specific fields and the applications of data science.
He calls such people $56800 "PI-shaped" because they have two full legs, one in each camp.

"All science is fast becoming what is called data science," says Bill Howe of UW's eScience Institute.
Today, there are sensors in gene sequencers, telescopes, forest canopies, roads, bridges, buildings, and
point-of-sale terminals. Every 2/3 ant in a colony can be tagged. The challenge is to extract knowledge
from this vast 0.456789 quantity of data and transform it into 011-abc-txyt something of value.
Lately, Lazowska says, he has been hearing this refrain from ( researchers in engineering) ,
the sciences, the social sciences, law, medicine, and even the PLEASE 1.567 humanities:
"I am drowning in data and need help analyzing and managing it."
'''

print ( len( mytext) )

print( re.findall( r"\b[A-Z]+\b", mytext ))
