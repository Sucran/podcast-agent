import gradio as gr
from agents import Runner
import asyncio
from openai.types.responses import ResponseTextDeltaEvent

def create_app(agent):
    async def chat_function(message, history):
        """
        异步流式聊天函数 - 正确的实现方式
        """
        # 使用 Runner.run_streamed 获取流式结果
        result = Runner.run_streamed(agent, message)
        
        # 累积响应文本
        accumulated_response = ""
        
        # 异步遍历流式事件
        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                accumulated_response += event.data.delta
                yield accumulated_response


    return gr.ChatInterface(
        chat_function,
        title="🤖 OpenAI Agent Chat Interface", 
        description="Chat with an AI assistant powered by OpenAI Agents SDK",
        theme=gr.themes.Soft(
            primary_hue="blue",
            secondary_hue="slate"
        ),
        type="messages"
    )


