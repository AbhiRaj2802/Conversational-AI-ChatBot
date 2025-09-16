from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature= 1.0)

chat_history = [
    SystemMessage (content = "You are a helpful AI Asistant")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content = user_input))
    if(user_input == "exit"):
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content = result.content))
    print("Mr.Fixit: ",result.content)

print(chat_history)