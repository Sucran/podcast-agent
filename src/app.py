from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from ui.gradio_ui import create_app

load_dotenv()

# Disable tracing to avoid SSL errors when using non-OpenAI models
set_tracing_disabled(True)

# Create a custom OpenAI client pointing to DeepSeek
custom_client = AsyncOpenAI(
    api_key=os.getenv("DS_API_KEY"),
    base_url="https://api.deepseek.com"
)

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant that can answer questions and help with tasks. Please be concise and accurate in your responses.",
    model=OpenAIChatCompletionsModel(
        model="deepseek-chat",  # Use the correct model name for DeepSeek
        openai_client=custom_client
    ),
    tools=[],
)

app = create_app(agent)

if __name__ == "__main__":
    print("🚀 Starting OpenAI Agent Chat Interface...")
    print("📱 The interface will be available at: http://localhost:7860")
    print("🛑 Press Ctrl+C to stop the server\n")
    
    app.launch(
        server_port=7860,
        share=False,
        debug=True,
        show_error=True
    )









