---
icon: chevron-right
order: 5000
---

``Last update: Dec 17, 2024``  

***
###### ‎
:::content-center
## Introduction :icon-book:
:::     
- A vocal isolation app is a software designed to extract a person's vocals from an audio file, usually through the use of AI models.

- They can remove undesired noises, like background noise, reverb, echo, music, etc.    

- The goal is to get an audio sample with clean vocals, which is what RVC needs to give the most accurate & quality results.

- For RVC users, the best app is Ultimate Vocal Remover 5 (or **UVR**). It can be used either <u>[locally](https://docs.ai-hub.wtf/extra/glossary/#local-running)</u> or through the <u>[cloud](https://docs.ai-hub.wtf/rvc/resources/vocal-isolation/#cloud-uvr-)</u>.

- If you want to remove noise manually to avoid ai artifacts you can use RX 11, which is mentioned in this guide. 
***
<img src="../uvrmvsep-img/3.jpg" alt="image" width="" height="auto">‎       

###### ‎ 
:::content-center
## Local UVR
!!!warning 
*You'll require great specs & GPU to run it effectively. Otherwise, use either the <u>[google colab version](https://docs.ai-hub.wtf/rvc/resources/vocal-isolation/#cloud-uvr)</u> or the hugging face space.*
!!!
:::
‎ 
:   ‎ 

### Installation :icon-download:
*** 
1. Go to their <u>[official website</u>](https://ultimatevocalremover.com/) & press `Download UVR`. And if you want to use BS Roformer you are going to need to install [this](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/UVR_12_8_24_23_30_BETA_rofo_full_install.exe).

    <img src="../uvrmvsep-img/1.jpg" alt="image" width="" height="auto">   

***
###### ‎ 
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

!!!success
*If an issue arises, read the **Troubleshooting** chapter.*
!!!
***
###### ‎   
###### ‎       
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

==- *I couldn't find my answer.*
###### ‎   
- Report your issue <u>[here](https://docs.ai-hub.wtf/rvc/#contributions)</u>.
===

***
###### ‎ 
###### ‎ 
:::content-center
## X-Minus Pro
‎ 
:   ‎ 
:::

### How to Use :icon-checklist:

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



###### ‎ 
:::content-center
## Cloud UVR
‎ 
:   ‎ 
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


!!!success
*If an issue arises, read the **Troubleshooting** chapter.*
!!!
***

###### ‎  
###### ‎  

### Troubleshooting :icon-tools:
***
==- *Cannot connect to GPU backend.*
###### ‎   
- You have exhausted the <u>[GPU runtime](https://docs.ai-hub.wtf/rvc/extra/glossary/#google-colab)</u> of Colab.
===

==- *I couldn't find my answer.*
###### ‎   
- Report your issue <u>[here](https://docs.ai-hub.wtf/rvc/#contributions)</u>.
===

***

######
:::content-center
## UVR Zero GPU 
:::
***
###### ‎  
######

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

!!!success
*If an issue arises, read the **Troubleshooting** chapter.*
!!!
***

###### ‎  
###### ‎  

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

***

###### ‎
###### ‎ 
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
***

###### ‎  
:::content-center     
## MVSEP
:::
‎      
:   ‎

###### ‎ 
### Important Notes ‎ :icon-alert:
***
- MVSEP is a website for isolating vocals, that works similarly as UVR.

- The <u>[UVR Colab](https://docs.ai-hub.wtf/rvc/resources/vocal-isolation/#cloud-uvr)</u> is much faster & convenient for this task. Use MVSEP if you run out of GPU runtime or feel lazy to convert your audio to WAV.

- For free users, you can't convert audios in batches or longer than 10 minutes. If that's your case, trim it into different pieces.
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

!!!success
*If an issue arises, read the ***Troubleshooting*** chapter.*
!!!

***
###### ‎ 
###### ‎ 
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

==- *I couldn't find my answer.*
###### ‎   
- Report your issue <u>[here](https://docs.ai-hub.wtf/rvc/#contributions)</u>.
===
***       
###### ‎ 
###### ‎ 
:::content-center
## Best Models
#### `Their most convenient models, oriented to RVC.`    
###### ‎ 
:::

+++ UVR
Extraction | Process Method | Model
:---: | :---: | :---:
Vocals/Instrumental | MDX-Net | BS Roformer-Viper-X 1296 / 1297
De-Reverb | VR | UVR-DeEcho-DeReverb
Extract Backing Vocals | VR | UVR-BVE-4B_SN-44100-1
De-Noise | VR | UVR-DeNoise 

+++ MVSEP
Extraction | Separation Type | Model
:---: | :---: | :---:
Vocals/Instrumental | BS Roformer | ver 2024.08
De-Reverb | Reverb Removal | Reverb removal by anvuew (BS Roformer)
Extract Backing Vocals | MelBand Karaoke | Extract from vocals
De-Noise | DeNoise by aufr33  | Aggresive 

+++ X-Minus
Extraction | Model
:---: | :---: 
Vocals/Instrumental | BS Roformer
De-Reverb | MDX23C (De-Reverb)
Extract Backing Vocals | UVR BVE 2 
De-Noise | Mel Roformer De-Noise 

+++ Cloud UVR
The best model for this change a lot so it's best you look <u>[here](https://docs.google.com/spreadsheets/d/1pPEJpu4tZjTkjPh_F5YjtIyHq8v0SxLnBydfUBUNlbI/edit?usp=sharing)</u>, but as of `12/12/2024` these are the best: 
<img src="../clouduvr-img/6.png" alt="image" width="900" height="auto">‎

+++
***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/contributions/)
:::
