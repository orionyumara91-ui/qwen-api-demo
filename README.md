# Qwen AI API - 便宜 50% 的大模型 API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)

**比大厂便宜 50% 的 AI API 服务**，基于 Qwen2.5-7B-Instruct 模型，适合个人项目、学习测试、小型应用。

---

## 🚀 特点

- **价格优惠**: ¥0.002/1K tokens（阿里云/腾讯云的 5 折）
- **响应快速**: <500ms
- **中文优化**: Qwen2.5-7B-Instruct，中文能力强
- **适合场景**: 学习测试、个人项目、原型开发、小应用

---

## 📊 价格对比

| 服务商 | 输入价格 | 输出价格 | 对比 |
|--------|---------|---------|------|
| 阿里云百炼 | ¥0.005/1K | ¥0.012/1K | - |
| 腾讯云混元 | ¥0.004/1K | ¥0.010/1K | - |
| **我们的服务** | **¥0.002/1K** | **¥0.006/1K** | **省 50-60%** |

**示例**：生成一篇 1000 字的文章
- 阿里云：约¥0.15
- 我们的服务：约¥0.06
- **节省：60%**

---

## 🎯 适合谁用

✅ **个人开发者** - 做 AI 应用、学习测试  
✅ **学生** - 毕业设计、课程项目  
✅ **独立开发者** - MVP 原型验证  
✅ **小创业公司** - 预算有限，需要快速验证  
✅ **接外包的** - 帮客户集成 AI 功能  

❌ **不适合**: 需要 99.99% SLA 的大企业（建议用大厂）

---

## 📖 快速开始

### 1. 获取 API Key

联系微信/邮箱获取免费测试额度（10 万 tokens）

### 2. 调用示例

#### Python 示例

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
            {"role": "user", "content": "你好，请介绍一下你自己"}
        ],
        "max_tokens": 1024
    }
)

result = response.json()
print("回复:", result["choices"][0]["message"]["content"])
print("Token 使用:", result["usage"])
```

#### cURL 示例

```bash
curl -X POST http://58.144.141.41:8000/v1/chat/completions \
  -H 'Authorization: Bearer sk-autodl-gpu-token' \
  -H 'Content-Type: application/json' \
  -d '{
    "messages": [
      {"role": "user", "content": "你好"}
    ]
  }'
```

#### JavaScript 示例

```javascript
const response = await fetch('http://58.144.141.41:8000/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer sk-autodl-gpu-token',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    messages: [
      { role: 'user', content: '你好' }
    ]
  })
});

const result = await response.json();
console.log(result.choices[0].message.content);
```

---

## 🛠️ 示例项目

### 1. 聊天机器人
[查看示例代码](examples/chatbot.py)

### 2. 内容生成工具
[查看示例代码](examples/content-generator.py)

### 3. 数据分析助手
[查看示例代码](examples/data-analyst.py)

---

## 📋 API 文档

### 接口地址
```
http://58.144.141.41:8000/v1/chat/completions
```

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| messages | array | ✅ | 对话历史 |
| max_tokens | integer | ❌ | 最大生成 tokens，默认 1024 |
| temperature | float | ❌ | 温度，0-1，默认 0.7 |

### 响应格式

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
      "content": "你好！我是 Qwen..."
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

## 💰 价格说明

### 计费方式
- **输入 Token**: ¥0.002 / 1K tokens
- **输出 Token**: ¥0.006 / 1K tokens

### 免费测试
- 新用户注册送 **10 万 tokens** 免费额度
- 足够测试和开发使用

### 付费套餐
| 套餐 | 价格 | Token 数量 | 有效期 |
|------|------|-----------|--------|
| 体验包 | ¥9.9 | 200 万 | 7 天 |
| 基础包 | ¥49 | 1000 万 | 30 天 |
| 专业包 | ¥199 | 5000 万 | 90 天 |

---

## 📞 联系方式

- **微信**: [你的微信]
- **邮箱**: [你的邮箱]
- **QQ 群**: [你的 QQ 群]

**免费测试**: 联系获取 10 万 tokens 测试额度！

---

## ❓ 常见问题

### Q: 和 OpenAI/GPT-4 比怎么样？
A: Qwen2.5-7B 在中文场景下表现优秀，价格只有 GPT-4 的 1/100，适合预算有限的项目。

### Q: 稳定性如何？
A: 目前正常运行时间 99%+，响应时间<500ms。如需更高 SLA，建议用大厂服务。

### Q: 数据会存储吗？
A: 不会。所有请求数据内存处理，不落地存储，不用于模型训练。

### Q: 可以退款吗？
A: 可以。购买 7 天内 unused 额度可全额退款。

---

## 📄 License

MIT License

---

**🎉 立即开始使用，联系获取免费测试额度！**
