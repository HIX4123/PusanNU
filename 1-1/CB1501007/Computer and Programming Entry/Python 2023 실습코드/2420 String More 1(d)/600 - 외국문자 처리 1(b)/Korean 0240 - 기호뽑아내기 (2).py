#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-05-06
#-------------------------------------------------------------------------------

content = """test content☆ 漢字〓韓國外交部對外稱 end ◆
          日語〓慰謝料%$ #@
          としてフルハウス(Full House)をあげるというィヨンジェの
          言葉に,ジウンは寝ても寝る事ができないで悩む。end
          ◆ 한글〓해쉬(Hash)값 필터링 시스템
          """


def is_symbol(x):
    if(x == " " or x=="", x =='\n') : return(False)
    sun = ord(x)
    if ( 32 <= sun <= 47 or 58 <= sun <= 64):
    # !"#$%&'()*+,-./        :;<=>?@
         return(True)
    else : return(False)


for (i,w) in enumerate( list(content)) :
    if is_symbol(w) : print(i, w, "기호")





