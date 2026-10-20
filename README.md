# 🗺️ Global Travel Planner

> A multilingual city travel guide and trip planner with a **Google Gemini-powered AI assistant**, available in English, Hindi, Telugu and Spanish.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-4285F4?logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-AGPL--3.0-green)

Plan a trip in one place: explore a destination, estimate your budget, pack smart, and ask an AI companion for a custom itinerary, all in your own language.

---

## 📸 Preview

<!-- Add a screenshot or GIF of the app here, e.g. ![App screenshot](docs/screenshot.png) -->

---

## ✨ Features

| Feature | What it does |
|---|---|
| 🌐 **Multilingual UI** | Switch between English, Hindi (हिन्दी), Telugu (తెలుగు) and Spanish (Español); every label is localized |
| 📍 **Destination guides** | Top attractions, local delicacies and best time to visit for 10 cities |
| 🎒 **Travel styles** | Budget Friendly or Premium/Luxury, which also changes the budget defaults |
| 💰 **Smart budget estimator** | Days × hotel + daily food and activities, shown in **INR (₹)** or **USD ($)** |
| ✅ **Packing checklist** | Six pre-travel essentials, with a small celebration when you're fully packed |
| 📝 **Community travel journal** | Share a quick travel tip |
| 🤖 **AI travel assistant** | Generates itineraries and travel tips for your chosen city and style using Google Gemini |

**Supported destinations:** Hyderabad · Goa · Delhi · Mumbai · Jaipur · Kerala · Paris · Tokyo · London · New York

---

## 🤖 AI Assistant (Google Gemini)

The assistant is powered by **Google Gemini** (`gemini-3.5-flash`) through the official `google-genai` Python SDK.

- **Bring Your Own Key (BYOK):** paste a free Gemini API key into the sidebar. Get one from [Google AI Studio](https://aistudio.google.com/app/apikey).
- **Editable prompt:** it starts pre-filled with your destination and travel style (for example *"Give me a quick 3-day travel itinerary checklist for a budget friendly trip to Goa"*), and you can ask anything about your trip.
- **Safe by design:** the key is entered in a password field at runtime and is never hardcoded or committed.
- **Clear error handling:** friendly messages for a missing key, Gemini API errors, and unexpected failures.

---

## 🏗️ Architecture

```
┌──────────────────────────── Streamlit App (app.py) ────────────────────────────┐
│                                                                                │
│  Sidebar ──► Language · Travel style · Currency · Gemini API key               │
│                                                                                │
│  Main page ─► Destination guide ─► AI assistant ─► Budget ─► Packing ─► Journal│
│                                         │                                      │
│                                         ▼                                      │
│                           query_gemini_engine()                                │
│                                         │                                      │
│                                         ▼                                      │
│                       Google Gemini API (google-genai SDK)                     │
└────────────────────────────────────────────────────────────────────────────────┘
```

There is no separate backend or database. The Python code in `app.py` handles localization, content, budget logic and the Gemini request, and state lives in the Streamlit session.

**Design approach:** the project follows a spec-driven workflow. Requirements, plan and tasks live in [`specs/travel_planner_core`](specs/travel_planner_core) (`spec.md`, `plan.md`, `tasks.md`), starting with a unified dictionary-based i18n layer for English, Hindi, Telugu and Spanish.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A free [Google Gemini API key](https://aistudio.google.com/app/apikey)

### Installation

```bash
# Clone the repository
git clone https://github.com/pocharamjayanth/travel-app.git
cd travel-app

# (Recommended) create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run app.py
```

Open the URL shown in your terminal (usually `http://localhost:8501`), then paste your Gemini API key in the sidebar to use the AI assistant. All other features work without a key.

### Run with Docker

```bash
docker build -t travel-app .
docker run -p 8501:8501 travel-app
```

---

## 🧪 Testing & Code Quality

```bash
python -m unittest test_app.py
# or
pytest
```

The CI pipeline (`.gitlab-ci.yml`) runs these stages: **lint** (ruff, pylint, flake8) → **format** → **type check** (mypy) → **security** (Bandit, Semgrep) → **test** → **coverage**.

Pre-commit hooks are configured in `.pre-commit-config.yaml`:

```bash
pip install pre-commit
pre-commit install
```

---

## 📁 Project Structure

```
travel-app/
├── app.py               # Streamlit app: UI, translations, budget logic, Gemini gateway
├── test_app.py          # Unit tests (localization checks)
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Project and tooling configuration
├── Dockerfile           # Container build
├── .devcontainer/       # Dev container setup
├── .specify/            # Spec-driven development templates
├── specs/
│   └── travel_planner_core/   # spec.md, plan.md, tasks.md
├── .gitlab-ci.yml       # CI pipeline
├── .pre-commit-config.yaml
├── .env.example         # Example environment variables
├── AGENTS.md            # AI agent / architecture notes
├── USER_MANUAL.md       # End-user guide
├── SECURITY.md          # Security policy
├── CONTRIBUTING.md      # Contribution guide
├── CHANGELOG.md
└── LICENSE              # AGPL-3.0
```

---

## 🔒 Security & Privacy

- Your API key is entered at runtime through a password field and is never committed to the repository.
- Only the text of your prompt is sent to the Gemini API.
- Static analysis (Bandit, Semgrep) runs in CI. See [SECURITY.md](SECURITY.md) for how to report a vulnerability.

---

## 🛣️ Roadmap

- [ ] Persist community journal entries in a database
- [ ] Load destination data from JSON or an API instead of hardcoding it
- [ ] Live currency exchange rates
- [ ] Keep chat history and stream AI responses
- [ ] Pass budget, trip length and selected language into the AI prompt
- [ ] Make CI checks blocking and add mocked tests for the Gemini gateway
- [ ] More destinations and languages

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md) first, then:

1. Fork the repo and create a feature branch
2. Make your changes with tests
3. Run `pre-commit run --all-files`
4. Open a pull request

---

## 📖 Documentation

See the [User Manual](USER_MANUAL.md) for a walkthrough of every feature.

## 📄 License

Distributed under the **AGPL-3.0** license. See [LICENSE](LICENSE) for details.

## 👤 Author

**Pocharam Jayanth**, [@pocharamjayanth](https://github.com/pocharamjayanth)

---

<p align="center">Made with ❤️ for travelers everywhere ✈️</p>
