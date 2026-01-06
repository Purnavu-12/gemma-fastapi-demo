# Gemma-fastapi-demo
"Local Gemma2 2B-IT Chat API with Ollama + FastAPI | GSoC 2026 Prep @ Google DeepMind 🚀"

## Gemma2 FastAPI Chat Demo 🔥

A simple local chat API using **Gemma2 2B** via Ollama + FastAPI.

## Why?
Exploring Gemma models and building developer tools .

## Features
- Real-time chat with Gemma2 (instruction-tuned)
- FastAPI backend (Swagger UI at /docs)
- Easy local setup

## Requirements
1. fastapi
2. uvicorn
3. requests
- use this command: `pip install fastapi uvicorn requests`

## Quick Start
1. Install Ollama: https://ollama.com
2. `ollama run gemma2:2b-it`
3. In another terminal: `ollama serve`
4. `pip install -r requirements.txt`
5. `python app.py`
6. Open http://127.0.0.1:8000/docs

Excited about Gemma ecosystem! 🚀
