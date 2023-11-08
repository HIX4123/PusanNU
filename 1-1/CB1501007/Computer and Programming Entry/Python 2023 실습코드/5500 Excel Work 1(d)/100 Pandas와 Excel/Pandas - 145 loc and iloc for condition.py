#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-01
#-------------------------------------------------------------------------------



# http://blog.naver.com/PostView.nhn?blogId=rising_n_falling&logNo=221622971970&parentCategoryNo=12&categoryNo=15&viewDate=&isShowPopularPosts=false&from=postView
import pandas


df = pandas.read_excel('sam50.xlsx') # , sheet_name='region')


for (i,w) in enumerate( df.columns.tolist()):
    print(f'{i}= {w}')

print(f' df.shape= {df.shape}')

print( df.columns[2], df.columns[7] )

newdf = df[ [df.columns[3], df.columns[5]]  ]     # 2번째, 7번째만 추추
print( newdf.head(10))

# 특정한 row만 선택하기

onlyrow = df.loc[ [1,4,6,7], [ '성별코드', '허리둘레']  ]
print( onlyrow )

onlyrow = df.loc[ [1,10], [ df.columns[20], df.columns[25],df.columns[28] ]  ]
print( onlyrow )

mydf = df.iloc[:, [ 4, 9, 23 ] ] # 칼럼선택
print(mydf)

mydf = df.iloc[:,  9:14  ] # 칼럼 구간 선택   iloc
print(mydf)

mydf = df.iloc[ 5:9, :  ] # row 구간 선택   iloc
print(mydf)

mydf = df.iloc[ -5:-1, 5:10  ] # row 구간 선택   iloc
print(mydf)


yourdf = df[ df['성별코드']==1]
print( yourdf )

yourdf = df[ df['신장(5Cm단위)']> 170 ]
print( yourdf )

##print("\n -------------------------- \n")
##for w in range( len(onlyrow)):
##    print(f'{w} = { onlyrow.loc[ [w] ] }')


