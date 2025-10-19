import streamlit as st
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.output_parsers import StrOutputParser


# --- 1. RAG Setup Function (Cached) ---
@st.cache_resource(show_spinner="Initializing Finance Assistant...")
def setup_rag_chain():
    """Initializes and returns the complete RAG chain."""
    
    # 1. API Key Setup
    try:
        os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
    except KeyError:
        st.error("⚠️ GOOGLE_API_KEY not found in secrets. Please add it to .streamlit/secrets.toml")
        st.stop()
    
    # 2. Sample Data (Replace with your actual file loading logic)
    FINANCE_DATA = """
    Asset: Any resource owned by a business or economic entity. Assets are things of value that a company owns to operate its business. Examples include cash, accounts receivable, inventory, and property.
    Liability: A company's legal financial debts or obligations that arise during the course of business operations. Liabilities are settled over time through the transfer of economic benefits. Examples include accounts payable, debts, and loans.
    Equity: The value of ownership in a business or property. It is calculated by taking the total value of assets and subtracting the total value of liabilities (Assets - Liabilities = Equity).
    Bonds: A fixed-income investment in which an investor loans money to an entity (typically corporate or governmental) for a defined period at a variable or fixed interest rate.
    Inflation: A general rise in the price level of an economy over a period of time, leading to a decline in the purchasing power of money.
    Diversification: A risk management strategy that mixes a wide variety of investments within a portfolio. The rationale is that a portfolio constructed of different kinds of assets will yield higher returns and pose a lower risk than any individual investment found within the portfolio.
    Portfolio: A collection of financial investments like stocks, bonds, commodities, cash, and cash equivalents, including mutual funds and ETFs.
    Bull Market: A market condition in which prices are rising or are expected to rise. Typically characterized by optimism and investor confidence.
    Bear Market: A market condition in which prices are falling, typically by 20% or more from recent highs, usually accompanied by pessimism and negative investor sentiment.
    Dividend: A distribution of a portion of a company's earnings to its shareholders, usually paid quarterly.
    Capital Gains: The profit earned from selling an asset for more than its purchase price.
    """
    
    # 3. Text Processing
    splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=70)
    chunks = splitter.split_text(FINANCE_DATA)
    
    # 4. Embeddings and Vector Store
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    db = Chroma.from_texts(
        texts=chunks, 
        embedding=embeddings,
        collection_name="finance_rag_gemini_collection"
    )
    retriever = db.as_retriever(search_kwargs={"k": 5}) 
    
    # 5. LLM and Prompt Definition
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0.3) 
    
    RAG_PROMPT_TEMPLATE = """You are a friendly and expert financial assistant and welcoming users with humor also who explains banking terms in very simple English.
Use the following context to accurately answer the user's question and give one real-life example when possible. If the answer is not found in the context,
 always try to define the term if you can. 


CONTEXT:
{context}

QUESTION:
{question}

ANSWER:"""
    
    rag_prompt = ChatPromptTemplate.from_template(RAG_PROMPT_TEMPLATE)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # 6. RAG Chain Construction
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | rag_prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain


# --- 2. Streamlit Interface Logic ---

st.set_page_config(
    page_title="Finance Chatbot",
    page_icon="💰",
    layout="wide"
)

# Header
st.title("💰 Finance Assistant")
st.markdown("Ask any question about finance terms like *Equity, Bonds, Inflation*.")

# Sidebar with info
with st.sidebar:
    st.header("About")
    st.markdown("""
    This chatbot uses:
    - **Google Gemini** for AI responses
    - **RAG** (Retrieval Augmented Generation)
    - **LangChain** for orchestration
    
    It can answer questions about financial concepts based on its knowledge base.
    """)
    
    st.divider()
    
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    st.caption("Powered by Gemini & LangChain")

# Initialize RAG chain only once using caching
try:
    rag_chain = setup_rag_chain()
except Exception as e:
    st.error(f"Failed to initialize RAG system: {e}")
    st.stop()

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask a finance question..."):
    
    # 1. Display user message in chat container
    st.chat_message("user").markdown(prompt)
    
    # 2. Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 3. Get assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Invoke the RAG chain with the user's question
                full_response = rag_chain.invoke(prompt)
                st.markdown(full_response)
                
                # 4. Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": full_response})

            except Exception as e:
                error_message = f"❌ An error occurred: {str(e)}"
                st.error(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})