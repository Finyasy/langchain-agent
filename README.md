# Teams Chatbot LangChain

This project is a FastAPI-based chatbot agent using LangChain, OpenAI, and web scraping tools. It is containerized with Docker and includes linting/formatting via Ruff.

## Features
- Chatbot powered by GPT-4 (OpenAI)
- Web scraping tool for I&M Bank homepage
- Conversation memory
- REST API endpoint for messages
- Docker support
- Ruff linter/formatter configuration

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run locally:
   ```bash
   uvicorn main:app --reload
   ```
3. Build and run with Docker:
   ```bash
   docker build -t teams-chatbot .
   docker run -p 8000:8000 teams-chatbot
   ```
4. Interact with the API at `/api/messages`.

## Linting & Formatting
- Run Ruff linter:
  ```bash
  ruff check .
  ```
- Auto-fix issues:
  ```bash
  ruff check . --fix
  ```

## Environment Variables
- Store your OpenAI API key in a `.env` file:
  ```env
  OPENAI_API_KEY=your-key-here
  ```

## License
MIT