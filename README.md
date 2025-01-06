# AI Web Scraper
AI Web Scraper is an intelligent Python-based tool that leverages web scraping, natural language processing, and AI capabilities to extract and format information from websites according to user-defined instructions. The project integrates Selenium for scraping website content and a locally hosted LLM for structuring the extracted data.

## Features
- Web Scraping: Automates the retrieval of webpage content using Selenium and BeautifulSoup.
- Data Cleaning: Strips away unnecessary HTML elements (e.g., scripts, styles) and formats the content for readability.
- LLM-Powered Structuring: Uses a locally hosted large language model (LLM) to transform and structure the scraped content based on user-defined instructions.

## How It Works
1. Input the Website: Users specify the URL of the website to scrape.
2. Scraping & Cleaning: The tool retrieves the website's content and removes extraneous data.
3. Formatting with AI: The user provides detailed instructions for how the content should be structured. The system processes the cleaned content with a locally hosted LLM (via HTTP) to generate formatted output.
## File Structure
- ai.py: Handles interactions with the LLM for processing and structuring content.
- main.py: The main script for user interaction and orchestration of the scraping and formatting pipeline.
- scrapper.py: Implements web scraping functionality using Selenium and BeautifulSoup.
## Installation
### Prerequisites
- Python 3.x
- Google Chrome browser
- ChromeDriver (Ensure it's in the specified path in scrapper.py or adjust accordingly)
- Locally hosted LLM (API available at http://localhost:11434)
### Setup
#### 1. Clone the repository:

```bash
git clone <repository_url>
cd <repository_directory>
```
#### 2. Install dependencies:

```bash
pip install selenium beautifulsoup4 requests
```
#### 3. Set up ChromeDriver:
- Download ChromeDriver from https://chromedriver.chromium.org/.
- Replace the path in scrapper.py (Service(...)) with the location of your ChromeDriver.
#### 4. Run a local LLM:

- Ensure an LLM server is running and accessible via http://localhost:11434.
## Usage
#### 1. Run the script:

```bash
python main.py
```
#### 2. Follow prompts:

- Enter the website URL to scrape.
- Provide detailed instructions for formatting the scraped content.
#### 3. Output:

- The cleaned and formatted content will be displayed in the terminal.
## Technologies Used
### Web Scraping:
- Selenium
- BeautifulSoup
### AI Integration:
- Locally hosted LLM API (e.g., Llama3)
### Programming Language:
- Python

## Limitations
- Requires a locally hosted LLM.
- Website structure variability may affect scraping accuracy.
- ChromeDriver path must be configured correctly.
## Future Improvements
- Support for additional browser automation tools.
- Extend compatibility with cloud-based LLMs.
- Add error handling for various website formats.
