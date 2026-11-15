import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv(")


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=api_key,
    temperature=1
)

prompt = """
Suggest exactly 5 healthy breakfast ideas


Requirements:
- Use numbered list from 1 to 5.
- Write one line for each idea.
- No preamble.
- No introduction.
- No conclusion.
- Include traditional healthy breakfast dishes.
"""

# Step 6: Invoke the model
response = llm.invoke(prompt)

# Step 7: Print only the text of the reply
print(response.content)