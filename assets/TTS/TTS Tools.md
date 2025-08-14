---
icon: chevron-right
order: 2000
---

``Last update: Dec 12, 2024``
***

## Introduction :icon-book:
***
- TTS is an abbreviation of Text To Speech, an AI that converts any given text into vocal speech.

- The ones listed here offer a decent variety of features & options, such as <u>[model training](https://docs.aihub.gg/extra/glossary/#model-training)</u>, <u>[fine-tuning](https://docs.aihub.gg/extra/glossary/#fine-tuning)</u>, <u>[0 shot training](https://docs.aihub.gg/extra/glossary/#0-shot-training)</u>, or being <u>[mixed with RVC](https://ominous-waffle-r44vr6g95vvj2wqrx-5000.app.github.dev/other-ai/tts-tools/#rvc-forks)</u>.

- Here's an index of the best TTS tools out there:    
‎
***
## ElevenLabs/11Labs
- <u>[ElevenLabs](https://elevenlabs.io/)</u> is a **freemium** service that offers TTS, training TTS models & translating videos from different languages.  

‎
***
## Fish Speech
- Fish speech is a 0shot multilingual TTS model created by <u>[Fish Audio](https://fish.audio)</u>. 

- This is one of the best 0shot TTS as of now, it rarely hallucinates.

- It can be used either locally or on the cloud.

 +++ :icon-device-desktop: ‎ LOCAL
 - :icon-repo-forked: <u>[Offical github repo](https://github.com/fishaudio/fish-speech)</u>

 +++ :icon-cloud: ‎ CLOUD

- :icon-rocket: <u>[Offical site](https://fish.audio/)</u>
- :icon-rocket: <u>[HuggingFace Space](https://huggingface.co/spaces/fishaudio/fish-speech-1)</u>

 +++

***
## F5 TTS
- F5 is the best 0shot TTS model.

- F5 gives fairly high quality outputs that rarely hallucinate.

- But it is limited with issue like: Reading to fast = you are using a reference audio that is more the six seconds long or 100 characters. Hallucinates on low voices.

- It can be used either locally or on the cloud.

 +++ :icon-device-desktop: ‎ LOCAL
 - :icon-repo-forked: <u>[Offical github repo](https://github.com/SWivid/F5-TTS)</u>

 +++ :icon-cloud: ‎ CLOUD

- :icon-rocket: <u>[HuggingFace Space](https://huggingface.co/spaces/mrfakename/E2-F5-TTS)</u>

 +++


***
###### ‎
***
## Dia TTS
- Dia generates high quality English only dialogue from a transcript.

- Dia can create nonverbal sounds like laughter, coughing, clearing throat, etc.

- It can be used either locally or on the cloud.

 +++ :icon-device-desktop: ‎ LOCAL
 - :icon-repo-forked: <u>[Offical github repo](https://github.com/nari-labs/dia)</u>

 +++ :icon-cloud: ‎ CLOUD

- :icon-rocket: <u>[HuggingFace Space](https://huggingface.co/spaces/nari-labs/Dia-1.6B)</u>

 +++


***
###### ‎
***
## Edge TTS
***
- This is Microsoft Edge TTS, which is good **quality**, multilingual & works great on long sentences. 

- It can only be used online via their API, through their web browser, a HF/Colab space or **mixed with <u>[RVC](https://docs.aihub.gg/rvc/essentials/whats-rvc/)</u>**.

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
  3. Save it as “Microsoft Edge TTS.txt”
  
  4. Rename it to “Microsoft Edge TTS.html”
  
  5. Open Microsoft Edge & drag the .html to it.

  6. Use [Audacity](https://www.audacityteam.org/download/) to record the audio. Set the recording mode to loopback to record the internal audio (Realtek driver might be needed).
  
  7. In the TTS input the text you want & click Generate. Stop recording when the voice is done.
  
  8. You can then select Voice Options in the toolbar & change the speed to a faster/slower speech.
  
  +++ :icon-cloud: ‎ SPACES
  {.list-icon}
  - 📒 [Google Colab](https://github.com/Nick088Official/Edge-TTS-Google-Colab/tree/main)   
  - 🤗 [Hugging Face](https://huggingface.co/spaces/Nick088/Edge-TTS)

  +++ :icon-dependabot: RVC FORKS
  - [Ilaria RVC](https://docs.aihub.gg/rvc/cloud/ilaria-rvc/#tts-) 
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

- Has important model changes that make **cross-language 0 Shot voice cloning** & **multilingual** speech generation super easy.

- **You need less training data. Just least a 2 minute audio.**

- Can use it either online or locally:

+++ :icon-device-desktop: LOCAL
- [Official XTTS 2 Guide](https://docs.coqui.ai/en/latest/models/xtts.html)
- [XTTS 2 UI Fork](https://github.com/BoltzmannEntropy/xtts2-ui)

+++ :icon-cloud: ONLINE
- [Inference 0 Shot Training UI Colab](https://colab.research.google.com/github/camenduru/coqui-XTTS-colab/blob/main/coqui_XTTS_v2_colab.ipynb) (Run it & click the Public Link)
- [Training & Inference UI Colab](https://colab.research.google.com/github/Nick088Official/XTTS2_UI_Inference_Training_Google_Colab/blob/main/XTTS2_Inf_Train.ipynb)
- [Inference 0 Shot Training HF Space](https://huggingface.co/spaces/coqui/xtts)
+++    
###### ‎
***
## Zonos
***
- 0 Shot TTS with great emotion controls

- Can be used with English, French, German, Chinese and Japanese

- Can be used locally or online

+++ :icon-device-desktop: LOCAL
- [Official Github Repo](https://github.com/Zyphra/Zonos)

+++ :icon-cloud: ONLINE
- [Offical Playground](https://playground.zyphra.com/audio)
- [HuggingFace Space](https://huggingface.co/spaces/Steveeeeeeen/Zonos)
+++
###### ‎
***
## Kokoro-TTS
***
- CLI TTS

- Only has premade voices

- Voice bleeding for English, British English French, Itailian, Japanese and Chinese

- Not the best emotion control

+++ :icon-device-desktop: LOCAL
- [Official Github Repo](https://github.com/nazdridoy/kokoro-tts)

+++ :icon-cloud: ONLINE
- [Offical HuggingFace Space](https://huggingface.co/spaces/hexgrad/Kokoro-TTS)
+++

###### ‎
***
## OpenVoice
***
- Has Versatile Instant Voice Cloning (aka 0 Shot Training)
- Contains cross-lingual & flexible voice style control
- Available both locally & online:

+++ :icon-device-desktop: LOCAL
{.list-icon}
- :icon-repo: [Official GitHub repo](https://github.com/myshell-ai/OpenVoice)

+++ :icon-cloud: ONLINE
- [Inference GUI Colab](https://colab.research.google.com/github/camenduru/OpenVoice-colab/blob/main/OpenVoice_colab.ipynb)
- [Official Demo Part 1 Colab](https://colab.research.google.com/github/myshell-ai/OpenVoice/blob/main/demo_part1.ipynb)
- [Official Demo Part 2 Colab](https://colab.research.google.com/github/myshell-ai/OpenVoice/blob/main/demo_part2.ipynb)
- [Official HF Space](https://huggingface.co/spaces/myshell-ai/OpenVoice)
+++    
###### ‎
***
## Piper
***
- Fast TTS

- Great multilingual support

- Works for almost all languages

- Decent quality

+++ :icon-device-desktop: LOCAL
- [Official Github Repo](https://github.com/rhasspy/piper)

+++ :icon-cloud: ONLINE
- [Github Repo with Colabs](https://github.com/rmcpantoja/piper/tree/master/notebooks) (For training and inference)
- [Several HuggingFace Spaces for each Language](https://huggingface.co/spaces?q=piper+tts)
+++

###### ‎
***
## MeloTTS
***
- MeloTTS is a **high-quality multilingual** TTS library, made by MyShell.ai

- Includes almost **real-time inference**.

- It can be used both locally and online:

+++ :icon-device-desktop: LOCAL
- [Official GitHub Repo](https://github.com/myshell-ai/MeloTTS)

+++ :icon-cloud: ONLINE
- [UI Colab](https://colab.research.google.com/github/Nick088Official/MeloTTS-Google-Colabs/blob/main/MeloTTS_UI.ipynb)
- [NO UI Colab](https://colab.research.google.com/github/Nick088Official/MeloTTS-Google-Colabs/blob/main/MeloTTS_NO_UI.ipynb)
- [HF Space](https://huggingface.co/spaces/mrfakename/MeloTTS)
+++    
###### ‎
***
## GPT-SoVITS
***
- GPT-SoVITS has **cross language** inference, but there could be some noises.
- It's very good with **Chinese**, but also with English.
- **Most parts are in japanese & not deeply tested.** Expect some instability.

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