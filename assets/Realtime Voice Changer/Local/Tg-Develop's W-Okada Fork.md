---
icon: chevron-right
order: 3000
---
``Last update: September 6, 2025``
***
:::content-center
## Introduction
:::

- W-Okada is a realtime voice changer that uses RVC for its conversion.

- There are 3 versions of this realtime voice changer, the <u>[Offical Original W-Okada](https://github.com/w-okada/voice-changer)</u> made by Wok, the <u>[Deiteris' Fork](https://github.com/deiteris/voice-changer)</u> made by Deiteris, and the <u>[Tg-Develop's Fork](https://github.com/tg-develop/voice-changer)</u> made by Tg-Develop. Note that those 3 links are just for reference to the Source Code Github Repositories of both projects, you should instead follow the guide below.

- This guide will be about the Wokada Tg-Develop's fork since it's a fork of the Deiteris' Fork, containing the performance improvements, has an improved Web User Interface, supports Spin Embedder Models, and has Audio Effects.

- RVC does **NOT** mean realtime voice changer. RVC means Retrieval-based-Voice-Conversion.

***
#### Is The W-Okada Tg-Develop's Fork Safe?

RVC Models are PyTorch Models, a Python library used for AI.
PyTorch uses serialization via Pythons' Pickle Module, converting the model to a file.
Since pickle can execute arbitrary code when loading a model, it could be theoretically used for malware, but Wokada Tg-Develop's Fork has a **built-in feature to prevent code execution along the model.**
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
- Has Audio Effects
- Lets you choose the Model Embedder Type, including ContentVec & Spin.
||| ❌ **CONS** 
- Uses a Web User Interface, having issues on some browsers, and bugs with renaming or deleting models on it
- Doesn't have a very active development recently
- Has Cut Off Issues Using an Extra superior to 2.7
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

- First, go to the latest release page: <u>[Latest Release (click here to go to Github)](https://github.com/tg-develop/voice-changer/releases/latest)</u>
- On the release page, find the "Assets" section and download the files based on your GPU.

!!!
To check your GPU, open Task Manager (Ctrl+Shift+Esc), go to the "Performance" tab, and look at the GPU names. If you have an NVIDIA card, use the NVIDIA (CUDA) version.
!!!

***

### Download NVIDIA on Windows

- Download all of the `voice-changer-windows-amd64-cuda` files. This will include multiple files, likely ending in `.zip.001`, `.zip.002`, etc.
- Make sure all downloaded parts are in the same folder before extracting.

!!!danger
If you have a GTX 700 series card or older, the CUDA version may not work. Use the AMD/Intel (DML) version instead.
!!!

### Download AMD, INTEL and CPU on Windows

- Download the single file named `voice-changer-windows-amd64-dml.zip`.
- If you don't have a dedicated GPU or the `dml` version doesn't work, download `voice-changer-windows-amd64-cpu.zip`.

!!!danger
Some integrated graphics like Intel UHD may not be compatible. If it fails, you may need to use the CPU version or an online alternative.
!!!

***

### Opening on Windows

- Make sure you have <u>[7-Zip](https://www.7-zip.org/)</u> or <u>[WinRAR](https://www.win-rar.com/download.html)</u> installed to extract the files.
- To extract:
    - **For the NVIDIA version:** Right-click on the file ending in `.zip.001` (the first part of the archive) and choose to extract it. Your archiving program will automatically find the other parts and combine them.
    - **For the AMD/Intel or CPU version:** Right-click the single `.zip` file and extract it.
- Open the newly created `MMVCServerSIO` folder and run the `MMVCServerSIO.exe` application.

!!!warning
If nothing opens, then open a browser and type in `http://127.0.0.1:18888/`. This is a local URL, it runs on the WebUI.
!!!

***
## Mac

- First, go to the latest release page: <u>[Latest Release (click here to go to Github)](https://github.com/tg-develop/voice-changer/releases/latest)</u>
- On the release page, find the "Assets" section and download the file corresponding to your Mac's processor.

***

### Download for Apple Silicon Mac

- For Macs with an M1, M2, or newer Apple chip, download the file ending in `macos-arm64-cpu.tar.gz`.

### Download for Intel Mac

- For older Macs with an Intel processor, download the file ending in `macos-amd64-cpu.tar.gz`.

***

### Opening on Mac

- Double-click the downloaded `.tar.gz` file to unpack it. An `MMVCServerSIO` folder will appear.
- Open the `MMVCServerSIO` folder and double-click the `MMVCServerSIO` application to run it.

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

- First, go to the latest release page: <u>[Latest Release (click here to go to Github)](https://github.com/tg-develop/voice-changer/releases/latest)</u>
- On the release page, find the "Assets" section and download the file(s) corresponding to your hardware.

***

### Download for NVIDIA on Linux

- Download all files that start with `voice-changer-linux-amd64-cuda.tar.gz` (e.g., `.tar.gz.aa`, `.tar.gz.ab`).

### Download for AMD on Linux

- Download all files that start with `voice-changer-linux-amd64-rocm.tar.gz` (e.g., `.tar.gz.aa`, `.tar.gz.ab`).

### Download for CPU on Linux

- Download the single file named `voice-changer-linux-amd64-cpu.tar.gz`.

***

### Opening on Linux

- Make sure all downloaded parts for your version are in the same directory.
- Open a Terminal and navigate to your downloads folder.
- Use the `cat` command to combine and extract the multi-part archives. For the single-file CPU version, use `tar`.

  ```bash
  # For NVIDIA
  cat voice-changer-linux-amd64-cuda.tar.gz.* | tar xzf -

  # For AMD
  cat voice-changer-linux-amd64-rocm.tar.gz.* | tar xzf -

  # For CPU
  tar xzf voice-changer-linux-amd64-cpu.tar.gz
  ```

- A new folder named `MMVCServerSIO` will be created. Navigate into it:
  ```bash
  cd MMVCServerSIO
  ```

- Make the application executable:
  ```bash
  chmod +x ./MMVCServerSIO
  ```

- Run the voice changer:
  ```bash
  ./MMVCServerSIO
  ```

!!!warning
After the server finishes loading in your terminal, it will not open a window on its own. Open a web browser and go to `http://127.0.0.1:18888/` to access the user interface.
!!!


***
## Opening on Multi-PC Setups

This is only for the people that have 2 PCs, and want to use 1 PC for Gaming, the other only for Wokada Tg-Develop's Fork.

- Create a file named `.env` on the same folder where `MMVCServerSIO.exe` is located. Open it up with a notepad, copy paste the settings from the <u>[GitHub link](https://github.com/deiteris/voice-changer/issues/180#issuecomment-2359166278)</u>.

- After that, you create another file with the file extension ending `.bat`, open it up with a notepad, copy paste what is needed in there again from the <u>[GitHub link](https://github.com/deiteris/voice-changer/issues/180#issuecomment-2359166278)</u>. 


- Now run the bat file. After it starts, you should be able to open the link. For example, if you specified `HOST=192.168.0.1` and `ALLOWED_ORIGINS='["https://192.168.0.1:18888"]')`, you should be able to open `https://192.168.0.1:18888` in your browser and use the realtime voice changer UI from other machines in your local network.


***
## Voice Models
***

### Managing Models

#### Adding Models

<img src="../wokada-tg-develop-img/plus-button-models-list.png" alt="Plus Button in Wokada Tg-Develop's Fork to Add Models" width="430" height="auto">

#####

- Click on `+` on the left sidebar Model Selector menu.
- Only RVC models will work. If you have a gpt-sovits one or any other, they will not work.
- Upload the Model File (.pth, .safetensors, .onnx), give it a Name (this is currently bugged, no matter what name you give it, it will always use the actual model's name), and Select between Hubert_Base/ContentVec & SPIN for the Embedder Type
- Optionally Upload the Index File (.index), this controls the Trained Model Accent.
- Optionally Upload a Thumbnail Image.
- Optionally check "Select model after upload", to automatically select it after it gets uploaded.

***
#### Renaming Models

!!!danger A Common Bug
Attempting to rename a model directly within the Web User Interface will cause the program to delete the model. This is a known bug. Use fix below to safely rename your models.
!!!

1.  Navigate to your `MMVCServerSIO` folder.
2.  Inside, open the `model_dir` folder. You will see several numbered folders, each corresponding to a model slot in the UI.
3.  Open the folder for the slot number you want to rename.
4.  Inside this folder, you will find a `params.json` configuration file. Open this file with a text editor like Notepad.
5.  Look for the `"name":` field in the file. Change the text in the quotes to your desired new model name.

<img src="../wokada-tg-develop-img/json-rename-model.png" alt="Editing the model name in the JSON file with Notepad" width="800" height="auto">

6.  Save the `.json` file. The name will be updated in the program UI.

***
#### Deleting Models

If you wish to delete a model, you can simply click the red trashbin icon next to its name in the Model Selector sidebar list.

***
### Merging Models (Merge Lab) :icon-git-merge:

The Merge Lab allows you to combine multiple RVC V2 voice models (.pth Weights only, not indexs too) into a single, new hybrid model. This is useful for creating unique voices.

1.  **Open Merge Lab:** At the bottom left, click on the `Merge Lab` button.

  <img src="../wokada-tg-develop-img/merge-lab-button.png" alt="Merge Lab Button in Wokada Tg-Develop's Fork" width="300" height="auto">

2. **Select Models to Merge:**
    - In the "Filter Settings" section, you can use the `Search Models` bar to find specific models by name.
    - Select the desired `Sample Rate` and `Embedder` from the dropdown menus to filter the list of available models. Only models that share these same characteristics can be merged.
    - From the "Available Models" list, check the boxes next to the models you want to include in the merge.

  <img src="../wokada-tg-develop-img/merge-lab.png" alt="Merge Lab in Wokada Tg-Develop's Fork" width="600" height="auto">

3.  **Adjust Weights:** Use the sliders next to each model's name to set its "weight" (RVC models are PyTorch files, the .pth is the weight containing the voice) or influence in the merged model. The numbers (from 0 to 100) represent the percentage of each voice in the mix.

4. **Choose Merge Options:**
    - **Download merged model:** This is checked by default and will download the final merged model file to your computer.
    - **Save to merge slot:** This option saves the merged model to a dedicated merge slot.
    - **Save to empty slot (auto-select first available):** This will automatically save the merged model into the next open model slot.

5. **Finalize Merge:** Once you have selected your models and set your desired save options, click the `Merge` button to create the new hybdrid model.

!!!danger Index Merging
You **can't merge indexs** (in rvc context, the trained accent of the voice). Only the .pth actual voice file.
!!!


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
- Both Input and Output has to be the same (Windows WASAPI), you can't use MME for input and then Windows WASAPI for Output.
- You can not use the in-built noise suppressions in this mode
***

ASIO > WASAPI > MME as a general thumbrule (this also affects delay)

Sometimes Client does not work, then use SERVER with prefix "MME" or "Windows WASAPI". You can not use the in-built noise suppression and echo fix if you use SERVER.


***
## Settings Explained
***

- `Start Server:` Starts/Stops the realtime voice changer, be aware that you can't change every settings while it's running.

- `Passthrough:` Sends your actual voice and not the realtime voice changer through the virtual audio cable. You want this to be OFF for the realtime voice changer to work.

***
### Model Settings

- `Pitch:` This is the pitch. Going into negative will make it lower pitch, going higher will make it higher pitch. If you have a male voice using a female voice, aim for 10 - 14, this depends on your voice, try around those numbers until you find a sweet spot.

- `Formant Shift:` Alters harmonic frequencies and changes the voice timbre without affecting the pitch

- `Index Ratio:` This controls the accent of the voice model. In most cases, using Index on Realtime Voice Changer can add realism if you speak the language the model was trained in. If you have a heavy foreign accent, you may use this at a low rate. Beware, this increases CPU usage.

- `Save Settings:` Save the previous Settings for the specific model you're using.

***
#### AI Settings

- `Echo Cancellation:` if you experience echo issues despite having sup2, In. Sens to the right and having lowered your windows system value, then this will help you as a last resort.

- `Noise Suppression 1:` Noise suppression but weaker, not recommended to use this at all, because it barely has any impact whilst reportedly, making the voice inconsistent.

- `Noise Suppression 2:` Noise suppression on your microphone.

- `Input Sensivity:` microphone threshold, increasing this will cause less background noise to get picked up if it's a problem.

- `Chunk Size:` Controls the delay (lower number means less delay, but depends on what your GPU is capable of).

- `Extra Processing Time:` Controls voice model quality. 2.7s is the max, anything above can cause cutoff issues.

- `F0 det:` Pitch extraction algorithm. Both RMVPE (for the best precision and robustness) and FCPE (for less precision & robustness but lower delay) are good options.

- `Processing Unit:` Select your Processing Unit, which can be your GPU, CPU or M Chip.

***
#### Audio Settings
- `Input Volume:` This raises the microphone volume before it goes into the realtime voice changer (Recommended to leave it on the default or if needed, not to go too high, else it increases background noise and makes the voice sound worse).

- `Output Volume:` Raising realtime voice changer volume on the output.

- `Monitor Volume:` Increases volume of your headphones that you set on Monitor Device if you selected to hear yourself with the realtime voice changer.

***
### Audio Effects

Audio effects are powerful tools for shaping and enhancing your voice in real-time. They can be applied to either the input (your microphone) or the output (the final sound you and your audience hear). 

*** 

#### Input vs. Output Effects 

The same effects can be applied to both your input and output audio, but the application timing and purpose differ. 

- **Input effects** process your raw microphone audio before it's used by the voice changer. Applying effects here can alter how the AI processes your voice, which can be useful for creative sound design. 
- **Output effects** are applied to the audio after the voice-changing process. These are typically used to refine the final sound, add ambiance, or apply mastering touches. 

#### Effect Providers: Simple vs. Pedalboard 

Two types of effect providers are available, each offering a different level of complexity and control. 

- **Simple Provider:** Offers basic, essential effects with straightforward controls. It's ideal for quick adjustments and users who are new to audio effects. 
- **Pedalboard Provider:** Provides a more extensive collection of high-quality effects with detailed parameters. This provider is geared towards users who want to fine-tune their sound with greater precision, much like a guitarist's physical pedalboard. 

#### Simple Provider Effects 

- `Simple Gain:` Basic volume adjustment. 
    - `Gain:` Amount of volume boost or cut. 
- `Simple Low Pass:` Basic IIR low-pass filter. 
    - `Cutoff Frequency:` Frequency above which signals are filtered out. 
- `Simple High Pass:` Basic IIR high-pass filter. 
    - `Cutoff Frequency:` Frequency below which signals are filtered out. 
- `Simple Delay:` Basic delay effect. 
    - `Delay Time:` Time delay for echoes. 
    - `Feedback:` Amount of feedback for multiple echoes. 
    - `Wet Level:` Level of delayed signal. 

#### Pedalboard Provider Effects 

- `Reverb:` Adds room ambience and depth. 
    - `Room Size:` Controls the size of the simulated room space. 
    - `Damping:` Amount of high-frequency absorption in the room. 
    - `Wet/Dry Mix:` Balance between original and reverb signal. 
    - `Pre-delay:` Delay before reverb starts, simulates room distance. 
- `Echo:` Creates delayed repetitions. 
    - `Delay Time:` Time between the original sound and the echo. 
    - `Feedback:` How much of the echo is fed back to create repeats. 
    - `Wet Level:` Volume level of the echo effect. 
    - `High Cut:` Removes high frequencies from the echo. 
- `Chorus:` Adds richness and width. 
    - `Rate:` Speed of the chorus modulation. 
    - `Depth:` Intensity of the pitch modulation. 
    - `Mix:` Balance between dry and chorus signal. 
    - `Voice Count:` Number of virtual voices in the chorus. 
- `Distortion:` Adds harmonic saturation. 
    - `Drive:` Amount of distortion applied to the signal. 
    - `Tone:` EQ balance from dark to bright. 
    - `Level:` Output volume of the effect. 
    - `Type:` Character of the distortion algorithm. 
- `Compressor:` Controls dynamic range. 
    - `Threshold:` Level above which compression starts. 
    - `Ratio:` How much the signal is compressed (4:1 means 4dB in = 1dB out). 
    - `Attack:` How quickly the compressor responds to loud signals. 
    - `Release:` How quickly the compressor stops compressing. 
- `Equalizer:` Adjusts frequency response. 
    - `Low (80Hz):` Boost or cut low frequencies (bass). 
    - `Low-Mid (320Hz):` Boost or cut low-mid frequencies (warmth). 
    - `Mid (1.25kHz):` Boost or cut mid frequencies (presence). 
    - `High-Mid (5kHz):` Boost or cut high-mid frequencies (clarity). 
    - `High (12.5kHz):` Boost or cut high frequencies (air/brightness). 
- `Noise Gate:` Eliminates unwanted background noise. 
    - `Threshold:` Level below which audio is gated (silenced). 
    - `Ratio:` How aggressively the gate closes. 
    - `Attack:` How quickly the gate opens. 
    - `Release:` How quickly the gate closes. 
- `Gain:` Adjusts overall volume level. 
    - `Gain:` Amount of volume boost or cut. 
- `Low Pass Filter:` Removes high frequencies above cutoff. 
    - `Cutoff Frequency:` Frequency above which signals are filtered out. 
    - `Resonance:` Emphasis at the cutoff frequency. 
- `High Pass Filter:` Removes low frequencies below cutoff. 
    - `Cutoff Frequency:` Frequency below which signals are filtered out. 
    - `Resonance:` Emphasis at the cutoff frequency. 
- `Bitcrush:` Adds lo-fi digital reduction. 
    - `Bit Depth:` Number of bits for quantization (lower = more distorted). 
- `Clipping:` Hard distortion by signal clipping. 
    - `Threshold:` Level at which clipping occurs. 
- `Limiter:` Prevents audio from exceeding threshold. 
    - `Threshold:` Maximum output level. 
    - `Release:` Time to return to normal after limiting. 
- `Invert:` Flips signal polarity. 
- `Ladder Filter:` Moog-style multimode filter. 
    - `Cutoff Frequency:` Filter cutoff frequency. 
    - `Resonance:` Filter resonance (emphasis at cutoff). 
    - `Drive:` Amount of filter overdrive. 
    - `Mode:` Filter mode (LPF=lowpass, HPF=highpass, BPF=bandpass, 12/24=slope). 
- `Peak Filter:` Parametric EQ band. 
    - `Frequency:` Center frequency of the peak. 
    - `Gain:` Boost or cut at the center frequency. 
    - `Q Factor:` Width of the frequency band (higher = narrower). 
- `High Shelf Filter:` Boosts/cuts high frequencies. 
    - `Cutoff Frequency:` Frequency where shelf begins. 
    - `Gain:` Amount of boost or cut. 
    - `Q Factor:` Sharpness of the transition. 
- `Low Shelf Filter:` Boosts/cuts low frequencies. 
    - `Cutoff Frequency:` Frequency where shelf begins. 
    - `Gain:` Amount of boost or cut. 
    - `Q Factor:` Sharpness of the transition. 
- `Convolution:` Impulse response reverb/simulation. 
    - `Impulse Response:` Type of acoustic space to simulate. 
    - `Mix:` Balance between dry and processed signal. 
- `MP3 Compressor:` Adds MP3 compression artifacts. 
    - `VBR Quality:` MP3 VBR quality (0=highest, 9=lowest). 
- `GSM Compressor:` 2G cellular phone compression.

***
### Advanced Settings

- `UI Language:` Select the Web User Interface Language, currently there is only English, German and Japanese.
- `Protocol:` rest (Use SIO if you want less delay but if you encounter any issues with SIO switch back to rest. Rest has slightly more delay than SIO)
- `Crossfade Overlap:` Controls how smoothly the AI stitches different processed parts "chunks" of your voice back together. 0.1 or 0.15 (0.1 for fastest voice, 0.15 for improved quality but increases delay by 50 ms)
- `SilenceFront:` Reduce GPU usage when idle. This only reduces GPU resources when you're not talking or making sounds
- `Force FP32 mode:` on (THIS IS OFF BY DEFAULT! Turning this on improves stability. Increases VRAM usage by 200 MB)
- `Disable JIT compilation:` off for faster loading speed of the program, on for slightly better performance (10-15 ms) for Nvidia only.
- `Convert to ONNX:` Reduces delay and slightly reduces gpu usage. Enabling this increases CPU usage by around 5-10%. Reduces the quality of the voice a bit. If you decide to enable this, pair it with rmvpe_onnx for even less delay
- `Protect:` Reduces the occurrence of robotic sibilants and robotic breathing, but also reduces the effect of the index file. Lower values increase this protection, higher values decrease it. The default value is 0.5, which means that the protection is disabled, reduce this value to 0.33 to enable it
- `Interface - Switch To Classic UI:` It should use the same Web User Interface as the Original Wokada and Deiteris Fork, it's not suggested as it won't have all the new features, and is currently broken.
- `Skip Pass through confirmation:` It will skip the confirmation when you enable Passthrough, not suggested.


***
### Finding my own settings for Chunk Size and Extra Processing Time

First start with 500 ms, check what number your Perf (in the top right of the Performance Stats) is and go closer to that number but not lower.

Example: if your perf is 200, go down to 250 with your chunk. Chunk affects perf value, and Extra as well.

<img src="../wokada-tg-develop-img/green.png" alt="Wokada Tg-Develop's Fork Green Perf Value" width="170" height="auto">

If your perf value is green, your selected chunk is stable. You can experiment and go down in chunk for less delay, or increase extra for more quality (would not recommend to go above 2.7s extra. Anything above uses more resource for no clear benefit).

<img src="../wokada-tg-develop-img/yellow.png" alt="Wokada Tg-Develop's Fork Yellow Perf Value" width="170" height="auto">

If your perf value is yellow, your selected chunk is enough, but audio may be unstable if you run other processes at the same time. Operation in this range will also incur high GPU usage. Increasing Chunk size or reducing Extra is recommended.

<img src="../wokada-tg-develop-img/red.png" alt="Wokada Tg-Develop's Fork Red Perf Value" width="170" height="auto">

If your perf value is red, the realtime voice changer is unstable. Increase Chunk Size or reduce Extra Processing Time.

***
## Extras
***

### Information

!!! What's the best choice for AMD users?
This fork is a lot better for AMD GPU's compared to the original w-okada. On the original it requires converting models to onnx models which is annoying, requires more CPU and GPU resources, has a lot more delay and other little inconveniences/bugs.
!!!

!!! Which is better for NVIDIA users?
This fork is better for NVIDIA users who normally use the prebuilt w-okada version, because this version uses GPU accelerated extra compared to the original which uses CPU.

For the RTX GPUs the delay performance differences are minimal, but quality performance is better. For older cards like GTX or MX, this fork performs better in all aspects.
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

<img src="../wokada-tg-develop-img/microphone-properties.png" alt="Microphone Properties" width="450" height="auto">

4.  Now, go to the `Playback` tab. Right-click on your virtual audio cable (e.g., Line 1) and go to `Properties`.
5.  In the `Advanced` tab, adjust the sample rate to match your microphone: **48000 Hz**.

<img src="../wokada-tg-develop-img/vac-properties.png" alt="Virtual Audio Cable Properties" width="450" height="auto">

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

!!! Latency Explanation
Having the input latency at 0.0 can make your microphone crackle. Using 0.1 often works fine. If you experience crackles, experiment with this value (e.g., 0.12, 0.15) until it stops. The lower you can go, the better. If you don't want to experiment, you can keep it at `0.2`.
!!!
!!!danger
Click **SAVE TO DEFAULT FLEXASIO.TOML**. Do not forget this step. You can close the GUI afterwards.
!!!

#### Step 4: Setting it up on the voice changer
!!!warning
The Tg-Develop's Fork works with ASIO, while some older versions of the original w-okada do not.
!!!
In the voice changer app:
- Select **AUDIO:** `Server`
- Select **S.R.:** `48000`
- Select the **input** and **output** from ASIO. You can select "ALL" in the first column to filter for ASIO devices to make it easier.
- **Ch.:** For both input and output, it's best to leave them to "default", the numbers are for true asio devices which flex isnt.
- **Monitor:** You can use the WASAPI Windows, you could also use windows directsound but that might cause an issue if matching sample rates doesnt fix it.


Then, on your game or Discord, you select:

- **Input:** Your Virtual Audio Cable (e.g., Line 1 Output)
- **Output:** Your Headphones/Speakers

#### Common Errors
!!!danger sounddevice.PortAudioError: Error opening Stream: Invalid sample rate [PaErrorCode -9997]
You did not match the sample rate of your virtual audio cable to your microphone. Return to the prerequisite step and ensure both are set to 48000 Hz.
!!!
+++


***
## Help
***

### How to fix "Failed to download or verify"

After you start the program for the first time and it finished downloading files, but you have slow/unstable internet connection it might say Failed to download or verify: ... followed by "Press Enter to continue" at the end, then the pretrain download failed. To fix it, you can either:

!!! Method 1
Retry with a better connection later.
!!!

!!! Method 2
1. Go to the "pretrain" folder in the MMVCServerSIO folder.
2. Delete everything inside it if there is anything.
3. Download the [Zipped Version of the Pretrained folder](https://github.com/Nick088Official/Wokada-Tg-Develop-Fork-Pretrain/releases/download/b2364/pretrain.zip)
4. Extract the pretrain.zip, be sure the pretrain folder contains only the files, not a pretrain folder inside another pretrain folder with the files.
5. Then run MMVCServerSIO.exe again, this time it should work.
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

Because it uses a Web User Interface (WebUI) coded in JavaScript & TypeScript, the majority of (Open Source) AI programs are designed to run on the browser (even tho usually using things like Gradio) since it can be used both on cloud and locally. The original wokada also ran on a WebUI, just that it made it's own window.

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
### Are there unique Voice Models?
RVC Voice Models need to be trained on something, so the models themselves can't be unique, but you can use the [Merge Lab](http://docs.aihub.gg/realtime-voice-changer/local/tg-develops-w-okada-fork/#merging-models-merge-lab) to create a new unique merged model.


***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
