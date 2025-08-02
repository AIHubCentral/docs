---
icon: chevron-right
order: 1000
---

``Last update: August 3, 2025``

***
:::content-center
<img src="..\aicovermaker-img\banner.png" alt="image" width="700">

:::

###### ‎
:::content-center
## Introduction ‎
:::
- AICoverMaker (or known as RVC-AI-Cover-Maker-WebUI) is an Applio RVC <u>[Fork</u>](https://docs.aihub.gg/essentials/whats-rvc/#forks) developed by the <u>[Eddy</u>](https://github.com/Eddycrack864)</u>, as a better and updated version of the old AICoverGen.

- It's liked for its great **UI** & **Automated AI Cover Process**, making it the easiest way to make AI Covers, as it automatically separates instrumentals & vocals, and mixes them back with the converted vocals.

***
#### Are RVC Models Safe?

RVC Models are PyTorch Models, a Python library used for AI.
PyTorch uses serialization via Pythons' Pickle Module, converting the model to a file.
Since pickle can execute arbitrary code when loading a model, it could be theoretically used for malware, but this fork has a **built-in feature to prevent code execution along the model.**
Also, **HuggingFace has a <u>[Security Scanner](https://huggingface.co/docs/hub/security-pickle#hubs-security-scanner)</u>** which scans for any unsafe pickle exploits and uses also ClamAV for scanning dangerous files.
***

‎      
#### Pros & Cons :icon-tasklist:
==- *Learn more*
!!! *The pros & cons are subjective to your necessities.*        
!!! 
||| ✔️ **PROS** 
- Automatically separates instrumentals and mixes them with converted ones
- Currently stable
- Faster interface
- Automatic model upload
- Has Mangio-Crepe
- User-friendly UI
||| ❌ **CONS** 
- Can't Train models
- No Precompiled versions for Non-Windows Users
- Doesn't support Mac nor any NON-Nvidia GPUs
|||
===
***

## System & Hardware Requirements

**SPEC** | **MINIMUM REQUIREMENT** | 
:---: | :---: | :---: | 
OS | Windows 10 or later / Any Modern Linux Distro 
RAM | 6GB
Storage | 6 GB 

**SPEC** | **SUGGESTED REQUIREMENT** | 
:---: | :---: | :---: | 
OS | Windows 10 or later / Any Modern Linux Distro 
GPU | NVIDIA RTX 20 Series or later | 
RAM | 6GB+
Storage | 6GB+


In case you don't meet the <u>[requirements](https://docs.aihub.gg//rvc/local/aicovermaker/#system--hardware-requirements/)</u> to run it locally, it also has a <u>[2 Cloud Versions: Kaggle & Colab](https://docs.aihub.gg/rvc/cloud/aicovermaker/)</u>

***
###### ‎
:::content-center
## Download :icon-download:
:::
###### ‎
!!!warning Before Downloading (Applies to both methods):
- Don't put the folder in a directory with privileged access (like `C:\Program Files`).
- Make sure the file path does not contain any spaces or special characters.
- It's recommended to temporarily deactivate your antivirus and firewall to avoid missing dependencies during installation.
!!!

***

### Precompiled (Windows)

1. The easiest way to download RVC-AI-Cover-Maker-WebUI is by going to Eddy's <u>[Latest GitHub Release](https://github.com/Eddycrack864/RVC-AI-Cover-Maker-UI/releases/latest)</u>, and clicking the **Precompiled** version.

    <img src="..\aicovermaker-img\precompiled-github.png" alt="image" width="400">

***
2. Unzip the folder. It may take a few minutes.
***
3. Open the AICoverMaker folder & execute ``run.bat``.

    <img src="..\aicovermaker-img\bat-files.png" alt="image" width="550">‎    
‎       
- A console tab will appear, and after a moment your default browser will open with the WebUI ready to use.     

***

### Source / Manual (mainly for Linux)

<img src="..\aicovermaker-img\aicovermaker-normal-install.png" alt="image" width="700">‎     

1.  Download the source code, either .zip (which is the most suggested usually) or .tar.gz, from the latest release <u>[link](https://github.com/Eddycrack864/RVC-AI-Cover-Maker-UI/releases/latest)</u>.

    <img src="..\aicovermaker-img\aicovermaker-sources.png" alt="image" width="700">‎    
‎       

    !!!note
    If you download the `.zip` from the latest release make sure to rename the folder from `"rvc-ai-cover-maker-ui-v1.0.5"` (or whatever version is the latest version) to just `"rvc-ai-cover-maker-ui"` otherwise you may run into missing dependencies issues.
    !!!

2. Extract the folder. It may take a few minutes.

3. Open the AICoverMaker folder & execute the script `run.sh` for Linux, or `run.bat` for Windows.

    <img src="..\aicovermaker-img\bat-files.png" alt="image" width="550">‎    
‎       
- A console tab will appear, and after a moment your default browser will open with the WebUI ready to use.  


‎       
!!!warning Don't close the console until you're done using it in both cases, or it will stop working.     
!!! 


***
###### ‎
:::content-center
## Downloading Music & Models
:::
###### ‎
#### Music Download

**1.** When in the UI look at the top left and look for the tab named `Download Music` and click it.

   <img src="../aicovermaker-img/download-music-tab.png" alt="image" width="600" height="">

‎ 

**2.** Then put the song you want to download in the text box and click download.


   <img src="../aicovermaker-img/download-music-url.png" alt="image" width="1000" height="">

***

#### Model Download

**1.** In the UI look at the top left and look for the tab named `Download Model` and click it.

   <img src="../aicovermaker-img/download-model-tab.png" alt="image" width="600" height="">

‎ 

**2.** Then put the model you want to download in the text box and click download.


   <img src="../aicovermaker-img/download-models.png" alt="image" width="1000" height="">

‎

**3.** You can also drag and drop your model in the `Drop files` box to upload them directly.


***
###### ‎
:::content-center
## Inference :icon-unmute:   
:::
###### ‎

Please use our <u>[Inference Settings guide](https://docs.aihub.gg/rvc/resources/inference-settings/)</u> to find out the inference settings do what.

**TTA** - results in longer separation time, it gives a little better SDR score but hard to tell if it's really audible in most cases". it “means "test time augmentation", it will do 3 passes on the audio file instead of 1. 1 pass with be with original audio. 1 will be with inverted stereo (L becomes R, R become L). 1 will be with phase inverted and then results are averaged for final output. 


***
###### ‎
:::content-center
## Update :icon-download:
:::
###### ‎

To Update AICoverMaker, you can either:

A. Open AICoverMaker's folder & execute the script `update.sh` for Linux, or `update.bat` for Windows.

<img src="..\aicovermaker-img\bat-files.png" alt="image" width="550">‎    

<br>

B. Download the latest precompiled the next time a new version comes out and replace the files.


###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
