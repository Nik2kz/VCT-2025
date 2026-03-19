import streamlit as st
import pandas as pd

st.set_page_config(page_title="VCT 2025 Analytics", layout="wide", page_icon="🎯")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;700&family=Inter:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #ffffff;
    color: #111111;
}

h1, h2, h3 {
    font-family: 'Rajdhani', sans-serif;
    color: #FF4655;
    letter-spacing: 2px;
    text-transform: uppercase;
}

section[data-testid="stSidebar"] {
    background: #FF4655;
    border-right: none;
}

.sidebar-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 32px;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 4px;
    text-transform: uppercase;
    line-height: 1;
}

.vct-badge {
    background: #ffffff;
    color: #FF4655;
    font-family: 'Rajdhani', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    padding: 4px 10px;
    border-radius: 2px;
    display: inline-block;
    margin: 8px 0 4px 0;
    text-transform: uppercase;
}

.sidebar-meta {
    color: rgba(255,255,255,0.7);
    font-size: 11px;
    margin-bottom: 20px;
    letter-spacing: 1px;
}

div[data-testid="stSidebar"] .stRadio label {
    font-size: 15px !important;
    font-family: 'Rajdhani', sans-serif !important;
    letter-spacing: 2px !important;
    color: #ffffff !important;
    padding: 6px 0 !important;
    text-transform: uppercase;
}

div[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.3) !important;
}

.page-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 48px;
    font-weight: 700;
    color: #111111;
    text-transform: uppercase;
    letter-spacing: 4px;
    border-bottom: 3px solid #FF4655;
    padding-bottom: 10px;
    margin-bottom: 20px;
}

.page-title span {
    color: #FF4655;
}

.metric-card {
    background: #FF4655;
    border: none;
    border-radius: 4px;
    padding: 20px;
    text-align: center;
}

.metric-label {
    color: rgba(255,255,255,0.8);
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-family: 'Inter', sans-serif;
    margin-bottom: 8px;
}

.metric-value {
    color: #ffffff;
    font-size: 32px;
    font-weight: 700;
    font-family: 'Rajdhani', sans-serif;
    line-height: 1;
}

.section-header {
    font-family: 'Rajdhani', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: #FF4655;
    text-transform: uppercase;
    letter-spacing: 3px;
    border-left: 4px solid #FF4655;
    padding-left: 12px;
    margin: 30px 0 15px 0;
}

.map-banner img {
    height: 220px !important;
    width: 100% !important;
    object-fit: cover !important;
    object-position: center !important;
    border-radius: 6px !important;
    border: 2px solid #FF4655 !important;
}

.icon-small img {
    height: 60px !important;
    width: 60px !important;
    object-fit: cover !important;
    object-position: center top !important;
    border-radius: 4px !important;
    border: 1px solid #dddddd !important;
}

.tournament-card {
    background: #ffffff;
    border: none;
    border-left: 6px solid #FF4655;
    border-radius: 4px;
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.tournament-name {
    font-family: 'Rajdhani', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: #111111;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.tournament-winner {
    font-family: 'Rajdhani', sans-serif;
    font-size: 28px;
    font-weight: 700;
    color: #FF4655;
    margin: 4px 0;
}

.tournament-meta {
    color: #888888;
    font-size: 12px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

div[data-testid="stDataFrame"] {
    border: 1px solid #eeeeee;
    border-radius: 4px;
}

.stSelectbox label {
    color: #FF4655 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 13px !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
}

div[data-baseweb="select"] {
    border: 1px solid #FF4655 !important;
    border-radius: 4px !important;
}

.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
    max-width: 1400px;
    background-color: #ffffff;
}

.footer-credit {
    color: rgba(255,255,255,0.5);
    font-size: 10px;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-top: 10px;
}

hr {
    border-color: #eeeeee !important;
    margin: 20px 0 !important;
}

.stApp {
    background-color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

AGENT_IMAGES = {
    "Jett": "images/agents/Jett.png",
    "Reyna": "images/agents/Reyna.png",
    "Raze": "images/agents/Raze.png",
    "Phoenix": "images/agents/Phoenix.png",
    "Neon": "images/agents/Neon.png",
    "Yoru": "images/agents/Yoru.png",
    "Iso": "images/agents/Iso.png",
    "Sage": "images/agents/Sage.png",
    "Skye": "images/agents/Skye.png",
    "Sova": "images/agents/Sova.png",
    "Breach": "images/agents/Breach.png",
    "Fade": "images/agents/Fade.png",
    "Gekko": "images/agents/Gekko.png",
    "Tejo": "images/agents/Tejo.png",
    "Brimstone": "images/agents/Brimstone.png",
    "Omen": "images/agents/Omen.png",
    "Viper": "images/agents/Viper.png",
    "Astra": "images/agents/Astra.png",
    "Harbor": "images/agents/Harbor.png",
    "Clove": "images/agents/Clove.png",
    "Cypher": "images/agents/Cypher.png",
    "Killjoy": "images/agents/Killjoy.png",
    "Chamber": "images/agents/Chamber.png",
    "Deadlock": "images/agents/Deadlock.png",
    "Vyse": "images/agents/Vyse.png",
    "Kay/O": "images/agents/KayO.png",
}

MAP_IMAGES = {
    "Ascent": "images/maps/Ascent.png",
    "Bind": "images/maps/Bind.png",
    "Haven": "images/maps/Haven.png",
    "Split": "images/maps/Split.png",
    "Fracture": "images/maps/Fracture.png",
    "Icebox": "images/maps/Icebox.png",
    "Lotus": "images/maps/Lotus.png",
    "Pearl": "images/maps/Pearl.png",
    "Sunset": "images/maps/Sunset.png",
    "Abyss": "images/maps/Abyss.png",
    "Corrode": "images/maps/Corrode.png",
}

TEAM_LOGOS = {
    "NRG": "images/teams/NRG.png",
    "FNATIC": "images/teams/FNATIC.png",
    "Paper Rex": "images/teams/Paper_Rex.png",
    "G2 Esports": "images/teams/G2_Esports.png",
    "DRX": "images/teams/DRX.png",
    "Team Heretics": "images/teams/Team_Heretics.png",
    "MIBR": "images/teams/MIBR.png",
    "GIANTX": "images/teams/GIANTX.png",
    "Sentinels": "images/teams/Sentinels.png",
    "100 Thieves": "images/teams/100_Thieves.png",
    "Team Liquid": "images/teams/Team_Liquid.png",
    "Cloud9": "images/teams/Cloud9.png",
    "Evil Geniuses": "images/teams/Evil_Geniuses.png",
    "Gen.G": "images/teams/Gen.G.png",
    "EDward Gaming": "images/teams/EDward_Gaming.png",
    "Karmine Corp": "images/teams/Karmine_Corp.png",
    "BBL Esports": "images/teams/BBL_Esports.png",
    "KRÜ Esports": "images/teams/KRÜ_Esports.png",
    "LOUD": "images/teams/LOUD.png",
    "Leviatán": "images/teams/Leviatán.png",
    "FUT Esports": "images/teams/FUT_Esports.png",
}

TOURNAMENTS = [
    {
        "name": "Valorant Champions 2025",
        "date": "Sep 12 – Oct 5, 2025",
        "region": "International",
        "prize": "$2,250,000",
        "winner": "NRG",
        "runner_up": "FNATIC",
        "logo": "images/tournaments/Valorant_Champions_2025.png",
    },
    {
        "name": "Valorant Masters Toronto 2025",
        "date": "Jun 6 – Jun 22, 2025",
        "region": "International",
        "prize": "$500,000",
        "winner": "Paper Rex",
        "runner_up": "FNATIC",
        "logo": "images/tournaments/Valorant_Masters_Toronto_2025.png",
    },
    {
        "name": "Valorant Masters Bangkok 2025",
        "date": "Feb 13 – Mar 2, 2025",
        "region": "International",
        "prize": "$500,000",
        "winner": "FNATIC",
        "runner_up": "Gen.G",
        "logo": "images/tournaments/Valorant_Masters_Bangkok_2025.png",
    },
    {
        "name": "VCT 2025 Americas Stage 2",
        "date": "Jul – Aug 2025",
        "region": "Americas",
        "prize": "$200,000",
        "winner": "G2 Esports",
        "runner_up": "NRG",
        "logo": "images/tournaments/VCT_2025_Americas_Stage_2.png",
    },
    {
        "name": "VCT 2025 Americas Stage 1",
        "date": "Feb – Mar 2025",
        "region": "Americas",
        "prize": "$200,000",
        "winner": "NRG",
        "runner_up": "Sentinels",
        "logo": "images/tournaments/VCT_2025_Americas_Stage_1.png",
    },
    {
        "name": "VCT 2025 EMEA Stage 2",
        "date": "Jul – Aug 2025",
        "region": "EMEA",
        "prize": "$200,000",
        "winner": "FNATIC",
        "runner_up": "Team Heretics",
        "logo": "images/tournaments/VCT_2025_EMEA_Stage_2.png",
    },
    {
        "name": "VCT 2025 EMEA Stage 1",
        "date": "Feb – Mar 2025",
        "region": "EMEA",
        "prize": "$200,000",
        "winner": "Karmine Corp",
        "runner_up": "FNATIC",
        "logo": "images/tournaments/VCT_2025_EMEA_Stage_1.png",
    },
    {
        "name": "VCT 2025 Pacific Stage 2",
        "date": "Jul – Aug 2025",
        "region": "Pacific",
        "prize": "$200,000",
        "winner": "Paper Rex",
        "runner_up": "Rex Regum Qeon",
        "logo": "images/tournaments/VCT_2025_Pacific_Stage_2.png",
    },
    {
        "name": "VCT 2025 Pacific Stage 1",
        "date": "Feb – Mar 2025",
        "region": "Pacific",
        "prize": "$200,000",
        "winner": "Paper Rex",
        "runner_up": "DRX",
        "logo": "images/tournaments/VCT_2025_Pacific_Stage_1.png",
    },
    {
        "name": "VCT 2025 China Stage 2",
        "date": "Jul – Aug 2025",
        "region": "China",
        "prize": "$200,000",
        "winner": "EDward Gaming",
        "runner_up": "Bilibili Gaming",
        "logo": "images/tournaments/VCT_2025_China_Stage_2.png",
    },
    {
        "name": "VCT 2025 China Stage 1",
        "date": "Feb – Mar 2025",
        "region": "China",
        "prize": "$200,000",
        "winner": "EDward Gaming",
        "runner_up": "Bilibili Gaming",
        "logo": "images/tournaments/VCT_2025_China_Stage_1.png",
    },
]

def metric_card(label, value):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)

def section_header(title):
    st.markdown(f'<div class="section-header">{title}</div>', unsafe_allow_html=True)

def styled_df(df):
    df = df.copy()
    df.columns = [c.upper().replace("_", " ") for c in df.columns]
    st.dataframe(df, use_container_width=True, hide_index=False)

def show_icon(path, width=60):
    try:
        st.markdown('<div class="icon-small">', unsafe_allow_html=True)
        st.image(path, width=width)
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        pass

@st.cache_data
def load_data():
    match_df = pd.read_csv("vlr_match_data_clean.csv")
    player_df = pd.read_csv("vlr_clean_stats.csv")
    return match_df, player_df

match_df, player_df = load_data()
match_df["team"] = match_df["team"].str.replace("VISA KRÜ", "KRÜ Esports")
match_df["team"] = match_df["team"].str.replace("^KRÜ$", "KRÜ Esports", regex=True)
if "Team" in player_df.columns:
    player_df["Team"] = player_df["Team"].str.replace("VISA KRÜ", "KRÜ Esports")

with st.sidebar:
    st.markdown('<div class="sidebar-title">VCT<br/>2025</div>', unsafe_allow_html=True)
    st.markdown('<div class="vct-badge">● Live Analytics</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-meta">Playoff Data · 11 Events · 3510 Maps</div>', unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio(
        "Navigation",
        ["🏠  Home", "🗺️  Maps", "🧬  Agents", "🏆  Teams", "👤  Players"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.markdown('<div class="footer-credit">Data sourced from vlr.gg</div>', unsafe_allow_html=True)

# ── HOME PAGE ─────────────────────────────────────────────────────────────
if page == "🏠  Home":
    st.markdown('<div class="page-title">VCT 2025 <span>Season Results</span></div>', unsafe_allow_html=True)
    st.markdown('<div style="color:#555;font-size:13px;letter-spacing:1px;margin-bottom:30px;">Complete tournament results across all VCT 2025 events</div>', unsafe_allow_html=True)

    region_filter = st.selectbox(
        "Filter by Region",
        ["All Regions", "International", "Americas", "EMEA", "Pacific", "China"]
    )

    filtered_tournaments = TOURNAMENTS if region_filter == "All Regions" else [
        t for t in TOURNAMENTS if t["region"] == region_filter
    ]

    for t in filtered_tournaments:
        col1, col2, col3 = st.columns([1, 4, 2])

        with col1:
            st.markdown('<div style="display:flex;align-items:center;justify-content:center;height:100%;padding-top:20px;">', unsafe_allow_html=True)
            try:
                st.image(t["logo"], width=70)
            except:
                pass
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            region_color = {
                "International": "#FF4655",
                "Americas": "#4488FF",
                "EMEA": "#44CCAA",
                "Pacific": "#FFAA44",
                "China": "#FF6644"
            }.get(t["region"], "#888")

            st.markdown(f"""
            <div class="tournament-card">
                <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px;">
                    <span style="background:{region_color};color:#fff;font-size:10px;font-family:Rajdhani,sans-serif;font-weight:700;letter-spacing:2px;padding:2px 8px;border-radius:2px;">{t["region"].upper()}</span>
                    <span class="tournament-meta">{t["date"]}</span>
                </div>
                <div class="tournament-name">{t["name"]}</div>
                <div class="tournament-winner">🏆 {t["winner"]}</div>
                <div class="tournament-meta">Runner-up: {t["runner_up"]}</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            logo_path = TEAM_LOGOS.get(t["winner"], "")
            if logo_path:
                try:
                    st.markdown('<div style="background:#f5f5f5;border-radius:6px;padding:8px;display:inline-block;margin-bottom:8px;">', unsafe_allow_html=True)
                    st.image(logo_path, width=80)
                    st.markdown('</div>', unsafe_allow_html=True)
                except:
                    pass
            st.markdown(f'''
            <div style="background:#FF4655;border-radius:4px;padding:12px 16px;margin-top:8px;">
                <div style="color:#ffffff;font-family:Rajdhani,sans-serif;font-size:22px;font-weight:700;letter-spacing:1px;">{t["prize"]}</div>
                <div style="color:rgba(255,255,255,0.7);font-size:11px;letter-spacing:2px;text-transform:uppercase;">Prize Pool</div>
            </div>
            ''', unsafe_allow_html=True)

# ── MAP PAGE ──────────────────────────────────────────────────────────────
elif page == "🗺️  Maps":
    st.markdown('<div class="page-title">Map <span>Intelligence</span></div>', unsafe_allow_html=True)

    selected_map = st.selectbox("Select a Map", sorted(match_df["map"].unique()))
    map_df = match_df[match_df["map"] == selected_map]

    if selected_map in MAP_IMAGES:
        st.markdown('<div class="map-banner">', unsafe_allow_html=True)
        st.image(MAP_IMAGES[selected_map], use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    total_games = map_df["match_url"].nunique()
    avg_acs = round(map_df["ACS"].mean(), 1)
    top_agent = map_df.groupby("agent")["win"].mean().idxmax()

    col1, col2, col3 = st.columns(3)
    with col1:
        metric_card("Maps Played", total_games)
    with col2:
        metric_card("Avg ACS", avg_acs)
    with col3:
        metric_card("Best Agent by Win Rate", top_agent)

    st.markdown("---")
    section_header("Agent Meta")

    agent_stats = map_df.groupby("agent").agg(
        picks=("agent", "count"),
        wins=("win", "sum")
    ).reset_index()
    agent_stats["pick_rate"] = (agent_stats["picks"] / agent_stats["picks"].sum() * 100).round(1)
    agent_stats["win_rate"] = (agent_stats["wins"] / agent_stats["picks"] * 100).round(1)
    agent_stats = agent_stats.sort_values("pick_rate", ascending=False)

    cols = st.columns(5)
    for i, row in agent_stats.head(10).iterrows():
        with cols[i % 5]:
            show_icon(AGENT_IMAGES.get(row["agent"], ""))
            st.markdown(f'<div style="color:#111;font-family:Rajdhani,sans-serif;font-size:14px;font-weight:700;">{row["agent"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="color:#555;font-size:12px;">Pick <span style="color:#FF4655;font-weight:700;">{row["pick_rate"]}%</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div style="color:#555;font-size:12px;">Win <span style="color:#FF4655;font-weight:700;">{row["win_rate"]}%</span></div>', unsafe_allow_html=True)
            st.markdown("<br/>", unsafe_allow_html=True)

    st.markdown("---")
    section_header("Best Agent Combinations (Winning Comps)")
    winning_comps = map_df[map_df["win"] == 1].groupby("match_url")["agent"].apply(list).reset_index()
    winning_comps["comp"] = winning_comps["agent"].apply(lambda x: " · ".join(sorted(x[:5])))
    top_comps = winning_comps["comp"].value_counts().head(5).reset_index()
    top_comps.columns = ["Agent Combination", "Times Won"]
    styled_df(top_comps)

    st.markdown("---")
    section_header("Best Players on this Map")
    top_players = map_df.groupby("player").agg(
        maps_played=("ACS", "count"),
        avg_acs=("ACS", "mean"),
        team=("team", "first")
    ).reset_index()
    top_players = top_players[top_players["maps_played"] >= 2].sort_values("avg_acs", ascending=False).head(10)
    top_players["avg_acs"] = top_players["avg_acs"].round(1)
    styled_df(top_players[["player", "team", "maps_played", "avg_acs"]])

    st.markdown("---")
    section_header("Best Teams on this Map")

    team_wins = map_df[map_df["win"] == 1].groupby("team")["match_url"].nunique().reset_index()
    team_wins.columns = ["team", "wins"]
    team_total = map_df.groupby("team")["match_url"].nunique().reset_index()
    team_total.columns = ["team", "total"]
    team_map = team_total.merge(team_wins, on="team", how="left").fillna(0)
    team_map["win_rate"] = (team_map["wins"] / team_map["total"] * 100).round(1)
    team_map = team_map[team_map["total"] >= 2].sort_values("win_rate", ascending=False).head(10)

    top3 = team_map.head(3).reset_index(drop=True)
    medals = ["🥇", "🥈", "🥉"]
    cols = st.columns(3)
    for i, row in top3.iterrows():
        with cols[i]:
            logo_path = TEAM_LOGOS.get(row["team"], "")
            if logo_path:
                show_icon(logo_path, width=60)
            st.markdown(f'<div style="color:#FF4655;font-family:Rajdhani,sans-serif;font-size:22px;font-weight:700;">{medals[i]} {row["team"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="color:#555;font-size:13px;">Win Rate: <span style="color:#FF4655;font-weight:700;">{row["win_rate"]}%</span> &nbsp;|&nbsp; Maps: <span style="color:#111;font-weight:700;">{int(row["total"])}</span></div>', unsafe_allow_html=True)
            st.markdown("<br/>", unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)
    styled_df(team_map)

# ── AGENT PAGE ────────────────────────────────────────────────────────────
elif page == "🧬  Agents":
    st.markdown('<div class="page-title">Agent <span>Intelligence</span></div>', unsafe_allow_html=True)

    selected_agent = st.selectbox("Select an Agent", sorted(match_df["agent"].unique()))
    agent_df = match_df[match_df["agent"] == selected_agent]

    col1, col2 = st.columns([1, 5])
    with col1:
        show_icon(AGENT_IMAGES.get(selected_agent, ""), width=100)
    with col2:
        total_picks = len(agent_df)
        overall_wr = round(agent_df["win"].mean() * 100, 1)
        best_map = agent_df.groupby("map")["win"].mean().idxmax()
        c1, c2, c3 = st.columns(3)
        with c1:
            metric_card("Total Picks", total_picks)
        with c2:
            metric_card("Overall Win Rate", f"{overall_wr}%")
        with c3:
            metric_card("Best Map", best_map)

    st.markdown("---")
    section_header("Performance by Map")
    map_agent = agent_df.groupby("map").agg(
        picks=("agent", "count"),
        wins=("win", "sum"),
        avg_acs=("ACS", "mean")
    ).reset_index()
    map_agent["win_rate"] = (map_agent["wins"] / map_agent["picks"] * 100).round(1)
    map_agent["avg_acs"] = map_agent["avg_acs"].round(1)
    map_agent = map_agent.sort_values("win_rate", ascending=False)
    styled_df(map_agent[["map", "picks", "win_rate", "avg_acs"]])

    st.markdown("---")
    section_header("Best Players on this Agent")
    top_players = agent_df.groupby("player").agg(
        picks=("agent", "count"),
        avg_acs=("ACS", "mean"),
        win_rate=("win", "mean"),
        team=("team", "first")
    ).reset_index()
    top_players = top_players[top_players["picks"] >= 2].sort_values("avg_acs", ascending=False).head(10)
    top_players["avg_acs"] = top_players["avg_acs"].round(1)
    top_players["win_rate"] = (top_players["win_rate"] * 100).round(1)
    styled_df(top_players[["player", "team", "picks", "avg_acs", "win_rate"]])

# ── TEAM PAGE ─────────────────────────────────────────────────────────────
elif page == "🏆  Teams":
    st.markdown('<div class="page-title">Team <span>Intelligence</span></div>', unsafe_allow_html=True)

    selected_team = st.selectbox("Select a Team", sorted(match_df["team"].unique()))
    team_df = match_df[match_df["team"] == selected_team]

    maps_played = team_df["match_url"].nunique()
    wins = team_df[team_df["win"] == 1]["match_url"].nunique()
    overall_wr = round(wins / maps_played * 100, 1) if maps_played > 0 else 0
    best_map = team_df.groupby("map").apply(
        lambda x: x[x["win"] == 1]["match_url"].nunique() / x["match_url"].nunique(),
        include_groups=False
    ).idxmax()

    col1, col2, col3 = st.columns(3)
    with col1:
        metric_card("Maps Played", maps_played)
    with col2:
        metric_card("Map Win Rate", f"{overall_wr}%")
    with col3:
        metric_card("Strongest Map", best_map)

    st.markdown("---")
    section_header("Map Win Rates")
    map_wr = team_df.groupby("map").apply(
        lambda x: pd.Series({
            "maps_played": x["match_url"].nunique(),
            "wins": x[x["win"] == 1]["match_url"].nunique()
        }), include_groups=False
    ).reset_index()
    map_wr["win_rate"] = (map_wr["wins"] / map_wr["maps_played"] * 100).round(1)
    map_wr = map_wr.sort_values("win_rate", ascending=False)
    styled_df(map_wr)

    st.markdown("---")
    section_header("Player Roster")
    roster = team_df.groupby("player").agg(
        maps_played=("ACS", "count"),
        avg_acs=("ACS", "mean"),
        avg_k=("K", "mean"),
        avg_d=("D", "mean"),
        avg_adr=("ADR", "mean")
    ).reset_index()
    roster["avg_acs"] = roster["avg_acs"].round(1)
    roster["avg_adr"] = roster["avg_adr"].round(1)
    roster["KD"] = (roster["avg_k"] / roster["avg_d"]).round(2)
    roster = roster.sort_values("avg_acs", ascending=False)
    styled_df(roster[["player", "maps_played", "avg_acs", "KD", "avg_adr"]])

    st.markdown("---")
    section_header("Most Played Agents")
    team_agents = team_df["agent"].value_counts().head(8).reset_index()
    team_agents.columns = ["Agent", "Times Picked"]
    cols = st.columns(4)
    for i, row in team_agents.iterrows():
        with cols[i % 4]:
            show_icon(AGENT_IMAGES.get(row["Agent"], ""))
            st.markdown(f'<div style="color:#111;font-family:Rajdhani,sans-serif;font-size:14px;font-weight:700;">{row["Agent"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="color:#FF4655;font-size:13px;font-weight:700;">{row["Times Picked"]} picks</div>', unsafe_allow_html=True)
            st.markdown("<br/>", unsafe_allow_html=True)

# ── PLAYER PAGE ───────────────────────────────────────────────────────────
elif page == "👤  Players":
    st.markdown('<div class="page-title">Player <span>Leaderboard</span></div>', unsafe_allow_html=True)

    event_filter = st.selectbox("Filter by Event", ["All Events"] + sorted(match_df["event"].unique()))
    if event_filter != "All Events":
        filtered_df = match_df[match_df["event"] == event_filter]
    else:
        filtered_df = match_df

    leaderboard = filtered_df.groupby("player").agg(
        team=("team", "first"),
        maps_played=("ACS", "count"),
        avg_acs=("ACS", "mean"),
        avg_adr=("ADR", "mean"),
        avg_hs=("HS%", "mean"),
        win_rate=("win", "mean")
    ).reset_index()

    leaderboard = leaderboard[leaderboard["maps_played"] >= 3]
    leaderboard["avg_acs"] = leaderboard["avg_acs"].round(1)
    leaderboard["avg_adr"] = leaderboard["avg_adr"].round(1)
    leaderboard["avg_hs"] = leaderboard["avg_hs"].round(1)
    leaderboard["win_rate"] = (leaderboard["win_rate"] * 100).round(1)
    leaderboard = leaderboard.sort_values("avg_acs", ascending=False).reset_index(drop=True)
    leaderboard.index += 1

    st.markdown(f'<div style="color:#555;font-size:12px;letter-spacing:1px;margin-bottom:10px;">SHOWING {len(leaderboard)} PLAYERS · MIN 3 MAPS PLAYED</div>', unsafe_allow_html=True)
    styled_df(leaderboard)