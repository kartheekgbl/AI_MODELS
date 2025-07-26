from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent,MCPClient
import asyncio
import os



async def Calender_CreateEvent():
    load_dotenv()

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    config_file="Calender_MCP.json"

    print("Initializing chat...")

    client=MCPClient.from_config_file(config_file)
    llm=ChatGroq(model_name="qwen/qwen3-32b")
    agent=MCPAgent(llm=llm,client=client,max_steps=15,memory_enabled=True)

    print("\n===== Interactive MCP Chat =====\n")

    print("type 'exit' to quit the chat.\n")
    print("type 'clear' to clear the chat history.\n")

    try:
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting chat. Goodbye!")
                break
            elif user_input.lower() == 'clear':
                agent.clear_history()
                print("Chat history cleared.")
                continue
            print("\assistant: ", end="",flush=True)
            response = await agent.ainvoke({"messages": [{"role": "user", "content": user_input}]})
            print(f"Bot: {response['messages'][-1]['content']}")
            try:
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                print(f"\nError: {e}")
    finally:
        if client and client.sessions:
            await client.close_all_sessions()


if __name__ == "__main__":
    asyncio.run(Calender_CreateEvent())