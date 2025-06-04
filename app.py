import streamlit as st

# ✅ Expanded Database with Korean, EPL, and Spurs Players
players = [
    {"name": "Erling Haaland", "club": "Manchester City", "age": 24, "position": "FW", "league": "Premier League", "achievements": ["Champions League Winner 2023", "Premier League Golden Boot 2023"]},
    {"name": "Kevin De Bruyne", "club": "Manchester City", "age": 33, "position": "MF", "league": "Premier League", "achievements": ["Champions League Winner 2023", "Premier League Champion (x5)"]},
    {"name": "Mohamed Salah", "club": "Liverpool", "age": 32, "position": "FW", "league": "Premier League", "achievements": ["Premier League Winner 2020", "Champions League Winner 2019"]},
    {"name": "Son Heung-min", "club": "Tottenham Hotspur", "age": 32, "position": "FW", "league": "Premier League", "achievements": ["Premier League Golden Boot 2021–22", "Puskás Award 2020"]},
    {"name": "James Maddison", "club": "Tottenham Hotspur", "age": 28, "position": "MF", "league": "Premier League", "achievements": ["EFL Cup Runner-up 2021"]},
    {"name": "Cristian Romero", "club": "Tottenham Hotspur", "age": 27, "position": "DF", "league": "Premier League", "achievements": ["World Cup Winner 2022"]},
    {"name": "Guglielmo Vicario", "club": "Tottenham Hotspur", "age": 28, "position": "GK", "league": "Premier League", "achievements": ["Serie A Best Goalkeeper Nominee"]},
    {"name": "Kim Min-jae", "club": "Bayern Munich", "age": 28, "position": "DF", "league": "Bundesliga", "achievements": ["Serie A Champion 2022–23", "Bundesliga Champion 2023–24"]},
    {"name": "Lee Kang-in", "club": "Paris Saint-Germain", "age": 23, "position": "MF", "league": "Ligue 1", "achievements": ["Asian Games Gold Medal 2023"]},
    {"name": "Jude Bellingham", "club": "Real Madrid", "age": 21, "position": "MF", "league": "La Liga", "achievements": ["La Liga Player of the Season 2024", "Champions League Finalist 2024"]},
    {"name": "Vinícius Júnior", "club": "Real Madrid", "age": 24, "position": "FW", "league": "La Liga", "achievements": ["Champions League Winner 2022", "La Liga Winner 2022, 2024"]},
    {"name": "Harry Kane", "club": "Bayern Munich", "age": 31, "position": "FW", "league": "Bundesliga", "achievements": ["Premier League Golden Boot (x3)", "World Cup Golden Boot 2018"]},
    {"name": "Jamal Musiala", "club": "Bayern Munich", "age": 21, "position": "MF", "league": "Bundesliga", "achievements": ["Bundesliga Champion", "Golden Boy Finalist"]},
    {"name": "Manuel Neuer", "club": "Bayern Munich", "age": 38, "position": "GK", "league": "Bundesliga", "achievements": ["World Cup Winner 2014", "Champions League Winner (x2)"]},
    {"name": "Kylian Mbappé", "club": "PSG", "age": 26, "position": "FW", "league": "Ligue 1", "achievements": ["World Cup Winner 2018", "Ligue 1 Top Scorer (x5)"]},
    {"name": "Gianluigi Donnarumma", "club": "PSG", "age": 25, "position": "GK", "league": "Ligue 1", "achievements": ["Euro 2020 MVP", "Ligue 1 Champion"]},
    {"name": "Rafael Leão", "club": "AC Milan", "age": 25, "position": "FW", "league": "Serie A", "achievements": ["Serie A MVP 2022"]},
    {"name": "Nicolo Barella", "club": "Inter Milan", "age": 28, "position": "MF", "league": "Serie A", "achievements": ["Euro 2020 Winner", "Serie A Champion 2021"]},
    {"name": "Victor Osimhen", "club": "Napoli", "age": 26, "position": "FW", "league": "Serie A", "achievements": ["Serie A Top Scorer 2022–23", "Serie A Champion"]},
    {"name": "Paulo Dybala", "club": "AS Roma", "age": 31, "position": "FW", "league": "Serie A", "achievements": ["Serie A Champion", "World Cup Winner 2022"]},
]

# Age group function
def get_age_group(age):
    if age <= 20:
        return "20 and under"
    elif age < 30:
        return "21–29"
    elif age < 35:
        return "30–34"
    else:
        return "35 and over"

# UI
st.set_page_config("Football Player Explorer", layout="centered")
st.title("⚽ Explore Famous Active Footballers")

# Filters
leagues = sorted(set(p["league"] for p in players))
league = st.selectbox("🌍 Choose a League", leagues)

age_groups = ["20 and under", "21–29", "30–34", "35 and over"]
age_group = st.selectbox("🎂 Choose Age Group", age_groups)

positions = ["GK", "DF", "MF", "FW"]
position = st.selectbox("📌 Choose Position", positions)

# Filter logic
def filter_players():
    return [
        p for p in players
        if p["league"] == league
        and get_age_group(p["age"]) == age_group
        and p["position"] == position
    ]

results = filter_players()

if results:
    player_names = [p["name"] for p in results]
    selected_name = st.selectbox("🎯 Choose a Player", player_names)
    player = next(p for p in results if p["name"] == selected_name)

    st.subheader(f"👤 {player['name']}")
    st.markdown(f"**Club:** {player['club']}")
    st.markdown(f"**Age:** {player['age']} ({get_age_group(player['age'])})")
    st.markdown(f"**Position:** {player['position']}")
    st.markdown(f"**League:** {player['league']}")
    st.markdown("🏆 **Achievements:**")
    for ach in player["achievements"]:
        st.markdown(f"- {ach}")
else:
    st.warning("No players match your filter. Try different options.")
