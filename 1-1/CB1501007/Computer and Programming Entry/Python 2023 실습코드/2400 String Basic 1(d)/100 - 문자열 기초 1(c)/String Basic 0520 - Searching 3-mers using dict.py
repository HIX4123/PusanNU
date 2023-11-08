#

m_dict = {}
mogi = "AGTCCCCATCTACGGGTCGTGACGACGTGTCAGTCAGTGACCCAATCTCAGCGTGC"


for x in range(len(mogi)-2):
    word = mogi[x:x+3]
    if word not in m_dict :
        m_dict[word] = []
        m_dict[word].append(x)
    else :
        m_dict[word].append(x)

for x in m_dict:
    # 가장 많이 나타난 단어와 위치
    print(x, m_dict[x])
