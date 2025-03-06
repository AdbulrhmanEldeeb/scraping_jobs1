from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from browser_use import Agent
import asyncio


# Load environment variables
load_dotenv()

# Get API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Define the model (Ensure Config.LANGUAGE_MODEL_NAME is defined or replace it with a string)
llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name="llama-3.1-8b-instant")  # Replace with actual model name if needed

# Define prompt
prompt = ChatPromptTemplate.from_template("Hello, how are you?")

# Generate response
# response = llm.invoke(prompt.format())

# Print response
# print(response.content)

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
