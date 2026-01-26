import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="Republic Day 2026", page_icon="🇮🇳")

# 2. Background Music (Plays automatically)
# Note: Browsers usually require one click anywhere on the page to start audio.
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" 
st.audio(audio_url, format="audio/mp3", autoplay=True, loop=True)

# 3. Header with your name
st.title("🇮🇳 Happy Republic Day 2026")
st.markdown("##### *Created with Pride by Pooja Chowdhary*")
st.write("---")

# 4. Information Nuggets Bank
nuggets = [
    "The Indian Constitution is the longest handwritten constitution in the world!",
    "The original copies are kept in helium-filled cases in the Parliament Library.",
    "The first Republic Day parade at Rajpath (now Kartavya Path) was held in 1955.",
    "The date Jan 26 was chosen to honor the 'Purna Swaraj' declaration of 1930.",
    "It took exactly 2 years, 11 months, and 18 days to draft the Constitution.",
    "Nandalal Bose, a famous artist, illustrated every single page of the Constitution!",
    "The National Anthem was officially adopted just 2 days before the first Republic Day."
]

# 5. User Interaction
name = st.text_input("Enter your name for a surprise:", placeholder="Type here...")

if name:
    st.balloons()
    st.success(f"### Jai Hind, {name}! 🇮🇳 ✨")
    
    # Pick and display a random fact
    random_fact = random.choice(nuggets)
    st.info(f"📜 **Did you know?** \n\n {random_fact}")
    
    # 6. Share on WhatsApp Feature
    st.write("---")
    st.write("📢 **Spread the pride!** Share this fact with your friends:")
    
    share_text = f"Happy Republic Day 2026! 🇮🇳 I am {name}. Did you know? {random_fact}"
    # Encoding the text for a URL
    whatsapp_url = f"https://wa.me/?text={share_text.replace(' ', '%20')}"
    
    st.link_button("📲 Send to WhatsApp", whatsapp_url)

# Footer
st.caption("Jai Hind! 🇮🇳 | Stay Patriotic")
