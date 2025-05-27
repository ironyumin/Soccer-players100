import streamlit as st

# 선수 데이터 (위에서 정의한 players_data 사용)
players_data = {
    "Lionel Messi": {
        "club": "Inter Miami (전: FC Barcelona, PSG)",
        "achievements": [
            "8회 Ballon d'Or 수상",
            "2022 FIFA 월드컵 우승 (아르헨티나)",
            "4회 챔피언스리그 우승",
            "10회 라리가 우승"
        ]
    },
    "Cristiano Ronaldo": {
        "club": "Al-Nassr (전: Man Utd, Real Madrid, Juventus)",
        "achievements": [
            "5회 Ballon d'Or 수상",
            "5회 챔피언스리그 우승",
            "유로 2016 우승 (포르투갈)",
            "라리가, EPL, 세리에 A 우승"
        ]
    },
    "Kylian Mbappé": {
        "club": "Paris Saint-Germain",
        "achievements": [
            "2018 FIFA 월드컵 우승 (프랑스)",
            "리그 1 우승 다수",
            "FIFA 월드컵 골든 부트 (2022)"
        ]
    },
    "Erling Haaland": {
        "club": "Manchester City",
        "achievements": [
            "2022–23 UEFA 챔피언스리그 우승",
            "2022–23 프리미어리그 득점왕",
            "골든 보이 수상 (2020)"
        ]
    },
    "Kevin De Bruyne": {
        "club": "Manchester City",
        "achievements": [
            "프리미어리그 우승 (다수)",
            "챔피언스리그 우승 (2022–23)",
            "PFA 올해의 선수 (2회)"
        ]
    }
}

# Streamlit 앱 시작
st.title("세계적인 축구 선수 정보 앱 ⚽")
st.write("선수를 선택하면, 소속팀과 업적이 표시됩니다.")

# 선수 선택 드롭다운
selected_player = st.selectbox("선수를 선택하세요:", list(players_data.keys()))

# 선택된 선수 정보 출력
if selected_player:
    info = players_data[selected_player]
    st.subheader(f"{selected_player}")
    st.markdown(f"**소속팀:** {info['club']}")
    st.markdown("**주요 업적:**")
    for achievement in info['achievements']:
        st.markdown(f"- {achievement}")

