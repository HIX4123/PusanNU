#
content = """test content☆漢字〓韓國外交部對外稱 本週
          一個「非正式磋商」。end◆ 日語〓慰謝料
          としてフルハウス(Full House)をあげるというィヨンジェの
          言葉に,ジウンは寝ても寝る事ができないで悩む。end
          ◆ 한글〓해쉬(Hash)값 필터링 시스템(Filtering system
          """

def is_hanja(x):
    if ( '一' <=x <=  '龥' )  : return(True)

def is_nippon(x):
    if ( 'ぁ' <= x <= 'ゔ' )  : return(True)
    if ( 'ァ' <= x <= 'ヴ' )  : return(True)



clist = list( content )

for (i,w) in enumerate( clist ) :

    if( is_hanja(w) ) :
        print(f" 한자 i={i:3}, {w}")
    if( is_nippon(w) ) :
        print(f" 일본어 i={i:3}, {w}")

"""

and comment_msg not regexp '/[ぁ-ゔ]+|[ァ-ヴー]+[々〆〤]+/u'
and comment_msg not regexp '[一-龥]'
and (comment_msg regexp '[가-힇]'
or comment_msg regexp '[ㄱ-ㅎㅏ-ㅣ]');

#일본어 포함 한글 미포함 -> ja
select * from comment
and comment_msg not regexp '[가-힇]'
and comment_msg not regexp '[ㄱ-ㅎㅏ-ㅣ]'
and comment_msg regexp '[ぁ-ゔ]+|[ァ-ヴー]+[々〆〤]+/u';

#한자 포함 한글미포함 일어미포함 -> zh
select * from comment
and comment_msg not regexp '[가-힇]'
and comment_msg not regexp '[ㄱ-ㅎㅏ-ㅣ]'
and comment_msg not regexp '[ぁ-ゔ]+|[ァ-ヴー]+[々〆〤]+/u'
and comment_msg regexp '[一-龥]';

# 알파벳포함 한글,자음,일어,한자 미포함  -> en
select * from comment
and comment_msg not regexp '[가-힇]'
and comment_msg not regexp '[ㄱ-ㅎㅏ-ㅣ]'
and comment_msg not regexp '[一-龥]'
and comment_msg regexp '[a-zA-Z]';

"""



