import os
from dotenv import load_dotenv
import chainlit as cl
from agents import Agent, AsyncOpenAI, RunConfig, OpenAIChatCompletionsModel, Runner
from tools.crypto_tool import get_crypto_price 

#  Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in your .env file.")

#  Gemini API setup
external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

#  Model setup
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

#  Agent config
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

#  Agent Setup
cryptoAgent: Agent = Agent(
    name="CryptoDataAgent",
    instructions=(
        "You are a strict cryptocurrency assistant. Respond **only** to valid cryptocurrency-related queries. "
        "Accept only valid coin symbols like BTC, ETH, or DOGE. "
        "If the input is a greeting (like hello, hi, salam), politely greet and ask for a crypto query. "
        "If the input is unrelated, confusing, or about anything else — firmly respond with: "
        "`I only provide cryptocurrency price updates. Please share a valid symbol like BTC or ETH.Sorry, I can only help with cryptocurrency-related queries. Please ask about a crypto symbol like BTC, ETH, or DOGE.`"
    ),
    model=model,
    tools=[get_crypto_price]
)


#  On Chat Start
@cl.on_chat_start
async def welcome():
    await cl.Message(
        author="CryptoDataAgent 🪙",
        content="Welcome to the Crypto Market Bot! 👋\n\nAsk me about any cryptocurrency like `BTCUSDT`, `ETHUSDT`, or `DOGEUSDT` 💹"
    ).send()

#  Handle User Input
@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content.strip()

    try:
        loading_msg = cl.Message(author="🤖", content=" Fetching the latest market rate...")
        await loading_msg.send()

        result = await Runner.run(cryptoAgent, input=user_input, run_config=config)
        final_output = result.final_output.strip()

        loading_msg.content = f"### Latest Market Insight:\n\n{final_output}"
        await loading_msg.update()

    except Exception as e:
        print("Error:", e)
        await cl.Message(
            author="❗ Error",
            content="Oops! Something went wrong while processing your request. Please try again shortly."
        ).send()
