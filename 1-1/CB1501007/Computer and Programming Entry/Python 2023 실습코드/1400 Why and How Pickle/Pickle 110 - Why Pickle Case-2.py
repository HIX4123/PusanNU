
# pickle.load(파일) 을 통해서 파일 내용을 읽어오려면,
# pickle.dump를 사용해서 데이터를 입력한 파일이어야한다.

import pickle
import string



with open('./data/Ourshop.bin', 'rb') as pick_file :
    shoplist = pickle.load( pick_file) #링거액, 링게루

    for (i,w) in enumerate(shoplist) :
        if "고기" in w :
            print(f"{i:4},  {w}")













