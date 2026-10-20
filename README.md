# 🗺️ Global Travel Planner

> A multilingual city travel guide and trip planner with an AI assistant that runs **fully offline** on a local model or in the **cloud** with your own API key.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Local%20AI-Ollama-black)
![License](https://img.shields.io/badge/License-AGPL--3.0-green)

Plan a trip in one place: explore a destination, estimate your budget, pack smart, and ask an AI companion for a custom itinerary, in **English, Hindi, Telugu or Spanish**.

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
| 🤖 **AI travel assistant** | Generates itineraries and travel tips for your chosen city and style |

**Supported destinations:** Hyderabad · Goa · Delhi · Mumbai · Jaipur · Kerala · Paris · Tokyo · London · New York

---

## 🤖 AI Engine

The assistant uses a single gateway that talks to any OpenAI-compatible chat endpoint, so you can choose how it runs:

| Mode | Model | Best for |
|---|---|---|
| 🎒 **Local Inference (Ollama)** | `llama3` by default (configurable) | Free, private, works offline |
| ✨ **Cloud API (BYOK, OpenAI)** | `gpt-4o-mini` | Faster responses without local hardware |

- **Bring Your Own Key:** your OpenAI key is entered in a password field and is never hardcoded or stored.
- **Resilient:** 30-second timeout and clear messages for a missing key, API errors, an unreachable Ollama server, and network failures.

---

## 🏗️ Architecture

```
┌──────────────────────────── Streamlit App (app.py) ────────────────────────────┐
│                                                                                │
│  Sidebar ──► Language · Travel style · Currency · AI mode                      │
│                                                                                │
│  Main page ─► Destination guide ─► Budget estimator ─► Packing ─► Journal      │
│                      │                                                         │
│                      ▼                                                         │
│            query_ai_engine()  (unified AI gateway)                             │
│              │                          │                                      │
│              ▼                          ▼                                      │
│     Ollama (localhost:11434)     OpenAI API (BYOK)                             │
└────────────────────────────────────────────────────────────────────────────────┘
```

There is no separate backend or database: the Python code in `app.py` handles localization, content, budget logic and AI requests, and state lives in the Streamlit session.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- *(Optional, for local AI)* [Ollama](https://ollama.com) installed and running

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

Then open the URL shown in your terminal (usually `http://localhost:8501`).

### Set up the AI assistant

**Option A: Local (Ollama)**
```bash
ollama pull llama3
ollama serve        # if it isn't already running
```
In the sidebar, choose **Local Inference (Ollama)**. The defaults (`http://localhost:11434`, `llama3`) work out of the box.

**Option B: Cloud (OpenAI)**
In the sidebar, choose **Cloud API (BYOK - OpenAI)** and paste your API key.

### Run with Docker

```bash
docker build -t travel-app .
docker run -p 8501:8501 travel-app
```

> When running inside Docker, point the Ollama URL in the sidebar at your host (for example `http://host.docker.internal:11434`).

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
├── app.py               # Streamlit app: UI, translations, budget logic, AI gateway
├── test_app.py          # Unit tests (localization checks)
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Project and tooling configuration
├── Dockerfile           # Container build
├── .devcontainer/       # Dev container setup
├── .gitlab-ci.yml       # CI pipeline
├── .pre-commit-config.yaml
├── .env.example         # Example environment variables
├── specs/               # Project specifications
├── USER_MANUAL.md       # End-user guide
├── SECURITY.md          # Security policy
├── CONTRIBUTING.md      # Contribution guide
├── CHANGELOG.md
└── LICENSE              # AGPL-3.0
```

---

## 🔒 Security & Privacy

- API keys are entered at runtime through a password field and are never committed to the repository.
- Local mode keeps your prompts on your own machine.
- Static analysis (Bandit, Semgrep) runs in CI. See [SECURITY.md](SECURITY.md) for how to report a vulnerability.

---

## 🛣️ Roadmap

- [ ] Persist community journal entries in a database
- [ ] Load destination data from JSON or an API instead of hardcoding it
- [ ] Live currency exchange rates
- [ ] Stream AI responses and keep chat history
- [ ] Pass budget, trip length and selected language into the AI prompt
- [ ] Make CI checks blocking and add mocked tests for the AI gateway
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
