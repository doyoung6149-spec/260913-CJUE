import streamlit as st

# 페이지 설정
st.set_page_config(page_title="자기소개", layout="wide")

# 제목
st.title("👋 자기소개")

# 개인 정보 섹션
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("기본 정보")
    st.write("**이름:서도영")
    st.write("**학교 : 청주교육대학교 실과교육과")
    st.write("**이메일:** doyoung6149@gmail.com")
    st.write("**전화:** 010-7642-6149")

with col2:
    st.subheader("자기소개")
    st.write("""
    안녕하세요! 저는 서도영이고, 청주교육대학교 실과교육과 학생입니다.
    
    - 2006년생이며 현재 1학년에 재학중입니다.
    - 저는 다양한 분야에 관심이 많으며, 특히 예체능 과목을 좋아합니다.

    """)

st.divider()

# 기술 스택 섹션
st.subheader("💻 기술 스택")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("**프로그래밍 언어**")
    st.write("- Python\n- JavaScript")

with col2:
    st.write("**프레임워크**")
    st.write("- Streamlit\n- React")

with col3:
    st.write("**기타**")
    st.write("- Git\n- SQL")

st.divider()

# 연락처 섹션
st.subheader("📞 연락처")
st.write("""
- **이메일:** doyoung6149@gmail.com
- **전화:** 010-7642-6149
- **GitHub:** [링크 추가]
- **LinkedIn:** [링크 추가]
""")
