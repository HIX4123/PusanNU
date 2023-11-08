# List Comprehension, 가장 Pythonic 하게 리스트를 만드는 방법



#           생성 for 문장:     조건문
da = [ w    for w in range(25) if (w+11)**5 %3 == 1 ]
print("Orange 1=", da )


dc = [ (x,y) for x in range(3) for y in list("FM") ]
print("Apple 1= ", dc )

ld = [ str(x)+y  for y in list("FM") for x in range(3) ]
print("FM= ", ld )

le = [ a+b+c   for a in list("개똥밥") \
               for b in list("말소쥐") \
               for c in list("집땅") ]

for i,w in enumerate(le) :
    print(f"i={i:3} w= {w}" )
