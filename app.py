import streamlit as st
import requests
import json

# Set up page configuration
st.set_page_config(page_title="Global Travel Planner", page_icon="🗺️", layout="wide")

# ==========================================
# 🌐 i18n & l10n TRANSLATION DICTIONARY
# ==========================================
translations = {
    "English": {
        "title": "🗺️ Ultimate City Travel Guide & Planner",
        "subtitle": "Plan your custom itinerary, track expenses visually, and pack smart!",
        "lang_select": "🌐 Select Language / भाषा चुनें / భాషను ఎంచుకోండి / Seleccionar idioma",
        "preferences": "⚙️ Travel Preferences",
        "style": "Select Travel Style:",
        "currency_lbl": "Preferred Currency Display:",
        "dest_lbl": "Choose your destination:",
        "exploring": "## 📍 Exploring: {city} ({mode} Mode)",
        "attractions": "🌟 Top Attractions",
        "delicacies": "🍛 Local Delicacies to Try",
        "weather": "📅 Best Time & Weather Tips",
        "budget_title": "💰 Smart Budget Estimator",
        "days": "Number of days:",
        "hotel": "Hotel cost per night:",
        "food_lbl": "Daily food & activities:",
        "stay_exp": "Stay Expenses",
        "food_exp": "Food & Activity",
        "total_exp": "Total Estimated Cost",
        "pack_title": "🎒 Pre-Travel Packing Checklist",
        "journal_title": "📝 Community Travel Journal",
        "post_btn": "Post Note",
        "ai_title": "🤖 AI-Powered Travel Assistant",
        "ai_prompt_lbl": "Ask the AI Companion anything about planning your trip to {city}:",
        "ai_btn": "Generate Custom AI Insights",
        "ai_setup": "🤖 AI Engine Configuration",
        "ai_mode_lbl": "Select AI Architecture Execution Mode:",
        "byok_key_lbl": "Enter Your OpenAI API Key:",
        "ollama_url_lbl": "Ollama Local Host Endpoint URL:",
        "ollama_model_lbl": "Target Local Model Name:",
    },
    "Hindi": {
        "title": "🗺️ सर्वश्रेष्ठ शहर यात्रा गाइड और योजनाकार",
        "subtitle": "अपनी खुद की यात्रा की योजना बनाएं, खर्चों को ट्रैक करें और समझदारी से पैक करें!",
        "lang_select": "🌐 भाषा का चयन करें",
        "preferences": "⚙️ यात्रा प्राथमिकताएं",
        "style": "यात्रा शैली चुनें:",
        "currency_lbl": "पसंदीदा मुद्रा प्रदर्शन:",
        "dest_lbl": "अपना गंतव्य चुनें:",
        "exploring": "## 📍 अन्वेषण: {city} ({mode} मोड)",
        "attractions": "🌟 प्रमुख आकर्षण",
        "delicacies": "🍛 आजमाने के लिए स्थानीय व्यंजन",
        "weather": "📅 यात्रा का सबसे अच्छा समय",
        "budget_title": "💰 स्मार्ट बजट कैलकुलेटर",
        "days": "दिनों की संख्या:",
        "hotel": "प्रति रात होटल का खर्च:",
        "food_lbl": "दैनिक भोजन और गतिविधियाँ:",
        "stay_exp": "रहने का खर्च",
        "food_exp": "भोजन और गतिविधि",
        "total_exp": "कुल अनुमानित लागत",
        "pack_title": "🎒 यात्रा पैकिंग चेकलिस्ट",
        "journal_title": "📝 सामुदायिक यात्रा जर्नल",
        "post_btn": "नोट पोस्ट करें",
        "ai_title": "🤖 एआई-संचालित यात्रा सहायक",
        "ai_prompt_lbl": "{city} की अपनी यात्रा की योजना बनाने के बारे में एआई से कुछ भी पूछें:",
        "ai_btn": "कस्टम एआई अंतर्दृष्टि उत्पन्न करें",
        "ai_setup": "🤖 एआई इंजन कॉन्फ़िगरेशन",
        "ai_mode_lbl": "एआई आर्किटेक्चर निष्पादन मोड चुनें:",
        "byok_key_lbl": "अपना OpenAI API कुंजी दर्ज करें:",
        "ollama_url_lbl": "ओलामा लोकल होस्ट एंडपॉइंट URL:",
        "ollama_model_lbl": "लक्षित स्थानीय मॉडल का नाम:",
    },
    "Telugu": {
        "title": "🗺️ అల్టిమేట్ సిటీ ట్రావెల్ గైడ్ & ప్లానర్",
        "subtitle": "మీ అనుకూల ప్రయాణ ప్రణాళికను సిద్ధం చేసుకోండి, ఖర్చులను చూడండి మరియు స్మార్ట్‌గా ప్యాక్ చేయండి!",
        "lang_select": "🌐 భాషను ఎంచుకోండి",
        "preferences": "⚙️ ప్రయాణ ప్రాధాన్యతలు",
        "style": "ప్రయాణ శైలిని ఎంచుకోండి:",
        "currency_lbl": "కరెన్సీ ప్రదర్శన:",
        "dest_lbl": "మీ గమ్యస్థానాన్ని ఎంచుకోండి:",
        "exploring": "## 📍 సందర్శన స్థలం: {city} ({mode} మోడ్)",
        "attractions": "🌟 ప్రముఖ ఆకర్షణలు",
        "delicacies": "🍛 తప్పక రుచి చూడాల్సిన వంటకాలు",
        "weather": "📅 సందర్శించడానికి ఉత్తమ సమయం",
        "budget_title": "💰 స్మార్ట్ బడ్జెట్ అంచనా",
        "days": "రోజుల సంఖ్య:",
        "hotel": "ఒక రాత్రికి హోటల్ ఖర్చు:",
        "food_lbl": "రోజువారీ భోజనం & కార్యకలాపాలు:",
        "stay_exp": "వసతి ఖర్చులు",
        "food_exp": "భోజనం & కార్యకలాపాలు",
        "total_exp": "మొత్తం అంచనా ఖర్చు",
        "pack_title": "🎒 ప్రీ-ట్రావెల్ ప్యాకింగ్ చెక్‌లిస్ట్",
        "journal_title": "📝 కమ్యూనిటీ ట్రావెల్ జర్నల్",
        "post_btn": "నోట్ పోస్ట్ చేయండి",
        "ai_title": "🤖 AI ట్రావెల్ అసిస్టెంట్",
        "ai_prompt_lbl": "{city} ప్రయాణ ప్రణాళిక గురించి AI సహాయకుడిని ఏదైనా అడగండి:",
        "ai_btn": "కస్టమ్ AI సమాధానాన్ని పొందండి",
        "ai_setup": "🤖 AI కాన్ఫిగరేషన్",
        "ai_mode_lbl": "AI ఆర్కిటెక్చర్ మోడ్‌ను ఎంచుకోండి:",
        "byok_key_lbl": "మీ OpenAI API కీని నమోదు చేయండి:",
        "ollama_url_lbl": "ఒల్లామా లోకల్ హోస్ట్ URL:",
        "ollama_model_lbl": "లోకల్ మోడల్ పేరు:",
    },
    "Spanish": {
        "title": "🗺️ Guía y Planificador Definitivo de Viajes",
        "subtitle": "¡Planifique su itinerario personalizado, realice un seguimiento visual de los gastos y empaque de manera inteligente!",
        "lang_select": "🌐 Seleccionar idioma",
        "preferences": "⚙️ Preferencias de viaje",
        "style": "Seleccione el estilo de viaje:",
        "currency_lbl": "Moneda preferida:",
        "dest_lbl": "Elija su destino:",
        "exploring": "## 📍 Explorando: {city} (Modo {mode})",
        "attractions": "🌟 Principales atracciones",
        "delicacies": "🍛 Delicias locales para probar",
        "weather": "📅 Mejor época y consejos climáticos",
        "budget_title": "💰 Estimador de presupuesto inteligente",
        "days": "Número de días:",
        "hotel": "Costo de hotel por noche:",
        "food_lbl": "Comida diaria y actividades:",
        "stay_exp": "Gastos de estancia",
        "food_exp": "Comida y actividad",
        "total_exp": "Costo total estimado",
        "pack_title": "🎒 Lista de equipaje antes del viaje",
        "journal_title": "📝 Diario de viaje de la comunidad",
        "post_btn": "Publicar nota",
        "ai_title": "🤖 Asistente de viaje con IA",
        "ai_prompt_lbl": "Pregúntele al compañero de IA lo que sea sobre la planificación de su viaje a {city}:",
        "ai_btn": "Generar información personalizada de IA",
        "ai_setup": "🤖 Configuración del motor de IA",
        "ai_mode_lbl": "Seleccione el modo de ejecución de la arquitectura de IA:",
        "byok_key_lbl": "Ingrese su clave API de OpenAI:",
        "ollama_url_lbl": "URL del endpoint local de Ollama:",
        "ollama_model_lbl": "Nombre del modelo local de destino:",
    },
}


# ==========================================
# 🤖 UNIFIED AI GATEWAY INFRASTRUCTURE
# ==========================================
def query_ai_engine(mode, prompt, api_key, ollama_url, ollama_model):
    payload = {"messages": [{"role": "user", "content": prompt}], "temperature": 0.7}

    if mode == "✨ Cloud API (BYOK - OpenAI)":
        if not api_key:
            return (
                "⚠️ Please supply a valid OpenAI API key in the configuration sidebar."
            )
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        url = "https://api.openai.com/v1/chat/completions"
        payload["model"] = "gpt-4o-mini"
    else:
        url = f"{ollama_url.strip('/')}/v1/chat/completions"
        headers = {"Content-Type": "application/json"}
        payload["model"] = ollama_model

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"❌ API Error (Status Code {response.status_code}): {response.text}"
    except requests.exceptions.ConnectionError:
        if mode == "🎒 Local Inference (Ollama)":
            return f"❌ Failed to connect to Ollama. Ensure Ollama is running locally at {ollama_url} and your model is pulled (run: `ollama run {ollama_model}`)."
        return "❌ Connection timeout. Please verify your internet network link."
    except Exception as e:
        return f"❌ Encountered unexpected runtime exception: {str(e)}"


# ==========================================
# 🎛️ SIDEBAR CONTROL BAR
# ==========================================
selected_lang = st.sidebar.selectbox(
    translations["English"]["lang_select"], ["English", "Hindi", "Telugu", "Spanish"]
)
lang = translations[selected_lang]

st.sidebar.divider()
st.sidebar.header(lang["preferences"])
travel_mode = st.sidebar.radio(
    lang["style"], ["🎒 Budget Friendly", "✨ Premium/Luxury"]
)
currency = st.sidebar.selectbox(lang["currency_lbl"], ["INR (₹)", "USD ($)"])

st.sidebar.divider()
st.sidebar.header(lang["ai_setup"])
ai_mode = st.sidebar.radio(
    lang["ai_mode_lbl"], ["🎒 Local Inference (Ollama)", "✨ Cloud API (BYOK - OpenAI)"]
)

api_key = ""
ollama_url = "http://localhost:11434"
ollama_model = "llama3"

if ai_mode == "✨ Cloud API (BYOK - OpenAI)":
    api_key = st.sidebar.text_input(lang["byok_key_lbl"], type="password")
else:
    ollama_url = st.sidebar.text_input(
        lang["ollama_url_lbl"], value="http://localhost:11434"
    )
    ollama_model = st.sidebar.text_input(lang["ollama_model_lbl"], value="llama3")

# ==========================================
# 🏙️ MAIN APP RENDER LAYER
# ==========================================
st.title(lang["title"])
st.write(lang["subtitle"])

destination = st.selectbox(
    lang["dest_lbl"],
    [
        "Select a city...",
        "Hyderabad",
        "Goa",
        "Delhi",
        "Mumbai",
        "Jaipur",
        "Kerala",
        "Paris",
        "Tokyo",
        "London",
        "New York",
    ],
)

if destination != "Select a city...":
    st.markdown(lang["exploring"].format(city=destination, mode=travel_mode))

    col_left, col_right = st.columns(2)
    with col_left:
        with st.expander(lang["attractions"], expanded=True):
            if destination == "Hyderabad":
                st.markdown(
                    "- **Charminar:** Historical 16th-century mosque.\n- **Golconda Fort:** Majestic diamond-trading hub ruins.\n- **Hussain Sagar Lake:** Giant Buddha statue.\n- **Salar Jung Museum:** Incredible antique collection."
                )
            elif destination == "Goa":
                st.markdown(
                    "- **Baga Beach:** Nightlife and water sports.\n- **Dudhsagar Falls:** Four-tiered spectacular waterfall."
                )
            elif destination == "Delhi":
                st.markdown(
                    "- **India Gate:** Iconic war memorial arch.\n- **Red Fort:** Historic 17th-century Mughal fortress.\n- **Qutub Minar:** Tallest brick minaret."
                )
            elif destination == "Mumbai":
                st.markdown(
                    "- **Gateway of India:** Iconic arch monument.\n- **Marine Drive:** Stunning seaside promenade."
                )
            elif destination == "Jaipur":
                st.markdown(
                    "- **Hawa Mahal:** Pink sandstone 'Palace of Winds'.\n- **Amer Fort:** Hilltop fort with mirror halls."
                )
            elif destination == "Kerala":
                st.markdown(
                    "- **Alleppey Houseboats:** Coastal backwaters.\n- **Munnar Tea Gardens:** Mountain tea plantations."
                )
            else:
                st.markdown(
                    f"- Popular monuments and scenic spaces across {destination}."
                )

    with col_right:
        with st.expander(lang["delicacies"], expanded=True):
            if destination == "Hyderabad":
                st.write(
                    "🔥 Famous for: Hyderabadi Biryani, Haleem, Double Ka Meetha, Irani Chai."
                )
            elif destination == "Goa":
                st.write("🐟 Famous for: Goan Fish Curry, Bebinca (dessert).")
            elif destination == "Delhi":
                st.write(
                    "🥞 Famous for: Hot Chole Bhature, Paranthas from Chandni Chowk, Butter Chicken."
                )
            elif destination == "Mumbai":
                st.write("🍔 Famous for: Spicy Vada Pav, Pav Bhaji, Bhel Puri.")
            elif destination == "Jaipur":
                st.write(
                    "🍽️ Famous for: Traditional Dal Baati Churma, Pyaaz Kachori, Ghewar."
                )
            elif destination == "Kerala":
                st.write(
                    "🥥 Famous for: Soft Appam with Stew, Malabar Parotta with Curry."
                )
            else:
                st.write(
                    f"🍏 Explore localized traditional food variations in {destination}."
                )

        with st.expander(lang["weather"]):
            if destination in [
                "Hyderabad",
                "Goa",
                "Delhi",
                "Mumbai",
                "Jaipur",
                "Kerala",
            ]:
                st.info(
                    "❄️ **October to March:** Cool winter months are perfect for exploring smoothly."
                )
            else:
                st.info(
                    "🌸 Pleasant seasonal windows are highly ideal for travel planning."
                )

    st.divider()

    # ==========================================
    # 🤖 INTEGRATED AI COPILOT SECTION
    # ==========================================
    st.subheader(lang["ai_title"])
    ai_prompt = st.text_input(
        lang["ai_prompt_lbl"].format(city=destination),
        value=f"Give me a quick 3-day travel itinerary checklist for a {travel_mode.lower()} trip to {destination}.",
    )

    if st.button(lang["ai_btn"]):
        with st.spinner("🧠 Querying AI Engine Inference Pipeline..."):
            ai_response = query_ai_engine(
                ai_mode, ai_prompt, api_key, ollama_url, ollama_model
            )
            st.markdown("### 💬 AI Travel Planner Response:")
            st.write(ai_response)

    st.divider()

    # Budget Estimator
    st.subheader(lang["budget_title"])
    b_col1, b_col2, b_col3 = st.columns(3)
    with b_col1:
        days = st.slider(lang["days"], 1, 14, 3)
    with b_col2:
        default_hotel = 1500 if "Budget" in travel_mode else 6000
        hotel_cost = st.number_input(lang["hotel"], min_value=0, value=default_hotel)
    with b_col3:
        default_food = 1000 if "Budget" in travel_mode else 3000
        daily_food = st.number_input(lang["food_lbl"], min_value=0, value=default_food)

    total_stay = hotel_cost * days
    total_food = daily_food * days
    grand_total = total_stay + total_food

    symbol = "₹" if "INR" in currency else "$"
    factor = 1.0 if "INR" in currency else 0.012

    m1, m2, m3 = st.columns(3)
    m1.metric(lang["stay_exp"], f"{symbol} {int(total_stay * factor):,}")
    m2.metric(lang["food_exp"], f"{symbol} {int(total_food * factor):,}")
    m3.metric(
        lang["total_exp"],
        f"{symbol} {int(grand_total * factor):,}",
        delta="- Dynamic" if "Budget" in travel_mode else "+ Luxury",
    )

    st.divider()

    # Packing Checklist
    st.subheader(lang["pack_title"])
    col1, col2 = st.columns(2)
    with col1:
        p1 = st.checkbox("Passport / Government ID card")
        p2 = st.checkbox("Confirmed Tickets & Hotel Vouchers")
        p3 = st.checkbox("Universal Adapter & Phone Chargers")
    with col2:
        p4 = st.checkbox("Appropriate Clothes")
        p5 = st.checkbox("Emergency Medicines & First Aid kit")
        p6 = st.checkbox("Sunscreen & Essential Toiletries")

    if p1 and p2 and p3 and p4 and p5 and p6:
        st.balloons()

    st.divider()

    # Community Notes
    st.subheader(lang["journal_title"])
    user_note = st.text_area("Share a travel tip:")
    if st.button(lang["post_btn"]):
        if user_note:
            st.info(f"👉 {user_note}")
