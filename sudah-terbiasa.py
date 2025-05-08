import streamlit as st
import time
import base64

# Set page configuration
st.set_page_config(
    page_title="Lyrics Display",
    page_icon="💖",
    layout="centered"
)

# Custom CSS for a coquette and girly UI
def add_bg_and_styling():
    st.markdown("""
    <style>
        .main {
            background-color: #fff0f5;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(255, 182, 193, 0.5);
        }
        .stApp {
            background-image: linear-gradient(to bottom right, #ffe6f2, #ffb6c1);
        }
        h1, h2, h3 {
            color: #ff69b4 !important;
            font-family: 'Comic Sans MS', cursive, sans-serif;
            text-shadow: 1px 1px 4px #ffb6c1;
        }
        .ribbon-lyrics-container {
            background-color: #fff0f5;
            border-radius: 25px;
            padding: 30px 25px;
            border: 4px dashed #ff69b4;
            font-family: 'Comic Sans MS', cursive, sans-serif;
            font-size: 22px;
            line-height: 1.8;
            color: #ff69b4;
            box-shadow: 0 6px 18px rgba(255, 182, 193, 0.3);
            margin-top: 20px;
            margin-bottom: 20px;
            position: relative;
        }
        .ribbon-lyrics-container:before, .ribbon-lyrics-container:after {
            content: "🎀";
            font-size: 2.2rem;
            position: absolute;
        }
        .ribbon-lyrics-container:before {
            left: 10px;
            top: 10px;
        }
        .ribbon-lyrics-container:after {
            right: 10px;
            bottom: 10px;
        }
        .stMarkdown p {
            font-size: 20px;
        }
    </style>
    """, unsafe_allow_html=True)



# Set animation speed per line (seconds per character)
LINE_SPEEDS = [0.5, 0.1, 0.12, 0.1, 0.18, 0.2]  # Adjust these values manually per line

# Main app function
def main():
    add_bg_and_styling()
    st.markdown("<h2 style='text-align: center; color: #ff69b4;'>💕 TANTEEEE 💕</h2>", unsafe_allow_html=True)

    # Start button
    start = st.button("🎀 Start 🎶")

    if start:
        # Play music
        try:
            with open('tante.mp3', 'rb') as audio_file:
                audio_bytes = audio_file.read()
                b64 = base64.b64encode(audio_bytes).decode()
                audio_html = f"""
                <audio autoplay controls style='width: 100%; margin-bottom: 20px;'>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                    Your browser does not support the audio element.
                </audio>
                """
                st.markdown(audio_html, unsafe_allow_html=True)
        except FileNotFoundError:
            st.info('Put your tante file as tante.mp3 in the project folder to play music!')

        # Animated lyrics
        lyrics_lines = [
            "tantee",
            "sudah terbiasa terjadi tante.....",
            "teman datang ketika lagi butuh saja ",
            "coba kalo lagi susah.....",
            "mereka semua menghilangggggggggg",
            "TANTEEEEEE"
        ]
        lyrics_container = st.empty()
        displayed_text = ""
        for idx, line in enumerate(lyrics_lines):
            speed = LINE_SPEEDS[idx] if idx < len(LINE_SPEEDS) else LINE_SPEEDS[-1]
            for char in line:
                displayed_text += char
                lyrics_container.markdown(f"""
                <div class=\"ribbon-lyrics-container\">
                    🎀 {displayed_text.replace(chr(10), '<br>')} 🎀
                </div>
                """, unsafe_allow_html=True)
                time.sleep(speed)
            displayed_text += "<br>"
            lyrics_container.markdown(f"""
            <div class=\"ribbon-lyrics-container\">
                🎀 {displayed_text} 🎀
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("")

    st.markdown(
        """<div style='text-align:center; color:#ff69b4; font-size:1.2em; margin-bottom:10px;'>
        ini pny ileene jgn dicolong y
        </div>""",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()