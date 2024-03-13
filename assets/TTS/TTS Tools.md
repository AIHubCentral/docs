---
icon: chevron-right
order: 2000
---

``Last update: Mar 4, 2024``
***

## Introduction :icon-book:
***
- TTS is an abbreviation of Text To Speech, an AI that converts any given text into vocal speech.

- The ones listed here offer a decent variety of features & options, such as <u>[model training](https://docs.aihub.wtf/extra/glossary/#model-training)</u>, <u>[fine-tuning](https://docs.aihub.wtf/extra/glossary/#fine-tuning)</u>, <u>[0 shot training](https://docs.aihub.wtf/extra/glossary/#0-shot-training)</u>, or being <u>[mixed with RVC](https://ominous-waffle-r44vr6g95vvj2wqrx-5000.app.github.dev/other-ai/tts-tools/#rvc-forks)</u>.

- Here's an index of the best TTS tools out there:    
‎
***
## ElevenLabs/11Labs
***
- <u>[ElevenLabs](https://elevenlabs.io/)</u> is a **freemium** service (only one in this guide) that offers TTS, training TTS models & translating videos from different languages.    
‎
***
## Bark TTS
***

- Bark is a **multilingual** TTS model created by <u>[Suno AI](https://www.suno.ai/)</u>. 
- It’s characterized by its great ability to express **emotions** & non-speech sounds.
- Examples are laughter, laughs, sighs, gasps, clearing throat, hesitations ( - or … ), emphasis of words, etc.

- It can be used both <u>[locally](https://docs.aihub.wtf/extra/glossary/#local-running)</u> or in the <u>[cloud](https://docs.aihub.wtf/rvc/extra/glossary/#cloud-based)</u>:

  +++ :icon-device-desktop: ‎ LOCAL
  
  {.list-icon}
  - :icon-book: [Official Guide](https://github.com/suno-ai/bark)
  - :icon-repo-forked: [Fixed Fork](https://github.com/Nick088Official/bark-gui-fix) (with UI & [fine-tuning](https://docs.aihub.wtf/extra/glossary/#fine-tuning))
  - :icon-rocket: [Voice Cloning](https://github.com/KevinWang676/Bark-Voice-Cloning/tree/main)

  +++ :icon-cloud: ‎ CLOUD

  - [Bark TTS Colab](https://colab.research.google.com/github/Nick088Official/Easier-Bark-TTS-Google-Colab/blob/main/Easier_Bark_TTS.ipynb)
  - [GUI Version](https://colab.research.google.com/github/Nick088Official/bark-gui-fix-google-colab/blob/main/Bark_GUI_Fix.ipynb) (with [fine-tuning](https://docs.aihub.wtf/extra/glossary/#fine-tuning))
  - [0 Shot Voice Cloning](https://colab.research.google.com/github/Nick088Official/Easier-Bark-Voice-Cloning-Google-Colab/blob/main/Bark_Voice_Cloning.ipynb)
  - [Official HF Space](https://huggingface.co/spaces/suno/bark)
  - [0 Shot Voice Cloning HF Space](https://huggingface.co/spaces/kevinwang676/Bark-with-Voice-Cloning)
    - For training you'll need a paid GPU. Otherwise you can only TTS.
  +++    
###### ‎
***
## Edge TTS
***
- This is Microsoft Edge TTS, which is good **quality**, multilingual & works great on long sentences. 

- It can only be used online via their API, through their web browser, a HF/Colab space or **mixed with <u>[RVC](https://docs.aihub.wtf/rvc/essentials/whats-rvc/)</u>**.

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
  - [Ilaria RVC](https://docs.aihub.wtf/rvc/cloud/ilaria-rvc/#tts-) 
  - [Applio Colab](https://docs.aihub.wtf/rvc/cloud/applio-colab/#tts)
  - [Local Applio](https://docs.aihub.wtf/rvc/local/applio/)   
  ‎
  !!!
  These being mixed with RVC means it generates the speech & runs the output through RVC, applying the voice model.
  !!!    
###### ‎
***
## StyleTTS2
***
- StyleTTS 2 aims to achieve human-level TTS synthesis only in English.   
‎   
- It works better on full sentences, is both available locally & online, and you can [fine-tune](https://docs.aihub.wtf/extra/glossary/#fine-tuning) it with your own dataset.    
‎   
- It has 2 versions:   
‎       
  - <u>**LJSpeech**</u>:     
  Its dataset should only be of **single-speaker** recordings. Suitable for training models with a consistent voice.      
  ‎   
  - <u>**LibriTTS**</u>:    
  Its dataset can be of **multispeaker** recordings. Allows StyleTTS 2 to adapt to different voices.    
‎   
+++ :icon-device-desktop: LOCAL
{.list-icon}
- :icon-book: [Official StyleTTS2 Guide](https://github.com/yl4579/StyleTTS2)

+++ :icon-cloud: ONLINE
- [LJSpeech Colab](https://colab.research.google.com/github/yl4579/StyleTTS2/blob/main/Colab/StyleTTS2_Demo_LJSpeech.ipynb)
- [LibriTTS Colab](https://colab.research.google.com/github/yl4579/StyleTTS2/blob/main/Colab/StyleTTS2_Demo_LibriTTS.ipynb)
- [StyleTTS2 Finetuning Colab](https://colab.research.google.com/github/yl4579/StyleTTS2/blob/main/Colab/StyleTTS2_Finetune_Demo.ipynb)     
- [StyleTTS2 HF Space](https://huggingface.co/spaces/styletts2/styletts2) (Duplicate the space to skip queue. Without GPU you can only infer)
+++    
###### ‎
***
## Tortoise TTS
***
- Expressive but a little slow. Available both locally & online.

+++ :icon-device-desktop: LOCAL
{.list-icon}
- :icon-repo: [Official Github Repository](https://github.com/neonbjb/tortoise-tts)

+++ :icon-cloud: ONLINE
- [Colab Space](https://colab.research.google.com/github/Nick088Official/Easier-Tortoise-TTS-Google-Colab/blob/main/Easier_Tortoise_TTS.ipynb)
- [HF Space](https://huggingface.co/spaces/Manmay/tortoise-tts)
+++    
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
## MetaVoice-1B
***
- MetaVoice-1B is a 1.2B parameter base model, trained on **100k hours** of speech for TTS.   
‎   
- It has been built with the following priorities:
  - Emotional speech rhythm and tone in English.
  - Zero-shot cloning for American & British voices, with 30s reference audio.    
‎     
- Available both locally & online:

+++ :icon-device-desktop: LOCAL
{.list-icon}
- :icon-repo: [Model Github Repo](https://github.com/metavoiceio/metavoice-src) 

+++ :icon-cloud: ONLINE
- [TTS with 0 Shot Training Demo](https://ttsdemo.themetavoice.xyz/) | [Easier Version](https://colab.research.google.com/github/Nick088Official/Easier-MetaVoice-1B-Google-Colab/blob/main/Easier_MetaVoice_1B.ipynb)
- [TTS with 0 Shot Training HF Space](https://huggingface.co/spaces/mrfakename/MetaVoice-1B-v0.1)
- [Freemium MetaVoice Studio](https://colab.research.google.com/github/Nick088Official/Easier-MetaVoice-1B-Google-Colab/blob/main/Easier_MetaVoice_1B.ipynb) (Only premade voices)
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
***
## gTTS
***
- It's **Google Text To Speech**, which is the same one used in **Google Translate**.   
‎     
- It has **very few voices** in different languages, is a little **robotic** & doesn’t let you choose the gender of the voice (except in the Colab, but it's not that great).   
‎    
- It can be used only online (API):
‎     
  - [Colab Space](https://colab.research.google.com/github/Nick088Official/gTTS-Google-Colab/blob/main/gTTS.ipynb)
  - [HF Space](https://huggingface.co/spaces/Nick088/gTTS)
  - [Official Guide](https://github.com/pndurette/gTTS)
  - [Google Translate](https://translate.google.com/)

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.wtf/rvc/#contributions)
:::