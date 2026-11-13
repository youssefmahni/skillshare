---
name: voice-copilot
description: Use when the user requests speech-to-text dictation, voice-driven coding, or screen-contextual prompt execution using the native Windows C++ Whisper and local Ollama engine.
metadata:
  source: Native C++ Windows Voice Assistant
---

# Native Voice & Screen Copilot for OpenCode

This skill utilizes the local high-performance native Windows C++ assistant (`NativeVoiceAssistant.exe`) connected via `\\.\pipe\opencode_voice`.

## Capabilities
- **Direct Speech Dictation:** Uses `whisper.cpp` with AVX2 multi-core acceleration on 8 threads.
- **Contextual Desktop Copilot:** Reads active foreground window title, process, caret position, and selected text using Windows UI Automation (`IUIAutomation`).
- **Ollama Intelligence:** Polishes speech and executes voice instructions via local Ollama models (`gemma3:latest` or `qwen3:4b`) on the NVIDIA RTX 5090 GPU in under 60ms.
- **IPC Pipe Integration:** Automatically populates the OpenCode prompt buffer when the user speaks via Push-to-Talk (default: `F8`).

## Launching the Voice Daemon
Ensure the background service is running:
```powershell
Start-Process -FilePath "C:\Users\DarknessEye\NativeVoiceAssistant\build\NativeVoiceAssistant.exe" -WindowStyle Hidden
```
Or double-click `Run_Voice_Assistant.bat` on the Desktop.
