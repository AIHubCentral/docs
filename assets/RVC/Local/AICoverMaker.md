---
icon: chevron-right
order: 2000
---

``Last update: May 10, 2025``

***
:::content-center
<img src="..\aicovermaker-img\Banner.png" alt="image" width="600">

:::

###### ‎
:::content-center
## Introduction ‎
:::
- AICoverMaker (or known as RVC-AI-Cover-Maker-WebUI) is an Applio RVC <u>[Fork</u>](https://docs.aihub.gg/essentials/whats-rvc/#forks) developed by the <u>[Eddy</u>](https://github.com/Eddycrack864)</u>, as a better and updated version of the old AICoverGen.

- It's liked for its great **UI** & **Automated AI Cover Process**, making it the easiest way to make ai cover, as it automatically separates instrumentals and mixes them back with the converted vocals.

- It also has a <u>[cloud version](https://docs.aihub.gg/rvc/cloud/aicovermaker/)</u>, in case you don't meet the <u>[requirements](https://docs.aihub.gg/essentials/whats-rvc/#what-are-the-requirements-for-rvc-locally/)</u> to run it locally.   
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
- No Precompiled versions for Non-Windows Users.
|||
===
***
###### ‎
:::content-center
## Download :icon-download:
:::
###### ‎
!!!warning Before Downloading:
- Don't put it in a folder with privileged access.
- Make sure the path does not contain any spaces or special characters.
- Deactivate your antivirus and firewall to avoid missing dependencies.
!!!
***
1. The easiest way to download RVC-AI-Cover-Maker-WebUI is by going to Eddy's <u>[Latest GitHub Release](https://github.com/Eddycrack864/RVC-AI-Cover-Maker-UI/releases/latest)</u>, and clicking the **Precompiled** version for your Operative System.

    <img src="..\aicovermaker-img\Precompiled-Github.png" alt="image" width="400">

***
2. Unzip the folder. It may take a few minutes.
***
3. Open AICoverMaker's folder & execute ``run.bat``.

    <img src="..\aicovermaker-img\bat-files.png" alt="image" width="550">‎    
‎       
- A console tab will appear, and after a moment your default browser, with RVC-AI-Cover-Maker-WebUI ready to use.     
‎       
!!!warning Don't close the console until you're done using it, or it will stop working.     
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

## Inference

Please use our <u>[Inference Settings guide](https://docs.aihub.gg/rvc/resources/inference-settings/)</u> to find out the inference settings do what.

**TTA** - results in longer separation time, it gives a little better SDR score but hard to tell if it's really audible in most cases". it “means "test time augmentation", it will do 3 passes on the audio file instead of 1. 1 pass with be with original audio. 1 will be with inverted stereo (L becomes R, R become L). 1 will be with phase inverted and then results are averaged for final output. 

***

## Update

If you don't want to download the latest precompiled the next time a new version comes out, open AICoverMaker's folder & execute ``update.bat``.

<img src="..\aicovermaker-img\bat-files.png" alt="image" width="550">‎    



###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
