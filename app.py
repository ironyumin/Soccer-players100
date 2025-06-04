import streamlit as st

# ✅ Expanded FW-only Database (5 major leagues)
players = [
    {"name": "Erling Haaland", "club": "Manchester City", "age": 24, "position": "FW", "league": "Premier League", "achievements": ["Champions League Winner 2023", "Premier League Golden Boot 2023"]},
    {"name": "Mohamed Salah", "club": "Liverpool", "age": 32, "position": "FW", "league": "Premier League", "achievements": ["Premier League Winner 2020", "Champions League Winner 2019"]},
    {"name": "Son Heung-min", "club": "Tottenham Hotspur", "age": 32, "position": "FW", "league": "Premier League", "achievements": ["Premier League Golden Boot 2021–22", "Puskás Award 2020"]},
    {"name": "Harry Kane", "club": "Bayern Munich", "age": 31, "position": "FW", "league": "Bundesliga", "achievements": ["England Captain", "Premier League Golden Boot (x3)"]},
    {"name": "Kylian Mbappé", "club": "Paris Saint-Germain", "age": 26, "position": "FW", "league": "Ligue 1", "achievements": ["World Cup Winner 2018", "Ligue 1 Top Scorer"]},
    {"name": "Vinícius Júnior", "club": "Real Madrid", "age": 24, "position": "FW", "league": "La Liga", "achievements": ["Champions League Winner 2022"]},
    {"name": "Robert Lewandowski", "club": "Barcelona", "age": 36, "position": "FW", "league": "La Liga", "achievements": ["FIFA Best Player 2020, 2021"]},
    {"name": "Lautaro Martínez", "club": "Inter Milan", "age": 27, "position": "FW", "league": "Serie A", "achievements": ["Serie A Champion", "World Cup Winner 2022"]},
    {"name": "Olivier Giroud", "club": "AC Milan", "age": 37, "position": "FW", "league": "Serie A", "achievements": ["World Cup Winner 2018"]},
    {"name": "Victor Osimhen", "club": "Napoli", "age": 26, "position": "FW", "league": "Serie A", "achievements": ["Serie A Top Scorer 2023"]},
    {"name": "Marcus Rashford", "club": "Manchester United", "age": 27, "position": "FW", "league": "Premier League", "achievements": ["FA Cup Winner 2016", "Europa League Winner 2017"]},
    {"name": "Rasmus Højlund", "club": "Manchester United", "age": 21, "position": "FW", "league": "Premier League", "achievements": ["Denmark International"]},
    {"name": "Bukayo Saka", "club": "Arsenal", "age": 23, "position": "FW", "league": "Premier League", "achievements": ["England Player of the Year 2023"]},
    {"name": "Gabriel Jesus", "club": "Arsenal", "age": 28, "position": "FW", "league": "Premier League", "achievements": ["Copa América Winner 2019"]},
    {"name": "Antoine Griezmann", "club": "Atlético Madrid", "age": 33, "position": "FW", "league": "La Liga", "achievements": ["World Cup Winner 2018"]},
    {"name": "Álvaro Morata", "club": "Atlético Madrid", "age": 32, "position": "FW", "league": "La Liga", "achievements": ["Champions League Runner-up"]},
    {"name": "João Félix", "club": "Barcelona", "age": 24, "position": "FW", "league": "La Liga", "achievements": ["Golden Boy 2019"]},
    {"name": "Folarin Balogun", "club": "Monaco", "age": 23, "position": "FW", "league": "Ligue 1", "achievements": ["USMNT Star"]},
    {"name": "Jonathan David", "club": "Lille", "age": 24, "position": "FW", "league": "Ligue 1", "achievements": ["Ligue 1 Winner 2021"]},
    {"name": "Wissam Ben Yedder", "club": "Monaco", "age": 34, "position": "FW", "league": "Ligue 1", "achievements": ["Ligue 1 Top Scorer"]},
    {"name": "Serhou Guirassy", "club": "Stuttgart", "age": 28, "position": "FW", "league": "Bundesliga", "achievements": ["Bundesliga Top Scorer Contender"]},
    {"name": "Jamal Musiala", "club": "Bayern Munich", "age": 22, "position": "FW", "league": "Bundesliga", "achievements": ["Bundesliga Champion"]},
    {"name": "Karim Adeyemi", "club": "Borussia Dortmund", "age": 23, "position": "FW", "league": "Bundesliga", "achievements": ["DFB Pokal Winner"]},
    {"name": "Florian Wirtz", "club": "Bayer Leverkusen", "age": 21, "position": "FW", "league": "Bundesliga", "achievements": ["Bundesliga Champion 2024"]},
    {"name": "Tammy Abraham", "club": "Roma", "age": 27, "position": "FW", "league": "Serie A", "achievements": ["UECL Winner"]},
    {"name": "Romelu Lukaku", "club": "Roma", "age": 32, "position": "FW", "league": "Serie A", "achievements": ["Belgium Top Scorer"]},
    {"name": "Christian Pulisic", "club": "AC Milan", "age": 26, "position": "FW", "league": "Serie A", "achievements": ["Champions League Winner 2021"]},
    {"name": "Luis Suárez", "club": "Inter Miami", "age": 37, "position": "FW", "league": "Other", "achievements": ["La Liga Golden Boot", "Copa América Winner"]},
    {"name": "Cristiano Ronaldo", "club": "Al-Nassr", "age": 39, "position": "FW", "league": "Other", "achievements": ["5x Ballon d'Or", "Champions League Winner (x5)"]},
    {"name": "Lionel Messi", "club": "Inter Miami", "age": 37, "position": "FW", "league": "Other", "achievements": ["8x Ballon d'Or", "World Cup Winner 2022"]},
    {"name": "Kevin De Bruyne", "club": "Manchester City", "age": 33, "position": "MF", "league": "Premier League", "achievements": ["Premier League Champion", "UCL Winner 2023"]},
    {"name": "Bruno Fernandes", "club": "Manchester United", "age": 30, "position": "MF", "league": "Premier League", "achievements": ["UEFA Nations League Winner"]},
    {"name": "Martin Ødegaard", "club": "Arsenal", "age": 26, "position": "MF", "league": "Premier League", "achievements": ["Arsenal Captain"]},
    {"name": "Declan Rice", "club": "Arsenal", "age": 26, "position": "MF", "league": "Premier League", "achievements": ["UECL Winner 2023"]},
    {"name": "James Maddison", "club": "Tottenham Hotspur", "age": 28, "position": "MF", "league": "Premier League", "achievements": ["England International"]},
    {"name": "Jude Bellingham", "club": "Real Madrid", "age": 21, "position": "MF", "league": "La Liga", "achievements": ["La Liga Champion", "Golden Boy 2023"]},
    {"name": "Toni Kroos", "club": "Real Madrid", "age": 35, "position": "MF", "league": "La Liga", "achievements": ["5x UCL Winner", "World Cup Winner 2014"]},
    {"name": "Luka Modrić", "club": "Real Madrid", "age": 39, "position": "MF", "league": "La Liga", "achievements": ["Ballon d'Or 2018"]},
    {"name": "Frenkie de Jong", "club": "Barcelona", "age": 27, "position": "MF", "league": "La Liga", "achievements": ["La Liga Champion"]},
    {"name": "Pedri", "club": "Barcelona", "age": 22, "position": "MF", "league": "La Liga", "achievements": ["Golden Boy 2021"]},
    {"name": "Jamal Musiala", "club": "Bayern Munich", "age": 22, "position": "MF", "league": "Bundesliga", "achievements": ["Bundesliga Champion"]},
    {"name": "Joshua Kimmich", "club": "Bayern Munich", "age": 30, "position": "MF", "league": "Bundesliga", "achievements": ["UCL Winner 2020"]},
    {"name": "Florian Wirtz", "club": "Bayer Leverkusen", "age": 21, "position": "MF", "league": "Bundesliga", "achievements": ["Bundesliga Champion 2024"]},
    {"name": "Hakan Çalhanoğlu", "club": "Inter Milan", "age": 30, "position": "MF", "league": "Serie A", "achievements": ["Serie A Champion"]},
    {"name": "Nicolò Barella", "club": "Inter Milan", "age": 28, "position": "MF", "league": "Serie A", "achievements": ["EURO 2020 Winner"]},
    {"name": "Adrien Rabiot", "club": "Juventus", "age": 30, "position": "MF", "league": "Serie A", "achievements": ["Ligue 1 Winner", "Serie A Champion"]},
    {"name": "Warren Zaïre-Emery", "club": "Paris Saint-Germain", "age": 19, "position": "MF", "league": "Ligue 1", "achievements": ["Ligue 1 Champion"]},
    {"name": "Marco Verratti", "club": "Al-Arabi", "age": 32, "position": "MF", "league": "Other", "achievements": ["EURO 2020 Winner"]},
    {"name": "Lee Kang-in", "club": "Paris Saint-Germain", "age": 23, "position": "MF", "league": "Ligue 1", "achievements": ["Asian Games Gold Medalist"]},
    {"name": "Paik Seung-ho", "club": "Jeonbuk Hyundai", "age": 28, "position": "MF", "league": "Other", "achievements": ["K League Best XI"]},
    {"name": "Virgil van Dijk", "club": "Liverpool", "age": 33, "position": "DF", "league": "Premier League", "achievements": ["Champions League Winner 2019"]},
    {"name": "William Saliba", "club": "Arsenal", "age": 24, "position": "DF", "league": "Premier League", "achievements": ["Arsenal Young Player of the Season"]},
    {"name": "Cristian Romero", "club": "Tottenham Hotspur", "age": 27, "position": "DF", "league": "Premier League", "achievements": ["World Cup Winner 2022"]},
    {"name": "John Stones", "club": "Manchester City", "age": 30, "position": "DF", "league": "Premier League", "achievements": ["Premier League Champion"]},
    {"name": "Antonio Rüdiger", "club": "Real Madrid", "age": 32, "position": "DF", "league": "La Liga", "achievements": ["Champions League Winner 2021"]},
    {"name": "Éder Militão", "club": "Real Madrid", "age": 27, "position": "DF", "league": "La Liga", "achievements": ["La Liga Champion"]},
    {"name": "Ronald Araújo", "club": "Barcelona", "age": 26, "position": "DF", "league": "La Liga", "achievements": ["La Liga Champion"]},
    {"name": "Jules Koundé", "club": "Barcelona", "age": 26, "position": "DF", "league": "La Liga", "achievements": ["UEFA Nations League Winner"]},
    {"name": "Matthijs de Ligt", "club": "Bayern Munich", "age": 25, "position": "DF", "league": "Bundesliga", "achievements": ["Serie A Champion"]},
    {"name": "Alphonso Davies", "club": "Bayern Munich", "age": 24, "position": "DF", "league": "Bundesliga", "achievements": ["UCL Winner 2020"]},
    {"name": "Jonathan Tah", "club": "Bayer Leverkusen", "age": 28, "position": "DF", "league": "Bundesliga", "achievements": ["Bundesliga Champion 2024"]},
    {"name": "Kim Min-jae", "club": "Bayern Munich", "age": 28, "position": "DF", "league": "Bundesliga", "achievements": ["Serie A Defender of the Year 2023"]},
    {"name": "Federico Dimarco", "club": "Inter Milan", "age": 27, "position": "DF", "league": "Serie A", "achievements": ["Serie A Champion"]},
    {"name": "Alessandro Bastoni", "club": "Inter Milan", "age": 26, "position": "DF", "league": "Serie A", "achievements": ["EURO 2020 Winner"]},
    {"name": "Bremer", "club": "Juventus", "age": 28, "position": "DF", "league": "Serie A", "achievements": ["Serie A Best Defender"]},
    {"name": "Achraf Hakimi", "club": "Paris Saint-Germain", "age": 26, "position": "DF", "league": "Ligue 1", "achievements": ["Ligue 1 Champion"]},
    {"name": "Marquinhos", "club": "Paris Saint-Germain", "age": 30, "position": "DF", "league": "Ligue 1", "achievements": ["Multiple Ligue 1 Titles"]},
    {"name": "Lucas Hernández", "club": "Paris Saint-Germain", "age": 29, "position": "DF", "league": "Ligue 1", "achievements": ["World Cup Winner 2018"]},
    {"name": "Lee Ki-je", "club": "Suwon Samsung Bluewings", "age": 33, "position": "DF", "league": "Other", "achievements": ["K League Best XI"]},
    {"name": "Seol Young-woo", "club": "Ulsan HD FC", "age": 26, "position": "DF", "league": "Other", "achievements": ["Asian Games Gold Medalist"]},
    {"name": "Alisson Becker", "club": "Liverpool", "age": 31, "position": "GK", "league": "Premier League", "achievements": ["UEFA Champions League Winner 2019", "Premier League Winner 2020"]},
    {"name": "Ederson Moraes", "club": "Manchester City", "age": 30, "position": "GK", "league": "Premier League", "achievements": ["Premier League Winner", "EFL Cup Winner"]},
    {"name": "Hugo Lloris", "club": "Tottenham Hotspur", "age": 37, "position": "GK", "league": "Premier League", "achievements": ["World Cup Winner 2018"]},
    {"name": "David De Gea", "club": "Manchester United", "age": 33, "position": "GK", "league": "Premier League", "achievements": ["Multiple Player of the Year Awards"]},
    {"name": "Thibaut Courtois", "club": "Real Madrid", "age": 31, "position": "GK", "league": "La Liga", "achievements": ["UEFA Champions League Winner 2022", "La Liga Winner"]},
    {"name": "Marc-André ter Stegen", "club": "Barcelona", "age": 31, "position": "GK", "league": "La Liga", "achievements": ["Multiple Copa del Rey Titles"]},
    {"name": "Jan Oblak", "club": "Atlético Madrid", "age": 31, "position": "GK", "league": "La Liga", "achievements": ["La Liga Best Goalkeeper Multiple Years"]},
    {"name": "Manuel Neuer", "club": "Bayern Munich", "age": 37, "position": "GK", "league": "Bundesliga", "achievements": ["Multiple Bundesliga Titles", "World Cup Winner 2014"]},
    {"name": "Gregor Kobel", "club": "Borussia Dortmund", "age": 26, "position": "GK", "league": "Bundesliga", "achievements": ["Bundesliga Top Saves"]},
    {"name": "Mike Maignan", "club": "AC Milan", "age": 28, "position": "GK", "league": "Serie A", "achievements": ["Serie A Winner 2022"]},
    {"name": "Wojciech Szczęsny", "club": "Juventus", "age": 33, "position": "GK", "league": "Serie A", "achievements": ["Serie A Titles"]},
    {"name": "Gianluigi Donnarumma", "club": "Paris Saint-Germain", "age": 25, "position": "GK", "league": "Ligue 1", "achievements": ["EURO 2020 Winner", "Ligue 1 Title"]},
    {"name": "Keylor Navas", "club": "Paris Saint-Germain", "age": 36, "position": "GK", "league": "Ligue 1", "achievements": ["Multiple UCL Titles"]},
    {"name": "Lee Seung-woo", "club": "Ulsan Hyundai", "age": 27, "position": "GK", "league": "Other", "achievements": ["K League Best XI"]},
    {"name": "Jo Hyeon-woo", "club": "Ulsan Hyundai", "age": 30, "position": "GK", "league": "Other", "achievements": ["2022 FIFA World Cup Star"]},
    {"name": "Samir Handanović", "club": "Inter Milan", "age": 40, "position": "GK", "league": "Serie A", "achievements": ["Serie A Title", "UEFA Champions League Finalist"]},
    {"name": "Rui Patrício", "club": "Roma", "age": 35, "position": "GK", "league": "Serie A", "achievements": ["UEFA Europa League Winner"]},
    {"name": "Salvatore Sirigu", "club": "Napoli", "age": 36, "position": "GK", "league": "Serie A", "achievements": ["Serie A Champion"]},
    {"name": "Mike Maignan", "club": "AC Milan", "age": 28, "position": "GK", "league": "Serie A", "achievements": ["Serie A Champion 2022"]},
    {"name": "Lukáš Hrádecký", "club": "Bayer Leverkusen", "age": 34, "position": "GK", "league": "Bundesliga", "achievements": ["Bundesliga Team of the Season"]},
    {"name": "André Onana", "club": "Bayern Munich", "age": 27, "position": "GK", "league": "Bundesliga", "achievements": ["CAF Player of the Year Nominee"]},
    {"name": "Kevin Trapp", "club": "Eintracht Frankfurt", "age": 33, "position": "GK", "league": "Bundesliga", "achievements": ["Europa League Winner"]},
    {"name": "Alexander Schwolow", "club": "SC Freiburg", "age": 31, "position": "GK", "league": "Bundesliga", "achievements": ["Bundesliga Consistent Starter"]},
    {"name": "Frederik Rønnow", "club": "Union Berlin", "age": 31, "position": "GK", "league": "Bundesliga", "achievements": ["Bundesliga Starter"]},
    {"name": "Robin Olsen", "club": "Lazio", "age": 34, "position": "GK", "league": "Serie A", "achievements": ["Consistent Serie A Starter"]},
    {"name": "Benjamin Lecomte", "club": "Atlético Madrid", "age": 33, "position": "GK", "league": "La Liga", "achievements": ["Consistent La Liga Starter"]},
    {"name": "Yassine Bounou (Bono)", "club": "Sevilla", "age": 32, "position": "GK", "league": "La Liga", "achievements": ["Europa League Winner"]},
    {"name": "Álex Remiro", "club": "Real Sociedad", "age": 29, "position": "GK", "league": "La Liga", "achievements": ["Strong La Liga Starter"]},
    {"name": "David Raya", "club": "Brentford", "age": 28, "position": "GK", "league": "Premier League", "achievements": ["Premier League Starter"]},
    {"name": "Aaron Ramsdale", "club": "Arsenal", "age": 25, "position": "GK", "league": "Premier League", "achievements": ["England International"]},
    {"name": "Nick Pope", "club": "Newcastle United", "age": 31, "position": "GK", "league": "Premier League", "achievements": ["England International"]},
    {"name": "Kasper Schmeichel", "club": "Nice", "age": 36, "position": "GK", "league": "Ligue 1", "achievements": ["Premier League Winner"]},
    {"name": "Walter Benítez", "club": "Nice", "age": 28, "position": "GK", "league": "Ligue 1", "achievements": ["Ligue 1 Starter"]},
    {"name": "Jo Hyeon-woo", "club": "Ulsan Hyundai", "age": 30, "position": "GK", "league": "Other", "achievements": ["2022 FIFA World Cup Star"]},
    {"name": "Lee Bum-young", "club": "Gangwon FC", "age": 34, "position": "GK", "league": "Other", "achievements": ["K League Veteran"]}
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
custom_order = ["Premier League", "La Liga", "Bundesliga", "Serie A", "Ligue 1", "Saudi Pro League", "MLS", "Other"]
available_leagues = sorted(set(p["league"] for p in players), key=lambda x: custom_order.index(x) if x in custom_order else 999)
leagues = available_leagues
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
