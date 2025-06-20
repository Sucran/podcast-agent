from agents import Agent, OpenAIChatCompletionsModel
from model import deepseek_r1_model, model_settings
from agents.mcp import MCPServerStdio, MCPServerStdioParams
import os
from ai.instructions import dynamic_instructions
from datetime import timedelta
import asyncio

"""
"minmax": {
      "command": "uvx",
      "args": [
        "minimax-mcp",
        "-y"
      ],
      "env": {
        "MINIMAX_API_KEY": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiLmtbfonrrnlKjmiLdfMzc5NDM4NzIyODM1NjQwMzIzIiwiVXNlck5hbWUiOiLmtbfonrrnlKjmiLdfMzc5NDM4NzIyODM1NjQwMzIzIiwiQWNjb3VudCI6IiIsIlN1YmplY3RJRCI6IjE5MjIyMTgxOTkyNjk1MTIxMDAiLCJQaG9uZSI6IjE1MTA2MDMwODE4IiwiR3JvdXBJRCI6IjE5MjIyMTgxOTkyNjUzMTc3OTYiLCJQYWdlTmFtZSI6IiIsIk1haWwiOiIiLCJDcmVhdGVUaW1lIjoiMjAyNS0wNi0wNSAyMTo1MTo1NSIsIlRva2VuVHlwZSI6MSwiaXNzIjoibWluaW1heCJ9.lqW3OR02wS6kJIp38ZP1TkUm4er47FuUj-9BT-RWx19UEAzTTTvUwINlzoDWTRjlXpggETDwZEXWXbuHrUvALxvTqCSryzEVB-RRTuoNOG8QsecgBlhFr1CYqZNSikUYBqQkvsDjDT3LodxRugfSclmHOyFHkizZYPF86NIMGzZ9uxAoVV6V_K7UTx662I6RkbsGao-AG8QQF8gWqX39aL49IvHYS-AFkqJSnsmwe5dUSkxz59cw71APDq8TMB72dj0hKZFlhSJup-ApQ8mIGP-ZqyARZnKz9LFAGwc1TJHUKX-meowUNwfPJUw257A-QQTVYCzNz5j6XtV1Y-8JYw",
        "MINIMAX_MCP_BASE_PATH": "/User/richard/Downloads",
        "MINIMAX_API_HOST": "https://api.minimax.chat",
        "MINIMAX_API_RESOURCE_MODE": "url"
      }
    }
"""

minimax_mcp_server_params = MCPServerStdioParams(
    command="uvx",
        args=["minimax-mcp", "-y"],
        env={
            "MINIMAX_API_KEY": str(os.getenv("MINIMAX_API_KEY")),
            "MINIMAX_MCP_BASE_PATH": str(os.getenv("MINIMAX_MCP_BASE_PATH")),
            "MINIMAX_API_HOST": "https://api.minimax.chat",
            "MINIMAX_API_RESOURCE_MODE": "url",
        }
)

# agent_instructions = asyncio.run(dynamic_instructions(
#         [minimax_mcp_server_params], 
#         "minimax-mcp",
#         "stdio",
#         "You are a helpful assistant that can convert text to speech. Please be concise and accurate in your responses."
#     ))

minimax_mcp_server = MCPServerStdio(
    name="minimax-mcp",
    params=minimax_mcp_server_params,
    cache_tools_list=True,
    client_session_timeout_seconds=1800
)
    
tts_agent = Agent(
    name="Text to Speech Agent",
    instructions="You are a helpful assistant that can convert text to speech. Please be concise and accurate in your responses.",  # 使用已经await的结果
    model= deepseek_r1_model,
    mcp_servers=[minimax_mcp_server],
    model_settings=model_settings
)