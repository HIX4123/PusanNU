S = """
In 1956, a group of scientists led by John McCarthy,
a young assistant-professor of mathematics, gathered
at the Dartmouth College, NH, for an ambitious
six-week project: Creating computers that could
use language, form abstractions, and concepts,
solve kinds of problems now reserved for humans,
and improve themselves.
The project kickstarted the field that has become known
as artificial intelligence AI. At the time,
the scientists thought that a 2-month, 10-man study of
artificial intelligence would solve the biggest part
of the AI equation. We think that a significant advance
can be made in one or more of these problems if
a carefully selected group of scientists work on it
together for a summer, the first AI proposal read.
More than six decades later, the dream of creating
artificial intelligence still eludes us. We still
don’t have thinking machines that can think and solve
problems like a human child, let alone an adult.
But we’ve made a lot of progress, and as a result,
the field of AI has been divided into artificial
general intelligence AGI and artificial narrow
intelligence ANI.
"""

S = S.lower()
LS = S.split()
LS.sort( )

for i,w  in enumerate(LS) :
    print(f"i={i:3}, list word= {w}")


Lset = set ( LS )
Mlist = list(Lset)
Mlist.sort( )

for i,w  in enumerate( Mlist) :
    print(f"i={i:3}, set word= {w}")
