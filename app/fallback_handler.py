# fallback_handler.py

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage

# Initialize the fallback LLM
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Template for fallback clarification
clarification_template = ChatPromptTemplate.from_template(
    """
    The user asked: "{original_query}"
    But the system could not find a good answer.
    Please ask a clarifying question or rephrase the query to better understand their intent.
    Respond in the same language as the original input.
    """
)

def handle_fallback(original_query: str) -> str:
    prompt = clarification_template.format_messages(original_query=original_query)
    response = llm(prompt)
    return response.content


if __name__ == "__main__":
    user_input = input("❌ Fallback triggered. Enter user's original query: ")
    clarification = handle_fallback(user_input)
    print("🔄 Suggested clarification:")
    print(clarification)

