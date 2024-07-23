import streamlit as st

# 입력화면 - 버튼 생성
val1 = st.button("1고양이")
val2 = st.button("2고양이")
val3 = st.button("3고양이")

# 출력 - 선택된 버튼에 따라 다른 이미지 표시
if val1:
    st.image(r"./data/cat1.png", caption="1고양이")
    #st.write("1고양이 버튼이 눌렸습니다.")
elif val2:
    st.image(r"./data/cat2.png", caption="2고양이")
    #st.write("2고양이 버튼이 눌렸습니다.")
elif val3: 
    st.image(r"./data/cat3.png", caption="3고양이")
    #st.write("3고양이 버튼이 눌렸습니다.")
