# AkbankBootCamp-FinanceChatbot


<img width="1344" height="450" alt="FinaceNew" src="https://github.com/user-attachments/assets/ca20fe6a-1f01-4792-9311-0a5222a83ba1" />

# 💰 Finance Assistan (RAG) Chatbot

A finance assistant chatbot using Google Gemini AI and RAG (Retrieval Augmented Generation).

## 📋 About This Project

This is an AI-powered finance chatbot that helps you understand financial concepts quickly and easily.

### What does it do?

- **Answers finance questions** using Google's Gemini AI
- **Searches through finance knowledge** to give you accurate answers
- **Explains complex terms** in simple language
- **Remembers your conversation** so you can ask follow-up questions

### How does it work?

1. You ask a question about finance (like "What is equity?" or "Explain bonds")
2. The chatbot searches through its finance knowledge base
3. It finds relevant information and creates a clear answer using AI
4. You get an accurate, easy-to-understand response!

### What topics can you ask about?

- Assets, Liabilities, and Equity
- Bonds and Stocks
- Inflation and Diversification
- Portfolios and Investments
- Bull and Bear Markets
- Dividends and Capital Gains
- And more!

### Technology Used

- **Google Gemini AI** - For intelligent responses
- **RAG (Retrieval Augmented Generation)** - To search and find relevant information
- **LangChain** - To connect everything together
- **Streamlit** - For the web interface

## 🚀 Setup Instructions

### 1. Clone or Download this Repository
```bash
git clone https://github.com/salihbulutt/AkbankBootCamp-FinanceChatbot.git
cd AkbankBootCamp-FinanceChatbot
```

### 2. Install Python Packages
```bash
pip install streamlit langchain langchain-google-genai langchain-community chromadb
```

### 3. Get Your Google API Key
- Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
- Click "Create API Key"
- Copy your key

### 4. Set Up Your Secrets File
1. Go to the `.streamlit` folder
2. Copy `secrets.toml.example` and rename it to `secrets.toml`
3. Open `secrets.toml` and replace `your-google-api-key-here` with your actual API key

**Your `.streamlit` folder should have:**
- ✅ `secrets.toml.example` (this gets uploaded to GitHub)
- ✅ `secrets.toml` (this stays on computer only)

### 5. Run the App
```bash
streamlit run finance_rag_app.py
```
## 🗂️ Project Structure
```
your-project-folder/
├── .gitignore                    ← Tells Git what to ignore
├── .streamlit/
│   └── secrets.toml.example      ← Template
├── finance_rag_app.py            ← Main code
├── README.md                     ← Instructions
└── requirements.txt              ← Package list
```
## ⚠️ Important Notes
- **NEVER** share your `secrets.toml` file!
- The `.gitignore` file prevents `secrets.toml` from being uploaded to GitHub
- Each person needs to create their own `secrets.toml` file with their own API key

## 📦 Required Packages
- streamlit
- langchain
- langchain-google-genai
- langchain-community
- chromadb

## 🎓 Learn More
- [Streamlit Documentation](https://docs.streamlit.io)
- [LangChain Documentation](https://python.langchain.com)
- [Google Gemini AI](https://ai.google.dev)
```
