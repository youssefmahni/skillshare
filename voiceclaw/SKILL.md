---
name: voiceclaw
description: Use when transcribing audio locally with Whisper or generating an offline Piper voice reply through the configured Ubuntu WSL runtime from OpenCode on Windows.
metadata:
  source: /home/youssef/.openclaw/workspace/skills/voiceclaw/SKILL.md
---

# VoiceClaw through WSL

Source: `/home/youssef/.openclaw/workspace/skills/voiceclaw/SKILL.md`.
Adapter: `/home/youssef/.config/opencode/openclaw/runtime/voice.mjs`.

```powershell
node /home/youssef/.config/opencode/openclaw/runtime/voice.mjs check
node /home/youssef/.config/opencode/openclaw/runtime/voice.mjs transcribe --input C:/path/to/audio.ogg
node /home/youssef/.config/opencode/openclaw/runtime/voice.mjs speak --text "Your short reply." --output /home/youssef/.config/opencode/openclaw/artifacts/voice-reply.wav
```

Supply the actual input path and a new output filename; verify the parent directory first. The adapter launches Ubuntu as `darknesseye`, translates Windows paths, passes the existing Piper/Whisper environment, and uses the installed FFmpeg directory. It invokes the original skill scripts with argument arrays.

The installed voice is `en_US-lessac-high`, not the source script's default `en_US-lessac-medium`. Whisper uses the existing English base model. Both inference paths are local and require no cloud API key.

Show the transcript, then the text reply and requested audio artifact. For a requested Telegram voice message, convert WAV to OGG Opus with the installed FFmpeg and use the actual channel tool/CLI. Speech synthesis and message delivery have separate outcomes.
