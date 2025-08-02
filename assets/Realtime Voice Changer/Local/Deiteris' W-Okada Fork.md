---
icon: chevron-right
order: 4000
---
``Last update: July 30, 2025``
***
:::content-center
## Introduction
:::

- W-Okada is a realtime voice changer that uses RVC for its conversion.

- There are two versions of this realtime voice changer, the <u>[offical original](https://github.com/w-okada/voice-changer)</u> made by Wok, and the <u>[Deiteris fork](https://github.com/deiteris/voice-changer)</u> made by Deiteris. Note that those 2 links are just for reference to the Source Code Github Repositories of both projects, you should instead follow the guide below.

- This guide will be about the Wokada Deiteris fork since it has better preformance and quality compared to the Original Wokada.

- RVC does **NOT** mean realtime voice changer. RVC means Retrieval-based-Voice-Conversion.

***
#### Is The W-Okada Deiteris Fork Safe?

RVC Models are PyTorch Models, a Python library used for AI.
PyTorch uses serialization via Pythons' Pickle Module, converting the model to a file.
Since pickle can execute arbitrary code when loading a model, it could be theoretically used for malware, but Wokada Deiteris Fork has a **built-in feature to prevent code execution along the model.**
Also, **HuggingFace has a <u>[Security Scanner](https://huggingface.co/docs/hub/security-pickle#hubs-security-scanner)</u>** which scans for any unsafe pickle exploits and uses also ClamAV for scanning dangerous files.
***

‎      
#### Pros & Cons :icon-tasklist:
==- *Learn more*
!!! *The pros & cons are subjective to your necessities.*        
!!! 
||| ✔️ **PROS** 
- Currently stable
- Good Performance
- Has great support for Nvidia, AMD, Intel, Mac, Linux, Windows
- Uses a Web User Interface, meaning it can be run on the Cloud
- Uses FP16 Inference by default, and let's you choose to use FP32 for better quality/precision
||| ❌ **CONS** 
- Uses a Web User Interface, having issues on some browsers, and bugs with renaming or deleting models on it
- Doesn't have an active development recently
- Has Cut Off Issues Using an Extra superior to 2.7
- Doesn't let you choose the embedder, using only RVC models trained on contentvec (the majority)
|||
===
***
###### ‎

***

## System & Hardware Requirements

***

- Windows 10 or Later
- macOS 12 Monterey or later. With Apple Silicon or Intel CPU
- Any Linux Distro

and

- At least 6GB of RAM
- At least 6GB of free disk storage

***
##### For GPU-conversion

TLDR: Make sure you have Nvidia RTX 20xx or AMD Radeon RX 5xxx or better. GTX 10xx or RX 580 will also work, but may run into issues with games and higher delay. If you have an iGPU (mostly AMD Radeon Graphics or Vega) use online hosted alternative instead.


 Long answer:

`Minimum:`

- An integrated graphics card: AMD Radeon Vega 7 (with AMD Ryzen 5 5600G) or later; with 2GB VRAM (in FP32 mode), ~1GB VRAM (in FP16 mode, if supported). But this is NOT recommended at all and we will most likely not recommend you to download the realtime voice changer with iGPUs.

- A dedicated graphics card: Nvidia GeForce GTX 900 Series or later, or AMD Radeon RX 400 series or later, or Intel Arc A300 series or later.

`Recommended:`

- A dedicated graphics card Nvidia GeForce RTX 20 Series or later, or AMD Radeon RX 5000 series or later, or Intel Arc A500 series or later.

***
##### For CPU-conversion

TLDR: don't bother. You can't run games, discord usage might be the only thing that will work decently, but you might potentially damage your CPU. People with no GPU usually have old CPU's, so delay will be high too. Not worth it.

`Minimum:`
- Intel Core i5-4690K or AMD FX-6300.

`Recommended:`
- Intel Core i5-10400F or AMD Ryzen 5 1600X.

!!!warning CPU-Conversion is not recommended at all
If you plan on playing games at the same, do not use CPU-conversion. With CPU, the delay will be massive and your PC will not run smoothly at all. If you have a higher-end CPU you can make it work, but those that have higher end CPUs most likely also have higher end GPUs, so you should be using your GPU if possible.
!!!

***


## Online Alternatives [Colab/Kaggle]

#### Kaggle

!!!danger
It's free, but you will need a phone number verification.
!!!

<u>[Read the Tutorial HERE](https://docs.aihub.gg/rvc-voice-changer/cloud/deiteris-w-okada-fork-kaggle/)</u>

***
#### Google Colab

!!!danger
You need the Google Colab Paid Tier to run this, as it uses a Web User Interface, else you could risk getting disconnected or getting banned off Colab.
!!!

<u>[Read the tutorial HERE](https://docs.aihub.gg/rvc-voice-changer/cloud/deiteris-w-okada-fork-colab/)</u>

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

## Windows

- Download based on your GPU. You don't know what GPU you have? Open Task Manager > Performance tab and check for your GPU0 and GPU1 names. Prioritize the Nvidia one if you have one, else use the other.

<img src="../wokada-img/cap.png" alt="Task Manager" width="600" height="auto">

####
!!!
Use Online Hosted if you have an integrated GPU (AMD Radeon Graphics ; AMD Radeon Vega ; Intel UHD) and if you do not have a GPU at all
!!!
***

### Download NVIDIA on Windows

- The latest version as of December 7th 2024 is: <u>[nvidia-b2332 (click here to download)](https://huggingface.co/Shadicti/deiteris-Fork/blob/main/voice-changer-windows-nvidia-b2332.zip)</u>

!!!danger
If you have a GTX 700 card or below, use AMD/Intel version instead.
!!!

***
### Download NVIDIA RTX 5000-series on Windows

- NVIDIA RTX-5000 series, the newest release of GPU's, require a separate download. You do not need it if you have an older GPU, follow the normal Nvidia link in that case. <u>[nvidia-5000-Series (click here to download)](https://github.com/IllIlIlIllIl/voice-changer/releases/tag/b2335)</u>

!!!danger
Download all 3 files, then extract the .zip file, it will automatically extract ALL 3 FILES into one. Then open the `MMVCServerSIO` folder and run `MMVCServerSIO.exe` (or called `MMVCServerSIO` if you don't have extensions activated).
!!!

***
### Download AMD, INTEL and CPU on Windows

- The latest version as of December 7th 2024 is: <u>[dml-b2332 (click here to download)](https://github.com/deiteris/voice-changer/releases/download/b2332/voice-changer-windows-amd64-dml.zip)</u>

!!!danger
Intel UHD Graphics do NOT work at this point in time. Use Online Alternative.
!!!

***
### Opening on Windows

- First Make sure you have <u>[7zip](https://www.7-zip.org/)</u> or <u>[WinRAR](https://www.win-rar.com/download.html)</u> for extracting / unzipping.

- After the download, you extract the zip file. You open the folders until you see an exe application called `MMVCServerSIO` and run that.

!!!warning
If nothing opens, then open a browser and type in `http://127.0.0.1:18888/`. This is a local URL, it runs on the WebUI.
!!!

***
## Mac


***
### Download Mac Silicon

- The latest version as of December 7th 2024 is: <u>[arm-b2332 (click here to download)](https://github.com/deiteris/voice-changer/releases/download/b2332/voice-changer-macos-arm64-cpu.tar.gz)</u>

***
### Download Mac Intel

- The latest version as of December 7th 2024 is: <u>[macos-amd-b2332 (click here to download)](https://github.com/deiteris/voice-changer/releases/download/b2332/voice-changer-macos-amd64-cpu.tar.gz)</u>

***
### Opening on Mac

- Double click the voice-changer-macos-arm64-cpu.tar.gz file. The realtime voice changer will unpack and the MMVCServerSIO folder will appear.

- Open the extracted MMVCServerSIO folder.

- Double-click `MMVCServerSIO` to run the realtime voice changer.

!!! Apple quarantine stops you from running the realtime voice changer
You do not get a popup notification for this, so if it does not open or says "Pytorch is damaged", do the following:

1. Open the Terminal

2. Run the following command: `xattr -dr com.apple.quarantine <PUT IN THE PATH TO YOUR MMVCServerSIO FOLDER HERE>`
For example, if you extracted the realtime voice changer to your desktop, the command may look as follows: `xattr -dr com.apple.quarantine ~/Desktop/MMVCServerSIO`

3. Now, open the extracted MMVCServerSIO folder and run `MMVCServerSIO` to run the realtime voice changer.
!!!
!!!warning
If nothing opens, then open a browser and type in `http://127.0.0.1:18888/`. This is a local URL, it runs on the WebUI.
!!!

***
## Linux

Installation of CUDA Toolkit or AMD **HIP SDK is NOT REQUIRED**. All other necessary libraries are bundled with the application.


### Download on Nvidia on Linux

you need to download both these files:

https://github.com/deiteris/voice-changer/releases/download/b2332/voice-changer-linux-amd64-cuda.tar.gz.aa

https://github.com/deiteris/voice-changer/releases/download/b2332/voice-changer-linux-amd64-cuda.tar.gz.ab

### Download on AMD on Linux

you need to download all these files:

https://github.com/deiteris/voice-changer/releases/download/b2332/voice-changer-linux-amd64-rocm.tar.gz.aa

https://github.com/deiteris/voice-changer/releases/download/b2332/voice-changer-linux-amd64-rocm.tar.gz.ab

https://github.com/deiteris/voice-changer/releases/download/b2332/voice-changer-linux-amd64-rocm.tar.gz.ac


### Download on CPU on Linux

you need only this file:

https://github.com/deiteris/voice-changer/releases/download/b2332/voice-changer-linux-amd64-cpu.tar.gz


### Opening on Linux

I'm not sure about the capabilities of UI tar archive extractors, but you can extract these archive parts with the following command that will merge them and extract: `cat voice-changer-linux-amd64-cuda.tar.gz.* | tar xzf -`, change **cuda** to **rocm** or **cpu** depending on your PC GPU.

After you extract the files using the command above, a new folder called `MMVCServerSIO` will appear.

- Open a Terminal and navigate into that folder:
  ```bash
  cd MMVCServerSIO
  ```

- You may need to make the application executable. Run this command just in case:
  ```bash
  chmod +x ./MMVCServerSIO
  ```

- Now, run the realtime voice changer:
  ```bash
  ./MMVCServerSIO
  ```

!!!warning
After the server finishes loading in your terminal, it will not open a window on its own. Open a web browser and go to `http://127.0.0.1:18888/` to access the user interface.
!!!


***
## Opening on Multi-PC Setups

This is only for the people that have 2 PCs, and want to use 1 PC for Gaming, the other only for Wokada Deiteris Fork.

- Create a file named `.env` on the same folder where `MMVCServerSIO.exe` is located. Open it up with a notepad, copy paste the settings from the <u>[GitHub link](https://github.com/deiteris/voice-changer/issues/180#issuecomment-2359166278)</u>.

- After that, you create another file with the file extension ending `.bat`, open it up with a notepad, copy paste what is needed in there again from the <u>[GitHub link](https://github.com/deiteris/voice-changer/issues/180#issuecomment-2359166278)</u>. 


- Now run the bat file. After it starts, you should be able to open the link. For example, if you specified `HOST=192.168.0.1` and `ALLOWED_ORIGINS='["https://192.168.0.1:18888"]')`, you should be able to open `https://192.168.0.1:18888` in your browser and use the realtime voice changer UI from other machines in your local network.

***
## Voice Models
***

### Adding Models

<img src="../wokada-img/edit.png" alt="Edit Button in Wokada Deiteris Fork to Add Models" width="430" height="auto">

#####

- Click on `Edit` on the small blue square located around the the top left side
- Pick any slot you want, click `upload`
- Only RVC models will work. If you have a gpt-sovits one or any other, they will not work.
- Select `Type: RVC`, then `select file` on the `Model` slot and upload your `.pth` file.
- No need for an `Index` file, but you can upload it. This controls the accent of the voice model

***
### Merging Models (Merge Lab) :icon-git-merge:

The Merge Lab allows you to combine multiple RVC V2 voice models (.pth Weights only, not indexs too) into a single, new hybrid model. This is useful for creating unique voices.

1.  **Open Merge Lab:** Scroll down in the user interface and click on the `Merge Lab` button.

  <img src="../wokada-img/merge-lab-button.png" alt="Merge Lab Button in Wokada Deiteris Fork" width="300" height="auto">


2.  **Select Model Type:** From the `Type` dropdown menu, choose the type of models you wish to merge. Only models that share the same sample rate and type (e.g., "pyTorchRVCv2, 32000Hz, 768" which are all RVC v2 models with the 32kHz Sample Rate, or "pyTorchRVC, 40000Hz, 256" which are all RVC v1 models with the 40kHz Sample Rate) will be shown and can be merged together.

  <img src="../wokada-img/merge-lab.png" alt="Merge Lab in Wokada Deiteris Fork" width="600" height="auto">

3.  **Adjust Weights:** Use the sliders next to each model's name to set its "weight" (RVC models are PyTorch files, the .pth is the weight containing the voice) or influence in the merged model. The numbers (from 0 to 100) represent the percentage of each voice in the mix.

4.  **Merge and Download:** Once you have set the desired proportions, click the `Merge` button. Your browser will automatically download the new, `merged.pth` model file.

!!! Manual Download
The merged model is **not** automatically added to your model list. You must upload it to an empty slot yourself by following the steps in the **Adding Models** section.
!!!

!!!danger Index Merging
You **can't merge indexs** (in rvc context, the trained accent of the voice). Only the .pth actual voice file.
!!!


***
### Deleting Models

If you wish to delete a model, you can overwrite the slot with a new model. If you insist on fully emptying a slot, head over to the `model_dir` folder, open the folder of the slot number you want to delete, and delete the model from that folder


***
## Audio Setup
***

### Discord & Games

On the realtime voice changer app wokada, you select:

- Input: Your microphone
- Output: Virtual Audio Cable
- Monitor (if you wish to hear the realtime voice changer on your headphones aswell): Your headphones

On discord and games, you select:

- Input: Virtual Audio Cable
- Output: Your headphones


***
### Client and Server Setup

Audio: `CLIENT`

- Uses MME (normal audio processed through windows. You use this automatically with every application)
- You can use the boxes echo, sup1, sup2 using this
***
Audio: `SERVER`

- Use S.R. 48000
- I recommend using [Windows WASAPI] on all prefixes for less delay, because this uses your audio devices (e.g. microphone) directly, before processing through windows.
- Both Input and Output has to be the same (Windows WASAPI), you can't use MME for input and then Windows WASAPI for Output. You may also use [ASIO](https://rentry.co/lessdelayasio).
- You can not use the in-built noise suppressions in this mode
***

ASIO > WASAPI > MME as a general thumbrule (this also affects delay)

Sometimes Client does not work, then use SERVER with prefix "MME" or "Windows WASAPI". You can not use the in-built noise suppression and echo fix if you use SERVER.

***
### Settings Explained
***
- `PASSTHRU button:` Sends your actual voice and not the realtime voice changer through the virtual audio cable. You want this to be GLOWING GREEN or GREY (grey for dark mode users) for the realtime voice changer to work.

- `F0 det:` Pitch extraction algorithm. Both RMVPE (for the best precision and robustness) and FCPE (for less precision & robustness but lower delay) are good options.

- `Chunk:` Controls the delay (lower number means less delay, but please check out the recommended settings for what your GPU is capable of).

- `Extra:` Controls voice model quality. 2.7s is the max, anything above is not worth it and can cause issues for no benefit.
***
#### `VOL:`
- `in:` This raises the microphone volume before it goes into the realtime voice changer (Recommended to leave it on the default or if needed, not to go too high, else it increases background noise and makes the voice sound worse).

- `OUT:` Raising realtime voice changer volume on the output.

- `MON:` Increases volume of your headphones that you set on "mon" if you selected to hear yourself with the realtime voice changer.
***
- `Pitch:` This is the pitch. Going into negative will make it lower pitch, going higher will make it higher pitch. If you have a male voice using a female voice, aim for 10 - 14, this depends on your voice, try around those numbers until you find a sweet spot.

- `Formant Shift:` Alters harmonic frequencies and changes the voice timbre without affecting the pitch

- `Index:` This controls the accent of the voice model. In most cases, using Index on Realtime Voice Changer can add realism if you speak the language the model was trained in. If you have a heavy foreign accent, you may use this at a low rate. Beware, this increases CPU usage
***
- `In. Sens:` microphone threshold, increasing this will cause less background noise to get picked up if it's a problem

- `Sup2:` Noise suppression on your microphone.

- `Sup1:` Noise suppression but weaker, not recommended to use this at all, because it barely has any impact whilst reportedly, making the voice inconsistent

- `Echo:` if you experience echo issues despite having sup2, In. Sens to the right and having lowered your windows system value, then this will help you as a last resort

***
## Settings

***
### Advanced Settings

- Protocol: rest (Use SIO if you want less delay but if you encounter any issues with SIO switch back to rest. Rest has slightly more delay than SIO)
- Crossfade length: Controls how smoothly the AI stitches different processed parts "chunks" of your voice back together. 0.1 or 0.15 (0.1 for fastest voice, 0.15 for improved quality but increases delay by 50 ms)
- SilenceFront: Reduce GPU usage when idle. This only reduces GPU resources when you're not talking or making sounds
- Force FP32 mode: on (THIS IS OFF BY DEFAULT! Turning this on improves stability. Increases VRAM usage by 200 MB)
- Disable JIT compilation: off for faster loading speed of the program, on for slightly better performance (10-15 ms) for Nvidia only)
- Convert to ONNX: Reduces delay and slightly reduces gpu usage. Enabling this increases CPU usage by around 5-10%. Reduces the quality of the voice a bit. If you decide to enable this, pair it with rmvpe_onnx for even less delay
- Protect: Reduces the occurrence of robotic sibilants and robotic breathing, but also reduces the effect of the index file. Lower values increase this protection, higher values decrease it. The default value is 0.5, which means that the protection is disabled, reduce this value to 0.33 to enable it

***
### Finding my own settings for Chunk

First start with 500 ms, check what number your perf is and go closer to that number but not lower.

Example: if your perf is 200, go down to 250 with your chunk. Chunk affects perf value, and Extra as well.

<img src="../wokada-img/greem.png" alt="Wokada Deiteris Fork Green Perf Value" width="170" height="auto">

If your perf value is green, your selected chunk is stable. You can experiment and go down in chunk for less delay, or increase extra for more quality (would not recommend to go above 2.7s extra. Anything above uses more resource for no clear benefit).

<img src="../wokada-img/yellow.png" alt="Wokada Deiteris Fork Yellow Perf Value" width="170" height="auto">

If your perf value is yellow, your selected chunk is enough, but audio may be unstable if you run other processes at the same time. Operation in this range will also incur high GPU usage. Increasing Chunk size or reducing Extra is recommended.

<img src="../wokada-img/red.png" alt="Wokada Deiteris Fork Red Perf Value" width="170" height="auto">

If your perf value is red, the realtime voice changer is unstable. Increase chunk size or reduce Extra.

***
### Known working settings for Chunk and Extra

!!! These settings are intentionally higher than what your GPU is capable of
If you are playing a video game with the realtime voice changer, you will have to increase the chunk higher than what you usually can handle.
This is because the game runs on GPU and the realtime voice changer aswell. The game will always take higher priority by default, so the listed settings are safe options that should run with most games.
If you run into issues, you will need to lower quality and limit your FPS, or increase chunk. It is best to first tweak your game's settings first

It is recommended to go up to Finding my own settings after you are comfortable with the program
!!!

+++ NVIDIA

||| GPU
:::content-left
RTX xx90 (e.g. 3090)

RTX xx80 Ti (e.g.3080 Ti)

RTX xx80 (e.g. 3080)

RTX xx70 Ti (e.g. 3070 Ti)

RTX xx70 (e.g. 3070)

RTX xx60 Ti (e.g. 3060 Ti)

RTX xx60 (e.g. 3060)

RTX xx50 (e.g. 3050)

GTX 16xx-series

GTX 10xx-series

GTX 900-series

MX 330
:::
||| Max Settings
:::content-center
30 - 60 ms chunk + 2.7s extra

30 - 60 ms chunk + 2.7s extra

100 - 120 + 2.7s extra

50 - 80 ms chunk + 2.7s extra

50 - 80 ms chunk + 2.7s extra

50 - 90 ms chunk + 2.7s extra

60 - 90 ms chunk + 2.7s extra

110 - 130 ms chunk + 2.7s extra

140 - 180 ms chunk + 2.7s extra

200 ms chunk + 2.0s extra

250 ms chunk + 1.0s extra

500 ms chunk + 0.6s extra
:::
||| For gaming
:::content-right
perf number + 40 ms chunk

perf number + 40 ms chunk

perf number + 40 ms chunk

perf number + 40 ms chunk

perf number + 40 ms chunk

perf number + 40 ms chunk

perf number + 50 ms chunk

perf number + 60 ms chunk

perf number + 60 ms chunk

perf number + 80 ms chunk

perf number + 80 ms chunk

perf number + 100 ms chunk
:::
|||

+++ AMD
||| GPU
:::content-left
7xxx XT cards

6xxx XT cards

5xxx XT cards

7xxx cards

6xxx cards

5xxx cards

RX 6600M

RX 580

RX 570

RX 560
:::
||| Max Settings
:::content-center
60 - 80 ms + 2.7s extra

70 - 100 ms + 2.7s extra

80 - 120 ms + 2.7s extra

*bugged* 256 ms + 2.7s extra

128 ms + 2.7s extra

140 - 200ms + 2.0s extra

128ms + 2.7s extra

perf number + 60 ms chunk

perf number + 60 ms chunk

perf number + 60 ms chunk
:::
||| For gaming
:::content-right
perf number + 40 ms chunk

perf number + 40 ms chunk

perf number + 40 ms chunk

perf number + 60 ms chunk

perf number + 60 ms chunk

perf number + 60 ms chunk

perf number + 60 ms chunk

perf number + 60 ms chunk

perf number + 60 ms chunk

perf number + 80 ms chunk
:::
|||
+++ AMD iGPU
||| GPU
:::content-left
AMD Radeon(TM) Graphics (with Ryzen 7 5800H)

AMD Radeon RX Vega 10 (with Ryzen 7 3700U)

AMD Radeon RX Vega 8 (with Ryzen 3 3200G)
:::
||| Chunk + Extra
256 ms + 2.7s extra

600 ms + 0.6s extra

700 ms + 1.0s extra
|||
+++ Mac & CPU's
||| Mac and CPU
Mac M1

Mac M1 Air

Mac M2

Mac M2 Air

Ryzen 7 5800x
||| F0 + Chunk + Extra
fcpe ; for chunk check the perf number and add 50 to it ; 1.0s extra

fcpe + 230ms + 2.7s extra

rmvpe_onnx + 650ms + 1.0s extra

fcpe ; for chunk check the perf number and add 50 to it ; 2.7s extra

rmvpe_onnx + 260 ms + 0.6s extra
|||
+++ 

***
## Extras
***

### Information

!!! What's the best choice for AMD users?
This fork is a lot better for AMD GPU's compared to the original w-okada. On the original it requires converting models to onnx models which is annoying, requires more CPU and GPU resources, has a lot more delay and other little inconveniences/bugs.

Example: AMD RX 6650 XT lowest latency is 298 ms chunk on original w-okada. On this fork lowest latency is around 60 - 80 ms chunk
!!!

!!! Which is better for NVIDIA mainline w-okada or Deiteris' fork?
Deiteris' fork is better for NVIDIA users who normally use the prebuilt w-okada version, because this version uses GPU accelerated extra compared to the original which uses CPU.

For the RTX GPUs the delay performance differences are minimal, but quality performance is better. For older cards like GTX or MX, this fork performs better in all aspects.

Example: NVIDIA RTX 3070 on prebuilt w-okada reaches 170 - 213 ms chunk latency. On manually set up environment of w-okada reaches 42 ms chunk latency. On this fork it can reach 30 - 38 ms chunk latency, depending on the extra set. Keep in mind these are settings tested to the max, without a video game or intense operations running in the background
!!!

***
### Reduce more Delay (Windows Only)
***
#### Prerequisite: Match Sample Rates (for both WASAPI & ASIO)
This first step is mandatory for both methods. You must select the same `sample rate` for your microphone and the virtual audio cable before proceeding.

!!!
If you don't know how to open your sound devices, press **WIN+R**, type "**mmsys.cpl**", then hit enter.
!!!

1.  Navigate to the `Recording` tab, right-click on your microphone, and select `Properties`.
2.  Go to the last tab, `Advanced`, and set the sample rate to **48000 Hz**.
3.  Ensure both options for **Exclusive Mode** are activated.

<img src="../wokada-img/microphone-properties.png" alt="Microphone Properties" width="450" height="auto">

4.  Now, go to the `Playback` tab. Right-click on your virtual audio cable (e.g., Line 1) and go to `Properties`.
5.  In the `Advanced` tab, adjust the sample rate to match your microphone: **48000 Hz**.

<img src="../wokada-img/vac-properties.png" alt="Virtual Audio Cable Properties" width="450" height="auto">

With the sample rates matched, you can now proceed to configure either WASAPI or ASIO.

+++ WASAPI
!!! What does WASAPI do?
WASAPI accesses your audio devices directly, while the driver that you use by default (which is "MME") *goes through multiple layers within the Windows audio subsystem*, causing more delay. This will in total cut down **50-80ms delay**.
!!!

#### Enable WASAPI
Assuming you completed the prerequisite step, you can now select the correct inputs and outputs in the voice changer as follows:

- **AUDIO:** `SERVER`
- **S.R.:** Match the sample rate you chose above, which should be `48000`.
- **Input:** `[WINDOWS WASAPI] Your Microphone`
- **Output:** `[WINDOWS WASAPI] Your Virtual Audio Cable (e.g., Line 1)`

<img src="../wokada-img/wasapi-server.png" alt="Wokada WASAPI Server Settings" width="600" height="auto">

!!!warning
You cannot use the noise suppression (`sup1`, `sup2`) or `echo` functions in `SERVER` mode.
!!!

Then, on your game or Discord, you select:

- **Input:** Your Virtual Audio Cable (e.g., Line 1 Output)
- **Output:** Your Headphones/Speakers

#### Common Errors
!!!danger sounddevice.PortAudioError: Error opening Stream: Invalid sample rate [PaErrorCode -9997]
You did not match the sample rate of your virtual audio cable to your microphone. Return to the prerequisite step and ensure both are set to the same value (48000 Hz).
!!!
+++ ASIO
!!!
I would recommend using WASAPI first if you are a normal user, as ASIO is more complex to set up.
!!!
!!! What does ASIO do?
Like WASAPI, ASIO accesses your audio devices directly, bypassing multiple layers within the Windows audio subsystem that "MME" (the default driver) has to go through. It has a lower algorithmic delay and can reduce total delay by **50-80ms**.
!!!

#### Step 1: Download and Install FlexASIO
- Download and run the installer from here: <u>[FlexASIO Download](https://github.com/dechamps/FlexASIO/releases/download/flexasio-1.9/FlexASIO-1.9.exe)</u>

#### Step 2: Download and Install FlexASIO GUI
- First, you need the .NET Desktop runtime. Download and install it from here: <u>[.NET 6.x Desktop runtime](https://dotnet.microsoft.com/en-us/download/dotnet/6.0)</u>
- Afterwards, download and install the FlexASIO GUI: <u>[FlexASIO GUI Download](https://github.com/flipswitchingmonkey/FlexASIO_GUI/releases/download/v0.35/FlexASIO.GUIInstaller_0.35.exe)</u>

#### Step 3: Configuring FlexASIO GUI
Run `FlexASIO GUI`. If it doesn't open, you missed installing the .NET runtime from the previous step. Copy the following settings:

- **Backend:** `Windows WASAPI`
- **Buffer Size:** ✅ Set to `256`
- **Input Device:** Select your Microphone.
- **Output Device:** Select your Virtual Audio Cable (e.g., Line 1).
- **Latency:** ✅ Set Input Latency: `0.2` ; ✅ Set Output Latency: `0.2`
- **Output:** ✅ Set: `;` ✅ AutoConvert

<img src="../wokada-img/FlexASIO-GUI.jpg" alt="FlexASIO GUI Configuration" width="600" height="auto">

!!! Latency Explanation
Having the input latency at 0.0 can make your microphone crackle. Using 0.1 often works fine. If you experience crackles, experiment with this value (e.g., 0.12, 0.15) until it stops. The lower you can go, the better. If you don't want to experiment, you can keep it at `0.2`.
!!!
!!!danger
Click **SAVE TO DEFAULT FLEXASIO.TOML**. Do not forget this step. You can close the GUI afterwards.
!!!

#### Step 4: Setting it up on the voice changer
!!!warning
The Deiteris Fork works with ASIO, while some older versions of the original w-okada do not.
!!!
In the voice changer app:
- Select **AUDIO:** `Server`
- Select **S.R.:** `48000`
- Select the **input** and **output** from ASIO. You can select "ALL" in the first column to filter for ASIO devices to make it easier.

<img src="../wokada-img/FlexASIO-server.jpg" alt="Wokada FlexASIO Server Settings" width="600" height="auto">

Then, on your game or Discord, you select:

- **Input:** Your Virtual Audio Cable (e.g., Line 1 Output)
- **Output:** Your Headphones/Speakers

#### Common Errors
!!!danger sounddevice.PortAudioError: Error opening Stream: Invalid sample rate [PaErrorCode -9997]
You did not match the sample rate of your virtual audio cable to your microphone. Return to the prerequisite step and ensure both are set to 48000 Hz.
!!!
+++

***

### Models to try

- You will need to connect your account to <u>[weights.com](http://weights.com/)</u> to be able to download these models
    - Click on the 3 dots (...) on weights.com models, then Download model. You will need an account

**Female:**

Gawr Gura: [Hugging Face Link](https://huggingface.co/dacoolkid44/VTuber-RVC/tree/main/Gawr%20Gura%20(Talking)) / [Weights Link](https://www.weights.com/models/clm72kp5p01sycctcp3ti9xaw)

**Male:**

[Bob Ross voice made by dieseldog34](https://www.weights.com/models/clm72t7ra0qqhcctc4zyax181)

[Markiplier voice made by hobqueer](https://www.weights.com/models/clm72nuvi0c8scctcvzrckuqp)

***
## Help
***

After you start the program for the first time and it finished downloading files: if it says Failed to download or verify: ... followed by "Press Enter to continue" at the end, then the pretrain download failed. This can happen randomly. Here is what you will need to do:
!!! Fix
Go to the "pretrain" folder in the MMVCServerSIO folder.
Delete everything inside it if there is anything.

Download ALL THE FILES from this drive:
https://drive.google.com/drive/folders/1OFfM9rmxCZkiYjxoK_yzhRbcXpt0TiJ0?usp=drive_link

Copy paste everything from this Google Drive inside the pretrain folder.

Then run MMVCServerSIO.exe again, this time it should work
!!!

### Crackle Fix
Open Task Manager > Details

Right click `audiodg.exe` and set priority to `High`

Right click `audiodg.exe` again > set affinity > uncheck everything except CPU 2 (only ✅ CPU 2, turn off the rest)

With a program called ProcessLasso you can automate this to always be active, since Windows resets these sometimes.
Or you can open up CMD/Powershell (or make a bat file) and type in:

`powershell "ForEach($PROCESS in GET-PROCESS audiodg) { $PROCESS.ProcessorAffinity=4; $PROCESS.PriorityClass='High' }"`

***
### Discord Crackle Fix
Make sure to do the Crackle Fixes in this step before doing this to see if it fixes your issue

If the voice sounds fine in the app AND it sounds fine in games, but ONLY sounds weird on discord, then:

- Turn off Echo Cancellation
- Turn off Noise Suppression (sometimes causes issues, maybe not. Check for yourself)

***
### GPU Idling
Sometimes your GPU will start idling after the program is in the background for a while and affect performance. 


- In the folder where w-okada is located there should be a .bat file called `force_gpu_clocks.bat`, run that and it should fix your gpu idling.
- Once you no longer want your gpu clock speed to be forced anymore you can run `reset_gpu_clocks.bat`.

***
## FAQ
***
### Why does it run in a browser and not it's own window?

Because it uses a Web User Interface (WebUI) coded in JavaScript & TypeScript, the majority of (Open Source) AI programs are designed to run on the browser (even tho usually using things like Gradio) since it can be used both on cloud and locally. The original wokada also ran on a WebUI, just that it made it's own window

***
### What browser should I use?

It's better you try and test, some people had issues on Chrome, some others on Firefox, it might depend on the settings you use and also Java/Type Script having issues. The browser that usually is reported by most people to have issues is OperaGX, which is why we don't suggest it much

***
### Why are most YouTube (Video) Tutorials old? Is there going to be an updated one?

YouTube Tutorials take way more time to make, and get outdated easily in this case, as AI progresses fast and continues to change in better, with more different settings and versions. Written guides are easier to update, since you don't have to remake an entire video. It's unknown if we will ever release a video since they easily get outdated, but if we will, it will be linked inside of this guide.

***
### Do I need an extremely expensive mic for good quality?

We had a conversation about this in https://discord.com/channels/1159260121998827560/1159290161683767298/1352325982689951765 & https://discord.com/channels/1159260121998827560/1159290161683767298/1356265862704926907,
RVC works by downsampling your audio voice to 16khz because f0 estimators only works at that sample rate, after that the model outputs the results using it's original sample rate (without any upscaling). So there won't be the need of having a super extremely expensive, a decent one should do the job.

***
### Are there unique Voice Models?
RVC Voice Models need to be trained on something, so the models themselves can't be unique, but you can use the [Merge Lab](http://docs.aihub.gg/realtime-voice-changer/local/deiteris-w-okada-fork/#merging-models-merge-lab) to create a new unique merged model.


***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
