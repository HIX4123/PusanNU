
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc('font', family='NanumGothic')  # 한글 폰트 설정

plt.text(0.2, 0.5, "Winter", size=50, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5), # 글자색상
                   fc=(1., 0.8, 0.2), # 배경색상
                   )
         )

plt.text( 0.8, 0.5, "Summer", size=50, rotation=-30.,
         ha="right", va="top",
         bbox=dict(boxstyle="square",
                   ec=(1., 0.2, 0.8),
                   fc=(1., 0.8, 0.8),
                   )
         )


plt.draw()
plt.show()