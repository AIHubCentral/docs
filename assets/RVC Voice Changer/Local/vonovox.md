---
icon: chevron-right
order: 4000
---
``Last update: June 2, 2025``
***
:::content-center
## Introduction
:::

- Vonovox is a realtime voice changer that uses RVC for its conversion.

- Vonovox was developed by dr87.

***
#### Is Vonovox Safe?

RVC Models are PyTorch Models, a Python library used for AI.
PyTorch uses serialization via Pythons' Pickle Module, converting the model to a file.
Since pickle can execute arbitrary code when loading a model, it could be theoretically used for malware, but Vonovox has a **built-in feature to prevent code execution along the model.**
Also, **HuggingFace has a <u>[Security Scanner](https://huggingface.co/docs/hub/security-pickle#hubs-security-scanner)</u>** which scans for any unsafe pickle exploits and uses also ClamAV for scanning dangerous files.
***

‎      
#### Pros & Cons :icon-tasklist:
==- *Learn more*
!!! *The pros & cons are subjective to your necessities.*        
!!! 
||| ✔️ **PROS** 
- Has an active development
- Good Performance
- Currently stable
- It doesn't use a Web User Interface, meaning that it is less prone to errors and opens on it's own window
- Easily reduces delay on Windows via facilitating the WASAPI/ASIO Backend process
- Lets you choose the embedder, including spin
- Uses TF32 Inference by default, which is more precise than FP16, and has very very slightly less precision/quality but better performance compared to FP32
- Extra Effects, such as "Noise Gate"
||| ❌ **CONS** 
- Not Open Source (right now, but the dev is working on an Open Source version)
- Supports only Nvidia GPUs on Windows
- It doesn't use a Web User Interface, meaning that it can't be run on the Cloud
- Many Effects are Premium, such as "Low Quality Mic"
|||
===
***
###### ‎
:::content-center

***

## System & Hardware Requirements

***

- Windows 10 or Later

and

- At least 6GB of RAM
- At least 6GB of free disk storage

***
##### For GPU-conversion

TLDR: Make sure you have Nvidia RTX 20xx better. GTX 10xx or RX 900 will also work, but may run into issues with games and higher delay. If you have an iGPU (mostly AMD Radeon Graphics or Vega) use Wokada Deiteris Fork Cloud instead.

 Long answer:

`Minimum:`

- A dedicated graphics card: Nvidia GeForce GTX 900 Series or later.

`Recommended:`

- A dedicated graphics card Nvidia GeForce RTX 20XX Series or later.

***

## Virtual Audio Cable

#### A Virtual Audio Cable (VAC) is what you need to use the voice changer on Discord & Games.

!!! For Windows
Download this: <u>[VAC Lite (Virtual-Audio-Cable by Muzychenko)](https://software.muzychenko.net/freeware/vac470lite.zip)</u>
!!!

- Run `setup64`, not 64a, after extracting the zip to a new folder

- After installing the Virtual Cable, it changes your default audio system. Click **Yes** when it asks you to open the audio device settings (or press WIN+R, type "mmsys.cpl" if you closed it already), and change your **Recording** and **Playback** devices back to your usual devices. Same for communications device aswell (right click -> set as default communication device)

***

## Windows

- Make sure you have a Nvidia and a good enough one to run Vonovox. You don't know what GPU you have? Open Task Manager > Performance tab and check for your GPU0 and GPU1 names.

<img src="../wokada-img/cap.png" alt="image" width="600" height="auto">

####
!!!
Use Online Hosted if you have an integrated GPU (AMD Radeon Graphics ; AMD Radeon Vega ; Intel UHD) and if you do not have a GPU at all
!!!
***

### Download NVIDIA on Windows

- Go to Vonovox's <u>[github repo](https://github.com/dr87/Vonovox/releases)</u> and download the latest release of Vonovox. 

!!!danger
If you have a GTX 800 card or below you can't use Vonovox.
!!!

***
### Opening on Windows

- First Make sure you have <u>[7zip](https://www.7-zip.org/)</u> or <u>[WinRAR](https://www.win-rar.com/download.html)</u> for extracting / unzipping.

- After the download extract the zip file. Open the folders until you see an .bat file called `setup.bat` and run that.

- Vonovox will start downloading everything it needs to run. Be patient as it can take up to 5 minutes to download everything it needs.

- Once it's done downloading everything it will display `Setup complete!` in the command line. You can now go ahead and run `start.bat`. 

***
## Voice Models
***

### Adding Models

<img src="../vonovox-img/select.png" alt="image" width="800" height="auto">

#####

- Click on `Select .pth file` on the blue square located around the the top
- Only RVC models will work. If you have a gpt-sovits one or any other, they will not work.
- Select your `.pth` file and click `upload`.
- No need for an `Index` file.
***
### Changing Models

If you wish to use a different a model, you can overwrite the model you are currently using with a new model.

***
## Audio Setup
***

### Discord & Games

In Vonovox select:

- Input: Your microphone
- Output: Virtual Cable or your headphones if you wish to hear the model first

On discord and games, you select:

- Input: Virtual Cable
- Output: Your headphones

***
### Settings
***
- `Embedder:` Select between contentvec or spin trained models. Most current models are trained on contentvec. Make sure you read the model's description to find out what embedder it uses. Spin has kinda better breaths, more robust to noise, has some training related differences, but it's less used and newer.

- `F0 det:` Pitch algorithm. Pitch algorithm. Both RMVPE (for the best quality and robustness) and FCPE (for nice quality and being lightweight) are good options.

- `Pitch smoothing factor:` Pitch smoothing will dampen pitch changes. It still follows the exact curve of the f0 predictor allowing it to maintain 100% accuracy, just to a lower magnitude. This allows normal speaking voices to have better stability, since sometimes f0 can be over aggressive and cause pitch wobble on minor pitch fluctuations.

- `Output volume:` Controls how loud the output volume is.
***
#### `Noise Reduction:`
- `RNNoise Reduction:` Greatly filters input background noise for very minimum latency. This can mitigate the chances of Vonovox trying to infer on noise.

- `VAD Noise Reduction:` Completely mutes the output when speech is not detected. When speech is detected, it uses a 400ms release window. It is also much better at filtering breathe noises than RNNoise.

- `AP-BWE 48k Upscaler:` This is an upscaler that extends the bandwidth of speech by adding missing frequency information up to 48k.

***
#### `Voice Settings:`
- `Pitch:` This is the pitch. Going into negative will make it lower pitch, going higher will make it higher pitch. If you have a male voice using a female voice, aim for 10 - 14, this depends on your voice, try around those numbers until you find a sweet spot.

- `Formant Shift:` Alters harmonic frequencies and changes the voice timbre without affecting the pitch

- `Block Size:` Critical setting. The optimal block size is the lowest you can get without audio being choppy. Listen to your output. This is GPU dependent, the more powerful the gpu, the lower the block size you can use. However the optimizations I made allow much smaller block sizes to work on lower end GPUs. At extremely low block sizes, quality may be reduced.

- `Lookahead Buffer:` Gives the model more or less context to work with. Recommended 2.0 for best quality/latency ratio. The added latency of this setting is far less impactful than the block size.
***
***
## Extras
***

### Realtime Sound File Inferencing

You are able to load and play sound files, converted to your model's voice in realtime.

The sound file replaces your input mic while active. Whatever sound is coming from your loaded file is your "new microphone" while the sound is playing. That means it will infer and play the sound file as if it was your own voice in realtime. You can play speech, singing, or whatever you want. Just make sure the audio is clean, as the client still needs to inference it, no different than the real mic.

When a sound file is playing, it will zero out the input from your real mic, meaning you don't have to worry about overlapping your voice with playback. Mic will automatically unmute when sound is playing again. Also mute and unmute is handled properly when pausing and resuming the playback of audio files.

Seek timer and playback timer so you can go to specific times in your sound file.

<img src="../vonovox-img/soundfile.png" alt="image" width="800" height="auto">

‎

!!!
If you are playing singing files with high pitch, you must turn off all noise suppression options as suppression models are trained on speech, not high pitch singing.
!!!
!!!
Supports wav, mp3 and flac.
!!!


***
### Models to try

- You will need to connect your account to <u>[weights.gg](http://weights.gg/)</u> to be able to download these models
    - Click on the 3 dots (...) on weights.gg models, then Download model.

**Female:**

Gawr Gura: [Hugging Face Link](https://huggingface.co/dacoolkid44/VTuber-RVC/tree/main/Gawr%20Gura%20(Talking)) / [Weights Link](https://www.weights.com/models/clm72kp5p01sycctcp3ti9xaw)

**Male:**

[Bob Ross voice made by dieseldog34](https://www.weights.gg/models/clm72t7ra0qqhcctc4zyax181)

[Markiplier voice made by hobqueer](https://www.weights.gg/models/clm72nuvi0c8scctcvzrckuqp)

***
## FAQ
***
### Do I need an extremely expensive mic for good quality?

We had a conversation about this in https://discord.com/channels/1159260121998827560/1159290161683767298/1352325982689951765 & https://discord.com/channels/1159260121998827560/1159290161683767298/1356265862704926907,
RVC works by downsampling your audio voice to 16khz because f0 estimators only works at that sample rate, after that the model outputs the results using it's original sample rate (without any upscaling). So there won't be the need of having a super extremely expensive, a decent one should do the job.

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::