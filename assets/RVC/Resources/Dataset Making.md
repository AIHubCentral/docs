---
icon: chevron-right
order: 2000
---

``Last update: Dec 24, 2024``
***
 ‎
:::content-center
## Introduction
:::
- In this massive guide it will be explained how to **properly** prepare a dataset to make a RVC model.

- ***In the field of AI***, it's the collection of data used to train an AI model. It contains examples of the inputs the model is expected to handle, along with the correct outputs.

- **In the context of RVC**, it's an audio file that's given to RVC, containing the voice the model is going to replicate. It can be a speaking, singing voice drums, sound effects or noise.

- The **quality**, **variety** & **length** of the dataset are the biggest determining factors for the final quality of the model. Let's explain Length and Variety.
***
 ‎
:::content-center
## Length & Variety
:::
- For beginners we recommend sticking with a dataset length of **15 minutes** of pure data not counting silence, or if you desire a natural sounding model go for **40+** minutes of dataset. Just remember **quality over quantity**.            

- **Variety** in your dataset is also important because without it RVC lacks the ability to generate diverse audio.

- Some things to increase the generalization abilities of RVC and increase the diversity in your dataset include:
    - Removing repeated words. ( If you want you can be extreme you can do this and remove every single repeated word that's fine, but generally there is no need to do this. )
    - Include speech in many ranges and pitches. 
    - Longer datasets.
    - Expressive speech
***
 ‎
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
- The higher the audio quality, the better. If possible have it in a <u>[lossless](https://docs.ai-hub.wtf/extra/glossary/#lossless-formats)</u> format like **WAV** or **FLAC**, not a lossy one like MP3. No converting a MP3 to a FLAC or WAV won't remove the compression.  
‎   
#### :icon-chevron-down: No harsh sibilance/popping.
- Additionally, don't include harsh sibilance (loud "S" & "SH" pronunciation) or popping sounds (loud "P" sound) 
    - Robotic sibilances are due to your dataset being short. You can fix this by making your dataset larger
    - Harsh sibilances are due to your dataset having harsh sibilants. You can fix this by de-essing or making your dataset larger
‎  
#### :icon-chevron-down: No Audio Damage.
- The most inportant part of a clean dataset, if your audio is damaged RVC will struggle with it causing it to overall sound worse because RVC will create synthetic data and try to learn from it, so make sure your audio isn't damged.  
‎   
***

## Artifacts        
In RVC, artifacting refers to an anomaly where the output voice sounds "robotic" & glitchy.     
This occurs after the <u>[inference](https://docs.ai-hub.wtf/extra/glossary/#inference)</u> or model training process.     
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
- If possible, it's best if your audio is in a <u>[lossless format](https://docs.ai-hub.wtf/extra/glossary/#lossless-formats)</u> like **WAV** or **FLAC**, preserving its original quality.

- Avoid using lossy ones like MP3 or OGG.
‎   
#### 2. If doing inference:
- Remove undesired noises with an <u>[vocal isolation</u>](https://docs.ai-hub.wtf/rvc/resources/vocal-isolation/) software.

- Lowering the <u>[search feature ratio</u>](https://docs.ai-hub.wtf/rvc/resources/inference-settings/) can also minimize this issue.

- If breathing sounds produce it, lower the <u>[Protection](https://docs.ai-hub.wtf/rvc/resources/inference-settings/)</u> value.
‎   
#### 3. If training models:
- Ensure to <u>[clean your dataset](https://docs.ai-hub.wtf/rvc/resources/datasets/#cleaning-datasets)</u> properly, this includes removing silences and distortions.

***
 ‎
:::content-center
## Vocal Isolation & Cleaning
:::  
- A vocal isolation app is a software designed to extract a person's vocals from an audio file, usually through the use of AI models.

- They can remove undesired noises, like background noise, reverb, echo, music, etc.    

- The goal is to get an audio sample with clean and natural vocals, which is what RVC needs to give the most accurate & quality results.

- For RVC users, the best app is Ultimate Vocal Remover 5 (or **UVR**). It can be used either <u>[locally](https://docs.ai-hub.wtf/extra/glossary/#local-running)</u> or through the <u>[cloud](https://docs.ai-hub.wtf/rvc/resources/vocal-isolation/#cloud-uvr-)</u>.

- If you want to remove noise manually to avoid ai artifacts you can use RX 11, which is mentioned in this guide. 

‎ 

+++ Local

:::content-center
## Local UVR
!!!warning 
*You'll require great specs & GPU to run it effectively. Otherwise, use either the <u>[google colab version](https://docs.ai-hub.wtf/rvc/resources/vocal-isolation/#cloud-uvr)</u> or the Huggingface space.*
!!!
:::
‎ 
:   ‎ 

### Installation :icon-download:
*** 
1. Go to their <u>[official website</u>](https://ultimatevocalremover.com/) & press `Download UVR`. And if you want to use BS Roformer you are going to need to install <u>[this](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/UVR_12_8_24_23_30_BETA_rofo_full_install.exe)</u>.

    <img src="../uvrmvsep-img/1.jpg" alt="image" width="" height="auto">   

***
###### 
2. It will redirect you their GitHub page. Click the download link for your **operating system**.   
UVR is available both on **Windows & Mac**.
***
###### ‎ 
3. Once the installer finishes downloading, execute it & follow the instructions.     
Make sure to tick `🗹 Create a desktop shortcut` for an easier access to UVR.

    <img src="../uvrmvsep-img/2.jpg" alt="image" width="500" height="auto"> 
***
###### ‎       
###### ‎     
### How to Use :icon-checklist:  
***  

==- *Extracting Vocals From Songs 🎶*
###### ‎  
#### 1. Input audio.        
###### ‎  
- Click `Select input` to select your audio/s. Or just drag the files to it.  
‎   
- In `Select output` you can define the folder for the results.      

    <img src="../uvrmvsep-img/4.jpg" alt="image" width="300" height="auto">         ‎    

!!!success 
For better results, have the audio in a <u>[lossless format](https://docs.ai-hub.wtf/extra/glossary/#lossless-formats)</u> (**WAV** or **FLAC**), & not MP3.
!!!
***
‎ 
#### 2. Select FLAC & GPU Conversion.
###### ‎  
a. At the right you can select the output format.       
We recommend picking `FLAC`. Learn why <u>[here](https://docs.ai-hub.wtf/extra/glossary/#lossless-formats)</u>.   
‎  
b. If your GPU is **compatible with <u>[CUDA](https://docs.ai-hub.wtf/extra/glossary/#cuda)</u>**, toggle `GPU Conversion` on for a faster process.    

    <img src="../uvrmvsep-img/16.png" alt="image" width="350" height="auto">‎      

###### ‎       
>This step is not mandatory, but recommended for better results.
***
‎
#### 3. Extract vocals. 
###### ‎  
a. In **CHOOSE PROCESS METHOD** select `MDX-Net`, and select either the `BS Roformer-Viper-X 1296` or `MDX23C` model.   

    <img src="../uvrmvsep-img/5.jpg" alt="image" width="250" height="auto">‎      
###### ‎  
###### ‎    
b. Now click the long `Start Processing` button.    
###### ‎  
!!!success 
<u>**TIP:**</u> To **test** models/options more efficiently, tick `Sample Mode` to only process 30 seconds of your sample.
!!!   
***
‎
#### 4. Clean vocals. 
###### ‎    
- Usually songs include reverb & backing vocals. These **negatively** impact the results in RVC. 

- So if the output has any undesired noises, follow the procedure on **Cleaning Vocals**.       
‎  
===

==- *Cleaning Vocals 🗣️*

###### ‎    
#### 1. Input audio.
###### ‎      
- Click `Select input` to input the vocals. Or just drag the files to it.  
‎   
- In `Select output` you can define the folder for the results.    

    <img src="../uvrmvsep-img/4.jpg" alt="image" width="300" height="auto">         ‎    

!!!success 
For better results, have the audio in a [lossless format](https://docs.ai-hub.wtf/extra/glossary/#lossless-formats)</u> (**WAV** or **FLAC**), & not MP3.
!!!
***
‎   
#### 2. Select FLAC & GPU Conversion.
###### ‎      
a. At the right you can select the output format.       
We recommend picking `FLAC`. Learn why <u>[here](https://docs.ai-hub.wtf/extra/glossary/#lossless-formats)</u>.     
‎   
b. If your GPU is **compatible with <u>[CUDA](https://docs.ai-hub.wtf/extra/glossary/#cuda)</u>**, toggle `GPU Conversion` on for a faster process.    
    ‎       
        <img src="../uvrmvsep-img/16.png" alt="image" width="350" height="auto">‎      
###### ‎       
>This step is not mandatory, but recommended for better results.
***
‎   
#### 3. Select model.  
###### ‎      
a. In **Process Method** select `VR`.     
‎   
b. Set **Window Size** to ``320``. (optional)        
Lower Window Size yield a higher output **quality**, but will take **longer** to process.   
‎   
b. Check the <u>[model list](https://docs.ai-hub.wtf/rvc/resources/vocal-isolation/#best-models)</u>. In **Select VR Model** pick the one according to what you need to remove.         
‎       
If you need to remove multiple noises, follow this pipeline for the best results:   
``Remove instrumental -> Remove reverb -> Extract main vocals -> Remove noise``  
###### ‎  
!!!success 
<u>**TIP:**</u> To **test** models/options more efficiently, tick `Sample Mode` to only process 30 seconds of your sample.
!!!  
***
‎  
#### 4. Process.
###### ‎      
Click the `Start processing` button at the bottom. And that will be all. 

***
###### ‎  
:::content-center
[!button variant="danger" size="m" corners="pill" icon="heart-fill" iconAlign="right" text="Support UVR"](https://www.buymeacoffee.com/uvr5)
:::     
‎  
===

- #### The best models for UVR are:

Extraction | Process Method | Model
:---: | :---: | :---:
Vocals/Instrumental | MDX-Net | BS Roformer-Viper-X 1296 / 1297
De-Reverb | VR | UVR-DeEcho-DeReverb
Extract Backing Vocals | VR | UVR-BVE-4B_SN-44100-1
De-Noise | VR | UVR-DeNoise 

‎
### Troubleshooting :icon-tools:

***

==- *A model isn't there.*
###### ‎ 
- Click the wrench (🔧) on the left & go to `Download Center`
- Select the category of the model (MDX-NET or VR)
- Unfold its dropdown & select the model that you need
- Then click the download button (📥). The model will download, which will take a few minutes
===

==- *UVR extracted too little/too much.*
###### ‎
- Modify the `Aggression Setting` value on the right. 
- This determines the **depth** of the extraction. Only the **VR** method has it.
- A higher value will deepen the extraction, and a lower one will soften it.
- Each audio is different, so you'll have to test the ideal value.
===

==- *I can't remove some of the backing vocals.*
###### ‎
- Run the audio through BVE. Modify the <u>[Aggression Setting](https://docs.ai-hub.wtf/rvc/resources/vocal-isolation/#uvr-extracted-too-little-too-much)</u> if necessary.
===

***
:::content-center
## RX 11
:::
‎ 
:   ‎ 

### Installation :icon-download:
*** 
1. Go to their <u>[official website</u>](https://www.izotope.com/en/shop/rx-11-advanced/?srsltid=AfmBOor--irjtR7Bsl08_bPj-7UMUGd49tYy9C_U2iXOAupjQ74Mat_s) & buy it or sail the seven seas and find a treasure box which contains RX 11. 
***
###### ‎ 
### Usage 
2. To use RX 11 it is **STONGLY** recommended that you read this <u>[guide](https://rentry.co/RVC-dataset-RX11)</u> on RX 11.

+++ Colab
:::content-center
## Cloud UVR
:::

### How to Use :icon-checklist:

***
==- *Extracting Vocals From Songs* 🎶
###### ‎       
#### 1. Set up Colab
###### ‎ 
1. First access the Colab space <u>[here](https://colab.research.google.com/github/jarredou/Music-Source-Separation-Training-Colab-Inference/blob/main/Music_Source_Separation_Training_(Colab_Inference).ipynb)</u>.   
‎       
2. Then **Log in** to your Google account.      
‎   
3. Execute the **Gdrive Connection** cell by pressing the play button :icon-play:. Grant all the permissions.   
‎   
    <img src="../clouduvr-img/1.png" alt="image" width="270" height="auto">‎   
‎   
- It'll finish once the logs say `Mounted at /content/drive`
‎   

5. Then run the **Install** cell. 

    <img src="../clouduvr-img/3.png" alt="image" width="270" height="auto">

- Once it's done it will look like this: 

    <img src="../clouduvr-img/4.png" alt="image" width="600" height="auto">

***

‎  
#### 2. Set up folders
###### ‎ 
- In Google Drive, make two folders, named **input** & **output**.       
‎       
    <img src="../clouduvr-img/2.png" alt="image" width="600" height="auto">     
‎     
‎     
***
‎  
#### 3. Separate
###### ‎   
a. Select your model of choice and run the **Separation** cell. You can look <u>[here](https://docs.ai-hub.wtf/rvc/resources/vocal-isolation/#best-models)</u> for the best models

‎   
    <img src="../clouduvr-img/5.png" alt="image" width="500" height="auto">‎   
‎         
!!!
These are the best settings: 
- Overlap: 8
- Chunk Size: 485100
!!!
b. Download the result located in the output folder.
***
===

- #### The best model for this change a lot so it's best you look <u>[here](https://docs.google.com/spreadsheets/d/1pPEJpu4tZjTkjPh_F5YjtIyHq8v0SxLnBydfUBUNlbI/edit?usp=sharing)</u>, but as of `12/12/2024` these are the best: 
<img src="../clouduvr-img/6.png" alt="image" width="900" height="auto">‎

‎
### Troubleshooting :icon-tools:
***

#### Cannot connect to GPU backend.
- You have exhausted the <u>[GPU runtime](https://docs.ai-hub.wtf/rvc/extra/glossary/#google-colab)</u> of Colab.

+++ Huggingface Spaces

:::content-center
## UVR Zero GPU 
:::
***

## How to use :icon-checklist:

***

==- Extract vocals
###### ‎

Access the space <u>[here](https://huggingface.co/spaces/TheStinger/UVR5_UI)</u>, you don't need an account to use this.           
    
#### 2. Select vocals & options
###### ‎  
a. Tap the **Input Audio** box & select your audio, or simply drag & drop.     
‎        
<img src="../hugging-img/1.png" alt="image" width="1000" height="auto">‎           
‎       
‎       
b. Once it's done uploading, in **CHOOSE PROCESS METHOD**, select ``BS/Mel Roformer``. Under that you can change **Segment Size** and **Overlap**, the defaults are fine.   
‎   
<img src="../hugging-img/2.png" alt="image" width="1000" height="auto">‎              

‎ 
#### 3. Select model
###### ‎  
d. Check the <u>[model list](https://docs.ai-hub.wtf/rvc/resources/vocal-isolation/#best-models)</u> & in **CHOOSE MODEL** pick the one according to what you need to remove.    
‎       
If you need to remove multiple noises, follow this pipeline for the best results:   
``Remove instrumental -> Remove reverb -> Extract main vocals -> Remove noise``  
‎  
#### 4. Start Processing
###### ‎  
a. Click **Spererate!** below. Wait a moment for the audio to process.       
‎       
b. Playable audios will then appear in the output boxes below. To download the output, click the little download icon in the top right.            
     
- If you're extracting lead vocals, remember to download the backing ones if you wish to keep them.     
===

### Troubleshooting :icon-tools:
***
==- *UVR extracted too little/too much.*
###### ‎
- Modify the `Aggression Setting` value on the right. 
- This determines the depth of the extraction. Only the VR method has it.
- A higher value will deepen the extraction, and a lower one will soften it.
- Each audio is different, so you'll have to test the ideal value.
===

==- *I can't remove some of the backing vocals.*
- Run the audio through BVE. Modify the Aggression Setting if necessary.
===

==- *I couldn't find my answer.*
###### ‎   
- Report your issue <u>[here](https://docs.ai-hub.wtf/rvc/#contributions)</u>.
===

==- Errors
#### GPU task aborted:
ZeroGPU HuggingFace Spaces have a max inference time duration, it’s the time it takes to do an Inference (use the model, not the time of your audio file itself), on default it’s around 1 minute which is what Ilaria RVC uses. You need to retry with a shorter audio, you could also split your audio.
***
#### You have exceeded your GPU quota ( NUMBER s left vs. 60s requested). Sign-up on Hugging Face to get more quotas or retry in Hour:Minutes:Seconds
ZeroGPU HuggingFace Spaces have a quota per account, if you aren’t signed in you will get less quota so it’s better to login for more quota. You could get the ‘Sign-up’ part even if you are logged in. The ZeroGPU Quota can’t be seen but it isn’t unlimited. You can either:
- Login so you get more quota
- Wait
- Pay to be an HuggingFace PRO Member to get X5 times more quota
===

+++ MVSEP  

###### ‎ 
### Important Notes ‎ :icon-alert:
***
- MVSEP is a website for isolating vocals, that works similarly as UVR.

- The <u>[UVR Colab](https://docs.ai-hub.wtf/rvc/resources/vocal-isolation/#cloud-uvr)</u> is much faster & convenient for this task. Use MVSEP if you run out of GPU runtime or feel lazy to convert your audio to WAV.

- For free users, you can't convert audios in batches or longer than 10 minutes. If that's your case, trim it into different pieces.

- There is a queue so make sure you make an account to skip most of it.
***
###### ‎ 
###### ‎  
### How to Use ‎ :icon-checklist:
***
==- *Extracting Vocals From Songs* 🎶
###### ‎     
#### 1. Log in.  
###### ‎
a. First, make an account <u>[here</u>](https://mvsep.com/register).        
‎       
b. Once logged in, go to the <u>[main page</u>](https://mvsep.com).     

!!!
Logging in is not mandatory, but recommended for **shorter waiting lists**.
!!!
***
‎
#### 2. Select audio.   
###### ‎
a. Click `Browse File` & select your audio, or simply drag & drop. The audio will begin to upload.  

    
    <img src="../uvrmvsep-img/9.png" alt="image" width="330" height="auto">‎   
    
***
‎
#### 3. Extract vocals.
###### ‎
a. In **Separation type** select `BS Roformer`     
‎     
b. In **Output encoding** select `FLAC`.          
We recommend selecting FLAC from now on. Learn more <u>[here</u>](https://docs.ai-hub.wtf/extra/glossary/#lossless-formats).        
‎     
c. Once the audio is done uploading, click `Separate`       

    <img src="../uvrmvsep-img/11.png" alt="image" width="400" height="auto">‎   

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

    <img src="../uvrmvsep-img/12.png" alt="image" width="400" height="auto">‎   
***

‎
#### 4. Clean vocals
###### ‎    
- Usually songs include reverb & backing vocals. These **negatively** impact the results in RVC.    
‎   
- So if the output has any undesired noises, follow the procedure on **Cleaning Vocals**.     
‎  
===

==- Cleaning Vocals 🗣️   
###### ‎     
#### 1. Log in.  
###### ‎
a. First, make an account <u>[here</u>](https://mvsep.com/register).      
‎     
b. Once logged in, go to the <u>[main page</u>](https://mvsep.com).     

!!!
Logging in is not mandatory, but recommended for **shorter waiting lists**.
!!!
***
‎
#### 2. Select audio & output format.    
###### ‎
a. Click `Browse File` & select your audio, or simply drag & drop. The audio will begin to upload.      
‎     
    <img src="../uvrmvsep-img/9.png" alt="image" width="330" height="auto">‎        
‎       
‎     
b. In **Output encoding** select `FLAC`.      
We recommend selecting FLAC from now on. Learn more <u>[here</u>](https://docs.ai-hub.wtf/extra/glossary/#lossless-formats).        

    <img src="../uvrmvsep-img/10.png" alt="image" width="420" height="auto">‎    
***
‎
#### 3. Select model.  
###### ‎
a. In **Separation Type**, select `DeNoise by aufr33`.      
‎     
b. Check the <u>[model list](https://docs.ai-hub.wtf/rvc/resources/vocal-isolation/#best-models)</u>. Pick the one according to what you need to remove.         
‎       
If you need to remove multiple noises, follow this pipeline for the best results:       
``Remove instrumental -> Remove reverb -> Extract main vocals -> Remove noise`` 
*** 
‎
#### 4. Download output.       
###### ‎
a. Click `Separate` & when it's done converting it will redirect you to a page, where you can listen the results.    
‎     
b. Tap the three dots of the audio you need and then `Download`.    
If you wish to keep the backing vocals stem, remember to download it too.      
      
    <img src="..\uvrmvsep-img\12.png" alt="image" width="400" height="auto">‎   
***
:::content-center
[!button variant="danger" corners="pill" icon="heart-fill" iconAlign="right" text="Support MVSEP"](https://mvsep.com/billing)
:::
===

- #### The best models for MVSEP are:

Extraction | Separation Type | Model
:---: | :---: | :---:
Vocals/Instrumental | MelBand Roformer | ver 2024.10
De-Reverb | Reverb Removal | Reverb removal by anvuew V2 (MelRoformer)
Extract Backing Vocals | MelBand Karaoke | Extract from vocals
De-Noise | DeNoise by aufr33  | Aggresive


### Troubleshooting ‎ :icon-tools:
***
==- *MVSEP extracted too much/too little.*
###### ‎ 
- Using the **Separation Type** of `DeNoise by aufr33`, you can modify the `Aggressiveness`. 
This determines the depth of the extraction.
- A higher value will deepen the extraction, and a lower one will soften it.
- Each audio is different, so you'll have to test the ideal value.
===

==- *I can't remove some of the backing vocals.*
###### ‎ 
- Try running the audio through MelBand Karaoke or BVE. Modify the Aggression Setting if necessary.
===

+++ X-Minus
:::content-center
## How to Use :icon-checklist:
:::
***

!!!warning
Most of the extraction model are behind a pay wall.
!!!

==- *Extrating Vocals From Songs* 🎶
###### 
#### 1. Choose a Separator
######
a. First go to <u>[X-minus's website](https://x-minus.pro)</u> and click the "Vocal Remover" at the top right. 

<img src="../x-minus-img/1.png" alt="image" width="600" height="auto"> 

b. Then select "Music and vocals" and choose "Bs Roformer"
  
<img src="../x-minus-img/2.png" alt="image" width="600" height="auto">

***
#### 2. Upload Your Audio File

c. Then click "select a file" and choose a audio file, or you can drag and drop a file. And when it's done it will look like this: 

<img src="../x-minus-img/3.png" alt="image" width="600" height="auto">

d. You can now click "Vocals" to download the vocals and "Other" to download the instrumentals.

===

==- *Cleaning Vocals* 🗣️
######
#### 1. Choose a De-Noiser
######
a.  In "De-Noise" select "Mel-Roformer De-Noise". You can also check the [model list](https://docs.ai-hub.wtf/rvc/resources/vocal-isolation/#best-models) to see what is the best model for your needs.

<img src="../x-minus-img/4.png" alt="image" width="600" height="auto">

***
#### 2. Upload Your Audio File

c. Then click "select a file" and choose a audio file, or you can drag and drop a file. And when it's done it will look like this: 

<img src="../x-minus-img/3.png" alt="image" width="600" height="auto">

d. You can now click "Vocals" to download the vocals and "Other" to download the instrumentals.

===

- #### The best models for X-Minus are:

Extraction | Model
:---: | :---: 
Vocals/Instrumental | BS Roformer
De-Reverb | MDX23C (De-Reverb)
Extract Backing Vocals | UVR BVE 2 
De-Noise | Mel Roformer De-Noise 

+++
***

:::content-center
## Preparing the dataset
:::

#### Step 1: Find the Sample Rate
:::
- This is a unit in that defines the total amount of **samples** (data) that can **fit** within **1 second** of an audio. They are measured in kilohertz (kHz).

- The most common sample rates are **32, 40, 44.1, & 48**. The **higher** the sample rate, the more information it stores, therefore the higher the **quality**.  

- While training in RVC, you'll have to set the **target sample rate** as your dataset's. This value affects the final quality.  
   
- ##### A simple way to determine it is with <ins>Spek</ins>:  

    - ##### STEP 1:   
        Download and install Spek <u>[here</u>](https://www.spek.cc/p/download).        
    - ##### STEP 2:   
        Open spek and just drag & drop audio into it. 

        <img src="../audioformats-img/3.png" alt="image" width="500" height="auto">‎   

    !!!danger <u>WARNING:</u>   
    If the frequencies don't reach the top of the spectrogram, see at which number peaks & multiply it by <U>**2**</u>. Here it reached 20 kHz. **Doubling** it gives 40kHz. Therefore the ideal target sample rate would be ``40k``
    !!!
***
#### Step 2: Truncating Silence.   

- Go to Effects -> Special -> Truncate Silence     
- Use the following values:         
    ‎  
    <img src="../datasets-img/trunc.png" alt="image" width="420" height="auto">    
    ***
    ‎
    #### Step 2: Audio Normalization.    
    - Go go to Effects -> Volume and Compression -> Loudness Normalization
    - Use these values:     
‎       
<img src="../datasets-img/norm.png" alt="image" width="420" height="auto"> 

> LUFS are used over db because hifigan needs perceptual quality and db doesnt offer that.
***
#### Step 3: Export.
- On the upper right corner go to File and click ``Export Audio``.       
    ‎   
    <img src="../datasets-img/4.png" alt="image" width="370" height="auto"> 
    ‎       
    ‎              

    - And finally, introduce these values:  

        - **Format**: ``FLAC``    
        - **Bit depth**: ``24 bit``
        - **Level**: ``8``       

        ###### ‎    

        <img src="../datasets-img/5.png" alt="image" width="650" height="auto">

***
#### Step 4: Manual Audio Slicing (Optional)
- Download this: [!file](../datasets-img/split_audio.py)
- Then place it in Applio's root folder. Then type `cmd` into the top bar where it shows your location.

<img src="../datasets-img/cmd.png" alt="image" width="420" height="auto">
‎  

- Then type this into the cmd line `python split_audio.py wavfilelocationhere exportfolderhere sampleratehere 3 0.3`.
    - for example it would look something like this `python split_audio.py C:\Users\dawnm\Downloads\dataset.wav C:\Users\dawnm\Desktop\split\ 32000 3 0.3`.

> If you get an error saying something is missing simply type `pip install librosa numpy scipy tqdm`. 

- Then once it's done go into the folder where you told it to export all of the slices to, then copy / cut all of the files there are place them into your dataset folder. 

!!!danger
If you use this method you **have** to disable the slicer and post processing in Applio.
!!!

***
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/contributions/)
:::