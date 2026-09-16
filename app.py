import streamlit as st

st.set_page_config(page_title="Streamlit 배포 테스트", page_icon="🚀")

st.title("🚀 Streamlit 배포 테스트")
st.write("배포가 정상적으로 완료되었습니다!")

name = st.text_input("이름을 입력하세요", placeholder="홍길동")
if name:
    st.success(f"안녕하세요, {name}님!")

if st.button("클릭해보세요"):
    st.balloons()
