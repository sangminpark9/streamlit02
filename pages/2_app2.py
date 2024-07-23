import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
             'https://i.imgur.com/ECROFMC.png', 
             'https://i.imgur.com/MDKQoDc.jpg']

# 검색창 
# 입력창에서 데이터를 받아서 
# 해당 문자열이 일치하는 이미지를 화면에 출력해 보세요.
tmp = st.text_input('애니메이션을 입력하세요:')

for ani, img in zip(ani_list, img_list):
    if tmp in ani and tmp != '':
        st.image(img)
    