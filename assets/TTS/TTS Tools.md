---
icon: chevron-right
order: 2000
---

``Last update: March 23, 2026``
***

## Introduction :icon-book:
***
- TTS is an abbreviation of Text To Speech, an AI that converts any given text into vocal speech.

- The ones listed here offer a decent variety of features & options, such as [model training](https://docs.aihub.gg/extra/glossary/#model-training), [fine-tuning](https://docs.aihub.gg/extra/glossary/#fine-tuning), [0-shot training](https://docs.aihub.gg/extra/glossary/#0-shot-training), or being [mixed with RVC](https://ominous-waffle-r44vr6g95vvj2wqrx-5000.app.github.dev/other-ai/tts-tools/#rvc-forks).

- The TTS landscape moves fast — new state-of-the-art models appear every few months. Always check the linked GitHub repos and HuggingFace pages for the latest model versions, as entries here reflect what was current at the last update date above.

- Here's an index of the best TTS tools out there:
‎
***
## ElevenLabs/11Labs
- [ElevenLabs](https://elevenlabs.io/) is a **freemium** service that offers TTS, voice cloning, video translation & an AI voice agent platform.

- Now on their **Eleven v3** model, which introduced an **audio tag system** for fine-grained emotion and delivery control directly in your script (e.g. `[nervous]`, `[laughs]`, `[whispering]`), as well as a **Text to Dialogue** feature for multi-speaker conversations in a single generation.

- Supports **32+ languages** and offers both instant voice cloning (from ~1 min of audio) and professional voice cloning (30+ min) for higher fidelity.

!!!
ElevenLabs' older v1 TTS models are deprecated as of December 2025. Make sure to use v2 or v3 models.
!!!

‎
***
## Fish Speech / FishAudio S1
- Fish Speech is a 0-shot multilingual TTS developed by [Fish Audio](https://fish.audio). The project has since rebranded: the current flagship model is **FishAudio S1** (also known as **OpenAudio S1**).

- S1 is a 4B parameter model focused on generating speech that sounds genuinely human — natural intonation, pauses, and emotional intent rather than polished studio audio. A distilled **S1-mini** (0.5B params) is also available open-source on HuggingFace.

- Achieves **#1 ranking on TTS-Arena2** (the main public TTS leaderboard), with **0.008 WER** and **0.004 CER** on English — significantly better than prior models.

- Supports **fine-grained open-domain emotion control** with a large set of explicit tags. Basic emotions include: `(angry)` `(sad)` `(excited)` `(surprised)` `(scared)` `(nervous)` `(confused)` `(joyful)` and many more. Tone markers include `(shouting)` `(whispering)` `(soft tone)`. Special audio effects include `(laughing)` `(chuckling)` `(sobbing)` `(sighing)`. Tags work across English, Chinese, Japanese, German, French, Spanish, Korean, Arabic, Russian, and more.

- Zero-shot voice cloning from a 10–30 second reference sample, with no additional fine-tuning required.

- It can be used either locally or on the cloud.

!!!
The codebase is **Apache 2.0**; model weights are **CC-BY-NC-SA-4.0** (non-commercial). Commercial use of S1 is available via the Fish Audio API/platform.
!!!

 +++ :icon-device-desktop: ‎ LOCAL
 - :icon-repo-forked: [Official GitHub repo](https://github.com/fishaudio/fish-speech)

 +++ :icon-cloud: ‎ CLOUD

- :icon-rocket: [Official site / App](https://fish.audio/)
- :icon-rocket: [HuggingFace Space (S1-mini)](https://huggingface.co/spaces/fishaudio/openaudio-s1-mini)

 +++

***
## Higgs Audio
- Higgs Audio V2 is an **open-source audio foundation model** developed by [Boson AI](https://www.boson.ai/), released in July 2025 under the **Apache 2.0 license**, making it freely usable for commercial projects.

- Pretrained on over **10 million hours of audio** (speech, music, and sound events in a single unified system). Built on top of Llama-3.2-3B with a custom **DualFFN** adapter and a 24kHz audio tokenizer running at just 25 frames per second.

- Goes beyond traditional TTS with several emergent capabilities rarely seen in open-source models: zero-shot multi-speaker dialogues, **automatic prosody adaptation** based on narrative context, **melodic humming** with the cloned voice, and simultaneous speech & background music generation.

- On EmergentTTS-Eval, it achieves **75.7% win rate over GPT-4o-mini-TTS** on emotion expressiveness — the best result of any open-source model at time of release.

- The model family also includes a lightweight **V2.5** (1B params, GRPO-aligned), which outperforms V2 on speed and accuracy while being smaller.

- Can be used locally or on the cloud.

!!!
The full V2 (3B params) requires at least an RTX 4090 for efficient inference. **V2.5 (1B params) is recommended for most users** — it outperforms V2 on speed and accuracy and runs comfortably on 8GB+ VRAM GPUs, as well as via managed platforms (Microsoft Foundry, Eigen AI, Deep Infra) with no local GPU needed.
!!!

+++ :icon-device-desktop: LOCAL
- [Official GitHub Repo](https://github.com/boson-ai/higgs-audio)

+++ :icon-cloud: ONLINE
- [HuggingFace Space](https://huggingface.co/spaces/smola/higgs_audio_v2)
- [Replicate API](https://replicate.com/lucataco/higgs-audio-v2)
+++
###### ‎
***
## VibeVoice
- VibeVoice is a **family of open-source frontier voice AI models** developed by Microsoft Research, released under the **MIT License**.

- A core innovation is its use of continuous speech tokenizers (Acoustic & Semantic) operating at an ultra-low frame rate of **7.5 Hz**, feeding into a next-token diffusion framework for high-fidelity acoustic detail.

- The family currently has three active models:
  - **VibeVoice-TTS-1.5B** — Long-form multi-speaker TTS. Synthesizes speech up to **90 minutes** in a single pass, with up to **4 distinct speakers** and natural turn-taking. Supports English and Chinese. Weights are on HuggingFace; community-maintained inference code is available.
  - **VibeVoice-Realtime-0.5B** — Lightweight real-time streaming TTS (~300ms first-audio latency). Includes 9 experimental multilingual voices (DE, FR, IT, JP, KR, NL, PL, PT, ES) and 11 English style voices.
  - **VibeVoice-ASR-7B** — Long-form speech recognition (up to 60 minutes), generating structured transcriptions with speaker diarization and timestamps. Supports 50+ languages.

- Can be used locally or on the cloud.

!!!
Microsoft pulled the original VibeVoice-TTS inference code on September 5, 2025 due to misuse. The **1.5B weights remain available** on HuggingFace, and community Colabs using them exist. The Realtime-0.5B and ASR models are fully open with official code.
The model card explicitly states VibeVoice is for **research use only** — not recommended for commercial deployment without further testing.
!!!

+++ :icon-device-desktop: LOCAL
- [Official GitHub Repo](https://github.com/microsoft/VibeVoice)
- [HuggingFace Model (TTS 1.5B)](https://huggingface.co/microsoft/VibeVoice-1.5B)
- [HuggingFace Model (Realtime 0.5B)](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B)

+++ :icon-cloud: ONLINE
- [Colab (TTS 1.5B, community)](https://colab.research.google.com/github/microsoft/VibeVoice/blob/main/demo/VibeVoice_colab.ipynb)
- [Colab (Realtime 0.5B, official)](https://colab.research.google.com/github/microsoft/VibeVoice/blob/main/demo/vibevoice_realtime_colab.ipynb)
- [ASR Playground (official)](https://aka.ms/vibevoice-asr)
+++
###### ‎
***
## Chatterbox
- Chatterbox is a **production-grade open-source TTS** family developed by [Resemble AI](https://www.resemble.ai/chatterbox/), released under the **MIT License**.

- Consistently **outperforms ElevenLabs** in blind side-by-side evaluations (63.75% preference rate in independent testing).

- **First open-source TTS model with emotion exaggeration control** — dial expressiveness from monotone to dramatic with a single parameter.

- The family includes three variants:
  - **Chatterbox** — High-quality English TTS with 0-shot voice cloning & emotion control (0.5B params)
  - **Chatterbox Multilingual** — Supports 23 languages with 0-shot voice cloning
  - **Chatterbox Turbo** — Fastest variant (350M params), sub-200ms latency, designed for real-time voice agents. Supports paralinguistic tags like `[laugh]`, `[cough]`, `[chuckle]` natively.

- All outputs include an imperceptible **neural watermark** (Perth Watermarker) for responsible AI use.

- It can be used locally or on the cloud.

 +++ :icon-device-desktop: ‎ LOCAL
 - :icon-repo-forked: [Official GitHub repo](https://github.com/resemble-ai/chatterbox)

 +++ :icon-cloud: ‎ CLOUD

- :icon-rocket: [HuggingFace Space (English)](https://huggingface.co/spaces/ResembleAI/Chatterbox)
- :icon-rocket: [HuggingFace Space (Multilingual)](https://huggingface.co/spaces/ResembleAI/Chatterbox-Multilingual-TTS)

 +++

***
## Orpheus TTS
- Orpheus is a **Llama-3B based** open-source TTS developed by [Canopy AI](https://canopylabs.ai/), released in March 2025.

- Designed for **human-like speech** — natural intonation, emotion and rhythm that rivals closed-source models.

- Supports **0-shot voice cloning** and **guided emotion control** via simple inline tags (e.g. `<laugh>`, `<sigh>`, `<gasp>`, `<cough>`).

- Achieves ~200ms streaming latency for real-time applications, reducible to ~100ms with input streaming.

- A family of **multilingual models** also exists, covering Chinese, Hindi, Korean, and Spanish.

- It can be used locally or on the cloud.

 +++ :icon-device-desktop: ‎ LOCAL
 - :icon-repo-forked: [Official GitHub repo](https://github.com/canopyai/Orpheus-TTS)

 +++ :icon-cloud: ‎ CLOUD

- :icon-rocket: [HuggingFace Space](https://huggingface.co/spaces/MohamedRashad/Orpheus-TTS)
- :icon-rocket: [Colab (Finetuned model)](https://colab.research.google.com/drive/1KhXT56UePPUHhqitJNUxq63k-pQomz3N?usp=sharing)

 +++

***
## IndexTTS
- IndexTTS is an **industrial-level zero-shot TTS** developed by Bilibili (Index Team), built on top of XTTS/Tortoise with significant architectural improvements.

- Uses a **conformer-based speech conditioning encoder** and **BigVGAN2** decoder, giving it the lowest Word Error Rate of all evaluated models — ideal for audiobook production and content where accuracy is paramount.

- The latest release is **IndexTTS-2** (September 2025), which achieves state-of-the-art emotional fidelity, decouples **timbre from emotion** (independent control of voice identity and expression via style prompts or natural-language descriptions), and introduces the **first precise duration control** mechanism in an autoregressive TTS model — specifying audio length to the millisecond for video dubbing use cases.

!!!
The precise **duration control** feature exists in the research paper but is **not yet enabled** in the current public release code. The rest of the model (0-shot cloning, emotion control, timbre decoupling) is fully functional.
!!!


- Can be used locally or on the cloud.

+++ :icon-device-desktop: LOCAL
- [Official GitHub Repo](https://github.com/index-tts/index-tts)

+++ :icon-cloud: ONLINE
- [HuggingFace Space (IndexTTS-2)](https://huggingface.co/spaces/IndexTeam/IndexTTS-2-Demo)
+++

***
## OuteTTS
- OuteTTS is a novel TTS approach built on **pure language modeling** — no external adapters, encoders, or diffusion steps. Speech is generated directly from text and audio tokens using a standard LLM backbone (Qwen3).

- Now on **v1.0** (released September 2025), offering strong 0-shot voice cloning from a reference audio clip. Built-in default speaker profiles are currently English-only, but reference-based cloning works across languages including Chinese, Japanese, Korean, German, and French via zero-shot generalization from v0.3 onwards.

- Particularly well-suited for **local and edge deployment**: supports GGUF, EXL2, Transformers, and vLLM backends out of the box, meaning you can run it with llama.cpp on modest hardware with no dedicated GPU required.

- Available under the **MIT License**.

+++ :icon-device-desktop: LOCAL
- [Official GitHub Repo](https://github.com/edwko/OuteTTS)

+++ :icon-cloud: ONLINE
- [HuggingFace Space (v0.3 demo)](https://huggingface.co/spaces/OuteAI/OuteTTS-0.3-Demo)
+++

***
###### ‎
***
## Dia TTS
- Dia generates high quality **English-only dialogue** from a transcript.

- Now on **Dia2** (released November 19, 2025), with improved voice consistency, zero-shot voice cloning via audio prompts, and native HuggingFace Transformers support.

- Can create nonverbal sounds like laughter, coughing, clearing throat, etc., using simple inline tags like `(laughs)` and `(sighs)`.

- Requires ~8–10GB VRAM. Runs at ~40 tokens/second on an A4000.

- It can be used either locally or on the cloud.

 +++ :icon-device-desktop: ‎ LOCAL
 - :icon-repo-forked: [Official GitHub repo](https://github.com/nari-labs/dia)

 +++ :icon-cloud: ‎ CLOUD

- :icon-rocket: [HuggingFace Space](https://huggingface.co/spaces/nari-labs/Dia-1.6B)

 +++

***
###### ‎
***
## Edge TTS
***
- This is Microsoft Edge TTS, which is **good quality**, multilingual & works great on long sentences.

- It can only be used online via their API, through their web browser, a HF/Colab space or **mixed with [RVC](https://docs.aihub.gg/rvc/essentials/whats-rvc/)**.

  +++ :icon-globe: ‎ BROWSER
  1. [Download the browser.](https://www.microsoft.com/en-us/edge/download?ch=1&form=MA13FJ)
  
  2. Open your Notepad & paste the following code:
  
    ```
  <!DOCTYPE html>
  <html>
  <body style="background-color:#dddddd">

  <h3 aria-hidden="true">Browser TTS "Hack"</h3>

  <textarea rows="10" cols="50" id="ttsText" style="background-color:#eeeeee"></textarea>
  <br />
  <button aria-hidden="true" onclick="genText()"><font aria-hidden="true">Generate</font></button>

  <pre id="tts"></pre>

  <script>
  function genText() {
  var x = document.getElementById("ttsText").value;
  document.getElementById("tts").innerHTML = x;
  }
  </script>



  </body>
  </html>
  ```   
  ###### ‎   
  3. Save it as "Microsoft Edge TTS.txt"
  
  4. Rename it to "Microsoft Edge TTS.html"
  
  5. Open Microsoft Edge & drag the .html to it.

  6. Use [Audacity](https://www.audacityteam.org/download/) to record the audio. Set the recording mode to loopback to record the internal audio (Realtek driver might be needed).
  
  7. In the TTS input the text you want & click Generate. Stop recording when the voice is done.
  
  8. You can then select Voice Options in the toolbar & change the speed to a faster/slower speech.
  
  +++ :icon-cloud: ‎ SPACES
  {.list-icon}
  - 📒 [Google Colab](https://github.com/Nick088Official/Edge-TTS-Google-Colab/tree/main)   
  - 🤗 [Hugging Face](https://huggingface.co/spaces/Nick088/Edge-TTS)

  +++ :icon-dependabot: RVC FORKS
  %%
  - [Ilaria RVC Zero](https://docs.aihub.gg/rvc/cloud/ilaria-rvc/#tts-) 
  %%
  - [Applio Colab](https://docs.aihub.gg/rvc/cloud/applio-colab/#tts)
  - [Local Applio](https://docs.aihub.gg/rvc/local/applio/)   
  ‎
  !!!
  These being mixed with RVC means it generates the speech & runs the output through RVC, applying the voice model.
  !!!    
###### ‎
***  
###### ‎
***
## XTTS2
***
- Built on 🐢 Tortoise TTS & developed by Coqui AI, which has been **discontinued** unfortunately.

- Has important model changes that make **cross-language 0-shot voice cloning** & **multilingual** speech generation super easy.

- **You need less training data. Just at least a 2 minute audio.**

- Full streaming support with 200ms time-to-first-chunk. Still a solid choice for fine-tuning workflows thanks to its mature training tooling — but newer models like XTTS community forks or Chatterbox are generally preferred for new projects.

- Can use it either online or locally:

+++ :icon-device-desktop: LOCAL
- [Official XTTS 2 Guide](https://docs.coqui.ai/en/latest/models/xtts.html)
- [XTTS 2 UI Fork](https://github.com/BoltzmannEntropy/xtts2-ui)

+++ :icon-cloud: ONLINE
- [Inference 0-Shot Training UI Colab](https://colab.research.google.com/github/camenduru/coqui-XTTS-colab/blob/main/coqui_XTTS_v2_colab.ipynb) (Run it & click the Public Link)
- [Training & Inference UI Colab](https://colab.research.google.com/github/Nick088Official/XTTS2_UI_Inference_Training_Google_Colab/blob/main/XTTS2_Inf_Train.ipynb)
- [Inference 0-Shot Training HF Space](https://huggingface.co/spaces/coqui/xtts)
+++    
###### ‎
***
## CosyVoice
***
- Multilingual 0-shot TTS by **Alibaba FunAudioLLM**, now on its third generation (**CosyVoice 3 / Fun-CosyVoice3**).

- Covers **9 major languages** (Chinese, English, Japanese, Korean, German, Spanish, French, Italian, Russian), **18+ Chinese dialects & accents**, and supports both multilingual and cross-lingual 0-shot voice cloning.

- Achieves state-of-the-art performance in content consistency, speaker similarity, and prosody naturalness.

- Supports **streaming inference** with ultra-low latency (~150ms).

- Can be used locally or online.

+++ :icon-device-desktop: LOCAL
- [Official GitHub Repo](https://github.com/FunAudioLLM/CosyVoice)

+++ :icon-cloud: ONLINE
- [Official HuggingFace Space](https://huggingface.co/spaces/FunAudioLLM/CosyVoice2-0.5B)
+++
###### ‎
***
## Qwen3-TTS
***
- Qwen3-TTS is a family of **advanced multilingual TTS models** developed by the Qwen team at Alibaba Cloud, released on January 22, 2026 under the **Apache 2.0 license**.

- Trained on over **5 million hours of speech data** across 10 languages (Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, and Italian), plus multiple Chinese dialectal voice profiles.

- The family ships three purpose-built model variants (available in 0.6B and 1.7B sizes):
  - **Base** — 3-second voice cloning from a reference audio clip.
  - **CustomVoice** — Style control over 9 premium preset timbres (various gender, age, language, and dialect combos) via user instructions.
  - **VoiceDesign** — Create entirely new voices from a natural-language text description (e.g. "a warm, slightly husky young male voice speaking slowly").

- Supports **streaming generation** with end-to-end synthesis latency as low as **97ms** via its proprietary Qwen3-TTS-Tokenizer-12Hz — a 12.5 Hz, 16-layer multi-codebook codec with a lightweight causal ConvNet for fast waveform reconstruction.

- Features strong **contextual understanding**: the model automatically adapts tone, speaking rate, and emotional expression based on the semantics of the input text.

- Can be used locally or on the cloud.

+++ :icon-device-desktop: LOCAL
- [Official GitHub Repo](https://github.com/QwenLM/Qwen3-TTS)

+++ :icon-cloud: ONLINE
- [Official HuggingFace Space](https://huggingface.co/spaces/Qwen/Qwen3-TTS)
+++
###### ‎
***
## Kokoro-TTS
***
- Lightweight yet **high-quality** TTS model with just 82 million parameters — one of the most downloaded TTS models on HuggingFace.

- Faster-than-realtime inference due to its StyleTTS2/ISTFTNet architecture (no encoders or diffusion steps). Processes text in under 0.3 seconds.

- **Only has premade voices** — no voice cloning. Not the best emotion control.

- Voice support for English, British English, French, Italian, Japanese and Chinese (with some voice bleeding between languages).

- Fully open-source under the **Apache 2.0 license**, making it great for commercial use.

!!!
Some standalone websites claim to be the "official Kokoro TTS" — they are unaffiliated and potentially fraudulent. Always use the links below.
!!!

+++ :icon-device-desktop: LOCAL
- [Official GitHub Repo](https://github.com/nazdridoy/kokoro-tts)

+++ :icon-cloud: ONLINE
- [Official HuggingFace Space](https://huggingface.co/spaces/hexgrad/Kokoro-TTS)
+++

###### ‎
***
## Piper
***
- Fast TTS with great **multilingual support** — works for almost all languages.

- Decent quality; primarily intended for **edge / local deployment** (runs on a Raspberry Pi with minimal latency).

- Not recommended as a primary choice for quality-focused generation — better suited for offline assistants, embedded systems, and pipelines where speed matters more than expressiveness.

+++ :icon-device-desktop: LOCAL
- [Official GitHub Repo](https://github.com/rhasspy/piper)

+++ :icon-cloud: ONLINE
- [GitHub Repo with Colabs](https://github.com/rmcpantoja/piper/tree/master/notebooks) (For training and inference)
- [Several HuggingFace Spaces for each Language](https://huggingface.co/spaces?q=piper+tts)
+++

###### ‎
***
## GLM-TTS
***
- GLM-TTS is an **industrial-grade open-source TTS** system developed by **Zhipu AI (ZAI)** — the team behind the GLM language model family — released December 11, 2025.

- Uses a two-stage LLM + Flow Matching architecture. Its standout feature is a **multi-reward reinforcement learning (GRPO) framework** that trains the model across four simultaneous reward signals (speaker similarity, character error rate, emotion accuracy, and laughter naturalness), resulting in more expressive and emotionally consistent speech than most open-source alternatives.

- On benchmarks, GLM-TTS_RL achieves the **lowest Character Error Rate (0.89) of any open-source TTS** while maintaining high speaker similarity — competitive with commercial systems like MiniMax.

- Key features:
  - **0-shot voice cloning** from just 3–10 seconds of reference audio
  - **Phoneme-level pronunciation control** via "Hybrid Phoneme + Text" input — critical for polyphone disambiguation in Chinese (e.g., the character "行" can be xíng or háng) and for professional audiobook/dubbing use cases
  - **Streaming inference** with ~400ms first-frame latency on GPU

- Primarily supports **Chinese**, with decent bilingual Chinese-English mixed-text support. Not a multilingual model.

- Available under **Apache 2.0 (code)** and **MIT (weights)** — both permit commercial use.

- Can be used locally or on the cloud.

!!!
The online demo (`audio.z.ai`) was not deployed at launch. Use the HuggingFace model weights + local inference script for now. Upcoming updates include RL-optimized weights and a 2D Vocos vocoder for improved audio quality.
!!!

+++ :icon-device-desktop: LOCAL
- [Official GitHub Repo](https://github.com/zai-org/GLM-TTS)

+++ :icon-cloud: ONLINE
- [HuggingFace Model Weights](https://huggingface.co/zai-org/GLM-TTS)
+++

###### ‎
***
## GPT-SoVITS
***
- GPT-SoVITS is a few-shot voice cloning & TTS system — just **1 minute of audio** is enough to fine-tune a voice, and zero-shot works from a 5-second reference clip.

- Very good with **Chinese**, and supports English, Japanese, Korean and Cantonese cross-language synthesis, though some noise artifacts remain in non-Chinese outputs.

- Now on **v4**, which fixes the metallic artifacts of v3 caused by non-integer upsampling and natively outputs **48kHz audio**. The new **v2Pro/v2ProPlus** variants offer v4-level quality at v2's hardware cost and speed — recommended for most users.

- Can be used both locally & online:

+++ :icon-device-desktop: LOCAL
- [Official GitHub Repo](https://github.com/RVC-Boss/GPT-SoVITS/)

+++ :icon-cloud: ONLINE
- [Colab Space](https://colab.research.google.com/github/RVC-Boss/GPT-SoVITS/blob/main/colab_webui.ipynb#scrollTo=4oRGUzkrk8C7) (with fine-tuning, inference & UI)
+++    
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/rvc/contributions/)
:::