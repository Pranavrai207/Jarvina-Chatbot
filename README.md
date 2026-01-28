Jarvina: The AI-Powered Personal Assistant Platform

Jarvina is an AI-powered personal assistant built with a modern full-stack web architecture, providing a clean and responsive chat interface powered by the Gemini AI model. The project is designed as an all-rounder template for building AI-driven applications, with a focus on real-time conversational experiences, structured data handling, and business-ready product workflows. Jarvina demonstrates how technical systems can support analytics, customer-facing demos, and scalable SaaS-style applications.

Features

Conversational AI: Integrates with the Gemini AI model via a dedicated Python client to support natural, multi-turn conversations suitable for real-world usage and demonstrations.

Structured Responses: The backend is configured to prompt the AI for structured JSON outputs, enabling reliable data parsing, organized frontend display, and downstream analytical use cases.

Responsive Web Interface: A clean, modern UI built with HTML, CSS, and JavaScript. The interface is fully responsive, ensuring consistent user experience across desktop and mobile devices, making it demo-ready for customer-facing scenarios.

Customizable Persona: A memory.json configuration file allows easy customization of the AI’s persona, including its name, tone, and behavioral rules, supporting flexible product and demo use cases.

Custom Instructions: Users can provide custom instructions through a settings interface, which are dynamically injected into the system prompt to personalize interactions.

Persistent Chat History: Chat conversations are stored locally, allowing users to leave and return without losing session context, reflecting real SaaS-style user experience design.

Secure Environment Setup: API keys and sensitive configuration are managed using a .env file, following secure development and deployment best practices.

Tech Stack

Backend:
FastAPI – High-performance Python framework for building scalable API endpoints
Uvicorn – ASGI server used to run the FastAPI application
google-generativeai – Official Python client for interacting with the Gemini API
python-dotenv – Manages environment variables for secure API key handling

Frontend:
HTML, CSS, JavaScript – Core technologies for the user interface and client-side logic
Tailwind CSS – Utility-first CSS framework for rapid, responsive, and consistent styling

Getting Started

Follow the instructions below to run the project locally.

Prerequisites
Python 3.8+
pip (Python package installer)

Installation

Clone the repository:
git clone https://github.com/Pranavrai207/Jarvina-Chatbot.git

cd Jarvina-Chatbot

Create and activate a Python virtual environment:
python -m venv venv

On Windows:
.\venv\Scripts\activate

On macOS or Linux:
source venv/bin/activate

Install the required Python packages:
pip install -r requirements.txt

If requirements.txt is not available, install dependencies manually:
pip install fastapi uvicorn python-dotenv pydantic google-generativeai jinja2

Set Up Gemini API Key

Obtain a Gemini API key from Google AI Studio.
Create a file named .env in the root directory.
Add your API key in the following format:
GEMINI_API_KEY="YOUR_API_KEY_HERE"

Running the Application

Start the FastAPI server using Uvicorn:
uvicorn app:app --reload

The --reload flag enables automatic server restarts during development.

Open your browser and navigate to:
http://127.0.0.1:8000

You should see the Jarvina AI Assistant chat interface and can begin interacting with the system.

Project Structure

jarvina-ai-assistant/
├── app.py – Main FastAPI application file
├── llm_client.py – Python client for interacting with the Gemini API
├── index.html – Frontend web interface for the chat application
├── requirements.txt – Project dependency definitions
├── .env – Environment variables (API keys, not committed)
└── memory.json – Stores AI persona configuration and rules

Contributing

Contributions are welcome. If you have suggestions, feature ideas, or bug reports, feel free to open an issue or submit a pull request.

License

This project is licensed under the MIT License.
