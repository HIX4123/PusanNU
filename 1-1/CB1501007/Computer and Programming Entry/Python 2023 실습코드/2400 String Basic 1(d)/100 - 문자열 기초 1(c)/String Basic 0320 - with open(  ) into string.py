
with open("mogi-dna-01.inp") as f:
    this = f.read() #.strip()

print( f"모기 DNA={this} \n 충길이= {len(this)}")

that=this.replace('\n', '') # 각 줄 끝에 있는 enter 문자를 지운다.
#왜 ? 한 줄로 만들기 위해서

print( f"\n\n 모기 DNA={that} \n 충길이= {len(that)}")

