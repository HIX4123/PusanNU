# https://blog.ostermiller.org/finding-comments-in-source-code-using-regular-expressions/

import re


source = '''
#include <stdio.h>
template <typename T>
std::vector<T> slice;

int main( ) {
    auto first = v.cbegin() + m;
    long x , y ; // 변수 선언 ...
    float rt[ 345 ] ;
    while(1) {  /* 이것은 설명문 입니다. */
         rt = x[2]+2345 ;
    }
    // Hey This is a comment
    if( x == y ) r->ptr2 += 3 ;
    else r -= 5 ;
    /****   Multi line
         3개의 줄에 걸쳐진
       Another comments ****/

    return 0 ;

'''


print(" source의 길이 =", len( source) )

s_comment = r'//.*'    # // 로 시작하거나
             #/\*([^*]|[\r\n]|(\*([^/]|[\r\n])))*\*/
c_comment = r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/' #/* 안에 들어있는 모든 설명문
mypat     = s_comment+'|'+c_comment # r'//.*|/\*([^*]|[\r\n])*\*/'




itlist = re.finditer( mypat, source )

for no, mym in enumerate(itlist) :
    print(f"no.{no}:  span[{mym.span()[0]},{mym.span()[1]}]", end=": ")
    print( mym.group() )

