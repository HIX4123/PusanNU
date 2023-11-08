
# 특정 원소의 위치를 모두 찾아내고 싶다면

ltext="""
In general, the main tasks of the first stage of the
operation have been completed," Colonel General Sergei
Rudskoy, first deputy chief of Russia's General Staff,
said in a Friday briefing. "The combat potential of the
armed forces of Ukraine has been significantly reduced,
allowing us, I emphasize again, to focus the main efforts
on achieving the main goal - the liberation of Donbas.
""".split()


wlist=[ i for (i,word) in enumerate(ltext) if word=="the"]


print("단어 the의 위치= ", wlist)