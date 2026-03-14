# Affordable AI API - 80% Cheaper than OpenAI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)

**Qwen2.5-7B powered API for developers and startups.**

---

## 🚀 Features

- **💰 Affordable**: $0.0003/1K tokens (80% cheaper than GPT-4)
- **⚡ Fast**: <500ms response time
- **🎯 Quality**: Qwen2.5-7B-Instruct model
- **🌍 Perfect for**: MVP, prototypes, learning, side projects

---

## 📊 Price Comparison

| Provider | Input Price | Output Price | vs Us |
|----------|-------------|--------------|-------|
| OpenAI GPT-4 | $0.03/1K | $0.06/1K | 100x |
| Anthropic Claude | $0.015/1K | $0.075/1K | 50x |
| Google Gemini | $0.005/1K | $0.015/1K | 17x |
| **Our API** | **$0.0003/1K** | **$0.001/1K** | **-** |

**Example**: Generate a 1000-word article
- OpenAI: ~$0.15
- Our API: ~$0.006
- **Save: 96%!**

---

## 🎯 Who Is This For?

✅ **Indie Hackers** - Build AI apps without breaking the bank  
✅ **Students** - Learn AI, build projects, thesis  
✅ **Developers** - Side projects, prototypes, MVP  
✅ **Startups** - Validate ideas before scaling  
✅ **Freelancers** - Client projects with AI features  

❌ **Not for**: Enterprise needing 99.99% SLA (use big clouds)

---

## 📖 Quick Start

### 1. Get API Key

Contact us for free 100K tokens trial!

### 2. Call the API

#### Python Example

```python
import requests

API_URL = "http://58.144.141.41:8000/v1/chat/completions"
API_KEY = "sk-autodl-gpu-token"

response = requests.post(
    API_URL,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "messages": [
            {"role": "user", "content": "Hello, introduce yourself"}
        ],
        "max_tokens": 1024
    }
)

result = response.json()
print("Reply:", result["choices"][0]["message"]["content"])
print("Tokens used:", result["usage"])
```

#### cURL Example

```bash
curl -X POST http://58.144.141.41:8000/v1/chat/completions \
  -H 'Authorization: Bearer sk-autodl-gpu-token' \
  -H 'Content-Type: application/json' \
  -d '{
    "messages": [
      {"role": "user", "content": "Hello"}
    ]
  }'
```

#### JavaScript Example

```javascript
const response = await fetch('http://58.144.141.41:8000/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer sk-autodl-gpu-token',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    messages: [
      { role: 'user', content: 'Hello' }
    ]
  })
});

const result = await response.json();
console.log(result.choices[0].message.content);
```

---

## 🛠️ Example Projects

### 1. Chatbot
[View Code](examples/chatbot.py)

### 2. Content Generator
[View Code](examples/content-generator.py)

### 3. Data Analyst
[View Code](examples/data-analyst.py)

---

## 📋 API Documentation

### Endpoint
```
POST http://58.144.141.41:8000/v1/chat/completions
```

### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| messages | array | ✅ | Conversation history |
| max_tokens | integer | ❌ | Max tokens to generate, default 1024 |
| temperature | float | ❌ | Temperature, 0-1, default 0.7 |

### Response Format

```json
{
  "id": "chatcmpl-1773474885",
  "object": "chat.completion",
  "created": 1773474885,
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "Hello! I'm Qwen..."
    },
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 63,
    "completion_tokens": 160,
    "total_tokens": 223
  }
}
```

---

## 💰 Pricing

### Pay-as-you-go
- **Input Tokens**: $0.0003 / 1K tokens
- **Output Tokens**: $0.001 / 1K tokens

### Free Trial
- New users get **100K tokens FREE**
- Enough for testing and development

### Packages
| Plan | Price | Tokens | Validity |
|------|-------|--------|----------|
| Starter | $9.9 | 2M tokens | 7 days |
| Basic | $49 | 10M tokens | 30 days |
| Pro | $199 | 50M tokens | 90 days |

---

## 📞 Contact

- **Email**: [your-email@example.com]
- **Twitter**: [@your-handle]
- **Discord**: [your-discord]

**Free Trial**: Contact us for 100K free tokens!

---

## ❓ FAQ

### Q: How does it compare to GPT-4?
A: Qwen2.5-7B excels in Chinese scenarios, at 1/100th the price of GPT-4. Perfect for budget-conscious projects.

### Q: What's the uptime?
A: Currently 99%+ uptime, <500ms response time. For higher SLA, consider big cloud providers.

### Q: Do you store my data?
A: No. All requests are processed in-memory, not stored, not used for training.

### Q: Can I get a refund?
A: Yes. Unused credits within 7 days of purchase are fully refundable.

---

## 📄 License

MIT License

---

**🎉 Start building today! Contact us for free trial!**
