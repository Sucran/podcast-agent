import os
from openai import AsyncOpenAI
from openai.types.shared.reasoning import Reasoning
from agents import OpenAIChatCompletionsModel, ModelSettings

# Create a deepseek OpenAI client pointing to DeepSeek
custom_client = AsyncOpenAI(
    api_key=os.getenv("DS_API_KEY"),
    base_url="https://api.deepseek.com"
)


deepseek_r1_model = OpenAIChatCompletionsModel(
        model="deepseek-chat",
        openai_client=custom_client
)

model_settings = ModelSettings(
    temperature=0.0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)



