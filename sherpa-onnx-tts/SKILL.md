---
name: sherpa-onnx-tts
description: Use when generating offline speech on Windows with the installed Sherpa ONNX/Piper voice, or checking the local Sherpa runtime and model.
metadata:
  source: /home/youssef/AppData/Roaming/npm/node_modules/openclaw/skills/sherpa-onnx-tts/SKILL.md
---

# Native Windows offline speech

Source: `/home/youssef/AppData/Roaming/npm/node_modules/openclaw/skills/sherpa-onnx-tts/SKILL.md`.
OpenCode adapter: `/home/youssef/.config/opencode/openclaw/runtime/voice.mjs`.

```powershell
node /home/youssef/.config/opencode/openclaw/runtime/voice.mjs check
node /home/youssef/.config/opencode/openclaw/runtime/voice.mjs sherpa --text "Your short spoken summary." --output /home/youssef/.config/opencode/openclaw/artifacts/reply.wav
```

Use a new output filename and verify its parent directory exists. The adapter reads `SHERPA_ONNX_RUNTIME_DIR` and `SHERPA_ONNX_MODEL_DIR` from the existing OpenClaw skill configuration and passes them to the native Node wrapper. OpenCode does not inject OpenClaw's skill environment automatically.

The installed voice is English Lessac high quality. Keep speech concise, preserve the full text response separately and verify the resulting WAV. Synthesis is local; returning a file is separate from any requested channel delivery.
