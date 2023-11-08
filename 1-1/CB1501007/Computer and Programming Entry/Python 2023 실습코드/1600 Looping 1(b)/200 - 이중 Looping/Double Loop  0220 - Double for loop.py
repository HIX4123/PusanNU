#for loop


mystr = "Korea-Japan"
n = len( mystr )

for i in range(n) :
    for j in range(i+1, n+1) :
        print("[", i, ",", j, "]=", end="")
        print(mystr[i:j])
