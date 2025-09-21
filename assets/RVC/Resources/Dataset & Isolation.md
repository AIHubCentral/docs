---
icon: chevron-right
order: 2000
---

``Last update: August 18, 2025``
***
:::content-center
## Introduction
:::
- In this massive guide it will be explained how to **properly** prepare a dataset to make a RVC model.

- ***In the field of AI***, it's the collection of data used to train an AI model. It contains examples of the inputs the model is expected to handle, along with the correct outputs.

- **In the context of RVC**, it's an audio file that's given to RVC, containing the voice the model is going to replicate. It can be a speaking, singing voice drums, sound effects or noise.

- The **quality**, **variety** & **length** of the dataset are the biggest determining factors for the final quality of the model. Let's explain Length and Variety.
***
:::content-center
## Length & Variety
:::
- For beginners we recommend sticking with a dataset length of **15 minutes** of pure data not counting silence, or if you desire a natural sounding model go for **40+** minutes of dataset. Just remember **quality over quantity**.            

- **Variety** in your dataset is also important because without it RVC lacks the ability to generate diverse audio.

- Some things to increase the generalization abilities of RVC and increase the diversity in your dataset include:
    - Removing repeated words. ( If you want you can be extreme you can do this and remove every single repeated word that's fine, but generally there is no need to do this. )
    - Include speech in many ranges and pitches. 
    - Longer datasets.
    - Expressive speech.
***
:::content-center
## Quality  
:::

- A quality dataset is super important for RVC since without one RVC will struggle to make anything good or believable. 

:::content-center
#### ``Here are some recommendations for a quality dataset.``
:::

###### ‎        
#### :icon-chevron-down: Clean vocals.
- Ensure there isn't much background noise, reverb, overlapping voices, music, distortion, or small silences. *Some* quiet natural background noise is fine and won't ruin your model since the original pretrains for RVC were made with a noisy dataset, so RVC knows how to deal with noise. You'll learn more on cleaning vocals in the **Vocal Isolation & Cleaning** section below.   
‎   
#### :icon-chevron-down: Audio quality.
- The higher the audio quality, the better. If possible have it in a <u>[lossless](https://docs.aihub.gg/extra/glossary/#lossless-formats)</u> format like **WAV** or **FLAC**, not a lossy one like MP3. No converting a MP3 to a FLAC or WAV won't remove the compression.  
‎   
#### :icon-chevron-down: No harsh sibilance/popping.
- Additionally, don't include harsh sibilance (loud "S" & "SH" pronunciation) or popping sounds (loud "P" sound) 
    - Robotic sibilances are due to your dataset being short or they are overfitted. You can fix this by making your dataset larger or by choosing an epoch where the sibilants aren't overfitted.
    - Harsh sibilances are due to your dataset having harsh sibilants. You can fix this by de-essing or making your dataset larger.
‎  
#### :icon-chevron-down: No Audio Damage.
- The most inportant part of a clean dataset, if your audio is damaged RVC will struggle with it causing it to overall sound worse because RVC will create synthetic data and try to learn from it, so make sure your audio isn't damged.  
‎   
***
:::content-center
## Artifacts 
:::       
In RVC, artifacting refers to an anomaly where the output voice sounds "robotic" & glitchy.     
This occurs after the <u>[inference](https://docs.aihub.gg/extra/glossary/#inference)</u> or model training process.     
#### Causes    
It usually occurs when the dataset/vocal sample meets any of these criteria: 

 •  Audio is low-quality      
 •  Voice model was overfitted, undertrained or overtrained        
 •  There are overlapping voices      
 •  There is reverb       
 •  There is noise
             
As you noticed, most of the issues boil down to the audio sample not being properly **clean**. RVC is built for purely working with voices, not other sounds.         

Remember that the cleaner your input audio is, the better the results.

#### Solutions    
#### 1. Use a lossless format:
- If possible, it's best if your audio is in a <u>[lossless format](https://docs.aihub.gg/extra/glossary/#lossless-formats)</u> like **WAV** or **FLAC**, preserving its original quality.

- Avoid using lossy ones like MP3 or OGG.
‎   
#### 2. If doing inference:
- Remove undesired noises with an <u>[vocal isolation](https://docs.aihub.gg/rvc/resources/vocal-isolation/)</u> software.

- Lowering the <u>[search feature ratio](https://docs.aihub.gg/rvc/resources/inference-settings/)</u> can also minimize this issue.

- If breathing sounds produce it, lower the <u>[Protection](https://docs.aihub.gg/rvc/resources/inference-settings/)</u> value.
‎   
#### 3. If training models:
- Ensure to clean your dataset properly, this includes removing silences and distortions.

***
 ‎
:::content-center
## Vocal Isolation & Cleaning
:::  
- A vocal isolation app is a software designed to extract a person's vocals from an audio file, usually through the use of AI models.

- They can remove undesired noises, like background noise, reverb, echo, music, etc.    

- The goal is to get an audio sample with clean and natural vocals, which is what RVC needs to give the most accurate & quality results.

- For RVC users, the best app is Ultimate Vocal Remover 5 (or **UVR**). It can be used either <u>[locally](https://docs.aihub.gg/extra/glossary/#local-running)</u> or through the <u>[cloud](https://docs.aihub.gg/rvc/resources/dataset-isolation/#cloud-uvr)</u>.

- If you need to remove multiple noises, follow this pipeline for the best results: ``Remove instrumental -> Remove reverb -> Extract main vocals -> Remove noise``  

- If you want to remove noise manually to avoid ai artifacts you can use RX 11, which is mentioned in this guide. 

‎ 


+++ Local UVR

:::content-center
## Local UVR
:::

:::content-center
[!button variant="danger" size="m" corners="pill" icon="heart-fill" iconAlign="right" text="Support UVR5"](https://www.buymeacoffee.com/uvr5)
:::

!!!warning 
*You'll require great specs & GPU to run it effectively. Otherwise, use either the <u>[Eddy's UVR5 UI Google Colab](https://docs.aihub.gg/rvc/resources/dataset-isolation/#uvr5-ui-colab)</u> or the <u>[HuggingFace Space](http://docs.aihub.gg/rvc/resources/dataset-isolation/#uvr5-ui-hf)</u>.*
!!!

### Installation :icon-download:
*** 
1. Go to their <u>[official website](https://ultimatevocalremover.com/)</u> & press `Download UVR`. If you want to use BS / Mel Roformer you are going to need to install <u>[this](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/UVR_1_15_25_22_30_BETA_full.exe)</u>.

    <img src="../uvr-img/website.jpg" alt="UVR Official Website Download Button" width="300" height="auto">   

***
###### 
2. It will redirect you their GitHub page. Click the download link for your **operating system**.   
UVR is available both on **Windows & Mac**.
***
###### ‎ 
3. Once the installer finishes downloading, execute it & follow the instructions.     
Make sure to tick `🗹 Create a desktop shortcut` for an easier access to UVR.

    <img src="../uvr-img/installation-shortcut.jpg" alt="UVR Installation Desktop Shortcut" width="500" height="auto">
***
###### ‎     
### How to Use :icon-checklist:  
***  

#### 1. Input audio.        
###### ‎  
- Click `Select input` to select your audio/s. Or just drag the files to it.  
‎   
- In `Select output` you can define the folder for the results.      

    <img src="../uvr-img/input-output-folders.jpg" alt="Select input and outputs and folders" width="300" height="auto">         ‎    

!!!success 
For better results, have the audio in a <u>[lossless format](https://docs.aihub.gg/extra/glossary/#lossless-formats)</u> (**WAV** or **FLAC**), & not MP3.
!!!
***
‎ 
#### 2. Select FLAC & GPU Conversion.
###### ‎  
a. At the right you can select the output format.       
We recommend picking `FLAC`. Learn why <u>[here](https://docs.aihub.gg/extra/glossary/#lossless-formats)</u>.   
‎  
b. If your GPU is **compatible with <u>[CUDA](https://docs.aihub.gg/extra/glossary/#cuda)</u>**, toggle `GPU Conversion` on for a faster process.    

    <img src="../uvr-img/flac-gpu-settings.png" alt="Setting FLAC & GPU Conversion" width="350" height="auto">   

###### ‎       
>This step is not mandatory, but recommended for better results.
***
‎
#### 3. Extract vocals.
###### ‎  
a. **Select** the Process Method and Model depending on your use case and [the List of Best Models](https://docs.aihub.gg/rvc/resources/vocal-isolation/#best-models-for-uvr).

    <img src="../uvr-img/process-method-model.jpg" alt="UVR Process Method & Model Selection" width="250" height="auto">‎      
###### ‎  
###### ‎    
b. Now click the long `Start Processing` button.    
###### ‎  
!!!success 
<u>**TIP:**</u> To **test** models/options more efficiently, tick `Sample Mode` to only process 30 seconds of your sample.
!!!   
***
‎

#### Best models for UVR:

Note: they actually are all MelBand Roformer models, but there isn't a proper list yet for them

Extraction | Process Method | Model
:---: | :---: | :---:
Vocals | MDX-Net | Gabox's voc_fv4
Instrumental | MDX-Net | INST Gabox V7
De-Reverb | MDX-Net | Anvuew mel dereverb v2
Extract Backing Vocals | MDX-Net | Mel roformer karaoke
De-Noise | MDX-Net | Mel denoiser v2

‎
### Troubleshooting :icon-tools:

***

#### A model isn't there.
- Click the wrench (🔧) on the left & go to `Download Center`
- Select the category of the model (Process Method)
- Unfold its dropdown & select the model that you need
- Then click the download button (📥). The model will download, which will take a few minutes

#### UVR extracted too little/too much.
- Modify the `Aggression Setting` value on the right. 
- This determines the **depth** of the extraction. Only the **VR** method has it.
- A higher value will deepen the extraction, and a lower one will soften it.
- Each audio is different, so you'll have to test the ideal value.

#### I can't remove some of the backing vocals.
- Run the audio through BVE. Modify the <u>[Aggression Setting](https://docs.aihub.gg/rvc/resources/vocal-isolation/#uvr-extracted-too-little-too-much)</u> if necessary.


+++ Local Eddy UVR5 UI

:::content-center
## Local Eddy's UVR5 UI
:::

!!!warning 
*You'll require great specs & GPU to run it effectively. Otherwise, use either the <u>[Eddy's UVR5 UI Google Colab ](https://docs.aihub.gg/rvc/resources/dataset-isolation/#uvr5-ui-colab)</u> or the <u>[HuggingFace Space](http://docs.aihub.gg/rvc/resources/dataset-isolation/#uvr5-ui-hf)</u>.*
!!!

### Installation :icon-download:
*** 
1. Go to their <u>[Eddy's UVR5 UI Latest Release](https://github.com/Eddycrack864/UVR5-UI/releases/latest)</u> & Follow the installation steps (**Precompiled** versions are suggested).

    <img src="../localeddyuvr5ui-img/installation-steps.png" alt="Eddy's UVR5 UI Local Installation Steps" width="700" height="auto">   

***
###### ‎     
### How to Use :icon-checklist:  

#### 1. Select input & options
###### ‎  
a. Tap the **Input Audio** box & select your audio, or simply drag & drop.     
‎        
<img src="../localeddyuvr5ui-img/input-audio.png" alt="Input Audio" width="1000" height="auto">‎           
‎       

‎ 
#### 2. Select model
###### ‎  
b. Once it's done uploading, select a Model by the [List of the Best Models](http://docs.aihub.gg/rvc/resources/dataset-isolation/#best-models-for-local-eddy-uvr5-ui). Under that you can change **Segment Size** and **Overlap**, the defaults are fine.   
    <img src="../localeddyuvr5ui-img/model-selection.png" alt="Model Selection" width="1000" height="auto">‎              

‎
#### 3. Start Processing
###### ‎  
a. Click **Spererate!** below. Wait a moment for the audio to process.       
‎       
b. Playable audios will then appear in the output boxes below. To download the output, click the little download icon in the top right.            


### Best Models for Local Eddy UVR5 UI

Extraction | Model
:---: | :---:
Vocals | ``MelBand Roformer | Vocals FV4 by Gabox``
Instrumental | ``MelBand Roformer | INSTV7 by Gabox``
De-Reverb | ``MelBand Roformer | De-Reverb by anvuew``
Extract Backing Vocals | Mel-Roformer-Karaoke-Aufr33-Viperx
De-Noise | Mel-Roformer-Denoise-Aufr33-Aggr


***
### Troubleshooting :icon-tools:
***
#### UVR extracted too little/too much.
- Modify the `Aggression Setting` value on the right. 
- This determines the depth of the extraction. Only the VR method has it.
- A higher value will deepen the extraction, and a lower one will soften it.
- Each audio is different, so you'll have to test the ideal value.

#### I can't remove some of the backing vocals.
- Run the audio through BVE. Modify the Aggression Setting if necessary.

#### I couldn't find my answer.
- Report your issue <u>[here](https://docs.aihub.gg/contributions/)</u>.


+++ UVR5 UI HF

:::content-center
## Eddy's UVR5 UI HuggingFace ZeroGPU Space
:::
***

### How to use :icon-checklist:

#### 1. Access the HuggingFace Space
Access the space <u>[here](https://huggingface.co/spaces/TheStinger/UVR5_UI)</u>, you don't need an account to use this, but making one will get you more free time, and paying for HuggingFace PRO will give you the most ZeroGPU time.
    
#### 2. Select input & options
###### ‎  
a. Tap the **Input Audio** box & select your audio, or simply drag & drop.     
‎        
<img src="../hugging-img/input-audio.png" alt="Input Audio" width="1000" height="auto">‎           
‎       

‎ 
#### 3. Select model
###### ‎  
b. Once it's done uploading, select a Model by the [List of the Best Models](http://docs.aihub.gg/rvc/resources/dataset-isolation/#best-models-for-uvr5-ui-hf). Under that you can change **Segment Size** and **Overlap**, the defaults are fine.   
    <img src="../hugging-img/model-selection.png" alt="Model Selection" width="1000" height="auto">‎              

‎
#### 4. Start Processing
###### ‎  
a. Click **Spererate!** below. Wait a moment for the audio to process.       
‎       
b. Playable audios will then appear in the output boxes below. To download the output, click the little download icon in the top right.            


### Best Models for UVR5-UI-HF

Extraction | Model
:---: | :---:
Vocals | ``MelBand Roformer | Vocals FV4 by Gabox``
Instrumental | ``MelBand Roformer | INSTV7 by Gabox``
De-Reverb | ``MelBand Roformer | De-Reverb by anvuew``
Extract Backing Vocals | Mel-Roformer-Karaoke-Aufr33-Viperx
De-Noise | Mel-Roformer-Denoise-Aufr33-Aggr


***
### Troubleshooting :icon-tools:
***
#### UVR extracted too little/too much.
- Modify the `Aggression Setting` value on the right. 
- This determines the depth of the extraction. Only the VR method has it.
- A higher value will deepen the extraction, and a lower one will soften it.
- Each audio is different, so you'll have to test the ideal value.

#### I can't remove some of the backing vocals.
- Run the audio through BVE. Modify the Aggression Setting if necessary.

#### I couldn't find my answer.
- Report your issue <u>[here](https://docs.aihub.gg/contributions/)</u>.

### GPU task aborted:
ZeroGPU HuggingFace Spaces have a max inference time duration, it’s the time it takes to do an Inference (use the model, not the time of your audio file itself), on default it’s around 1 minute which is what Ilaria RVC uses. You need to retry with a shorter audio, you could also split your audio.

### You have exceeded your GPU quota ( NUMBER s left vs. 60s requested). Sign-up on Hugging Face to get more quotas or retry in Hour:Minutes:Seconds
ZeroGPU HuggingFace Spaces have a quota per account, if you aren’t signed in you will get less quota so it’s better to login for more quota. You could get the ‘Sign-up’ part even if you are logged in. The ZeroGPU Quota can’t be seen but it isn’t unlimited. You can either:
- Login so you get more quota
- Wait
- Pay to be an HuggingFace PRO Member to get X5 times more quota


+++ UVR5 UI Colab

:::content-center
## Eddy's UVR5 UI Google Colab
:::

***
### How to Use :icon-checklist:
     
#### 1. Set up Colab
###### ‎ 
1. First access <u>[Eddy's UVR UI Google Colab](https://colab.research.google.com/github/Eddycrack864/UVR5-UI/blob/main/UVR_UI.ipynb)</u>.   
‎       
2. Then **Log in** to your Google account.      
‎   
3. Execute the **Installation** cell by pressing the play button :icon-play: , optionally check `use_drive` & grant all the permissions for Batch Separation.
‎   
    <img src="../uvrcolab-img/installation.png" alt="UVR5 UI Colab Installation Cell" width="330" height="auto">‎   
‎   

5. Then run the **Run UI** cell. You can choose different tunnels in case one is down. 

    <img src="../uvrcolab-img/run-ui.png" alt="UVR5 UI Colab Run UI Cell" width="600" height="auto">

- Once it's done open the public url, and it will be the same as using Eddy's UVR5 UI Local/HF-Space.


***
### Best Models for UVR5-UI-Colab

Extraction | Model
:---: | :---:
Vocals | ``MelBand Roformer | Vocals FV4 by Gabox``
Instrumental | ``MelBand Roformer | INSTV7 by Gabox``
De-Reverb | ``MelBand Roformer | De-Reverb by anvuew``
Extract Backing Vocals | Mel-Roformer-Karaoke-Aufr33-Viperx
De-Noise | Mel-Roformer-Denoise-Aufr33-Aggr


***
### Troubleshooting :icon-tools:
***

#### Cannot connect to GPU backend.
- You have exhausted the <u>[GPU runtime](https://docs.aihub.gg/rvc/extra/glossary/#google-colab)</u> of Colab.


+++ MSST Colab

:::content-center
## MSST Colab
:::

This is jarredou's Music Source Separation Training (MMST) (Colab Inference).

### How to Use :icon-checklist:

#### 1. Set up Colab
###### ‎ 
1. First access the Colab space <u>[here](https://colab.research.google.com/github/jarredou/Music-Source-Separation-Training-Colab-Inference/blob/main/Music_Source_Separation_Training_(Colab_Inference).ipynb)</u>.   
‎       
2. Then **Log in** to your Google account.      
‎   
3. Execute the **Gdrive Connection** cell by pressing the play button :icon-play:. Grant all the permissions.   
‎   
    <img src="../msstcolab-img/gdrive-connection.png" alt="GDrive Connection cell" width="270" height="auto">‎   
‎   
- It'll finish once the logs say `Mounted at /content/drive`
‎   

5. Then run the **Install** cell. 

    <img src="../msstcolab-img/install-cell.png" alt="Installation Cell" width="270" height="auto">

- Once it's done it will look like this: 

    <img src="../msstcolab-img/installation-done.png" alt="Finished Installation" width="600" height="auto">

***

‎  
#### 2. Set up folders
###### ‎ 
- In Google Drive, make two folders, named **input** & **output**.       
‎       
    <img src="../msstcolab-img/drive-folders.png" alt="GDrive folders input & output" width="600" height="auto">     
‎     
‎     
***
‎  
#### 3. Separate
###### ‎   
a. Select your model of choice and run the **Separation** cell. You can look for the <u>[List of the Best Models](https://docs.aihub.gg/rvc/resources/vocal-isolation/#best-models-for-msst)</u>.

‎   
    <img src="../msstcolab-img/model-selection.png" alt="image" width="500" height="auto">‎   
‎         
!!!
These are the best settings: 
- Overlap: 8
- Chunk Size: 485100
!!!
b. Download the result located in the output folder.
***

#### Best models for MSST:

Extraction | Model
:---: | :---:
Vocals | Gabox's voc_fv4
Instrumental | INST Gabox V7
De-Reverb | Anvuew mel dereverb v2
Extract Backing Vocals | Mel roformer karaoke
De-Noise | Mel denoiser v2


‎
### Troubleshooting :icon-tools:
***

#### Cannot connect to GPU backend.
- You have exhausted the <u>[GPU runtime](https://docs.aihub.gg/rvc/extra/glossary/#google-colab)</u> of Colab.


+++ MVSEP  

:::content-center
## MVSEP
:::

:::content-center
[!button variant="danger" corners="pill" icon="heart-fill" iconAlign="right" text="Support MVSEP by Paying"](https://mvsep.com/billing)
:::

### Important Notes ‎ :icon-alert:
***
- MVSEP is a website for isolating vocals, that works similarly as UVR.

- For free users, you can't convert audios in batches or longer than 10 minutes. If that's your case, trim it into different pieces.

- There is a queue so make sure you make an account to skip most of it.
***
### How to Use :icon-checklist:
***

#### 1. Log in.  
###### ‎
a. First, <u>[login](https://mvsep.com/register)</u>.
‎       
b. Once logged in, go to the <u>[main page](https://mvsep.com)</u>.

!!!
Logging in is not mandatory, but recommended for **shorter waiting lists**.
!!!
***
‎
#### 2. Select audio.   
###### ‎
a. Click `Browse File` & select your audio, or simply drag & drop. The audio will begin to upload.  

    
    <img src="../mvsep-img/upload-input.png" alt="Upload Input" width="330" height="auto">
    
***
‎
#### 3. Model usage.
###### ‎
a. In **Separation type** Select a Model based on the [Best Models List](https://docs.aihub.gg/rvc/resources/vocal-isolation/#best-models-for-mvsep).
‎     
b. In **Output encoding** select `FLAC`.          
We recommend selecting FLAC from now on. Learn more <u>[here](https://docs.aihub.gg/extra/glossary/#lossless-formats)</u>.        
‎     
c. Once the audio is done uploading, click `Separate`       

    <img src="../mvsep-img/model-selection.png" alt="Model Selection" width="400" height="auto">‎   

    <img src="../mvsep-img/output-encoding.png" alt="Flac as Output Encoding" width="420" height="auto">‎    

!!! Leave "Model Type" untouched.
!!!
***
‎
#### 4. Download output.      
###### ‎
- When it's done converting it will redirect you to a page where you can listen the results.      
     
a. Tap the three buttons of the **Vocals** audio and then `Download`.    
‎     
b. Same thing for the **Instrumental**, if you wish to keep it.      

    <img src="../mvsep-img/results.png" alt="Results of separated Stems" width="400" height="auto">‎   


***
#### Best Models for MVSEP:

Extraction | Separation Type | Model
:---: | :---: | :---:
Vocals | MelBand Roformer | `either:` unwa big beta v5e `OR` 2024.10
Instrumental | MelBand Roformer | `either:` unwa instrumental v1e plus `OR` 2024.10
De-Reverb | Reverb Removal | Reverb removal by `either`: Sucial V2 (MelRoformer) `OR` Anvuew V2 (MelRoformer)
Extract Backing Vocals | MelBand Karaoke | Model fuzed gabox & aufr33/viperx (SDR: 9.85)
De-Noise | DeNoise by aufr33 | Aggresive


***
### Troubleshooting :icon-tools:
***
#### MVSEP extracted too much/too little.
- Using the **Separation Type** of `DeNoise by aufr33`, you can modify the `Aggressiveness`. 
This determines the depth of the extraction.
- A higher value will deepen the extraction, and a lower one will soften it.
- Each audio is different, so you'll have to test the ideal value.

#### I can't remove some of the backing vocals.
- Try running the audio through MelBand Karaoke or BVE. Modify the Aggression Setting if necessary.

#### What is SDR?
Signal to distortion ratio, the higher is technically better, but your ears are more trustworthy.


+++ X-Minus

:::content-center
## X-Minus (aka UVROnline)
:::

### How to use :icon-checklist:

!!!warning
Most of the extraction model are behind a pay wall.
!!!


#### 1. Choose a Separator
a. First go to <u>[X-minus's website](https://x-minus.pro)</u> and click the "Vocal Remover" at the top right. 

<img src="../x-minus-img/homepage.png" alt="X-Minus Homepage" width="600" height="auto"> 

b. Then select the Seperator type you need and the model based on the [Best Models List](https://docs.aihub.gg/rvc/resources/vocal-isolation/#best-models-for-x-minus)

  
<img src="../x-minus-img/model-selection.png" alt="Select a Model in X-Minus" width="600" height="auto">

***
#### 2. Upload Your Audio File

c. Then click "select a file" and choose a audio file, or you can drag and drop a file. And when it's done it will look like this: 

<img src="../x-minus-img/model-usage.png" alt="Use a Model in X-Minus" width="600" height="auto">

d. You can now click "Vocals" to download the vocals and "Other" to download the instrumentals.


- #### Best models for X-Minus:

Extraction | Model
:---: | :---: 
Vocals/Instrumental | Mel-RoFormer by Gabox Fv7z
De-Echo / De-Reverb | De-reverb & De-echo by Sucial v2
Extract Backing Vocals | Mel-RoFormer Lead/Back (the only, invisible, available one)
De-Noise (found in Restoration) | Mel Roformer De-Noise 
Restoration | Apollo Universal by Lew (to enhance mp3 and other low quality files)


+++ RX11

:::content-center
## RX 11
:::

Go to their <u>[Official Website](https://www.izotope.com/en/shop/rx-11-advanced/)</u> & buy it.

***
:::content-center
### Getting a Dataset
:::
Getting the highest quality audio works best for Izotope and will result in a better model. Ideally, you want to preserve the **dynamic range**, the **frequencies**, and the **fidelity/clarity**.
If you're working with low quality audio, RX cannot upscale or restore the missing details that were originally there. The end result will be audible as the voice model quality will be muddied with artifacts/tearing.

**Mic proximity** is also another factor to consider as you want the voice to be consistent since RVC does not handle **audio frequency response** well and will muffle the pronunciation of words. Keep this in mind for studio sessions and video game voice lines rips as it may have been bass boosted, compressed, or eq'd by default. Arguably, more variation of the voice will add to the vocal range of the model but we want to keep the accent consistent as well.

#### For Youtube ripping
You can use [Cobalt](https://cobalt.tools/), [yt-dlp](https://github.com/yt-dlp/yt-dlp), or [Loader.to](https://en.loader.to/4/). Overall, yt-dlp is the best for ripping.
Preferably rip the audios in Opus format so the downloaded audio will be 48khz, which can be resampled down to 44.1k on Izotope and trained on 40k via RVC. The quality depends on what is uploaded on the server side so this might not always be the case.

For YT-dlp, the command prompt is:
> yt-dlp -x
> ffmpeg -i audio.opus audio.wav
or
 >yt-dlp.exe --audio-format wav -x https://www.youtube.com/watch?v=5aYwU4nj5QA&t=2s

Resampling down to 32k is also fine since it results in less harsher **sibilance** and **-plosives** for your model.
- Sibilance's are the hissing sounds when a person speaks, and plosives are the sounds of air that are released through the mouth. They are both considered **consonant** sounds with RVC.

Whenever you export the dataset, you can export it to WAV 32-bit. For Flac files, use 24-bit. We never use MP3 files since RVC heavily compresses those audio files.

***
:::content-center
### Loading The Audio And Changing Settings
:::
Open the WAV or FLAC file.

Now that we have the file in RX, make sure to turn this slider to the right to show the Spectrogram only.
<img src="../rx11-img/waveform.png" alt="Waveform" width="auto" height="auto">

Now after that it should look like this:
<img src="../rx11-img/spectrogramview.png" alt="Spectogram View" width="auto" height="auto">

This is using Mel scaling, if you right click on the numbers list(20k and such). you can change the scaling.
Mel is the best scaling in our case since it shows vocals better than Linear scaling would.

!!!success
The brighter a color on the spectrogram, the louder it is and will be audible.
!!!
!!!success
The spectrogram in the example is slightly above a frequency of 15khz. Take the khz x 2 and it would equal to a 32k audio. If it were 20khz, then it'll be a 40k audio. 32k is the lowest sample rate you can train on in RVC if your khz is below 15.
!!!
***
:::content-center
### Trying To Explain a Spectrogram
:::
Spectrograms are graphical representations of frequencies which can determine whether your audio sample rate is 32k, 40k, or 48k.

<img src="../rx11-img/frequency.png" alt="frequency.png" width="auto" height="auto">

There is a distinction between **high-end frequency** and **low-end frequency** in a spectrogram. The high-end frequency (48k-40khz), or the air region in the chart isn't audible for the human ears. But, it'll help to handle **aliasing**. Aliasing is the effect of new frequencies appearing in the sampled signal after reconstruction, that were not present in the original signal. In other words, it creates artifacts to your model.

Meanwhile you can hear some of the low-end frequencies. If you were to resample from 40k to 32k, then most of the high-end and low-end frequencies are gone at the cost of less harsher sibilances and -plosives sounds like I mentioned before.

<img src="../rx11-img/chart.png" alt="Chart.png" width="auto" height="auto">

#### Example of Audios Through a Spectrogram
For example, this is noise. The orange area may look like breathing that's masked under the artifacts, but RVC will consider this noise as it's barely audible and you'll only hear static or dry air. The blue areas surrounding the audio are also noise. You can think of these as layers that needs to be removed when we use the Spectral Denoise module later.

<img src="../rx11-img/noiseprofile.png" alt="noiseprofile.png" width="auto" height="auto">

Now this is breathing. Keep in mind that RVC will consider "soft breathing" as a white noise if the breath sounds are too low (around -40db). Proper vocal breathing are grunts like "huffs, "hahhhhs, "hoohhhhhs". There cannot be harsh inhaling sounds. Breathe sounds by itself without a voice or tone behind it will also cause RVC to think it is noise. Without breathes, the model sound will robotic.
<img src="../rx11-img/breathing.png" alt="Breathing.png" width="auto" height="auto">

And this is speech:
<img src="../rx11-img/speech.png" alt="Speech.png" width="auto" height="auto">
***
:::content-center
### Preparing the Dataset Through Music/SFX Removal
:::
The key principal behind preparing your dataset is doing the *least audio processing* as possible as you want to keep the overall robustness of the model. Excessively stacking vocal separator models such as **UVR** Inst Voc, Kim Vocals, Denoise, ensemble mode, and so forth can introduce noises to your dataset as it rips away frequencies from your audio. This harms the model fidelity and quality.
***
#### RX De-Clipping
This helps to remove most of the clipping that is occurring throughout the audio around the -0db range. Do not touch the make-up gain as it will alter the natural dynamic range of the audio. You can press "preview" to see that it is working as indicated with "clipped intervals repaired". If it does nothing, then you can skip this part.

<img src="../rx11-img/de-clip-settings.png" alt="de-clip-settings.png" width="auto" height="auto">

#### Removing DC Offset
Before starting the process for separation, make sure that the audio has zero DC offset to prevent further issues that would interrupt the processing due to the bottom line noise. The **waveform statistics** is under the Window tab in RX11.
<img src="../rx11-img/dcoffset.png" alt="dcoffset.png" width="auto" height="auto">

This can be done in audacity by going to the Effect tab > Volume and Compression > Normalize then check the box to remove the DC offset.
<img src="../rx11-img/remove-dc-offset.png" alt="Remove-dc-offset.png" width="auto" height="auto">

If you prefer to **EQ** in RX 11, then click on the EQ module and enable only the hp bell curve. Keep the frequency precision to 6 and the frequency at 30-32hz. Your DC offset will be at 0% if you've done it correctly.

Here's a small comparison with the changes after vocal separation.
Without DC offset:
<img src="../rx11-img/resizing.png" alt="resizing.png" width="auto" height="auto">

With DC offset:
<img src="../rx11-img/with-dc-offset.png" alt="With-dc-offset.png" width="auto" height="auto">
***

#### Dereverbing and De-echo The Audio
While keeping in mind of doing the least processing, *you want to keep the audio as natural* as possible for RVC, or **Hifigan**. Hifigan is the generative adversarial network that makes up our discriminator and generator for cloning sounds and training stability. Having audio that has been damaged or reconstructed will affect the generalization of the graphs to fully replicate the clarity and accent of the voice.

**Reverb** is multiple sources of sound returning and **echo** is the delay. It is important to remove these from the dataset otherwise it'll cause your model to have artifacts as Hifigan cannot replicate the model's clarity.

#### Best Model for Dereverb And De-echo
The current best Dereverb plugin is the **Clarity VX** DeReverb Pro module, another paid software that you can get for free. The aggressiveness can be tweaked or finetuned to your liking as it cuts into the audio and does not reconstruct the frequencies. Clarity VX cannot de-echo the audio so you need to use UVR De-echo or RX Dialogue Isolate.

<img src="../rx11-img/clarity-vx.png" alt="Clarity-VX.png" width="auto" height="auto">

!!!warning Audio damage
Any use of the De-echo model with UVR will slightly damage your audio with a 17khz cutoff frequency on the spectrogram.
!!!
If you don't want to use ClarityVX, the most common method is to use UVR Dereverb and De-echo separately as you have full control on what's needed for your audio. *There is no predetermined settings as each audio is different.* The rule of thumb is to use an aggression of 3.0 -5.0 and nothing more than that. If the audio does not have reverb or echo, do not use any of these models as it can muffle the audio.

If you only rely on MVSEP, you're forced to use UVR-DeEcho-Dereverb as there is no standalone option for the dereverb model. The cutoff frequency for this separation model would be 17.5khz.

<img src="../rx11-img/deecho.png" alt="Deecho.png" width="auto" height="auto">

Here's what audio with mono reverb will look like on Izotope RX11:
<img src="../rx11-img/mono-reverb.png" alt="mono-reverb.png" width="auto" height="auto">

And the result of DeEcho-Dereverb at 0.5 aggression:
<img src="../rx11-img/aggression.png" alt="aggression.png" width="auto" height="auto">

There may be leftover reverb or echo that weren't removed so that'll be addressed in the **RX Dereverb** module later in the **Manual Denoising** section. I will also troubleshoot the audio increasing in volume after dereverb and deecho in the **FAQ Regarding Normalization and Compression** section.
***
:::content-center
### RX11 Modules
:::
***
#### Spectral Denoising The Audio
Izotope's Spectral Denoise provides natural noise reduction and will preserve the quality of your audio as it minimizes artifacts. It analyzes the signals of noise that we select and modifies the frequency components. Essentially, **UVR Denoise** is not needed afterwards since the cleaning has been processed in spectral. The rest of the the cleanup is done through our manual denoising via RX11.

Here is the settings that were used in the previous guide, which is mostly fine if you can't recognize patterns in a noise profile. *Artifact control, whitening, Release [ms], Smoothing, and Reduction* could be adjusted based on particular datasets. Again, don't fix it if it aint broke.
<img src="../rx11-img/spectral-denoise.png" alt="Spectral-denoise.png" width="auto" height="auto">

You only need to do one or two passes of spectral denoising. Doing further processing than that will compress, or degrade your audio. Be cautious of overdoing it with the noise profile (selecting breathing or speech by accident) as RX might take away details and important aspects of a person's voice.

!!!success
Wouldn't this take up too much time?
If your dataset is too long for spectral denoising, I suggest splitting it into sections so it is more manageable. It won't mess up with the overall noise profile of the whole dataset if you do so. You're prone to make mistakes/misclicks when selecting audio, especially when the dataset is 20 minutes to an hour long.
!!!

!!!success
What if I didn't capture the entire profile?
Some noises may, or may not stay in tact even after the second pass with Spectral Denoise. RX will only pick out each respective noise samples to the audio that has been selected so it's better that you capture it in full.
!!!

This is what the audio looks like before spectral denoising:
<img src="../rx11-img/spectral-denoise-1.png" alt="Spectral-denoise-1.png" width="auto" height="auto">

Now we select the noise (click and hold shift after selecting an area to include multiple audios) then press learn in the Spectral Denoise module after we captured the entire noise profile. Unselect the audio and click render.
<img src="../rx11-img/spectral-denoise-2.png" alt="Spectral-denoise-2.png" width="auto" height="auto">

Now in this case one pass of spectral denoise wasn't enough. Repeat the steps done in the first pass by selecting the areas with the blue noise.
<img src="../rx11-img/spectral-denoise-3.png" alt="Spectral-denoise-3.png" width="auto" height="auto">

The 2nd pass will remove the noise.
<img src="../rx11-img/2pass.png" alt="2Pass.png" width="auto" height="auto">
***
#### FAQ Regarding Normalization and Compression
**Why does my audio sounds like it's clipping or distorted? Should I use the gain tool in RX?**
Audios will usually have crackling and clicking noises introduced if it's over 1.0+db. We don't want to use the gain tool to address this since it's a compressor. If it doesn't have any of those issues, then leave the dialogue alone to maintain its natural range.
<img src="../rx11-img/too-loud.png" alt="too-loud.png" width="auto" height="auto">

!!!danger
Do not use any form of compression on speech as it'll squash the dynamics and introduce artificial tearing to your model.
!!!
Again, try to maintain the **natural dynamic range** if possible. If you must decrease the volume on a particular dialogue because its too loud for your ears and you still need to use the RX Dereverb module, consider normalizing between -2db or -3db. The use of the **RX Dereverb** will put it back to normal volume.

**When should I normalize the whole dataset?**
It is optional to use this module as it can be argued that rvc will do the normalization for you with -2db. You can normalize the dataset when it has been thoroughly cleaned at the end, if you want.

<img src="../rx11-img/normalization.png" alt="Normalization.png" width="auto" height="auto">
***
#### Modules overview
**De-ess**
This tool is used so that the -ess /fff/z/ch sounds, or sibilances, are less harsh/robotic when the voice model tries to pronounce certain words. Only use this on the actual sibilances and not the entire dataset/dialogue. Automatic de-ssing with Ctrl + A can select the wrong consonant sounds or skip audios that needs more de-essing so keep that in mind. Adjust spectral shaping as needed if you know what you're doing.

<img src="../rx11-img/de-ess.png" alt="De-ess.png" width="auto" height="auto">

**De-crackle**
Only use this tool if you hear crackling noises in specific parts of your dialogue/speech. It's not a requirement to use it.
<img src="../rx11-img/de-crackle.png" alt="De-crackle.png" width="auto" height="auto">

**Mouth De-clicking and De-click**
Only use mouth de-clicking when clicking noises are audible. It's a good practice to use mouth de-clicking on only the click and not the entire dialogue/audio. Adjust the sensitivity or frequency skew as needed, but do not go overboard as it can remove the finer details of our audio.
- This module is specifically tailored to address mouth noise issues in vocal recordings. Mouth noises are typically caused by saliva, lip smacks, tongue clicks, or other oral sounds that can be distracting or unpleasant to listen to in vocal recordings. Mouth de-click module preserves the integrity and naturalness of the vocal performance while reducing these types of mouth noises.

We run the **de-click** module only as a last resort when mouth de-click doesn't work. Using both modules together may strip away the "k" consonants of our model.
<img src="../rx11-img/de-click.png" alt="De-click.png" width="auto" height="auto">
- This module is designed to remove or reduce short impulse noises such as clicks, pops, and digital clipping artifacts from audio recordings. These noises can occur due to various reasons, including imperfections in the recording equipment, electrical interference, or flaws in the audio signal itself. The De-click module analyzes the audio waveform and identifies these short, transient noises, then applies processing algorithms to smooth out or remove them, restoring the audio to a cleaner state.


**Dialogue Isolate**
Use this tool when you have audible room echo that could be removed on specific parts of your speech. Do not use it for the entire dataset because it may be inaccurate and strip away details. Or sometimes it doesn't work. Keep the settings the same here including sensitivity.
<img src="../rx11-img/dialogue-isolate.png" alt="dialogue-isolate.png" width="auto" height="auto">

**De-plosive**
Use Deplosives when there are audible thumps of air coming through the mouth. Again, -plosives are consonant sounds that needs attention. Specifically the P, T, K, and CH sounds. There are no right settings for this so adjust it until the roughness of the -plosives are gone.
<img src="../rx11-img/deplosive.png" alt="Deplosive.png" width="auto" height="auto">

Plosives look like this. Do not select the whole speech and only the plosives as suggested in the red lines.
<img src="../rx11-img/plosive-examples.png" alt="plosive-examples.png" width="auto" height="auto">

**De-hum**
Use De-humming to take care of low or high frequency hums. There are no consistent settings for this as each situation is different for your audio.
- Sensitivity will adjust the amount of hum that will be removed.
- Bands, or notch filters will increase depending on the complexity of the noise.
- Filter Q is the range selector.

<img src="../rx11-img/dehum.png" alt="dehum.png" width="auto" height="auto">


For example, use the **frequency selector tool**, select the humming occurring below 100hz, then press learn and render.
<img src="../rx11-img/freq.png" alt="freq.png" width="auto" height="auto">

<img src="../rx11-img/fnwwdec.png" alt="FnwwDec.png" width="auto" height="auto">

The red underline shows what you should be looking for.
<img src="../rx11-img/humming100hz.png" alt="humming100hz.png" width="auto" height="auto">

**EQ**
This has already been covered in the section for removing the **Removing DC Offset**. Do this if you haven't done it already. It takes care of low-end noise, but if your dc offset is already at 0% then skip this module.
***
#### Manual Denoising
You should have noticed that RX11 moves the audio closer to each other whenever you delete a space or speech. Use the **Lasso** or **Brush tool** to delete dialogue precisely, which should preserve the spacing in **phonetics**. Make sure it does not cause clipping on the waveform as it'll look like a sharp spike. You can also clean up the leftover residuals left behind by spectral denoising.

Audios with thumping, SFX sounds, ringing noises, and weird vocalizations or breaths that might affect the voice model should be removed from the dataset as it'll have those characteristics. You can try to lasso out the possible source of the noise, but keep the audio as natural as possible without damaging the frequencies.

<img src="../rx11-img/lasso.png" alt="lasso.png" width="auto" height="auto">

<img src="../rx11-img/lasso-3.png" alt="lasso-3.png" width="auto" height="auto">


The **RX Dereverb** module will remove reverb that's leftover from the audio and may help remove noises.
With RX Dereverb, select the audio, press learn and render. Adjust the reduction if needed. Do not use a strong reduction as it may muffle the audio. You can always undo with Ctrl + Z.

Refer to the **FAQ Regarding Normalization and Compression** if the volume is peaking or "introducing noises", which isn't the case at all. Do note that RX Dereverb will raise the volume by 2db each time you use it.

<img src="../rx11-img/dereverb.png" alt="dereverb.png" width="auto" height="auto">
When the dataset has been thoroughly cleaned, you can resample the dataset to 32k or 44.1k and export as a WAV 32-bit or Flac 24-bit.

<img src="../rx11-img/resample.png" alt="resample.png" width="auto" height="auto">
***
:::content-center
### Noise Gating and Audio Labeling
:::
[Auburn Renegate](https://www.auburnsounds.com/products/Renegate.html)
(basically Audacity noisegate but better) the free version will be more than enough.
<img src="../rx11-img/auburn-noise-gate.png" alt="Auburn-noise-gate.png" width="auto" height="auto">

We can open Audacity and run the the dataset through **Auburn Renegate**. After that convert your dataset to mono since RVC works on mono and not stereo. There are two ways of neatly removing the silences in your dataset called **Audio Labeling and Truncate**.

Follow these steps:
Open the menu for labeling.
<img src="../rx11-img/audiolabel1.png" alt="audiolabel1.png" width="auto" height="auto">
<img src="../rx11-img/audiolabel2.png" alt="audiolabel2.png" width="auto" height="auto">

You will now have it like this:
<img src="../rx11-img/audiolabel3.png" alt="audiolabel3.png" width="auto" height="auto">

Turn off shaped dither with `Ctrl + P` > Quality since we are exporting with WAV 32-Bit or FLAC 24-bit anyways.
<img src="../rx11-img/preferences-quality.png" alt="preferences-quality.png" width="auto" height="auto">

Now we go to export our audio.
<img src="../rx11-img/audiolabel4.png" alt="audiolabel4.png" width="auto" height="auto">
<img src="../rx11-img/audiolabel5.png" alt="audiolabel5.png" width="auto" height="auto">

The output will be like this:
<img src="../rx11-img/audiolabel6.png" alt="audiolabel6.png" width="auto" height="auto">

Now go in the RVC folder and place all these files in datasets folder. Zip it up if needed.


+++

You can find an extremely long and complex guide by the [Audio Separation's Discord](https://discord.gg/ZPtAU5R6rP): [here](https://docs.google.com/document/d/17fjNvJzj8ZGSer7c7OFe_CNfUKbAxEh_OBv94ZdRG5c/edit?tab=t.0), but it's not suggested and might have some outdated info as it got hundrends of pages.


***

:::content-center
## Preparing the dataset
:::

- To do these next steps you are going to need <u>[Spek](https://www.spek.cc/p/download)</u> and <u>[Audacity](https://www.audacityteam.org)</u>.

### Step 1: Find the Sample Rate
:::
- This is a unit in that defines the total amount of **samples** (data) that can **fit** within **1 second** of an audio. They are measured in kilohertz (kHz).

- The most common sample rates are **32, 40, 44.1, & 48**. The **higher** the sample rate, the more information it stores, therefore the higher the **quality**.  

- While training in RVC, you'll have to set the **target sample rate** as your dataset's. This value affects the final quality.  
   
- ##### A simple way to determine it is with <ins>Spek</ins>:  

    - ##### STEP 1:   
        Download and install Spek <u>[here](https://www.spek.cc/p/download)</u>.
    - ##### STEP 2:   
        Open spek and just drag & drop audio into it. 

        <img src="../audioformats-img/3.png" alt="image" width="500" height="auto">‎   

    !!!danger <u>WARNING:</u>   
    If the frequencies don't reach the top of the spectrogram, see at which number peaks & multiply it by <U>**2**</u>. Here it reached 20 kHz. **Doubling** it gives 40kHz. Therefore the ideal target sample rate would be ``40k``
    !!!
***
### Step 2: Truncating Silence 

- In Audacity import your audio 
- Go to Effects -> Special -> Truncate Silence     
- Use the following values:         
    ‎  
    <img src="../datasets-img/truncnew.png" alt="image" width="420" height="auto">    
    ***
‎
***

### Step 2.1: Audio Normalization (Optional)

- LUFS are used over db because hifigan needs perceptual quality and db doesnt offer that.
- You can perform this step directly within Applio or using Audacity (for any RVCs).

***
#### Method 1: Using Applio's Built-in Normalization

Applio includes a convenient built-in normalization feature that can process your audio during the slicing step.

1.  Go to Applio -> Training -> Preprocess -> Advanced Settings -> Normalization mode.
2.  Select the **`post`** option.

This will normalize each audio slice individually after it has been separated from the main file.

<img src="../datasets-img/applio-normalization.png" alt="Applio Normalization Setting" width="500" height="auto">

***
#### Method 2: Using Audacity

!!!danger
The model learns the (normalized) sliced audios, not the whole dataset at once, otherwise the model doesn't properly learn the frequencies. For using this method, you would have to manually 3 seconds slice dataset which might not be perfect, unlike Applio which already slices it (unless you manually turn that off) and then normalizes it with the other method. Usually the Applio method is more suggested
!!!

1.  Open your audio file in Audacity.
2.  Go to `Effects` -> `Volume and Compression` -> `Loudness Normalization`.
3.  Use the following values:
    - **Normalize:** perceived loudness
    - **Loudness:** -23.0 LUFS
    - **Treat mono as dual-mono:** checked (recommended)

<img src="../datasets-img/norm.png" alt="Audacity Loudness Normalization Settings" width="500" height="auto">

***
#### Step 2.2: Combining Audio  

- Go go to Tracks -> Align Tracks -> Align End to End

<img src="../datasets-img/combine.png" alt="image" width="420" height="auto"> 

***
### Step 3: Export
- On the upper right corner go to File and click ``Export Audio``.       
    ‎   
    <img src="../datasets-img/4.png" alt="image" width="370" height="auto"> 
    ‎       
    ‎              

    - And finally, introduce these values:  
        - **Format**: ``WAV``
        - **Encoding**: ``32-Bit Float``

        ###### ‎    

        <img src="../datasets-img/settings-wav.png" alt="image" width="650" height="auto">


***
:::content-center
## Communities :icon-people:
:::

<div style="display: flex; flex-direction: column; gap: 1rem; align-items: center; padding: 1rem 0;">
    <a href="https://discord.gg/aihub" style="display: inline-flex; align-items: center; gap: 0.5rem; background-color: #1a1c1d; color: white; padding: 0.6rem 1.2rem; border-radius: 9999px; text-decoration: none; font-weight: bold; font-size: 1rem; min-width: 150px; justify-content: center; border: 1.5px solid #555;">
        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjcuMTQgOTYuMzYiPgogICAgPHBhdGggZmlsbD0iIzU4NjVmMiIKICAgICAgICBkPSJNMTA3LjcsOC4wN0ExMDUuMTUsMTA1LjE1LDAsMCwwLDgxLjQ3LDBhNzIuMDYsNzIuMDYsMCwwLDAtMy4zNiw2LjgzQTk3LjY4LDk3LjY4LDAsMCwwLDQ5LDYuODMsNzIuMzcsNzIuMzcsMCwwLDAsNDUuNjQsMCwxMDUuODksMTA1Ljg5LDAsMCwwLDE5LjM5LDguMDlDMi43OSwzMi42NS0xLjcxLDU2LjYuNTQsODAuMjFoMEExMDUuNzMsMTA1LjczLDAsMCwwLDMyLjcxLDk2LjM2LDc3LjcsNzcuNywwLDAsMCwzOS42LDg1LjI1YTY4LjQyLDY4LjQyLDAsMCwxLTEwLjg1LTUuMThjLjkxLS42NiwxLjgtMS4zNCwyLjY2LTJhNzUuNTcsNzUuNTcsMCwwLDAsNjQuMzIsMGMuODcuNzEsMS43NiwxLjM5LDIuNjYsMmE2OC42OCw2OC42OCwwLDAsMS0xMC44Nyw1LjE5LDc3LDc3LDAsMCwwLDYuODksMTEuMUExMDUuMjUsMTA1LjI1LDAsMCwwLDEyNi42LDgwLjIyaDBDMTI5LjI0LDUyLjg0LDEyMi4wOSwyOS4xMSwxMDcuNyw4LjA3Wk00Mi40NSw2NS42OUMzNi4xOCw2NS42OSwzMSw2MCwzMSw1M3M1LTEyLjc0LDExLjQzLTEyLjc0UzU0LDQ2LDUzLjg5LDUzLDQ4Ljg0LDY1LjY5LDQyLjQ1LDY1LjY5Wm00Mi4yNCwwQzc4LjQxLDY1LjY5LDczLjI1LDYwLDczLjI1LDUzczUtMTIuNzQsMTEuNDQtMTIuNzRTOTYuMjMsNDYsOTYuMTIsNTMsOTEuMDgsNjUuNjksODQuNjksNjUuNjlaIiAvPgo8L3N2Zz4=" alt="Discord Icon" style="width: 20px; height: 20px;"/>
        <span>AI HUB's Discord</span>
    </a>
    <a href="https://discord.gg/ZPtAU5R6rP" style="display: inline-flex; align-items: center; gap: 0.5rem; background-color: #1a1c1d; color: white; padding: 0.6rem 1.2rem; border-radius: 9999px; text-decoration: none; font-weight: bold; font-size: 1rem; min-width: 150px; justify-content: center; border: 1.5px solid #555;">
        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjcuMTQgOTYuMzYiPgogICAgPHBhdGggZmlsbD0iIzU4NjVmMiIKICAgICAgICBkPSJNMTA3LjcsOC4wN0ExMDUuMTUsMTA1LjE1LDAsMCwwLDgxLjQ3LDBhNzIuMDYsNzIuMDYsMCwwLDAtMy4zNiw2LjgzQTk3LjY4LDk3LjY4LDAsMCwwLDQ5LDYuODMsNzIuMzcsNzIuMzcsMCwwLDAsNDUuNjQsMCwxMDUuODksMTA1Ljg5LDAsMCwwLDE5LjM5LDguMDlDMi43OSwzMi42NS0xLjcxLDU2LjYuNTQsODAuMjFoMEExMDUuNzMsMTA1LjczLDAsMCwwLDMyLjcxLDk2LjM2LDc3LjcsNzcuNywwLDAsMCwzOS42LDg1LjI1YTY4LjQyLDY4LjQyLDAsMCwxLTEwLjg1LTUuMThjLjkxLS42NiwxLjgtMS4zNCwyLjY2LTJhNzUuNTcsNzUuNTcsMCwwLDAsNjQuMzIsMGMuODcuNzEsMS43NiwxLjM5LDIuNjYsMmE2OC42OCw2OC42OCwwLDAsMS0xMC44Nyw1LjE5LDc3LDc3LDAsMCwwLDYuODksMTEuMUExMDUuMjUsMTA1LjI1LDAsMCwwLDEyNi42LDgwLjIyaDBDMTI5LjI0LDUyLjg0LDEyMi4wOSwyOS4xMSwxMDcuNyw4LjA3Wk00Mi40NSw2NS42OUMzNi4xOCw2NS42OSwzMSw2MCwzMSw1M3M1LTEyLjc0LDExLjQzLTEyLjc0UzU0LDQ2LDUzLjg5LDUzLDQ4Ljg0LDY1LjY5LDQyLjQ1LDY1LjY5Wm00Mi4yNCwwQzc4LjQxLDY1LjY5LDczLjI1LDYwLDczLjI1LDUzczUtMTIuNzQsMTEuNDQtMTIuNzRTOTYuMjMsNDYsOTYuMTIsNTMsOTEuMDgsNjUuNjksODQuNjksNjUuNjlaIiAvPgo8L3N2Zz4=" alt="Discord Icon" style="width: 20px; height: 20px;"/>
        <span>Audio Separation's Discord</span>
    </a>
</div>


***
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
