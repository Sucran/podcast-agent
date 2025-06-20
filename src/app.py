from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from ui.gradio_agent_ui import create_agent_app
from ai import podcast_mcp_server, minimax_mcp_server, sst_agent, tts_agent
import asyncio  
from model import deepseek_r1_model, model_settings
from event import EventHandlerChain

load_dotenv()

# Disable tracing to avoid SSL errors when using non-OpenAI models
set_tracing_disabled(True)

plan_agent = Agent(
    name="Planner",
    instructions="You are a helpful assistant that can answer questions and help with tasks. Please be concise and accurate in your responses.",
    model=deepseek_r1_model,
    handoff_description="You can handoff to sst_agent to convert speech to text. You can handoff to tts_agent to convert text to speech.",
    handoffs=[sst_agent, tts_agent],
    model_settings=model_settings
)

event_handler_chain = EventHandlerChain()
app = create_agent_app(plan_agent, [podcast_mcp_server, minimax_mcp_server], event_handler_chain)


if __name__ == "__main__":
    
    app.launch(
        server_port=8000,
        share=False,
        debug=True,
        show_error=True
    )

    # asyncio.run(main())










