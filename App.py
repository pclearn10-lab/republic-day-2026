import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="Republic Day 2026", page_icon="🇮🇳")

# 2. Background Music (Instrumental Vande Mataram style)
# This link plays a high-quality patriotic instrumental track
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3" 
st.audio(audio_url, format="audio/mp3", autoplay=True, loop=True)

# 3. Header with your name
st.title("🇮🇳 Happy Republic Day 2026")
st.markdown("### *Created with Pride by Pooja Chowdhary*")

# 4. Colorful Patriotic Image
# Using a high-quality tricolor/parade themed image
st.image("https://images.unsplash.com/photo-1532375810709-75b1da00537c?auto=format&fit=crop&w=800&q=80", 
         caption="Unity in Diversity - Jai Hind!")

st.write("---")

# 5. Information Nuggets Bank
nuggets = [
    "The Indian Constitution is the longest handwritten constitution in the world!",
    "The original copies are kept in helium-filled cases in the Parliament Library.",
    "The first Republic Day parade at Kartavya Path (Rajpath) was held in 1955.",
    "The date Jan 26 was chosen to honor the 'Purna Swaraj' declaration of 1930.",
    "It took exactly 2 years, 11 months, and 18 days to draft the Constitution.",
    "Nandalal Bose, a famous artist, illustrated every single page of the Constitution!",
    "The National Anthem was officially adopted just 2 days before the first Republic Day."
]

# 6. User Interaction
name = st.text_input("Enter your name for a surprise:", placeholder="Type here...")

if name:
    st.balloons()
    st.success(f"### Happy Republic Day, {name}! 🇮🇳 ✨")
    
    # Pick and display a random fact
    random_fact = random.choice(nuggets)
    st.info(f"📜 **Did you know?** \n\n {random_fact}")
    
    # 7. Share on WhatsApp Feature
    st.write("---")
    st.write("📢 **Spread the pride!** Share this with your friends:")
    
    share_text = f"Happy Republic Day 2026! 🇮🇳 I am {name}. Did you know? {random_fact}"
    whatsapp_url = f"https://wa.me/?text={share_text.replace(' ', '%20')}"
    
    st.link_button("📲 Send to WhatsApp", whatsapp_url)

# Footer
st.caption("Jai Hind! 🇮🇳 | Stay Patriotic | Designed by Pooja Chowdhary")
