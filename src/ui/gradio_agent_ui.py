from agents import Runner
import asyncio
from agents import Agent, RunItemStreamEvent
from agents.mcp import MCPServer
from openai.types.responses import ResponseTextDeltaEvent
from typing import List
import contextlib
import gradio as gr
from gradio.components import ChatMessage
from event import EventHandlerChain

def create_agent_app(agent: Agent, mcp_servers: list[MCPServer], event_handler_chain: EventHandlerChain):

    # Use closure to create chat function
    async def chat_function_with_agent(user_msg: str, history: list):
        """
        Asynchronous streaming chat function - uses closure to access agent and mcp_servers
        """
        current_message = ChatMessage(role="assistant", content="")

        # Initialize context
        context = {"response_buffer": "", "current_messages": [current_message]}

        async with contextlib.AsyncExitStack() as stack:
            for server in mcp_servers:
                await stack.enter_async_context(server)
            # Use Runner.run_streamed to get streaming results
            result = Runner.run_streamed(agent, user_msg)
            async for event in result.stream_events():
                # Use chain of responsibility to process all events
                if event_handler_chain.process_event(event, history, context):
                    # Get current messages from context and yield
                    current_messages = context.get("current_messages", [])
                    yield current_messages


    return gr.ChatInterface(
        chat_function_with_agent,
        title="🤖 OpenAI Agent Chat Interface",
        description="Chat with an AI assistant powered by OpenAI Agents SDK",
        theme=gr.themes.Soft(
            primary_hue="blue",
            secondary_hue="slate"
        ),
        examples=[["帮我转译播客 https://www.xiaoyuzhoufm.com/episode/684d7a22b24003f187dc1ab5"]],
        submit_btn=True,
        flagging_mode="manual",
        flagging_options=["Like", "Spam", "Inappropriate", "Other"],
        type="messages",
        save_history=True
    )

