import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

gemini_api_key = "AIzaSyDZpyIVi1ZfiBUpvPIIOgL1KGFLK7lX1Uk"

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(disabled=True)

# 👇 Yeh main function async hai
async def main():
    agent = Agent(
        name="Assistant",
        instructions="you are a help full assistance.",  # Sirf haiku me jawaab dega
        model=OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",
            openai_client=client
        ),
    )

    result = await Runner.run(agent, "What is the name of the capital of pakistan?")
    print("Final Output:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
