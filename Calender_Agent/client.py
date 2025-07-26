from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
# from groq import Groq
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()
import asyncio
import os
# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))
async def main():

    print("Client is starting...")
    connections={
        "math": {
            "command": "python",
            "args": ["mathserver.py"],  # Ensure correct absolute path to mathserver.py
            "transport": "stdio",
        },
        "calendar": {
            "url": "http://localhost:8000/mcp",  # Ensure the calender server is running on this URL
            "transport": "streamable_http",  # Corrected spelling from 'streamable-http' to 'streamable_http'
        }

        # Uncomment and configure the weather server if needed
        # "weather": {
        #     "url": "http://localhost:8000/mcp",  # Ensure the weather server is running on this URL
        #     "transport": "streamable_http",       # Check spelling if needed
        # }
    }
    print(connections)
    client = MultiServerMCPClient(connections)
    tools = await client.get_tools()
    # print("Tools fetched:", tools)
    
    model= ChatGroq(model_name="qwen/qwen3-32b")
    agent =create_react_agent(model,tools)
    try: 
        while True:
            userinput=input("Me:")
            if userinput.lower() in ['exit', 'quit']:
                print("Exiting chat. Goodbye!")
                break
            # elif userinput.lower() == 'clear':
            #     agent.clear_history()
            #     print("Chat history cleared.")
                # continue
            data = await agent.ainvoke({"messages": [{"role": "user", "content":userinput}]})
            #print("Response:", data['messages'][-1]['content'])
            print("Response:", data['messages'][-1].content)
    finally:
        # if client and client.sessions:
        #     await client.close_all_sessions()
        print("Closing sessions...")

    # print(response)
    # print(type(response))
asyncio.run(main())
# async def main():
#     agent= await call_agent()
# if __name__ == "__main__":
#     # Run the main function to execute the agent
#     print("Starting agent...")
    