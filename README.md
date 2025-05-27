import streamlit as st

# MBTI 성격 설명 딕셔너리
soccer100_descriptions = {
    "INTJ": "전략적이고 분석적인 성격으로, 장기적인 계획을 세우고 문제 해결에 능숙합니다.",
    "INTP": "논리적이고 창의적인 사색가로, 새로운 아이디어를 탐구하는 것을 즐깁니다.",
    "ENTJ": "리더십이 강하고 목표 지향적인 성격으로, 효율적인 시스템을 구축하는 데 능합니다.",
    "ENTP": "호기심 많고 에너지 넘치는 토론가로, 새로운 도전을 즐깁니다.",
    "INFJ": "통찰력 있고 이상주의적인 조언자로, 깊은 관계와 의미 있는 대화를 선호합니다.",
    "INFP": "이상주의적이며 감성적인 성격으로, 자기 가치와 조화를 중요하게 생각합니다.",
    "ENFJ": "사교적이고 따뜻한 리더로, 타인의 성장을 도우려는 마음이 큽니다.",
    "ENFP": "열정적이고 창의적인 성격으로, 새로운 사람과 경험을 추구합니다.",
    "ISTJ": "책임감 있고 신뢰할 수 있는 관리자 유형으로, 체계적이고 성실합니다.",
    "ISFJ": "조용하고 따뜻하며 헌신적인 성격으로, 타인을 돌보는 데 능숙합니다.",
    "ESTJ": "실용적이고 단호한 리더로, 조직을 잘 운영합니다.",
    "ESFJ": "사교적이고 친절한 성격으로, 공동체 안에서의 조화를 중시합니다.",
    "ISTP": "논리적이고 독립적인 문제 해결사로, 즉각적인 행동에 능숙합니다.",
    "ISFP": "조용하고 예술적인 감성을 지닌 성격으로, 자신의 감정을 중시합니다.",
    "ESTP": "활동적이고 현실적인 유형으로, 모험을 즐기고 즉각적인 판단을 잘합니다.",
    "ESFP": "사교적이고 에너지 넘치는 성격으로, 즐거움과 사람을 사랑합니다."
}

# Streamlit 앱 UI
st.title("Soccer player information")
st.write("If you choose your favorite player, you can see your players' information")

# 드롭다운으로 MBTI 선택
selected_100 = st.selectbox("Choose your favorite player", list(soccer100_descriptions.keys()))

# 선택한 MBTI의 설명 출력
if selected_100:
    st.subheader(f"{selected_100} status team and achievements")
    st.write(soccer100_descriptions[selected_100])
