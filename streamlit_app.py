import streamlit as st

st.set_page_config(page_title="Dein QR-Musikplayer", layout="centered")
st.title("Ali songs")

# DEINE GitHub-Links:
song_urls = [
    "https://github.com/sdh2025/Ali/songs/song1.mp3",
    "https://github.com/sdh2025/Ali/songs/song2.mp3"
]

# HTML mit Autoplay und Playlist
playlist_html = f"""
<audio id="player" controls autoplay>
  <source src="{song_urls[0]}" type="audio/mp3">
  Dein Browser unterstützt kein Audio.
</audio>

<script>
const songs = {song_urls};
let index = 0;
const player = document.getElementById("player");

player.onended = () => {{
    index++;
    if (index < songs.length) {{
        player.src = songs[index];
        player.play();
    }}
}};
</script>
"""

st.markdown(playlist_html, unsafe_allow_html=True)
