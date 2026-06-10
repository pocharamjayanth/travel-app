import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Ultimate Travel Guide", page_icon="🗺️", layout="wide")

# --- SIDEBAR ELEMENTS ---
st.sidebar.header("⚙️ Trip Preferences")
travel_mode = st.sidebar.radio("Select Travel Style:", ["🎒 Budget Friendly", "✨ Premium/Luxury"])
currency = st.sidebar.selectbox("Preferred Currency Display:", ["INR (₹)", "USD ($)"])

# Main App Header
st.title("🗺️ Ultimate City Travel Guide & Planner")
st.write("Plan your custom itinerary, track expenses visually, and pack smart!")

# 1. Destination Selector (Added top Indian places)
destination = st.selectbox(
    "Choose your destination:",
    ["Select a city...", "Hyderabad", "Goa", "Delhi", "Mumbai", "Jaipur", "Kerala", "Paris", "Tokyo", "London", "New York"]
)

if destination != "Select a city...":
    st.markdown(f"## 📍 Exploring: {destination} ({travel_mode} Mode)")
    
    # Layout split into two columns for attractions and details
    col_left, col_right = st.columns(2)
    
    with col_left:
        with st.expander("🌟 Top Attractions", expanded=True):
            if destination == "Hyderabad":
                st.markdown("- **Charminar:** Historical 16th-century mosque.\n- **Golconda Fort:** Majestic diamond-trading hub ruins.\n- **Hussain Sagar Lake:** Giant Buddha statue.\n- **Salar Jung Museum:** Incredible antique collection.")
            elif destination == "Goa":
                st.markdown("- **Baga Beach:** Nightlife and water sports.\n- **Dudhsagar Falls:** Four-tiered spectacular waterfall.\n- **Aguada Fort:** 17th-century Portuguese lighthouse.\n- **Basilica of Bom Jesus:** UNESCO World Heritage site.")
            elif destination == "Delhi":
                st.markdown("- **India Gate:** Iconic war memorial arch.\n- **Red Fort:** Historic 17th-century Mughal fortress.\n- **Qutub Minar:** Tallest brick minaret in the world.\n- **Lotus Temple:** Marvel of modern architecture open to all faiths.")
            elif destination == "Mumbai":
                st.markdown("- **Gateway of India:** Iconic 20th-century historical arch monument.\n- **Marine Drive:** Stunning arc-shaped seaside promenade.\n- **Elephanta Caves:** Ancient rock-cut cave temples dedicated to Shiva.\n- **Chhatrapati Shivaji Terminus:** UNESCO Heritage Victorian-Gothic railway station.")
            elif destination == "Jaipur":
                st.markdown("- **Hawa Mahal:** Iconic pink sandstone 'Palace of Winds'.\n- **Amer Fort:** Magnificent hilltop fort with mirror halls.\n- **City Palace:** Royal residence displaying museum textiles and weapons.\n- **Jantar Mantar:** Astronomical observatory with the world's largest stone sundial.")
            elif destination == "Kerala":
                st.markdown("- **Alleppey Houseboats:** Cruising scenic coastal backwaters.\n- **Munnar Tea Gardens:** Expansive lush green mountain tea plantations.\n- **Wayanad:** Wildlife sanctuaries and serene cave hikes.\n- **Varkala Beach:** Cliff-backed sandy beaches over the Arabian Sea.")
            elif destination == "Paris":
                st.markdown("- **Eiffel Tower:** Iconic wrought-iron lattice tower.\n- **Louvre Museum:** World's largest art museum.\n- **Notre-Dame Cathedral:** Gothic architecture marvel.\n- **Arc de Triomphe:** Famous triumphal arch.")
            elif destination == "Tokyo":
                st.markdown("- **Tokyo Skytree:** Tallest structure in Japan.\n- **Senso-ji Temple:** Tokyo's oldest Buddhist temple.\n- **Shibuya Crossing:** World's busiest pedestrian intersection.\n- **Meiji Shrine:** Serene Shinto shrine in a forested area.")
            elif destination == "London":
                st.markdown("- **Tower of London:** Historic castle and home to Crown Jewels.\n- **The London Eye:** Giant Ferris wheel offering panoramic city views.\n- **British Museum:** Dedicated to human history, art, and culture.\n- **Big Ben:** Iconic striking clock tower at Westminster.")
            elif destination == "New York":
                st.markdown("- **Statue of Liberty:** Iconic monument of freedom.\n- **Times Square:** Brightly illuminated hub of Broadway theaters.\n- **Central Park:** Expansive urban park in Manhattan.\n- **Empire State Building:** Legendary 102-story Art Deco skyscraper.")

    with col_right:
        with st.expander("🍛 Local Delicacies to Try", expanded=True):
            if destination == "Hyderabad":
                st.write("🔥 Famous for: Hyderabadi Biryani, Haleem, Double Ka Meetha, Irani Chai.")
            elif destination == "Goa":
                st.write("🐟 Famous for: Goan Fish Curry, Bebinca (dessert), Feni, Prawn Balchão.")
            elif destination == "Delhi":
                st.write("🥞 Famous for: Hot Chole Bhature, Paranthas from Chandni Chowk, Butter Chicken, Golgappe.")
            elif destination == "Mumbai":
                st.write("🍔 Famous for: Spicy Vada Pav, Pav Bhaji, Bhel Puri, Misal Pav.")
            elif destination == "Jaipur":
                st.write("🍽️ Famous for: Traditional Dal Baati Churma, Pyaaz Kachori, Ghewar, Royal Laal Maas.")
            elif destination == "Kerala":
                st.write("🥥 Famous for: Soft Appam with Veg/Meat Stew, Malabar Parotta with Curry, Banana Chips, Sadya Feast.")
            elif destination == "Paris":
                st.write("🥐 Famous for: Fresh Croissants, Escargot, Macarons, Baguettes & Cheese.")
            elif destination == "Tokyo":
                st.write("🍣 Famous for: Fresh Sushi, Tonkotsu Ramen, Tempura, Wagyu Beef.")
            elif destination == "London":
                st.write("🐟 Famous for: Classic Fish & Chips, Traditional Sunday Roast, Full English Breakfast, Afternoon Tea.")
            elif destination == "New York":
                st.write("🍕 Famous for: New York-style Pizza, Authentic Bagels & Lox, Cheesecake, Pastrami On Rye.")

        with st.expander("📅 Best Time & Weather Tips"):
            if destination in ["Hyderabad", "Goa", "Delhi", "Mumbai", "Jaipur", "Kerala"]:
                st.info("❄️ **October to March:** Cool, winter months are perfect for exploring these Indian locations smoothly.")
            elif destination in ["Paris", "Tokyo"]:
                st.info("🌸 **April to May (Spring):** Beautiful weather and blooming scenic landscapes.")
            elif destination in ["London", "New York"]:
                st.info("☀️ **May to September:** Warm, comfortable weather with long daylight hours for walking tours.")

    st.divider()

    # 2. Advanced Trip Budget Estimator with Metrics
    st.subheader("💰 Smart Budget Estimator")
    
    b_col1, b_col2, b_col3 = st.columns(3)
    with b_col1:
        days = st.slider("Number of days:", 1, 14, 3)
    with b_col2:
        default_hotel = 1500 if "Budget" in travel_mode else 6000
        hotel_cost = st.number_input("Hotel cost per night:", min_value=0, value=default_hotel)
    with b_col3:
        default_food = 1000 if "Budget" in travel_mode else 3000
        daily_food = st.number_input("Daily food & activities:", min_value=0, value=default_food)
    
    # Calculate costs
    total_stay = hotel_cost * days
    total_food = daily_food * days
    grand_total = total_stay + total_food
    
    # Currency conversion display logic
    symbol = "₹" if "INR" in currency else "$"
    factor = 1.0 if "INR" in currency else 0.012  # Simple mock exchange rate
    
    # UI Metric Blocks
    m1, m2, m3 = st.columns(3)
    m1.metric("Stay Expenses", f"{symbol} {int(total_stay * factor):,}")
    m2.metric("Food & Activity", f"{symbol} {int(total_food * factor):,}")
    m3.metric("Total Estimated Cost", f"{symbol} {int(grand_total * factor):,}", delta="- Dynamic" if "Budget" in travel_mode else "+ Luxury")

    st.divider()

    # 3. Interactive Packing Checklist
    st.subheader("🎒 Pre-Travel Packing Checklist")
    
    col1, col2 = st.columns(2)
    with col1:
        p1 = st.checkbox("Passport / Government ID card")
        p2 = st.checkbox("Confirmed Tickets & Hotel Vouchers")
        p3 = st.checkbox("Universal Adapter & Phone Chargers")
    with col2:
        p4 = st.checkbox("Appropriate Clothes (Based on Destination weather)")
        p5 = st.checkbox("Emergency Medicines & First Aid kit")
        p6 = st.checkbox("Sunscreen & Essential Toiletries")
        
    if p1 and p2 and p3 and p4 and p5 and p6:
        st.balloons()
        st.success("🎉 Packing complete! You are fully prepared to catch your flight.")

    st.divider()

    # 4. User Interaction Elements (Community Notes)
    st.subheader("📝 Community Travel Journal")
    user_note = st.text_area("Have you been here? Share a travel tip or recommendation with fellow travelers:")
    if st.button("Post Note"):
        if user_note:
            st.info(f"👉 **Anonymous Traveler says:** {user_note}")
            st.toast("Note posted successfully!")
        else:
            st.warning("Please type a note before clicking submit.")
