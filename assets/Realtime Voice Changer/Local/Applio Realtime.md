---
icon: chevron-right
order: 2000
---

``Last update: March 7, 2026``

***

:::content-center
## Introduction
:::

- Applio is an all-in-one RVC (Retrieval-based-Voice-Conversion) software that includes a powerful Realtime module for live voice changing.

- This guide focuses on the Applio Realtime interface, for Realtime Voice Changing.

- RVC does **NOT** mean Realtime Voice Changer. RVC means Retrieval-based-Voice-Conversion.

***

#### Is Applio Safe?

RVC Models are PyTorch Models, a Python library used for AI.
PyTorch uses serialization via Pythons' Pickle Module, converting the model to a file.
Since pickle can execute arbitrary code when loading a model, it could be theoretically used for malware, but Applio has a **built-in feature to prevent code execution along the model.**
Also, **HuggingFace has a <u>[Security Scanner](https://huggingface.co/docs/hub/security-pickle#hubs-security-scanner)</u>** which scans for any unsafe pickle exploits and uses also ClamAV for scanning dangerous files.

***

#### Pros & Cons :icon-tasklist:

==- *Learn more*
!!! *The pros & cons are subjective to your necessities.*        
!!! 
||| ✔️ **PROS** 
- Highly active development and frequent feature updates
- Uses a Web User Interface, meaning it can be run on the Cloud
- Excellent support for Nvidia (CUDA), AMD (ROCm), and Intel
- Supports the latest RVC V2 advancements and embedders
- Includes powerful audio effect racks
||| ❌ **CONS** 
- Doesn't have Audio Effects like VST Plugins.
|||
===
***
###### ‎


***
## Virtual Audio Cable

#### A Virtual Audio Cable (VAC) is what you need to use the realtime voice changer on Discord & Games.

- A VAC (Virtual Audio Cable) makes a fake audio device, used to re-route the audio of different programs.
- In Wokada Deiteris Fork context, it's used to get the output of Wokada Deiteris Fork as the input in other programs such as Discord.

!!! For Windows
Download this: <u>[VAC Lite (Virtual-Audio-Cable by Muzychenko)](https://software.muzychenko.net/freeware/vac470lite.zip)</u>.
(Be sure to not use any toher vac like VB Audio Cable.)
!!!

- Run `setup64`, not 64a, after extracting the zip to a new folder

- After installing the VAC Lite, it changes your default audio system. Click **Yes** when it asks you to open the audio device settings (or press WIN+R, type "mmsys.cpl" if you closed it already), and change your **Recording** and **Playback** devices back to your usual devices. Same for communications device aswell (right click -> set as default communication device)

!!! For Mac
Download either: 
<u>[Blackhole Virtual Audio Cable](https://existential.audio/blackhole)</u>
or
<u>[VB-Audio](https://vb-audio.com/Cable)</u>
!!!

!!! For Linux
For Debian / Ubuntu-based Systems (Ubuntu, Mint, Pop!_OS), run in the terminal:
```bash
sudo apt-get update && sudo apt-get install -y portaudio19-dev
```


For Fedora / RHEL-based Systems (CentOS, Rocky Linux), run in the terminal:
```bash
sudo yum install -y portaudio
```

For Arch / Arch-based Systems (Endeavour, Manjaro Linux), run in the terminal:
```bash
sudo pacman -Syu portaudio
```
!!!


***
## Get Applio

1. Install and Run Applio according to the <u>[main Applio installation guide](http://docs.aihub.gg/rvc/local/applio/#download--installation)</u>.
2. [Upload your RVC Voice Model](http://docs.aihub.gg/rvc/local/applio/#upload-models).
2. Navigate to the **Realtime** tab in the top navigation menu.
3. You must agree to the **Terms of Use** before the settings become accessible.

<img src="../applio-realtime-img/realtime-tab.png" alt="Applio Realtime Terms of Use" width="800" height="auto">

***

## Settings Explained

### 1. Audio Settings
<img src="../applio-realtime-img/audio-settings.png" alt="Audio Settings" width="800" height="auto">

- **Input Device:** Your microphone.
- **Output Device:** Your Virtual Audio Cable.
- **Input Gain (*)**: Adjusts the input volume before processing. Prevents clipping or boosts a quiet mic.
- **Output Gain (*)**: Adjusts the final volume of the converted voice after processing.
- **Input ASIO Channel**: For ASIO drivers, selects a specific input channel. Leave at -1 for default.
- **Output ASIO Channel**: For ASIO drivers, selects a specific output channel. Leave at -1 for default.
- **Enable VAD:** Highly recommended to save CPU/GPU resources by processing audio only when you speak.

<img src="../applio-realtime-img/monitor-device.png" alt="Monitor Device (Optional)" width="800" height="auto">

- **Monitor Device (Optional):** Select your headphones if you wish to hear yourself live.

<img src="../applio-realtime-img/record-audio.png" alt="Monitor Device (Optional)" width="800" height="auto">

- **Record Audio (Optional):** Use this to save your live conversion output directly to a file.


### 2. Model Settings
The Model Settings tab is split into two sections:

**Part 1: Voice Selection**
<img src="../applio-realtime-img/model-settings-1.png" alt="Model Selection" width="800" height="auto">

- **Voice Model / Index:** Select your model and corresponding index.
- **Pitch:** Adjusts your vocal pitch (-24 to +24).
- **Processing:** Toggle Autotune, Proposed Pitch, and Clean Audio as needed for your specific vocal style.

**Part 2: Advanced Tuning**
<img src="../applio-realtime-img/model-settings-2.png" alt="Advanced Model Tuning" width="800" height="auto">

- **Search Feature Ratio:** Controls index influence; higher values improve trained accent accuracy but may not work if you speak a different language than the model was trained in.
- **Volume Envelope:** Blends the output volume with the original.
- **Protect Voiceless Consonants:** Set to 0.33 to safeguard breathing sounds and prevent robotic tearing.
- **Pitch Algorithm:** Select `rmvpe` for best quality or `fcpe` for lower latency.
- **Embedder Model:** Choose your model's required embedder (ContentVec, Spin, etc.).

### 3. Performance Settings
<img src="../applio-realtime-img/performance-settings.png" alt="Performance Settings" width="800" height="auto">

- **Chunk Size (ms):** Lower values reduce latency but increase CPU load.
- **Crossfade Overlap Size (s):** Prevents "clicks" in audio transitions.
- **Extra Conversion Size (s):** Provides context to the model to improve quality.
- **Silence Threshold (dB):** Fine-tune the VAD sensitivity.


***
## FAQ

**Why does it run in a browser?**
Applio uses a Web User Interface (WebUI) coded in Gradio, allowing the tool to run consistently across local and cloud environments.

***
### What browser should I use?

It's better you try and test, some people had issues on Chrome, some others on Firefox, it might depend on the settings you use and also Java/Type Script having issues. The browser that usually is reported by most people to have issues is OperaGX, which is why we don't suggest it much.

***
### Why are most YouTube (Video) Tutorials old? Is there going to be an updated one?

YouTube Tutorials take way more time to make, and get outdated easily in this case, as AI progresses fast and continues to change in better, with more different settings and versions. Written guides are easier to update, since you don't have to remake an entire video. It's unknown if we will ever release a video since they easily get outdated, but if we will, it will be linked inside of this guide.

***
### Do I need an extremely expensive mic for good quality?

We had a conversation about this in https://discord.com/channels/1159260121998827560/1159290161683767298/1352325982689951765 & https://discord.com/channels/1159260121998827560/1159290161683767298/1356265862704926907,
RVC works by downsampling your audio voice to 16khz because f0 estimators only works at that sample rate, after that the model outputs the results using it's original sample rate (without any upscaling). So there won't be the need of having a super extremely expensive, a decent one should do the job.

***

:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::