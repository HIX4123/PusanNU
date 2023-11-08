#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-04
#-------------------------------------------------------------------------------

"""
class datetime.date
현재의 그레고리력이 언제나 적용되어왔고, 앞으로도 그럴 것이라는
가정하에 이상적인 날짜.
어트리뷰트: year, month 및 day.

class datetime.time
특정 날짜와 관계없이, 하루가 정확히 24*60*60초를 갖는다는 가정하에
이상적인 시간. (여기에는 《윤초》라는 개념이 없습니다.)
어트리뷰트: hour, minute, second, microsecond 및 tzinfo.

class datetime.datetime
날짜와 시간의 조합.
어트리뷰트: year, month, day, hour, minute, second, microsecond 및 tzinfo.

class datetime.timedelta
두 date, time 또는 datetime 인스턴스 간의 차이를 마이크로초 해상도로 나타내는 기간.

class datetime.tzinfo
시간대 정보 객체의 추상 베이스 클래스.
이것들은 datetime과 time 클래스에서 사용자 정의할 수 있는 시간 조정 개념(예를 들어, 시간대와/나 일광 절약 시간을 다루는 것)을 제공하기 위해 사용됩니다.

class datetime.timezone
tzinfo 추상 베이스 클래스를 구현하는 클래스로,
UTC로부터의 고정 오프셋을 나타냅니다.
"""
