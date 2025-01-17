# BotPenguin Chatbot Project
### This is a chatbot that answer user's queries regarding BotPenguin. The chatbot uses Retrieval-Augmented Generation (RAG) to answer user queries based on the BotPenguin Help Center documentation.

## Project Overview
The goal of this project was to create a chatbot that provides accurate, conversational responses to user queries by leveraging the documentation available on the BotPenguin website. The chatbot uses modern web scraping techniques, embedding generation, and RAG architecture to deliver meaningful responses.

## Features
**Web Scraping:** Extracts content from the BotPenguin Help Center documentation.
**RAG Architecture:** Combines retrieval-based and generative models to deliver accurate and context-aware responses.
**Semantic Search:** Uses ChromaDB to store embeddings for efficient similarity searches.
**State-of-the-Art LLM:** Built on Llama-3.3 from Groq for conversational AI.
**Conversational Responses:** Friendly and easy-to-understand chatbot responses, tailored for non-technical users.

## Technologies Used
**Programming Language:** Python
**Web Scraping:** BeautifulSoup
**Embeddings:** HuggingFace (all-MiniLM-L6-v2)
**Database:** ChromaDB
**LLM Integration:** Llama-3.3 model via Groq
**Environment Management:** Python virtual environment

# Setup Instructions
**1. Clone the Repository**
```bash
git clone https://github.com/pineaplonpizza/ChatBot-for-BotPenguin.git
cd ChatBot-for-BotPenguin
```

**2. Create and Activate Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # For Linux/macOS
env\Scripts\activate     # For Windows
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Run Web Scraper**
<p>To extract the BotPenguin Help Center data, run:</p>

```bash
python web_scraper.py
```
<p>This will save the scraped data in scraped_content.txt.</p>

**5. Covert the .txt file to pdf**

**6. Generate Embeddings and Save to ChromaDB**
<p>To create and persist embeddings:</p>

```bash
python generate_embeddings.py
```

**7. Start the Chatbot**
<p>Launch the chatbot interface using:</p>

```bash
python chatbot_rag.py
```

## Code Structure
**web_scraper.py:** Extracts data from the BotPenguin Help Center website.
**generate_embeddings.py:** Creates embeddings from the scraped content and stores them in ChromaDB.
**chatbot_rag.py:** Implements the RAG system to generate answers using Llama-3.3.
**scraped_content.pdf:** Contains the raw data extracted from the website.

## Sample Output
Query: _Can we migrate all message templates created on other platforms?_

Response:
_You can indeed migrate all the message templates that were created on other platforms to the BotPenguin platform, which is a great feature that allows you to bring over your existing templates and use them with your WhatsApp bot, making the transition process much smoother and more convenient for you._
