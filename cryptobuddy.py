import streamlit as st

# Bot's knowledge base
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

# Bot logic
def handle_query(query):
    query = query.lower()

    if "sustainable" in query:
        coin = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 {coin} is the most eco-friendly choice with a score of {crypto_db[coin]['sustainability_score']}/10."

    elif "trending" in query or "rising" in query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        return f"📈 These coins are trending up: {', '.join(trending)}"

    elif "growth" in query or "long-term" in query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 7:
                return f"🚀 {coin} is rising and has great sustainability! Strong long-term pick."

    else:
        return "🤔 I’m not sure about that. Try asking about trends or sustainability!"

# Streamlit UI
st.set_page_config(page_title="CryptoBuddy", page_icon="🤖")
st.title("🤖 CryptoBuddy")
st.write("Hey there! 👋 I’m CryptoBuddy — your friendly crypto advisor.")
st.write("_Ask me things like:_ **‘Which crypto is trending?’**, or **‘What's the most sustainable coin?’**")

user_query = st.text_input("💬 Ask me a question:")
if user_query:
    response = handle_query(user_query)
    st.markdown(f"**CryptoBuddy:** {response}")

# Disclaimer
st.caption("⚠️ Crypto is risky—always do your own research!")
