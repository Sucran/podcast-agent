# 🎤 Podcast Agent 

> **中文文档**: [README_zh.md](README_zh.md)

A multifunctional AI assistant project based on OpenAI Agents SDK, integrating Speech-to-Text (STT), Text-to-Speech (TTS), and podcast processing capabilities.

## 🌟 Features

### Core Functionality
- **Multi-Agent Collaboration**: Task distribution through agent system
- **Speech-to-Text**: Audio transcription using Podcast MCP server
- **Text-to-Speech**: Text-to-speech synthesis with Minimax API integration
- **Podcast Processing**: Support for podcast audio file transcription and analysis
- **Real-time Streaming Chat**: Gradio-based streaming chat interface

### Technical Features
- **Asynchronous Processing**: Full async support for enhanced performance
- **Event-Driven Architecture**: Event handler chain pattern for complex message flow processing
- **MCP Integration**: Support for multiple Model Context Protocol servers
- **Multi-Model Support**: Configurable AI models (DeepSeek R1, etc.)
- **Real-time Monitoring**: Complete event tracking and debugging information

## 💡 Technical Highlights

Since the OpenAI Agent SDK uses asynchronous loop waiting in multi-agent scenarios, users cannot intuitively see which stage the Agent is currently processing. This project uses a chain of responsibility pattern to map streaming events to agent messages, allowing users to visually see which stage is currently being processed.

I have also submitted a gradio-example to the OpenAI Agent SDK project: https://github.com/openai/openai-agents-python/pull/888. The example there is simpler and clearer, and users can run that project first.

## 🛠️ Tech Stack

- **Python**: 3.12+
- **UI Framework**: Gradio 5.33.1+
- **AI SDK**: OpenAI Agents SDK with LiteLLM
- **Package Manager**: UV
- **Async Processing**: AsyncIO
- **Configuration**: Python-dotenv
- **API Integrations**: 
  - DeepSeek API (Inference Model)
  - Minimax API (Text-to-Speech)
  - Podcast MCP (Speech-to-Text)

## 📦 Project Structure

```
podcast-agent/
├── src/
│   ├── app.py                    # Main application entry
│   ├── ai/                       # AI agent modules
│   │   ├── sst_agent.py         # Speech-to-text agent
│   │   ├── tts_agent.py         # Text-to-speech agent
│   │   └── instructions.py      # Dynamic instruction generation
│   ├── ui/                       # User interface modules
│   │   ├── gradio_ui.py         # Basic Gradio interface
│   │   └── gradio_agent_ui.py   # Agent-specific interface
│   ├── model/                    # Model configurations
│   │   └── model_config.py      # Model settings and configurations
│   └── event/                    # Event handling
│       └── event_handler.py     # Event handler chain
├── pyproject.toml               # Project configuration and dependencies
├── README.md                    # Project documentation (English)
└── README_zh.md                 # Project documentation (Chinese)
```

## 🚀 Quick Start

### Requirements

- Python 3.12+
- UV Package Manager

### Installation

```bash
# Install UV package manager (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the project
git clone https://github.com/Sucran/podcast-agent.git
cd podcast-agent

# Install dependencies
uv sync
```

### ⚠️ Important: Deploy Podcast MCP in local mode First

**Deploy podcast-mcp first, otherwise the speech-to-text agent cannot function properly.**

View GitHub repository: https://github.com/Sucran/modal-transcriber-mcp.git

### Environment Configuration

Create a `.env` file and configure the following environment variables:

```env
# DeepSeek API Configuration
DS_API_KEY=your_deepseek_api_key

# Minimax API Configuration
MINIMAX_API_KEY=your_minimax_api_key
MINIMAX_MCP_BASE_PATH=/path/to/your/files

# Other Configuration
OPENAI_API_KEY=your_openai_api_key_if_needed
```

### Launch Application

```bash
# Activate virtual environment
source .venv/bin/activate

# Start the application
python src/app.py
```

The application will start at `http://localhost:8000`.

## 🎯 Usage Guide

### Basic Usage

1. **Start Application**: Run `python src/app.py`
2. **Open Browser**: Navigate to `http://localhost:8000`
3. **Start Chatting**: Enter messages in the chat interface

### Speech-to-Text Feature

```
User: Help me transcribe this podcast https://www.xiaoyuzhoufm.com/episode/xxxxx
```

The system will automatically:
1. Switch to the speech-to-text agent
2. Download and process the audio file
3. Perform speech transcription (supports async mode)
4. Return transcription results

### Text-to-Speech Feature

```
User: Help me convert this text to speech: [text content]
```

The system will:
1. Switch to the text-to-speech agent
2. Call Minimax API to generate audio
3. Return audio file download link

### Agent Switching

The application supports intelligent agent switching:
- **Planning Agent**: Handles general conversation and task planning
- **STT Agent**: Specialized for speech-to-text tasks
- **TTS Agent**: Specialized for text-to-speech tasks

## 🔧 Configuration

### Model Configuration

Configure in `src/model/model_config.py`:
- Inference model selection (default: DeepSeek R1)
- Model parameters (temperature, top_p, etc.)
- Custom API endpoints

### MCP Server Configuration

The project supports two types of MCP servers:
1. **Podcast MCP**: HTTP streaming service for audio processing
2. **Minimax MCP**: Standard IO service for speech synthesis

### Event Handler Configuration

Event handler chain supports multiple event types:
- Tool call events
- Agent switching events
- Reasoning process events
- MCP approval events

## 🐛 Troubleshooting

### Common Issues

1. **SSL Errors**: Tracing is disabled by default to avoid SSL issues
2. **Large Audio Files**: Automatic segmentation to avoid token limits
3. **Async Processing**: Ensure async mode is used for audio transcription

### Debug Mode

The application starts with debug mode enabled by default, outputting detailed event information to console:
- Agent switching logs
- Tool call details
- MCP service status

## 🤝 Contributing

Welcome to submit Issues and Pull Requests to improve this project!

## 📄 License

Apache-2.0 License

## 🔗 Related Links

- [OpenAI Agents SDK](https://github.com/openai/openai-agents)
- [Gradio](https://gradio.app/)
- [DeepSeek API](https://platform.deepseek.com/)
- [Minimax API](https://www.minimax.chat/) 