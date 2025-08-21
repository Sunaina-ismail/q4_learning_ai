# # import asyncio
# # import os
# # from dotenv import load_dotenv
# # from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner, enable_verbose_stdout_logging
# # from openai.types.responses import ResponseTextDeltaEvent
# # from rich import print

# # load_dotenv()
# # GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# # MODEL_NAME = "gemini-2.0-flash"

# # if not GEMINI_API_KEY:
# #     raise ValueError("GEMINI_API_KEY is not set")


# # client = AsyncOpenAI(
# #     api_key=GEMINI_API_KEY,
# #     base_url="https://generativelanguage.googleapis.com/v1beta/openai"
# # )


# # enable_verbose_stdout_logging()

# # model = OpenAIChatCompletionsModel(
# #     model=MODEL_NAME,
# #     openai_client=client
# # )

# # config = RunConfig(
# #     model=model,
# #     tracing_disabled=True
# # )


# # lyrical_agent = Agent(
# #     name="LyricalPoetryAgent" ,
# #     instructions="""You are a poetry analyst for **lyric poetry**. 
# #     Your job is to provide a brief and great explanation in the **same language** which the PoetryTriageAgent give you.
# #     In the Final_output add Lyric Poetry on the Top as Main Heading""",
# #     model= model
# # )

# # narrative_agent = Agent(
# #     name="NarrativePoetryAgent" ,
# #     instructions="""You are a poetry analyst for **Narrative poetry**. 
# #     Your job is to provide a brief and great explanation in the **same language** which the PoetryTriageAgent give you.
# #     In the Final_output add  Narrative Poetry on the Top as Main Heading""",
# #     model=model
# # )


# # dramatic_agent = Agent(
# #     name="DramaticPoetryAgent" ,
# #     instructions="""You are a poetry analyst for **Dramatic poetry**. 
# #     Your job is to provide a brief and great explanation in the **same language** which the PoetryTriageAgent give you.
# #     In the Final_output add Dramatic Poetry on Top as Main Heading""",
# #     model=model
# # )

# # triage_agent = Agent(
# #     name="PoetryTriageAgent",
# #     instructions="""
# # You are a poetry classifier.

# # You will receive poetry. Your tasks:
# # 1. **Detect the language** of the poem (e.g., English or Urdu).
# # 2. **Classify** the poetry as:
# #    - Lyric Poetry
# #    - Narrative Poetry
# #    - Dramatic Poetry
# # 3. In the Final_output add the type of Poetry it and on the Top as Main Heading.

# # # Example:
# #     Dramatic Poetry
    
    
# # Then, hand off the poetry **and the language info** to the appropriate agent not other language just the one in which the user prompt is.
# # DO NOT explain the poem yourself.
# # """,
# #     handoffs=[lyrical_agent, narrative_agent, dramatic_agent],
# #     model=model,
# # )



# # async def main():
    
# #     result = await Runner.run(triage_agent, input="""The wind was a torrent of darkness among the gusty trees,
# # The moon was a ghostly galleon tossed upon cloudy seas,
# # The road was a ribbon of moonlight over the purple moor,
# # And the highwayman came riding—
# # Riding—riding—
# # The highwayman came riding, up to the old inn-door.

# # He'd a French cocked-hat on his forehead, a bunch of lace at his chin,
# # A coat of the claret velvet, and breeches of brown doe-skin;
# # They fitted with never a wrinkle: his boots were up to the thigh!
# # And he rode with a jeweled twinkle,
# # His pistol butts a-twinkle,
# # His rapier hilt a-twinkle, under the jeweled sky.""", run_config=config)
    
# #     print(result.final_output)
# #     # async for event in result.stream_events():
# #     #     if(event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent)):
# #     #         print(event.data.delta, end="", flush=True)
        
    

# # if __name__ == "__main__":
# #     asyncio.run(main())        
















import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner, enable_verbose_stdout_logging
from openai.types.responses import ResponseTextDeltaEvent
from rich import print

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.0-flash"


if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set")


client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)


enable_verbose_stdout_logging()


model = OpenAIChatCompletionsModel(
    model=MODEL_NAME,
    openai_client=client
)


config = RunConfig(
    model=model,
    tracing_disabled=True
)


# lyrical_agent = Agent(
#     name="LyricalPoetryAgent" ,
#     instructions="""You are a poetry analyst for **lyric poetry**. 
#     Your job is to provide a brief and great explanation in the **same language** which the PoetryTriageAgent give you.
#     In the Final_output add Lyric Poetry on the Top as Main Heading""",
#     model= model
# )



# narrative_agent = Agent(
#     name="NarrativePoetryAgent" ,
#     instructions="""You are a poetry analyst for **Narrative poetry**. 
#     Your job is to provide a brief and great explanation in the **same language** which the PoetryTriageAgent give you.
#     In the Final_output add  Narrative Poetry on the Top as Main Heading""",
#     model=model
# )


# dramatic_agent = Agent(
#     name="DramaticPoetryAgent" ,
#     instructions="""You are a poetry analyst for **Dramatic poetry**. 
#     Your job is to provide a brief and great explanation in the **same language** which the PoetryTriageAgent give you.
#     In the Final_output add Dramatic Poetry on Top as Main Heading""",
#     model=model
# )

# triage_agent = Agent(
#     name="PoetryTriageAgent",
#     instructions="""
# You are a poetry classifier.

# You will receive poetry. Your tasks:
# 1. **Detect the language** of the poem (e.g., English or Urdu).
# 2. **Classify** the poetry as:
#    - Lyric Poetry
#    - Narrative Poetry
#    - Dramatic Poetry
# 3. In the Final_output add the type of Poetry it and on the Top as Main Heading.

# # Example:
#     Dramatic Poetry
    
    
# Then, hand off the poetry **and the language info** to the appropriate agent not other language just the one in which the user prompt is.
# DO NOT explain the poem yourself.
# """,
#     handoffs=[lyrical_agent, narrative_agent, dramatic_agent],
#     model=model,
# )



# async def main():
    
#     result = await Runner.run(triage_agent, input="""Tell my mother I wore her smile,  
# Even when I marched the final mile.  
# That I held her love inside my chest,  
# When guns roared loud and gave no rest.  

# And if she weeps, just let her know—  
# I faced the fire, I didn’t bow low.  
# This letter, stained with blood and rain,  
# Is all I leave to ease her pain.

# """, run_config=config)
    
#     print(result.final_output)
#     # async for event in result.stream_events():
#     #     if(event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent)):
#     #         print(event.data.delta, end="", flush=True)
        
    

# if __name__ == "__main__":
#     asyncio.run(main())        


from agents import Agent, Runner
import asyncio

spanish_agent = Agent(
    name="Spanish agent",
    instructions="You translate the user's message to Spanish",
    model=model
)

french_agent = Agent(
    name="French agent",
    instructions="You translate the user's message to French",
    model=model
)

orchestrator_agent = Agent(
    name="orchestrator_agent",
    instructions=(
        "You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools."
    ),
    tools=[
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate the user's message to Spanish",
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate the user's message to French",
        ),
    ],
    model=model
)

async def main():
    result = await Runner.run(orchestrator_agent, input="Say 'Hello, how are you?' in Spanish.", run_config=config)
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main()) 