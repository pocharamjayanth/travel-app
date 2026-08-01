🌍 Travel App

A full-stack travel planning application built with a complete CI/CD pipeline and DevOps tooling for automated build, test, and deployment.

<p align="left"> <img src="https://img.shields.io/badge/build-passing-brightgreen?style=flat-square" /> <img src="https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" /> <img src="https://img.shields.io/badge/Docker-enabled-2496ED?style=flat-square&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" /> </p> <!-- 📸 Add a screenshot or GIF of the app here — this is the single highest-impact addition you can make. ![App Screenshot](docs/screenshot.png) -->
✨ Overview

Travel App helps users plan trips end-to-end — from discovering destinations to organizing itineraries. Beyond the app itself, this project is a demonstration of a production-style delivery pipeline: every push is automatically built, tested, and deployed with zero manual steps.

<!-- Rewrite this paragraph with the 2-3 real core features, e.g.: - Destination search & recommendations - Itinerary builder with day-by-day planning - User authentication & saved trips -->
🏗️ Architecture
[Add a simple diagram or bullet list of your architecture, e.g.:]

Client (React) → API (Node/Express) → Database (MongoDB/PostgreSQL)
                       ↓
              GitHub Actions CI/CD
                       ↓
              Docker → Deployment (Render/Vercel/AWS)
⚙️ CI/CD Pipeline

This project uses GitHub Actions to automate the software delivery lifecycle:

Stage	What happens
Lint & Test	Runs automatically on every pull request
Build	Application and Docker image are built
Deploy	Successful builds on main deploy automatically
<!-- Point to the actual workflow file, e.g.: See `.github/workflows/deploy.yml` for the full pipeline definition. -->
🛠️ Tech Stack
<!-- Fill in with your actual stack -->
Frontend: React / JavaScript
Backend: Node.js / Express
Database: MongoDB / PostgreSQL
DevOps: Docker, GitHub Actions
🚀 Getting Started
bash
# Clone the repository
git clone https://github.com/pocharamjayanth/travel-app.git
cd travel-app

# Install dependencies
npm install

# Run locally
npm start
Environment Variables

Create a .env file with:

DATABASE_URL=
API_KEY=
🧪 Running Tests
bash
npm test
📄 License

This project is licensed under the MIT License — see the LICENSE file for details.

👤 Author

Jayanth Pocharam GitHub · LinkedIn · jayanthpocharam@gmail.com
