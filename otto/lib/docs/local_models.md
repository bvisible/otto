# Using Local LLM Models with Otto

Otto now supports local LLM models through any OpenAI-compatible API server, including LM Studio, Ollama, vLLM, and others.

## Quick Start

1. **Configure your local server URL** in Otto Settings:
   - Go to Otto Settings
   - Set "Local LLM Server URL" to your server endpoint (e.g., `http://localhost:1234/v1`)
   - Click "Test Local Server" to verify connectivity

2. **Enable local models** in Otto LLM:
   - Go to Otto LLM list
   - Enable desired local models (they're prefixed with `local/` or `ollama/`)
   - Use the "Ask" button to test each model

3. **Use in your code**:
   ```python
   import otto.lib as otto
   
   session = otto.new(model="local/llama-3.3-70b")
   response = session.interact("Hello!")
   ```

## Supported Servers

### LM Studio
Default URL: `http://localhost:1234/v1`

1. Download and install [LM Studio](https://lmstudio.ai/)
2. Load your desired model
3. Start the server (it runs on port 1234 by default)
4. Configure Otto with the URL above

### Ollama
Default URL: `http://localhost:11434/v1`

1. Install [Ollama](https://ollama.ai/)
2. Pull a model: `ollama pull llama3.2`
3. Ollama runs automatically
4. Configure Otto with the URL above

### vLLM
Default URL: `http://localhost:8000/v1`

1. Install vLLM: `pip install vllm`
2. Start server: `python -m vllm.entrypoints.openai.api_server --model your-model`
3. Configure Otto with the URL above

### Text Generation WebUI
Default URL: `http://localhost:5000/v1`

1. Install [Text Generation WebUI](https://github.com/oobabooga/text-generation-webui)
2. Enable the OpenAI extension
3. Start the server
4. Configure Otto with the URL above

## Available Models

Otto includes fixtures for popular local models:

- **Large Models** (70B+):
  - `local/llama-3.3-70b` - Meta's latest Llama model
  - `local/qwen-2.5-72b` - Alibaba's Qwen with vision support
  - `local/mistral-large` - Mistral's flagship model

- **Ollama Models**:
  - `ollama/llama3.2` - Smaller, faster Llama variant
  - `ollama/phi3` - Microsoft's efficient small model

You can add custom models by creating new Otto LLM entries with provider "Local".

## Adding Custom Models

1. Go to Otto LLM list
2. Create new Otto LLM
3. Set:
   - **Provider**: Local
   - **Name**: Use format `local/model-name` or `ollama/model-name`
   - **Title**: Display name
   - **Size**: Model size category
   - **Other options** as needed

## Troubleshooting

### Connection Failed
- Verify your local server is running
- Check the URL is correct (including `/v1` suffix for OpenAI compatibility)
- Test with curl: `curl http://localhost:1234/v1/models`
- Check firewall settings

### Model Not Found
- Ensure the model is loaded in your local server
- Model names must match exactly
- For Ollama: run `ollama list` to see available models

### Slow Performance
- Local models require significant RAM/VRAM
- Consider using smaller models for faster responses
- Enable GPU acceleration in your server

### Function Calling
- Not all local models support function calling
- Test with the "Ask" button first
- Consider models like Qwen or newer Llama versions

## Best Practices

1. **Model Selection**:
   - Use smaller models for simple tasks
   - Reserve large models for complex reasoning
   - Test performance vs quality tradeoffs

2. **Server Configuration**:
   - Allocate sufficient RAM (2x model size recommended)
   - Use GPU acceleration when available
   - Consider quantized models for better performance

3. **Development Workflow**:
   - Test models locally before production use
   - Use the "Ask" button for quick testing
   - Monitor server resource usage

## Example Usage

### Basic Chat
```python
import otto.lib as otto

# Using LM Studio
session = otto.new(
    model="local/llama-3.3-70b",
    instruction="You are a helpful coding assistant"
)

response = session.interact("Write a Python hello world")
```

### With Ollama
```python
# First pull the model: ollama pull llama3.2

session = otto.new(model="ollama/llama3.2")
response = session.interact("Explain quantum computing simply")
```

### Multi-Model Comparison
```python
models = ["local/llama-3.3-70b", "ollama/phi3", "local/mistral-large"]

for model in models:
    if otto.is_model_available(model):
        response = otto.quick_query(
            "What is 2+2?",
            model=model,
            stream=False
        )
        print(f"{model}: {response[0]['text']}")
```

## Security Considerations

- Local models keep all data on your machine
- No API keys or external services required
- Ideal for sensitive data processing
- Ensure your local server is not exposed to the internet

## Performance Tips

1. **Quantization**: Use quantized models (GGUF, AWQ, GPTQ) for better performance
2. **Context Length**: Be mindful of context limits for local models
3. **Batch Processing**: Some servers support batch inference
4. **Model Loading**: Keep frequently used models loaded in memory

## Limitations

- Vision support depends on the model and server
- Reasoning capabilities vary by model
- Function calling support is model-dependent
- Performance is hardware-limited

For more information on Otto's LLM capabilities, see the main [Otto Lib documentation](./README.md).