# AI Web Scraper with LLM Integration

## Overview

AI Web Scraper is an intelligent Python-based tool that leverages web scraping, natural language processing, and AI capabilities to extract and format information from websites according to user-defined instructions. The project integrates Selenium for scraping website content and supports **both a locally hosted LLM (Ollama) and OpenAI API (GPT-4 Turbo)** for structuring the extracted data.

---

## Features

- **Web Scraping:** Automates the retrieval of webpage content using Selenium and BeautifulSoup.
- **Data Cleaning:** Strips away unnecessary HTML elements (e.g., scripts, styles) and formats the content for readability.
- **AI-Powered Structuring:** Uses either **Ollama (local)** or **OpenAI API (GPT-4 Turbo)** to transform and structure the scraped content.
- **Web-Based Interface:** Users interact with the scraper via a **React frontend** instead of the terminal.

---

## How It Works

1. **Enter Website URL & Instructions:** Users input a URL and specify how the extracted content should be formatted.
2. **Choose AI Model:** Select either **Ollama (local processing)** or **OpenAI API (GPT-4 Turbo)**.
3. **Scrape & Clean Content:** The tool retrieves and cleans website content.
4. **Process with AI:** The cleaned content is passed to the selected AI model for structuring.
5. **Display the Output:** The formatted content appears in the web UI.

---

## File Structure

- `ai.py`: Handles interactions with **Ollama** and **OpenAI API** for content processing.
- `app.py`: **Flask API** that manages scraping requests and AI model selection.
- `scrapper.py`: Implements web scraping functionality using Selenium and BeautifulSoup.
- `ai-web-scraper/`: React-based user interface for interacting with the scraper.

---

## Installation

### **Prerequisites**

- Python 3.x
- Node.js & npm (for frontend)
- Google Chrome browser
- ChromeDriver.exe
- Locally hosted **Ollama** or an **OpenAI API key**

### **1. Clone the Repository**

```bash
git clone <repository_url>
cd <repository_directory>
```

### **2. Backend Setup (Flask API)**

```bash
pip install -r requirements.txt
python app.py
```

(Default runs on `http://127.0.0.1:5000`)

### **3. Frontend Setup (React)**

```bash
cd ai-web-scraper  # Move into React directory
npm install
npm start
```

(Default runs on `http://localhost:3000`)

---

## Configuration

### **OpenAI API Key (Required for OpenAI Processing)**

1. Get an API key from OpenAI: [https://platform.openai.com/signup/](https://platform.openai.com/signup/)
2. Add it to your environment variables:
   ```bash
   export OPENAI_API_KEY="your-key-here"  # macOS/Linux
   set OPENAI_API_KEY="your-key-here"  # Windows
   ```

### **Running Ollama Locally**

If using Ollama, install and run the server:

```bash
ollama pull llama3  # or mistral
ollama run
```

---

## Technologies Used

### **Backend (Flask API - **``**)**

- Handles scraping requests and AI model selection
- Routes web UI requests to AI processors

### **Frontend (React - **``**)**

- Provides a UI for input (URL, instructions, AI selection)
- Sends requests to Flask backend
- Displays AI-processed output

### **Web Scraping (**``**)**

- Uses **Selenium** to load and extract webpage content
- Cleans unnecessary HTML elements using **BeautifulSoup**
- **Automatically manages ChromeDriver**

### **AI Processing (**``**)**

- Formats scraped content using AI
- Supports:
  - **Ollama (Llama3, Mistral) via **``
  - **OpenAI GPT-4 Turbo via API**

---

## Future Improvements

- 🚀 Enable File Export (CSV, JSON, PDF)
- 🚀 Improve UI Design & Add Loading Indicators
- 🚀 Deploy the App Online (Render/Vercel)

---

## Contributors

- **Louis Stalet** - Creator
- Contributions Welcome!

---

## License

MIT License © 2025 AI Web Scraper Project

