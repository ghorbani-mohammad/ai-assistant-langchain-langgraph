from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")
# Use ChatPromptTemplate instead of PromptTemplate
prompt = ChatPromptTemplate.from_template("Translate to French: {text}")
# Create a chain using the modern syntax
chain = prompt | llm

# Run the chain
result = chain.invoke({"text": "Hello, world!"})
print(result.content)
