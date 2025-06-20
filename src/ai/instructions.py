from agents.mcp import MCPUtil, MCPServerStreamableHttp, MCPServerSse, MCPServerStdio
import contextlib

async def dynamic_instructions(mcp_params: list[dict], name: str, mcp_type: str, instructions: str):
    """
    异步动态指令函数 - 直接利用 SDK 的原生支持
    """
    try:
        all_mcp_tools = []
        for param in mcp_params:
            async with contextlib.AsyncExitStack() as stack:
                if mcp_type == "streamable_http":
                    server = await stack.enter_async_context(MCPServerStreamableHttp(
                        name=name,
                        params=param,
                        cache_tools_list=True,
                        client_session_timeout_seconds=1800
                    ))
                elif mcp_type == "sse":
                    server = await stack.enter_async_context(MCPServerSse(
                        name=name,
                        params=param,
                        cache_tools_list=True,
                        client_session_timeout_seconds=1800
                    ))
                else:
                    server = await stack.enter_async_context(MCPServerStdio(
                        name=name,
                        params=param,
                        cache_tools_list=True
                    ))
                server_tools = await MCPUtil.get_all_function_tools([server], convert_schemas_to_strict=True)
                all_mcp_tools.extend(server_tools)
                
        if all_mcp_tools:
            prompt = f"""{instructions}
            You have access to the following tools: {all_mcp_tools}"""
            print("="*100)
            print(prompt)
            print("="*100)
            return prompt
        else:
            return instructions
             
    except Exception as e:
        print(f"⚠️ Warning: Could not load MCP tools ({e}), using base instructions")
        return instructions