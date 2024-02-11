``Last update: Feb 9, 2024``  

***
###### ‎
:::content-center
## Introduction
:::     
- A vocal isolation app is a software designed to extract a person's vocals from an audio file, usually through the use of AI models.

- They can remove undesired noises, like background noise, reverb, echo, music, etc.    

- The goal is to get an audio sample with clean vocals, which is what RVC needs to give the most accurate & quality results.

- ##### For RVC users, the best two are: 
    {.list-icon}
    - ##### :icon-device-desktop: ‎ <u>[Ultimate Vocal Remover 5](https://aihubdocs.github.io/en/vocal-isolation--datasets/vocal-isolation/#ultimate-vocal-remover-5)</u>       
    - ##### :icon-cloud: ‎ <u>[MVSEP](https://aihubdocs.github.io/en/vocal-isolation--datasets/vocal-isolation/#mvsep)</u>   
***
<img src="../uvrmvsep-img/3.jpg" alt="image" width="" height="auto">‎       
‎       
:::content-center
## Ultimate Vocal Remover 5
:::
###### ‎ 
- UVR is a free, open-source vocal isolation app, with a convenient & simple user interface. Considered to be the best vocal isolation app by many.

- It has a great amount of AI models for extracting pretty much anything you can think of from a voice recording/song.         
           
- For these reasons, UVR is the go-to app for local RVC users, for either cleaning audio samples or datasets.

!!!warning 
*You'll requires great specs & GPU to run it effectively. Otherwise, use <u>[MVSEP](https://aihubdocs.github.io/en/vocal-isolation--datasets/vocal-isolation/#mvsep)</u>*.
!!!
***
:::content-center
###### ‎  
### <u> Installation</u> ‎ :icon-download:    
::: 
###### ‎    
1. Go to their <u>[official website</u>](https://ultimatevocalremover.com/) & press `Download UVR`. 

<img src="../uvrmvsep-img/1.jpg" alt="image" width="" height="auto">   

***
2. It will redirect you their GitHub page. Click the download link for your **operating system**.   
UVR is available both on Windows and Mac.
***
3. Once the installer finishes downloading, execute it.     
Make sure to tick `🗹 Create a desktop shortcut` for an easier access to UVR.

    <img src="../uvrmvsep-img/2.jpg" alt="image" width="500" height="auto"> 
***
:::content-center
###### ‎       
### <u> How to Use</u> ‎ :icon-checklist:
###### ‎       
:::   
!!!success NOTES:
Click <u>[here</u>](https://www.reddit.com/media?url=https%3A%2F%2Fpreview.redd.it%2Fpmi3ialjjca91.png%3Fwidth%3D1016%26format%3Dpng%26auto%3Dwebp%26s%3D0e75311422270753ebca68fe00eaf9ce6a81218b) for a graphic explanation of the buttons. Keep in mind, the post is outdated.

If you come across a problem, read the <u>[Troubleshooting](https://aihubdocs.github.io/en/vocal-isolation--datasets/vocal-isolation/#troubleshooting--)</u> chapter.
!!!
###### ‎           
- ##### To extract & clean vocals from a <u>song</u>, read the `Extraction & Cleaning` guide.

- ##### For only cleaning vocals, read the `Cleaning Only` one.

+++ Extract & Cleaning 🎶  
###### ‎     
#### 1. Input audio.
- Click `Select input` to select your audio/s. Or just drag the files to it.  

- In `Select output` you select in which folder you want the results to be.    

<img src="../uvrmvsep-img/4.jpg" alt="image" width="300" height="auto">         ‎    

!!!success 
For better results, have the audio in a <u>[lossless format](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/)</u> (**WAV** or **FLAC**), & not MP3.
!!!
***
###### ‎ 
#### 2. Select FLAC & GPU Conversion.
a. At the right you can select the output format.       
We recommend picking `FLAC`. Learn why <u>[here](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/)</u>.   

b. If your GPU is **compatible with <u>[CUDA](https://aihubdocs.github.io/en/other/glossary/#cuda)</u>**, toggle `GPU Conversion` on for a faster process.    

    <img src="../uvrmvsep-img/16.png" alt="image" width="350" height="auto">‎      
###### ‎       
>This step is not mandatory, but recommended for better results.
***
###### ‎
#### 3. Extract vocals. 
a. In `Process Method` select `MDX-Net`.      

b. In `Select MDX-Net Model`, select the `MDX23C` model.   

    <img src="../uvrmvsep-img/5.jpg" alt="image" width="250" height="auto">‎      
 
b. Now click the long `Start Processing` button.  

!!!success <u>TIP:</u>
For testing models/options, I recommend ticking `Sample Mode`. This will only process 30 seconds of your sample, allowing you to test more efficiently.
!!!   
***
###### ‎
#### 4. Remove reverb.   
Usually songs include reverb in the vocals. Reverb **negatively** impacts the results in RVC, so be sure to remove it.

a. Input the vocals with no instrumental.

b. In `Process Method` select `VR Architecture`, & choose the `DeEcho-DeReverb` model.        

c. Turn on `No Reverb Only` & set `Window Size` to `320`. (Optional)     
    A lower Window Size yield a higher output **quality**, but will take **longer** to process.     

d. Start processing.

    <img src="../uvrmvsep-img/6.png" alt="image" width="380" height="auto">‎  

   
***
###### ‎
#### 5. Extract lead vocals. 
Just like reverb, songs also normally include backing vocals.

a. Input the vocals with no reverb.   

b. Choose the `UVR-BVE` model.         

c. If you want the backing vocals stem, untick `Vocals only`.

d. Begin processing. And that will be all.
If you then notice background noise, run the output through the `UVR-DeNoise` model.

    <img src="../uvrmvsep-img/17.png" alt="image" width="230" height="auto">
         
!!!warning For the best results, follow the pipeline explained before:       
Extract vocals -> Remove reverb -> Extract main vocals -> Remove noise
!!!  
***
:::content-center
[!button variant="danger" corners="pill" icon="heart-fill" iconAlign="right" text="Support UVR"](https://www.buymeacoffee.com/uvr5)
::: 

+++ Cleaning Only 🗣️   

###### ‎      
#### 1. Input audio.
- Click `Select input` to select your audio/s. Or just drag the files to it.  

- In `Select output` you select in which folder you want the results to be.    

<img src="../uvrmvsep-img/4.jpg" alt="image" width="300" height="auto">         ‎    

!!!success 
For better results, have the audio in a <u>[lossless format](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/)</u> (**WAV** or **FLAC**), & not MP3.
!!!
***
###### ‎ 
#### 2. Select FLAC & GPU Conversion.
a. At the right you can select the output format.       
We recommend picking `FLAC`. Learn why <u>[here](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/)</u>.   

b. If your GPU is **compatible with <u>[CUDA](https://aihubdocs.github.io/en/other/glossary/#cuda)</u>**, toggle `GPU Conversion` on for a faster process.    

    <img src="../uvrmvsep-img/16.png" alt="image" width="350" height="auto">‎      
###### ‎       
>This step is not mandatory, but recommended for better results.
***
###### ‎  
#### 3. Select model.  
a. In `Process Method` select `VR`.  

b. Set `Window Size` as ``320``. (optional)        
    Lower Window Size yield a higher output **quality**, but will take **longer** to process. 

b. Check the <u>[model list](https://aihubdocs.github.io/en/vocal-isolation--datasets/vocal-isolation/#uvrs-best-models-)</u> & in `Select VR Model` pick the one according to what you need to remove.         
‎       
If you need to remove multiple noises, follow this pipeline for the best results:   
``Remove reverb -> Extract main vocals -> Remove noise``  

!!!success <u>TIP:</u>
For testing models/options, I recommend ticking `Sample Mode`. This will only process 30 seconds of your sample, allowing you to test more efficiently.
!!!  
***
###### ‎  
#### 4. Process.
Click the `Start processing` button at the bottom. And that will be all. 

***
:::content-center
[!button variant="danger" corners="pill" icon="heart-fill" iconAlign="right" text="Support UVR"](https://www.buymeacoffee.com/uvr5)
::: 
+++

###### ‎      
:::content-center
### <u>UVR's Best Models</u> :icon-star-fill:
`Their most convenient models, oriented to RVC.`  
:::
###### ‎

Extraction | Process Method | Model
:---: | :---: | :---:
Vocals/Instrumental | MDX-Net | MDX23C
Reverb | VR | DeEcho-DeReverb
Main Vocals | VR | UVR-BVE
Noise | VR | UVR-DeNoise 

***  

:::content-center
‎  
### <u>Troubleshooting</u> ‎ :icon-tools:
:::
###### ‎ 
==- *I can't see a model.*
###### ‎ 
- Click the wrench (🔧) on the left & go to `Download Center`
- Select the category of the model (MDX-NET or VR)
- Unfold its dropdown & select the model that you need
- Then click the download button (📥). The model will download, which will take a few minutes
===

==- *UVR extracted too little/too much.*
###### ‎
- Modify the `Aggression Setting` on the right. This determines the depth of the extraction.
- A higher value will deepen it, and a lower one will soften it..
===
###### ‎
***        
:::content-center 
‎   
<img src="../uvrmvsep-img/8.png" alt="image" width="400" height="auto">

###### ‎       
## MVSEP
:::
###### ‎      
- MVSEP is a website for audio isolation that operates just like UVR, using AI models.

- It doesn't have all the models & options that UVR has, but it has the necessary tools for getting decent-enough vocals for RVC.

- It's one of the best free cloud-based alternatives for UVR.
*** 
:::content-center
‎  
### <u>How to Use</u> ‎ :icon-checklist:
:::
###### ‎ 
!!! <u>NOTES:</u>
***For free users***, you can only convert 1 audio at the time, & you can't use ones that are longer than 10 minutes. If that's your case, trim it into various pieces.

***If you encounter an issue***, read the <u>[Troubleshooting](https://aihubdocs.github.io/en/vocal-isolation--datasets/vocal-isolation/#troubleshooting---1)</u> chapter.
!!!
‎       
- ##### To extract & clean vocals from a <u>song</u>, read the `Extraction & Cleaning` guide.

- ##### For only cleaning vocals, read `Cleaning Only` one.

+++ Extract & Cleaning 🎶
###### ‎     
#### 1. Log in.  
a. First, make an account <u>[here</u>](https://mvsep.com/register).      

b. Once logged in, go to the <u>[main page</u>](https://mvsep.com).

!!!
Logging in is not mandatory, but recommended for **shorter waiting lists**.
!!!
***
###### ‎
#### 2. Select audio.   
a. Click `Browse File` & select your audio. The audio will begin to upload. (or just drag the file into it)    

    
    <img src="../uvrmvsep-img/9.png" alt="image" width="330" height="auto">‎   
    
***
###### ‎
#### 3. Extract vocals.
a. In `Separation type` select `MDX23C`

a. In `Output encoding` select `FLAC`.      
We recommend selecting FLAC from now on. Learn more <u>[here</u>](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/).

c. Once the audio is done uploading, click `Separate`

<img src="../uvrmvsep-img/11.png" alt="image" width="400" height="auto">‎   

!!! Leave "Model Type" untouched.
!!!
***
###### ‎
#### 4. Download output.      
When it's done converting it will redirect you to a page where you can listen the results.      
a. Tap the three buttons of the **Vocals** audio and then `Download`.    

b. Do the same for the `Instrumental` one, if you wish to keep it..

<img src="../uvrmvsep-img/12.png" alt="image" width="400" height="auto">‎   
***
###### ‎
#### 5. Remove reverb.       
Usually songs include reverb to the vocals. Leaving them in will **negatively** impact the quality in RVC.  

a. Go to the main page & input the vocals.

b. In `Separation type` select `Ultimate Vocal Remover HQ`.     

c. In `Model Type` select the model `UVR-DeEcho-DeReverb`.

c. Click `Separate` & then download the vocals with no reverb.

    <img src="../uvrmvsep-img/13.png" alt="image" width="420" height="auto">‎   

***
###### ‎
#### 6. Extract main vocals. 
Just like reverb, songs also normally include backing vocals.

a. Go to the main page & input the vocals with no reverb.

b. In `Separation type` select `Ultimate Vocal Remover HQ`.      

c. Select the model `UVR-BVE-4B_SN-44100-1`.

c. Click `Separate` and then download the main vocals. Also the backing vocals stem too, if you wish to keep them.

    <img src="../uvrmvsep-img/14.png" alt="image" width="420" height="auto">‎   
    ‎     

e. If you then notice background noise, use the model `UVR-DeNoise`.

!!!warning For the best results, follow the pipeline explained before:       
Extract vocals -> Remove reverb -> Extract main vocals -> Remove noise
!!!  
***
:::content-center
[!button variant="danger" corners="pill" icon="heart-fill" iconAlign="right" text="Support MVSEP"](https://mvsep.com/billing)
:::

+++ Cleaning Only 🗣️   
###### ‎     
#### 1. Log in.  
a. First, make an account <u>[here</u>](https://mvsep.com/register).      

b. Once logged in, go to the <u>[main page</u>](https://mvsep.com).

!!!
Logging in is not mandatory, but recommended for **shorter waiting lists**.
!!!
***
###### ‎
#### 2. Select audio & output format.    
a. Click `Browse File` and select your audio. The audio will begin to upload. (or just drag the file into it)    

    <img src="../uvrmvsep-img/9.png" alt="image" width="330" height="auto">‎   
‎       
b. In `Output encoding` select `FLAC`.      
We recommend selecting FLAC from now on. Learn more <u>[here</u>](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/).

    <img src="../uvrmvsep-img/10.png" alt="image" width="420" height="auto">‎    
***
###### ‎
#### 3. Select model.  
a. In `Separation Type`, select `Ultimate Vocal Remover 5 HQ`.

b. Check the <u>[model list](https://aihubdocs.github.io/en/vocal-isolation--datasets/vocal-isolation/#mvseps-best-models-)</u> & in `Select VR Model` pick the one according to what you need to remove.         
‎       
If you need to remove multiple noises, follow this pipeline for the best results:       
``Remove reverb -> Extract main vocals -> Remove noise`` 
*** 
#### 4. Download output.       
a. Click `Separate` & when it's done converting it will redirect you to a page, where you can listen the results.    

b. Tap the three dots of the audio you need and then `Download`. If you wish to keep the backing vocals stem, remember to download it too. 
      
    <img src="..\uvrmvsep-img\12.png" alt="image" width="400" height="auto">‎   
***
:::content-center
[!button variant="danger" corners="pill" icon="heart-fill" iconAlign="right" text="Support MVSEP"](https://mvsep.com/billing)
:::

+++

***
‎       
‎  
:::content-center
### <u>[MVSEP's Best Models</u> :icon-star-fill:         
#### `Their most convenient models, oriented to RVC.`    
:::
###### ‎       

Extraction | Separation Type | Model
:---: | :---: | :---:
Vocals/Instrumental | MDX23C | - 
Reverb | Ultimate Vocal Remover 5 HQ | UVR-DeEcho-DeReverb
Backing Vocals | Ultimate Vocal Remover 5 HQ | UVR-BVE-4B_SN-44100-1
Noise | Ultimate Vocal Remover 5 HQ | UVR-DeNoise

***

:::content-center
‎  
### <u>Troubleshooting</u> ‎ :icon-tools:
:::
###### ‎ 

==- *MVSEP extracted too much/too little.*
###### ‎ 
- Using the **Separation Type** of `Ultimate Vocal Remover HQ`, you can modify the `Aggressiveness` value. 
This determines the depth of the extraction.
- A higher value will deepen it, & a smaller one will soften it.
===
###### ‎ 
***
:::content-right
``Written by Julia``
:::
‎     
:::content-right
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Send Suggestions"](https://forms.gle/3GVR7opzpQrhgRCj9)
‎     
‎     
::: 
