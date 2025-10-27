

## Alternative TTS engines

- Open Text to Speech Server: https://github.com/synesthesiam/opentts?tab=readme-ov-file
```bash
docker run -it -p 5500:5500 synesthesiam/opentts:all
```
- Coqui.ai TTS: https://github.com/coqui-ai/TTS
```bash
docker run --rm -it -p 5002:5002 --entrypoint /bin/bash ghcr.io/coqui-ai/tts-cpu
python3 TTS/server/server.py --list_models #To get the list of available models
python3 TTS/server/server.py --model_name tts_models/en/vctk/vits # To start a server
```
- piper-tts: https://github.com/OHF-Voice/piper1-gpl?tab=readme-ov-file
- TTS: https://github.com/coqui-ai/TTS
