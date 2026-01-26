import streamlit as st
import random

# Set Page Title & Icon
st.set_page_config(page_title="Republic Day 2026!", page_icon="🇮🇳")
St.write("---")
St.subheader("created with pride by Pooja Chowdhary")
# --- DATA BANK ---
nuggets = [
    "The Indian Constitution is the longest handwritten constitution in the world!",
    "It took exactly 2 years, 11 months, and 18 days to draft the Constitution.",
    "The original copies are kept in helium-filled cases in the Parliament Library.",
    "The first Republic Day parade at Rajpath (now Kartavya Path) was held in 1955.",
    "The National Anthem was officially adopted just 2 days before the first Republic Day.",
    "The Constitution was calligraphed by Prem Behari Narain Raizada—he didn't charge a penny for it!",
    "The date Jan 26 was chosen to honor the 'Purna Swaraj' declaration of 1930."
]

# --- UI DESIGN ---
st.title("🇮🇳 Happy Republic Day 2026!")
st.subheader("Get your personalized wish & a historical nugget")

# Input for Name
name = st.text_input("Enter your name here:", placeholder="e.g. Rahul")

if name:
    # Trigger Celebration
    st.balloons()
    
    # Generate Personalized Message
    st.success(f"### Jai Hind, {name}! 🇮🇳")
    st.write(f"May the tricolor always fly high and our nation continue to prosper. Wishing you a very Happy 77th Republic Day!")
    
    # The "Nugget" Section
    st.divider()
    st.markdown("#### 📜 Your Republic Day Nugget:")
    random_fact = random.choice(nuggets)
    st.info(random_fact)
    
    # Button to get a new fact
    if st.button("🔄 Get Another Fact"):
        st.rerun()

# Footer
st.caption("Made with ❤️ and AI for Republic Day 2026")
