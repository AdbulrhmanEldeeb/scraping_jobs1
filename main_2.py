from langchain_openai import ChatOpenAI
from browser_use import Agent
from pydantic import SecretStr
from dotenv import load_dotenv
import os 
import asyncio
load_dotenv()
api_key=os.getenv("DEEPSEEK_API_KEY")
# Initialize the model
llm=ChatOpenAI(base_url='https://api.deepseek.com/v1', model='deepseek-chat', api_key=SecretStr(api_key))

# Create agent with the model
async def main():
    agent = Agent(
        task="what is today date?",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())