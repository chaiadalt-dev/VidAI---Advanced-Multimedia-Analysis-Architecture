 # 🎥 VidAI - Advanced Multimedia Analysis Architecture

An intelligent, LLM-powered platform that extracts raw video transcripts and processes them concurrently into structured, actionable insights using multi-provider AI orchestration.

## 🚀 Overview
VidAI is a robust backend architecture designed to handle asynchronous API requests, dynamic media extraction, and complex semantic tasks. The system concurrently routes data through leading AI providers (DeepSeek, Cohere, HuggingFace) to perform dynamic Q&A, FDA-style compliance checks, and structural data parsing.

## 🛠️ Tech Stack & Architecture
* **Backend:** Python, Flask
* **Caching & Queue Management:** Redis (for high-speed data delivery)
* **AI Orchestration:** DeepSeek, Cohere, HuggingFace APIs
* **Resilience:** Built-in error-handling and rate-limit management to handle network timeouts efficiently.

## 🔒 OpSec & Security Note
*This repository demonstrates secure coding practices.* No API keys or sensitive secrets are hardcoded in the source code. To run this project locally, you must provide your own credentials via environment variables:
`export DEEPSEEK_API_KEY="your_api_key_here"`

## 💻 Quick Start
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set your environment variables.
4. Run the server: `python app.py`
