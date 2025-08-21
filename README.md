Jarvina: The Personal AI Assistant
Jarvina is a personal AI assistant built with a modern web stack, providing a clean, responsive chat interface powered by the Gemini AI model. This project serves as a robust template for developing AI-driven applications with a focus on real-time conversational experiences, dynamic data handling, and structured outputs.

Features
Conversational AI: Integrates with the Gemini AI model via a dedicated Python client for natural, multi-turn chat.

Structured Responses: The backend is configured to prompt the AI for structured JSON output, which the frontend parses and displays in a clean, organized format.

Responsive Web Interface: A modern, visually appealing UI built with HTML, CSS, and JavaScript. The layout is fully responsive, ensuring a consistent user experience on both desktop and mobile devices.

Customizable Persona: A memory.json file allows for easy configuration of the AI's persona, including its name, tone, and specific rules.

Custom Instructions: Users can provide their own custom instructions through a dedicated settings page, which are then included in the system prompt for a personalized experience.

Persistent Chat History: Chat conversations are saved to local storage, allowing users to leave and return to their session without losing their conversation.

Local Environment Setup: The project is configured to read API keys from a .env file, promoting secure development practices by keeping sensitive information out of the codebase.

Tech Stack
Backend:

FastAPI: A high-performance, easy-to-use web framework for building the API endpoints.

Uvicorn: The ASGI server used to run the FastAPI application.

google-generativeai: The official Python client library for interacting with the Gemini API.

python-dotenv: Manages environment variables for secure API key handling.

Frontend:

HTML, CSS, JavaScript: The core technologies for the user interface and client-side logic.

Tailwind CSS: A utility-first CSS framework for rapid and responsive styling.

Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites
Python 3.8+

pip (Python package installer)

Installation
Clone the repository:

git clone https://github.com/your-username/jarvina-ai-assistant.git
cd jarvina-ai-assistant

Create and activate a Python virtual environment:

python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS or Linux
source venv/bin/activate

Install the required Python packages:

pip install -r requirements.txt

If you don't have a requirements.txt file, you can manually install the dependencies:

pip install fastapi uvicorn python-dotenv pydantic google-generativeai jinja2

Set up your Gemini API key:

Obtain a Gemini API key from the Google AI Studio.

Create a file named .env in the root of your project.

Add your API key to the file in the following format:

GEMINI_API_KEY="YOUR_API_KEY_HERE"

Running the Application
Start the FastAPI server using Uvicorn:

uvicorn app:app --reload

The --reload flag is useful for development, as it automatically restarts the server when code changes are detected.

Open your web browser and navigate to http://127.0.0.1:8000.

You should see the "Jarvina AI Assistant" chat interface. You can now start a new chat, and the AI will respond with a structured output.

Project Structure
jarvina-ai-assistant/
├── app.py              # Main FastAPI application file
├── llm_client.py       # Python client for interacting with the Gemini API
├── index.html          # Frontend web page for the chat interface
├── requirements.txt    # List of project dependencies
├── .env                # Environment variables (e.g., API keys)
└── memory.json         # Stores persona data and custom replies

Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.
