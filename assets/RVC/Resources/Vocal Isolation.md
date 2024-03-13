---
icon: chevron-right
order: 5000
---

``Last update: Feb 29, 2024``  

***
###### ‎
:::content-center
## Introduction :icon-book:
:::     
- A vocal isolation app is a software designed to extract a person's vocals from an audio file, usually through the use of AI models.

- They can remove undesired noises, like background noise, reverb, echo, music, etc.    

- The goal is to get an audio sample with clean vocals, which is what RVC needs to give the most accurate & quality results.

- For RVC users, the best app is Ultimate Vocal Remover 5 (or **UVR**). It can be used either <u>[locally](https://docs.aihub.wtf/extra/glossary/#local-running)</u> or through the <u>[cloud](https://docs.aihub.wtf/rvc/resources/vocal-isolation/#cloud-uvr-)</u>. 
***
<img src="../uvrmvsep-img/3.jpg" alt="image" width="" height="auto">‎       

###### ‎ 
:::content-center
## Local UVR
!!!warning 
*You'll require great specs & GPU to run it effectively. Otherwise, use the <u>[cloud version](https://docs.aihub.wtf/rvc/resources/vocal-isolation/#cloud-uvr)</u>.*
!!!
:::
‎ 
:   ‎ 

### Installation :icon-download:
*** 
1. Go to their <u>[official website</u>](https://ultimatevocalremover.com/) & press `Download UVR`. 

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
For better results, have the audio in a <u>[lossless format](https://docs.aihub.wtf/extra/glossary/#lossless-formats)</u> (**WAV** or **FLAC**), & not MP3.
!!!
***
‎ 
#### 2. Select FLAC & GPU Conversion.
###### ‎  
a. At the right you can select the output format.       
We recommend picking `FLAC`. Learn why <u>[here](https://docs.aihub.wtf/extra/glossary/#lossless-formats)</u>.   
‎  
b. If your GPU is **compatible with <u>[CUDA](https://docs.aihub.wtf/extra/glossary/#cuda)</u>**, toggle `GPU Conversion` on for a faster process.    

    <img src="../uvrmvsep-img/16.png" alt="image" width="350" height="auto">‎      

###### ‎       
>This step is not mandatory, but recommended for better results.
***
‎
#### 3. Extract vocals. 
###### ‎  
a. In **CHOOSE PROCESS METHOD** select `MDX-Net`, and select the `MDX23C` model.   

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
For better results, have the audio in a [lossless format](https://docs.aihub.wtf/extra/glossary/#lossless-formats)</u> (**WAV** or **FLAC**), & not MP3.
!!!
***
‎   
#### 2. Select FLAC & GPU Conversion.
###### ‎      
a. At the right you can select the output format.       
We recommend picking `FLAC`. Learn why <u>[here](https://docs.aihub.wtf/extra/glossary/#lossless-formats)</u>.     
‎   
b. If your GPU is **compatible with <u>[CUDA](https://docs.aihub.wtf/extra/glossary/#cuda)</u>**, toggle `GPU Conversion` on for a faster process.    
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
b. Check the <u>[model list](https://docs.aihub.wtf/rvc/resources/vocal-isolation/#best-models)</u>. In **Select VR Model** pick the one according to what you need to remove.         
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
- Run the audio through MDX23C or DeNoise. Modify the <u>[Aggression Setting](https://docs.aihub.wtf/rvc/resources/vocal-isolation/#uvr-extracted-too-little-too-much)</u> if necessary.
===

==- *I couldn't find my answer.*
###### ‎   
- Report your issue <u>[here](https://docs.aihub.wtf/rvc/#contributions)</u>.
===

***
###### ‎ 
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
a. First access the Colab space <u>[here](https://colab.research.google.com/github/Eddycrack864/Music-Source-Separation-Universal-Colab/blob/main/Music_Source_Separation_Universal_Colab.ipynb)</u>. This Colab only uses **WAV** audios. If yours isn't, convert it to WAV or use <u>[MVSEP](https://docs.aihub.wtf/rvc/resources/vocal-isolation/#mvsep)</u>.     
‎       
b. Then **Log in** to your Google account.      
‎   
c. Execute the **Setup** cell by pressing the play button :icon-play:. Grant all the permissions.   
‎   
    <img src="../uvrmvsep-img/3-setup.png" alt="image" width="350" height="auto">‎   
‎   
- It'll finish once the logs say "Ready!".     
‎   
    <img src="../uvrmvsep-img/3-check.png" alt="image" width="200" height="auto">

***

‎  
#### 2. Set up folders
###### ‎ 
- In Google Drive, make two folders, named **Separar** & **Vocales**.       
‎       
    <img src="../uvrmvsep-img/3-folders.png" alt="image" width="370" height="auto">     
‎     
‎     
- Name them as you want, as long as the input/output folders match the paths.      
‎       
    <img src="../uvrmvsep-img/3-paths.png" alt="image" width="400" height="auto">
***
‎  
#### 3. Separate
###### ‎   
a. Select the ``MDX23C 8KFFT InstVoc HQ 2`` model & run the **Separation** cell.     
‎   
    <img src="../uvrmvsep-img/3-model.png" alt="image" width="320" height="auto">‎   
‎       
‎   
b. Download the result located in the output folder.
***
‎
#### 4. Clean vocals
###### ‎    
- Usually songs include reverb & backing vocals. These **negatively** impact the results in RVC.    
‎   
- So if the output has any undesired noises, follow the procedure on **Cleaning Vocals**.     
‎  
===

==- *Cleaning Vocals* 🗣️ 
###### ‎ 
#### 1. Set up Colab
###### ‎
a. Access the Colab space <u>[here](https://colab.research.google.com/github/Eddycrack864/Ultimate-Vocal-Remover-5.6-for-Google-Colab/blob/main/Ultimate_Vocal_Remover_5_6_for_Google_Colab.ipynb)</u> & **Log in** to your Google account. Credits to <u>[Eddy](https://github.com/Eddycrack864)</u> for the Colab.         
‎   
b. Execute the **Install** cell. This will take around 5 - 10 minutes.     
‎   
<img src="../uvrmvsep-img/3-install.png" alt="image" width="270" height="auto">‎  
‎    
- It'll finish once the logs say "Installation Completed".      
‎    
<img src="../uvrmvsep-img/3-installdone.png" alt="image" width="270" height="auto">‎    

***
‎ 
#### 2. Run UI
###### ‎ 
a. Then below run the **WebUI** cell. This will take around 3 minutes.      
***For advanced users***, tick `VIP_MODELS` if you wish to use them.        
‎    
<img src="../uvrmvsep-img/3-webui.png" alt="image" width="310" height="auto">‎    
‎      
‎    
b. Open the **public URL**. That **Gradio** link contains the UVR app.      
‎       
    <img src="../uvrmvsep-img/20.png" alt="image" width="425" height="auto">‎  
###### ‎  
!!!warning 
Don't close **Colab** until you're done using it, and don't press buttons continuously too **quickly**, as it may cause errors.         
!!!
***
‎    
#### 3. Select vocals & options
###### ‎  
a. Tap the **Input Audio** box & select your audio, or simply drag & drop.     
‎        
    <img src="../uvrmvsep-img/21.png" alt="image" width="425" height="auto">‎           
‎       
‎       
b. Once it's done uploading, in **CHOOSE PROCESS METHOD**, select ``VR Arc``.       
‎   
<img src="../uvrmvsep-img/22.png" alt="image" width="600" height="auto">‎       
‎       
‎       
c. On the left, tick `GPU Conversion` & set **WINDOW SIZE** to `320`.       
Lower Window Size yield a higher output **quality**, but will take **longer** to process.       
‎    
<img src="../uvrmvsep-img/3-options.png" alt="image" width="300" height="auto">‎ 
*** 
‎ 
#### 4. Select model
###### ‎  
d. Check the <u>[model list](https://docs.aihub.wtf/rvc/resources/vocal-isolation/#best-models)</u> & in **CHOOSE VR MODEL** pick the one according to what you need to remove.    
‎       
If you need to remove multiple noises, follow this pipeline for the best results:   
``Remove instrumental -> Remove reverb -> Extract main vocals -> Remove noise``  
***
‎  
#### 5. Start Processing
###### ‎  
a. Click **Start Processing** below. Wait a moment for the audio to process.       
‎       
b. Playable audios will then appear in the output boxes below. To download the output, click the three dots on the right and `Download`.            
     
- If you're extracting lead vocals, remember to download the backing ones if you wish to keep them.    

!!!success 
**TIP:** To **test** models/options more efficiently, tick **Sample Mode** to only process 30 seconds of your sample.
!!!  

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
- Run the audio through MDX23C or DeNoise. Modify the Aggression Setting if necessary.
===

==- *I get a red error message.*
- This is normal. Try repeating your action.
- If it persists, reload the Gradio page.
===

==- *Cannot connect to GPU backend.*
###### ‎   
- You have exhausted the <u>[GPU runtime](https://docs.aihub.wtf/rvc/extra/glossary/#google-colab)</u> of Colab.
===

==- *I couldn't find my answer.*
###### ‎   
- Report your issue <u>[here](https://docs.aihub.wtf/rvc/#contributions)</u>.
===

***

###### ‎

:::content-center 
‎   
<img src="../uvrmvsep-img/8.png" alt="image" width="400" height="auto">

###### ‎       
## MVSEP
:::
‎      
:   ‎

###### ‎ 
### Important Notes ‎ :icon-alert:
***
- MVSEP is a website for isolating vocals, that works similarly as UVR.

- The <u>[UVR Colab](https://docs.aihub.wtf/rvc/resources/vocal-isolation/#cloud-uvr)</u> is much faster & convenient for this task. Use MVSEP if you run out of GPU runtime or feel lazy to convert your audio to WAV.

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
a. In **Separation type** select `MDX23C`     
‎     
b. In **Output encoding** select `FLAC`.          
We recommend selecting FLAC from now on. Learn more <u>[here</u>](https://docs.aihub.wtf/extra/glossary/#lossless-formats).        
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
We recommend selecting FLAC from now on. Learn more <u>[here</u>](https://docs.aihub.wtf/extra/glossary/#lossless-formats).        

    <img src="../uvrmvsep-img/10.png" alt="image" width="420" height="auto">‎    
***
‎
#### 3. Select model.  
###### ‎
a. In **Separation Type**, select `Ultimate Vocal Remover 5 HQ`.      
‎     
b. Check the <u>[model list](https://docs.aihub.wtf/rvc/resources/vocal-isolation/#best-models)</u>. In `Select VR Model` pick the one according to what you need to remove.         
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
- Using the **Separation Type** of `Ultimate Vocal Remover HQ`, you can modify the `Aggressiveness` value. 
This determines the depth of the extraction.
- A higher value will deepen the extraction, and a lower one will soften it.
- Each audio is different, so you'll have to test the ideal value.
===

==- *I can't remove some of the backing vocals.*
###### ‎ 
- Try running the audio through MDX23C or DeNoise. Modify the Aggression Setting if necessary.
===

==- *I couldn't find my answer.*
###### ‎   
- Report your issue <u>[here](https://docs.aihub.wtf/rvc/#contributions)</u>.
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
Vocals/Instrumental | MDX-Net | MDX23C
Reverb | VR | UVR-DeEcho-DeReverb
Main Vocals | VR | UVR-BVE-4B_SN-44100-1
Noise | VR | UVR-DeNoise 

+++ MVSEP
Extraction | Separation Type | Model
:---: | :---: | :---:
Vocals/Instrumental | MDX23C | - 
Reverb | Ultimate Vocal Remover 5 HQ | UVR-DeEcho-DeReverb
Main Vocals | Ultimate Vocal Remover 5 HQ | UVR-BVE-4B_SN-44100-1
Noise | Ultimate Vocal Remover 5 HQ | UVR-DeNoise

+++
***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.wtf/rvc/#contributions)
:::