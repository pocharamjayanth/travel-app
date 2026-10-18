# 🌍 Global Travel Planner

A Python-based travel planning application that brings destination discovery, AI-assisted itinerary suggestions, budget estimation, and trip preparation into one simple interface.

## About the Project

Planning a trip often means switching between different websites to explore destinations, research local food, estimate expenses, and organize travel essentials. We built **Global Travel Planner** to bring these basic planning activities together in one place.

The application combines Python and Streamlit with Google's Gemini API to provide an interactive travel-planning experience. Users can explore selected destinations, generate AI-assisted travel suggestions, estimate accommodation and food expenses, and prepare for their trip using a packing checklist.

We also wanted the application to be accessible to users with different language preferences, so we included support for English, Hindi, Telugu, and Spanish.

This project gave our team an opportunity to work with Python application development, API integration, user interaction, and software quality practices while solving a practical problem.

## ✨ Features

### 📍 Destination Discovery
- Explore a selection of popular Indian and international destinations.
- View destination-specific attractions and local food suggestions.
- Check general seasonal travel guidance.

### 🤖 AI-Assisted Travel Planning
- Generate travel suggestions using Google's Gemini API.
- Ask travel-related questions based on the selected destination.
- Receive AI-generated itinerary ideas and preparation suggestions.
- Provide your own Gemini API key through the application's password-masked input.

### 💰 Travel Budget Estimator
- Select the number of travel days.
- Enter the estimated hotel cost per night.
- Set a daily budget for food and activities.
- View calculated accommodation costs, food and activity expenses, and the estimated total.
- Switch between budget-friendly and premium travel preferences.

### 🎒 Packing Checklist
- Keep track of important travel essentials.
- Mark documents, tickets, chargers, clothing, medicines, and toiletries as ready.
- Receive a completion animation when all checklist items are selected.

### 🌐 Multilingual Interface
The application supports four interface languages:
- English
- Hindi
- Telugu
- Spanish

### 📝 Travel Notes
- Write a short travel tip or note.
- Display the submitted note in the application interface.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic, calculations, and feature implementation |
| Streamlit | Interactive web interface |
| Google Gemini API | AI-generated travel suggestions |
| Google Gen AI SDK | Communication with the Gemini model |
| Requests | HTTP library included in the project dependencies |
| Git and GitHub | Source control and project management |
| Docker | Containerization support |
| GitLab CI | Automated development-quality checks and testing workflow |
| Pytest | Automated testing |
| Ruff, Pylint, Flake8, and Mypy | Code quality, formatting, and type checking |
| Bandit and Semgrep | Static security analysis |

## ⚙️ How It Works

The application follows a straightforward workflow:

1. The user selects a destination, travel style, preferred currency, and interface language.
2. The application displays available destination information, attractions, local food suggestions, and general seasonal guidance.
3. When the user requests AI assistance, the application sends the entered prompt to the Gemini API using the Google Gen AI SDK.
4. The returned AI-generated response is displayed in the interface.
5. The budget estimator calculates accommodation and daily food/activity expenses based on the user's inputs.
6. The packing checklist helps the user track essential items before departure.

Destination information and budget calculations are handled by the application's Python code. AI-generated suggestions are obtained through the external Gemini service.

## 🧮 Budget Calculation

The budget estimator uses the following calculations:

**Accommodation Cost**

`Accommodation Cost = Hotel Cost Per Night × Number of Days`

**Food and Activity Cost**

`Food and Activity Cost = Daily Expenses × Number of Days`

**Estimated Total**

`Estimated Total = Accommodation Cost + Food and Activity Cost`

For example, consider a three-day trip with an estimated hotel cost of ₹1,500 per night and daily food/activity expenses of ₹1,000.

- Accommodation: ₹1,500 × 3 = ₹4,500
- Food and activities: ₹1,000 × 3 = ₹3,000
- **Estimated total: ₹7,500**

These values are estimates based on user inputs, not live hotel prices or booking quotations.

## 🚀 Getting Started

Follow these steps to run the project locally.

### Prerequisites

Make sure you have the following installed:

- Python 3.10 or a compatible version supported by the dependencies
- pip
- Git

A Google Gemini API key is required to use the AI travel assistant. The other application features can be explored without an API key.

### 1. Clone the Repository

```bash
git clone https://github.com/pocharamjayanth/travel-app.git
cd travel-app
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Obtain a Gemini API Key

Create an API key through [Google AI Studio](https://aistudio.google.com/app/apikey).

Keep your key private. Do not commit it to the repository or include it in screenshots, public logs, or source code.

### 5. Run the Application

```bash
streamlit run app.py
```

Streamlit will display a local URL, usually:

`http://localhost:8501`

Open that URL in your browser to use the application.

### 6. Generate AI Travel Suggestions

1. Select a destination.
2. Open the AI travel assistant section.
3. Enter your Gemini API key in the configuration sidebar.
4. Enter a travel-related prompt.
5. Select the button to generate AI insights.

The AI feature requires internet connectivity and a valid API key with access to the configured Gemini model.

## 🧪 Testing and Code Quality

The repository includes automated tests and a CI configuration intended to support maintainable development.

The existing test suite covers aspects of the language configuration and translation data. The configured pipeline includes checks for:

- Code formatting and linting
- Static type analysis
- Security analysis
- Automated tests
- Test coverage reporting

These tools help identify potential issues during development. Their effectiveness depends on the configured rules, test coverage, and pipeline failure conditions.

To run the tests locally, use:

```bash
pytest
```

To run the application with Docker, use the repository's `Dockerfile` and follow the configuration provided in the project files. The Docker image should be built and tested before being used for deployment.

## 🔐 Security Considerations

- The Gemini API key is entered through a password-masked input.
- Do not hardcode API credentials in the source code.
- Avoid committing `.env` files or other files containing secrets.
- Use environment-based configuration or a managed secrets service when adapting the application for deployment.
- Validate user inputs and review security-scanner findings regularly.

A password-masked input improves on-screen privacy but does not replace secure credential management.

## ⚠️ Current Scope and Limitations

The project focuses on travel guidance and trip preparation. Some features are intentionally simple:

- Destination information and seasonal guidance are predefined in the application.
- Budget estimates use values supplied by the user.
- Currency selection changes the displayed currency using a fixed conversion factor; it does not retrieve live exchange rates.
- The travel notes feature displays a submitted note but does not provide persistent community storage.
- The application does not currently implement hotel or flight bookings, payment processing, or live weather retrieval.
- AI-generated suggestions may be inaccurate and should be verified before making travel decisions.

## 🔮 Future Improvements

We would like to extend the application with:

- Live weather and destination information from external APIs.
- Interactive maps and route suggestions.
- User authentication and persistent storage for saved itineraries.
- More personalized travel plans based on budget, duration, and interests.
- Live currency conversion.
- Automated tests for budget calculations, invalid inputs, and AI API failures.
- Improved API error handling, caching, and secure deployment configuration.

These improvements would help make the application more reliable and useful for a wider range of travellers.

## 👥 Team Members

This project was developed as a team effort by:

- **Jayanth Pocharam**
- **Krishna**
- **Gargeya**
- **Srujan**
- **Nithin**

The team worked on the travel-planning application and its supporting functionality. For a detailed account of each member's contributions, please refer to the work completed and changes made by each person.

## 📚 Learning Outcomes

Through this project, we gained practical experience in:

- Building interactive web applications with Python and Streamlit.
- Integrating an external generative AI API.
- Working with user inputs, calculations, and conditional application logic.
- Organizing multilingual interface text.
- Handling API errors and configuration requirements.
- Using Git, automated testing, static analysis, and CI tooling.
- Identifying the difference between a functional prototype and a production-ready application.

## 📄 License

This repository includes a `LICENSE` file. Please refer to that file for the applicable licensing terms.

---

**Global Travel Planner** is a learning-oriented team project focused on making everyday travel planning more convenient through a simple web interface and AI-assisted suggestions.

Contributions, suggestions, and constructive feedback are welcome.
