# 🎤 Podacast Agent 

> **English Documentation**: [README.md](README.md)

一个基于 OpenAI Agents SDK 的多功能AI助手项目，集成了语音转文字(SST)、文字转语音(TTS)和播客处理功能。

## 🌟 功能特性

### 技术亮点

由于OpenAI Agent SDK在多智能体的情况下，是异步循环等待的。这对于用户来说，并不能直观的看到目前Agent正在处理哪个阶段，所以这个项目使用责任链的方式，对流式事件进行了代理消息的映射，让用户能直观的看到目前是哪一个阶段

同时我还提交了 gradio-example 到 OpenAI Agent SDK 项目 https://github.com/openai/openai-agents-python/pull/888. 这边的example会更加简单清晰，用户可以先去运行这个项目。

### 核心功能
- **多代理协作**：通过Agent代理系统实现任务分工
- **语音转文字**：使用播客MCP服务器进行音频转录
- **文字转语音**：集成Minimax API实现文本转语音
- **播客处理**：支持播客音频文件的转录和分析
- **实时流式对话**：基于Gradio的流式聊天界面

### 技术特性
- **异步处理**：全面支持异步操作，提升性能
- **事件驱动**：采用事件处理链模式，支持复杂的消息流处理
- **MCP集成**：支持多种Model Context Protocol服务器
- **多模型支持**：可配置不同的AI模型（DeepSeek R1等）
- **实时监控**：完整的事件追踪和调试信息

## 🛠️ 技术栈

- **Python**: 3.12+
- **UI框架**: Gradio 5.33.1+
- **AI SDK**: OpenAI Agents SDK with LiteLLM
- **包管理**: UV
- **异步处理**: AsyncIO
- **配置管理**: Python-dotenv
- **API集成**: 
  - DeepSeek API (推理模型)
  - Minimax API (文字转语音)
  - Podcast MCP (语音转文字)

## 📦 项目结构

```
openai-agent-sdk-learn/
├── src/
│   ├── app.py                    # 主应用入口
│   ├── ai/                       # AI代理模块
│   │   ├── sst_agent.py         # 语音转文字代理
│   │   ├── tts_agent.py         # 文字转语音代理
│   │   └── instructions.py      # 动态指令生成
│   ├── ui/                       # 用户界面模块
│   │   ├── gradio_ui.py         # 基础Gradio界面
│   │   └── gradio_agent_ui.py   # 代理专用界面
│   ├── model/                    # 模型配置
│   │   └── model_config.py      # 模型设置和配置
│   └── event/                    # 事件处理
│       └── event_handler.py     # 事件处理链
├── pyproject.toml               # 项目配置和依赖
└── README.md                    # 项目说明文档
```

## 🚀 快速开始

### 环境要求

- Python 3.12+
- UV 包管理器

### 安装依赖

```bash
# 安装UV包管理器（如果还没有安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 克隆项目
git clone <repository-url>
cd openai-agent-sdk-learn

# 安装依赖
uv sync
```

### 环境配置

创建 `.env` 文件并配置以下环境变量：

```env
# DeepSeek API配置
DS_API_KEY=your_deepseek_api_key

# Minimax API配置
MINIMAX_API_KEY=your_minimax_api_key
MINIMAX_MCP_BASE_PATH=/path/to/your/files

# 其他配置
OPENAI_API_KEY=your_openai_api_key_if_needed
```
### ⚠️ 重要: 要先本地部署 Podcast MCP

查看 github 仓库：https://github.com/Sucran/modal-transcriber-mcp.git

先部署 podcast-mcp，否则speech-to-text的agent无法正常使用

### 启动应用

```bash
# 激活虚拟环境
source .venv/bin/activate

# 启动应用
python src/app.py
```

应用将在 `http://localhost:8000` 启动。

## 🎯 使用说明

### 基本使用

1. **启动应用**：运行 `python src/app.py`
2. **打开浏览器**：访问 `http://localhost:8000`
3. **开始对话**：在聊天界面输入消息

### 语音转文字功能

```
用户: 帮我转译播客 https://www.xiaoyuzhoufm.com/episode/xxxxx
```

系统会自动：
1. 切换到语音转文字代理
2. 下载并处理音频文件
3. 进行语音转录（支持异步模式）
4. 返回转录结果

### 文字转语音功能

```
用户: 帮我把这段文字转换成语音：[文字内容]
```

系统会：
1. 切换到文字转语音代理
2. 调用Minimax API生成语音
3. 返回音频文件下载链接

### 代理切换

应用支持智能代理切换：
- **计划代理**：处理一般对话和任务规划
- **SST代理**：专门处理语音转文字任务
- **TTS代理**：专门处理文字转语音任务

## 🔧 配置说明

### 模型配置

在 `src/model/model_config.py` 中可以配置：
- 推理模型选择（默认DeepSeek R1）
- 模型参数（温度、top_p等）
- 自定义API端点

### MCP服务器配置

项目支持两种MCP服务器：
1. **Podcast MCP**：HTTP流式服务，用于音频处理
2. **Minimax MCP**：标准IO服务，用于语音合成

### 事件处理配置

事件处理链支持多种事件类型：
- 工具调用事件
- 代理切换事件  
- 推理过程事件
- MCP批准事件

## 🐛 故障排除

### 常见问题

1. **SSL错误**：已默认禁用追踪功能避免SSL问题
2. **音频文件过大**：自动分段处理避免token限制
3. **异步处理**：确保使用异步模式进行音频转录

### 调试模式

应用启动时默认开启调试模式，会在控制台输出详细的事件信息：
- 代理切换日志
- 工具调用详情
- MCP服务状态

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进这个项目！

## 📄 许可证

[添加您的许可证信息]

## 🔗 相关链接

- [OpenAI Agents SDK](https://github.com/openai/openai-agents)
- [Gradio](https://gradio.app/)
- [DeepSeek API](https://platform.deepseek.com/)
- [Minimax API](https://www.minimax.chat/)
