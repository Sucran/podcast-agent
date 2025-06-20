from agents import Agent, OpenAIChatCompletionsModel
from model import deepseek_r1_model, model_settings
from agents import ComputerTool, Computer
from agents.mcp import MCPUtil, MCPServerStreamableHttp, MCPServerStreamableHttpParams, MCPServer
from ai.instructions import dynamic_instructions
from datetime import timedelta
import asyncio

podcast_mcp_server_params = MCPServerStreamableHttpParams(
    url="http://127.0.0.1:7860/api/mcp",
    timeout=timedelta(seconds=600),
    sse_read_timeout=timedelta(seconds=600),
    terminate_on_close=True
)


# agent_instructions =  asyncio.run(dynamic_instructions(
#         [podcast_mcp_server_params], 
#         "podcast-mcp",
#         "streamable_http",
#         "You are a helpful assistant that can convert speech to text. Please be concise and accurate in your responses."
#     ))


podcast_mcp_server = MCPServerStreamableHttp(
    name="podcast-mcp",
    params=podcast_mcp_server_params,
    cache_tools_list=True,
    client_session_timeout_seconds=1800
)

sst_agent = Agent(
    name="Speech to Text Agent",
    instructions="""You are a helpful assistant that can convert speech to text. Please be concise and accurate in your responses.
    You can use the following tools to convert speech to text:
    - podcast-mcp: A tool that can convert speech to text.
    when you use transcribe_audio_file_tool, you should disable enable_speaker_diarization options which would slow down the process
    and you should use get_file_info tool to get the file info and see if the file size is larger than 16kb
    if it is, you should use read_text_file_segments_tool to read the file segments one by one avoid the error of exceed the max tokens
    if not, you can directly use read_text_file_segments_tool to read the file content
    once you read the transcrbed file content, you can handoff to the last agent to summarize the content
    """,
    model=deepseek_r1_model,
    mcp_servers=[podcast_mcp_server],
    model_settings=model_settings
)
