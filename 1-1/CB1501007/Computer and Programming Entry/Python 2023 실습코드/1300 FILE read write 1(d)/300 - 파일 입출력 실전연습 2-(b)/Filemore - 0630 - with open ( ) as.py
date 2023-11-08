# 모기 DNA 읽


with open("mogi-dna-01.inp") as f:
    this = f.read() #.strip()

print( this, len(this))

that=this.replace('\n', '') # 각 줄의 끝에 있는 enter 문자를 지운다.

print("\n 지운 다음 서열", that, len( that ))
