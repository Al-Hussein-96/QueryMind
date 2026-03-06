from langchain_community.agent_toolkits import create_sql_agent
from langchain_anthropic import ChatAnthropic
from app.database import get_db
import os

def create_agent():
    llm = ChatAnthropic(
        model="claude-haiku-4-5-20251001",
        api_key=os.getenv("ANTHROPIC_API_KEY"),
        temperature=0
    )

    db = get_db()

    agent = create_sql_agent(
        llm=llm,
        db=db,
        agent_type="zero-shot-react-description",
        verbose=True
    )
    return agent