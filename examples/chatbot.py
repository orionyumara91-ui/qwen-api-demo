#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的 AI 聊天机器人示例
使用 Qwen AI API
"""

import requests

API_URL = "http://58.144.141.41:8000/v1/chat/completions"
API_KEY = "sk-autodl-gpu-token"

def chat(message, history=None):
    """
    和 AI 聊天
    
    Args:
        message: 用户消息
        history: 对话历史（可选）
    
    Returns:
        AI 回复
    """
    if history is None:
        history = []
    
    messages = history + [{"role": "user", "content": message}]
    
    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "messages": messages,
            "max_tokens": 1024,
            "temperature": 0.7
        }
    )
    
    result = response.json()
    ai_reply = result["choices"][0]["message"]["content"]
    
    return ai_reply

def main():
    """命令行聊天机器人"""
    print("🤖 AI 聊天机器人（输入 'quit' 退出）")
    print("=" * 50)
    
    history = []
    
    while True:
        user_input = input("你：").strip()
        
        if user_input.lower() in ['quit', 'exit', '退出']:
            print("👋 再见！")
            break
        
        if not user_input:
            continue
        
        reply = chat(user_input, history)
        print(f"AI: {reply}")
        print("-" * 50)
        
        # 更新对话历史
        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    main()
