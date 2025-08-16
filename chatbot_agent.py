import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain.tools import tool
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

load_dotenv()

# Setup LLM
llm = ChatOpenAI(model_name="gpt-4", temperature=0)

# Memory for ongoing conversation
memory = ConversationBufferMemory(memory_key="history", return_messages=True)

# Tool: Scrape data from I&M Bank website
@tool
def get_bank_info() -> str:
    """Scrapes key data from I&M Bank homepage."""
    url = "https://www.imbankgroup.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headings = [h.text.strip() for h in soup.find_all(['h1', 'h2'])[:5]]
    return "Top headings from I&M Bank: " + ", ".join(headings)

# LangChain RunnableWithMessageHistory setup
conversation = RunnableWithMessageHistory(
    runnable=llm,
    get_session_history=lambda session_id: memory,
)
