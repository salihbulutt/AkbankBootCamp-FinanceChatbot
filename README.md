# AkbankBootCamp-FinanceChatbot


<img width="1344" height="450" alt="FinaceNew" src="https://github.com/user-attachments/assets/ca20fe6a-1f01-4792-9311-0a5222a83ba1" />

# 💰 Gemini Finance RAG Chatbot

A finance assistant chatbot using Google Gemini AI and RAG (Retrieval Augmented Generation).

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
- ✅ `secrets.toml` (this stays on YOUR computer only)

### 5. Run the App
```bash
streamlit run finance_rag_app.py
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

3. **Save** the file

---

## 📦 **Step 5: Create requirements.txt**

This lists all the Python packages needed.

### **Action:**

1. In your project folder, create `requirements.txt`
2. Paste this:
```
streamlit
langchain
langchain-google-genai
langchain-community
chromadb
```

3. **Save** the file

---

## 🗂️ **Step 6: Check Your Folder Structure**

Your project should look like this:
```
your-project-folder/
├── .gitignore                    ← Tells Git what to ignore
├── .streamlit/
│   ├── secrets.toml              ← YOUR SECRET (not uploaded)
│   └── secrets.toml.example      ← Template (uploaded)
├── finance_rag_app.py            ← Your main code
├── README.md                     ← Instructions
└── requirements.txt              ← Package list
