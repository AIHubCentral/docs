*`Written by Julia`*      
``Last update: Jan 25, 2024``  

***
###### ‎
:::content-center
## Vocal Isolation Apps
:::     
- A vocal isolation app is a software designed to extract a person's vocals from an audio file, a lot of times through the use of AI models.

- They can remove undesired noises, like background noise, reverb, echo, music, etc.    
Some models can also extract specific stems, like backing vocals, drums, bass, & more.

- The goal is to get an audio sample with clean vocals, which is what RVC needs to give the most accurate & quality results.

- The main two apps that RVC users use are [<u>Ultimate Vocal Remover 5</u>](https://aihubdocs.github.io/en/vocal-isolation--datasets/uvr5--mvsep/#ultimate-vocal-remover-5) (for **local** users) and [<u>MVSEP</u>](https://aihubdocs.github.io/en/vocal-isolation--datasets/uvr5--mvsep/#mvsep) (for **cloud** users).        
***
<img src="../uvrmvsep-img/3.jpg" alt="image" width="" height="auto">‎       
‎       
:::content-center
## Ultimate Vocal Remover 5
:::
###### ‎ 
### <u>Introduction</u> 📜   
- UVR is a free, open-source vocal isolation app, with a convenient & simple user interface.        
Considered to be the best vocal isolation app by many.

- It has a great amount of AI models for extracting pretty much anything you can think of from a voice recording/song.         
           
- For these reasons, UVR is the go-to app for local RVC users, for either cleaning audio samples or datasets.

!!!warning *Just like with RVC, you'll need decent specs and GPU to run it smoothly.*
!!!
***
###### ‎  
### <u> Installation</u> 📥    
###### ‎        
1. Go to their [<u>official website</u>](https://ultimatevocalremover.com/) and click `Download UVR`.  

    <img src="../uvrmvsep-img/1.jpg" alt="image" width="" height="auto">   
***
2. It will redirect you their GitHub page. Click the download link for your **operating system**.   
UVR is available both on Windows and Mac.
***
3. Once the installer finishes downloading, execute it.     
Make sure to tick `🗹 Create a desktop shortcut` for an easier access to UVR.

    <img src="../uvrmvsep-img/2.jpg" alt="image" width="500" height="auto"> 
***
###### ‎       
### <u> How to Use</u> 📋
###### ‎       
!!!success *Click [<u>here</u>](https://www.reddit.com/media?url=https%3A%2F%2Fpreview.redd.it%2Fpmi3ialjjca91.png%3Fwidth%3D1016%26format%3Dpng%26auto%3Dwebp%26s%3D0e75311422270753ebca68fe00eaf9ce6a81218b) for a graphic explanation of the buttons.*       
Credits to user 'thenormal' on Reddit. Keep in mind, the post is outdated.
!!!
###### ‎           
Depending on if you want to extract & clean vocals of a song from **scratch**, or if you only need to **clean** an already existing sample, the procedure is a little different:  

+++ Extract & Clean Vocals From Song 🎶  
###### ‎     
#### 1. <u>Input audio.</u>  
Click `Select input` to select your audio/s.     
Or just drag the audios to it.  

In `Select ouput` you select in which folder you want the results to be.    

<img src="../uvrmvsep-img/4.jpg" alt="image" width="300" height="auto">         ‎    

!!!success 
For better results, have the audio in a [<u>lossless format</u>](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/) (**WAV** or **FLAC**), & not MP3.
!!!
***
###### ‎ 
#### 2. <u>Select FLAC & GPU Conversion.</u> 
a. At the right you'll see three audio formats to pick as the output format.       
We recommend picking `FLAC`. Learn why [<u>here</u>](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/).   

b. If your GPU is **compatible with [<u>CUDA</u>](https://aihubdocs.github.io/en/other/glossary/#cuda)**, toggle `GPU Conversion` on for a faster process.    

    <img src="../uvrmvsep-img/16.png" alt="image" width="350" height="auto">‎      
###### ‎       
>This step is not mandatory but recommended for better results.
***
###### ‎
#### 3. <u>Remove instrumental.</u> 
a. In `Process Method` select `MDX-Net`.        
In `Select MDX-Net Model`, select the `MDX23C` model.   

    <img src="../uvrmvsep-img/5.jpg" alt="image" width="250" height="auto">‎      
 
    !!!info *If the model isn't installed.*
    Click the wrench (🔧) on the left, go to `Download Center`, select `MDX-Net`, select said model & click the download symbol (📥). Here's where you install models for UVR.
    !!!
###### ‎   
b. Now click the long `Start Processing` button.        
‎     
!!!success <u>TIPS:</u>
If you extracted too much/too little, modify the `Aggression Setting` to determine the **depth** of the extraction, until you find the sweet spot:      
    • **Lower** values **softens** the extraction.   
    • **Higher** values **deepens** it.     
‎       
For testing models/aggression settings, I recommend activating `Sample Mode`.       
This will process only `30` seconds of the sample, allowing you to test more efficiently.
!!!     
***
###### ‎
#### 4. <u>Remove reverb.</u>    
Usually songs include reverb to the vocals. If you leave it in, it will **negatively** impact the results in RVC.  
If yours don't have ANY, you can skip this step. 
a. Select the vocals with no instrumental as input.

b. In `Process Method`, select `VR Architecture`, & choose `DeEcho-DeReverb` model.        

c. Turn on `No Reverb Only` & set `Window Size` to `320`. (Optional)     
        • Lower Window Size yield a higher output **quality**, but will take **longer** to process.      
d. Start processing.

    <img src="../uvrmvsep-img/6.png" alt="image" width="380" height="auto">‎  

   
***
###### ‎
#### 5. <u>Remove backing vocals.</u> 
Just like reverb, songs also normally include backing vocals.
Skip this step if yours don't any.

a. Input the vocals with no reverb.   

b. In `Process Method`, select `VR Architecture` & choose the `UVR-BVE` model.         

c. Set `Window Size` to `320`. (Optional)     
A lower Window Size yield a higher output **quality**, but will take longer to process. 

d. To get the backing vocals stem, ensure `Vocals Only` is deselected.

    <img src="../uvrmvsep-img/17.png" alt="image" width="230" height="auto">

‎            
And that will be all. If they're all clean you're good to go & use it in RVC.    
!!!warning For the best results, follow the pipeline explained before:       
First, remove instrumental. Second, reverb. Third, backing vocals   
!!!  
***
:::content-center
:icon-heart-fill: If you liked the app, consider supporting the developers: https://www.buymeacoffee.com/uvr5 :icon-heart-fill:
:::

+++ Only Cleaning Vocals/Datasets 🗣️   

###### ‎      
#### 1. <u>Input audio.</u>   
Click `Select input` to select your audio/s.     
Or just drag the audios to it.  

In `Select ouput` you select in which folder you want the results to be.    

<img src="../uvrmvsep-img/4.jpg" alt="image" width="300" height="auto">‎        

!!!success 
For better results, have the audio in a [<u>lossless format</u>](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/) (**WAV** or **FLAC**), & not MP3.
!!!
***
###### ‎ 
#### 2. <u>Select FLAC & GPU Conversion.</u> 
a. At the right you'll see three audio formats to pick as the output format.       
We recommend picking `FLAC`. Learn why [<u>here</u>](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/).   

b. If your GPU is **compatible with [<u>CUDA</u>](https://aihubdocs.github.io/en/other/glossary/#cuda)**, toggle `GPU Conversion` on for a faster process.    

    <img src="../uvrmvsep-img/16.png" alt="image" width="350" height="auto">‎      
###### ‎       
>This step is not mandatory but recommended for better results.
***
###### ‎  
#### 3. <u>Select model.</u>   
a. In `Process Method` select `VR`.  

b. At the center select `Window Size` as ``320``. (optional)        
Lower Window Size yield a higher output **quality**, but will take **longer** to process. 

b. In `Select VR Model`, select a model according to what you need to remove:     

    - For **noise**: `UVR-DeNoise`. Make sure to tick `No Noise only`.      

    - For **reverb**: `DeEcho-DeReverb`. Make sure to tick `No Reverb Only`.       

    - For **overlapping voices**, `UVR-BVE`. To get the backing vocals stem, ensure `Vocals Only` is deselected.

‎       
If you need to remove multiple noises, follow this pipeline for the best results: First, remove reverb. Second, backing vocals. And third, noise.  

!!!success
If a model isn't installed, click the wrench (🔧) on the left, go to `Download Center`, select `VR`, select said model & click the download symbol (📥).
!!!
***
###### ‎  
#### 4.<u> Start processing</u>.
Click the `Start processing` button at the bottom.      

And that will be all. If the audio is all clean you can go use it in RVC.       
‎       
!!!success <u>TIPS:</u>           
1. If a model extracted too much/too little, modify the `Aggression Setting` to determine the **depth** of the extraction, until you find the sweet spot.      
    - **Lower** values **softens** the extraction.   
    - **Higher** values **deepens** the extraction.          
‎         
2. For testing models/aggression settings, I recommend activating `Sample Mode`. This will process only ``30`` seconds of the sample, allowing you to test more efficiently.
!!!
***
:::content-center
:icon-heart-fill: If you liked the app, please consider supporting the developers: https://www.buymeacoffee.com/uvr5 :icon-heart-fill:
:::content-center  
+++

***
###### ‎      
### <u>Best Models of UVR</u> 💾
Although there are plenty of models you could use in UVR, these are the best ones for RVC.     

Extraction | Process Method | Model
:---: | :---: | :---:
Vocals/Instrumental | MDX-Net | MDX23C
Reverb | VR | DeEcho-DeReverb
Backing Vocals | VR | UVR-BVE
Noise | VR | UVR-DeNoise 

***     
:::content-center 
‎   
<img src="../uvrmvsep-img/8.png" alt="image" width="400" height="auto">

###### ‎       
## MVSEP
:::
###### ‎     
### <u>Introduction</u> 📜     
- MVSEP is a website for audio isolation that operates just like UVR, using AI models.

- It doesn't have all the models & options that UVR has, but it has the necessary tools for getting decent-enough vocals for RVC.

- It's one of the best free cloud-based alternative for UVR.
***
###### ‎     
### <u> How to Use</u> 📝    
!!! *If you use the free version:*
‎ ‎ ‎ • ‎ The maximum audio length you can use is 10 minutes.
If yours is longer, trim it into various smaller pieces.   
‎ ‎ ‎ • ‎ You can only convert 1 audio at a time, not in batches. Remember, MVSEP has unlimited use.
!!!
‎       
Depending on if you want to extract & clean vocals of a song from **scratch**, or if you only need to **clean** an already existing sample, the procedure is a little different: 

+++ Extract & Clean Vocals From Song 🎶  
###### ‎     
#### 1. <u>Log in.</u>    
a. First, make an account [<u>here</u>](https://mvsep.com/register).      

b. Once logged in, go to the [<u>main page</u>](https://mvsep.com).

!!!
Logging in is not mandatory, but recommended for **shorter waiting lists**.
!!!
***
###### ‎
#### 2. <u>Select audio & output format.</u>    
a. Click `Browse File` & select your audio. The audio will begin to upload.     
(or just drag the file into the upload box)    

    
    <img src="../uvrmvsep-img/9.png" alt="image" width="330" height="auto">‎   
‎       
b. In `Output encoding` select `FLAC`.      
We recommend selecting FLAC from now on. Learn more [<u>here</u>](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/).

    <img src="../uvrmvsep-img/10.png" alt="image" width="420" height="auto">‎   
    
***
###### ‎
#### 3. <u>Extract vocals.</u> 
In `Separation Type`, select `MDX23C`.      
Once the audio is done uploading, click `Separate`

<img src="../uvrmvsep-img/11.png" alt="image" width="400" height="auto">‎   

!!! Leave ``Vocal model type`` untouched.
!!!
***
###### ‎
#### 4. <u>Download output.</u>       
When it's done converting it will redirect you to a page where you can listen the results.      
Tap the three buttons of the **Vocals** audio and then `Download`.    

Do the same for the `Instrumental` one too, if you want the instrumental.

<img src="../uvrmvsep-img/12.png" alt="image" width="400" height="auto">‎   
***
###### ‎
#### 5. <u>Remove reverb.</u>        
Usually songs include reverb to the vocals. Leaving them in will **negatively** impact the quality in RVC.  

a. Go to the main page & input the vocals with no instrumental.

b. In `Separation type` select `Ultimate Vocal Remover HQ`.      
In `Model Type` select `UVR-DeEcho-DeReverb`.
c. Click `Separate` & download the vocals with no reverb afterwards.

    <img src="../uvrmvsep-img/13.png" alt="image" width="420" height="auto">‎   

!!!success <u>TIP:</u>
If you extracted too much/too little, with the `Ultimate Vocal Remover HQ` separation type you can adjust the `Agressiveness` value. This determines the **depth** of the extraction:          
‎ ‎ ‎ • ‎ **Lower** values **softens** the extraction.   
‎ ‎ ‎ • ‎ **Higher** values **deepens** it.    
!!!
***
###### ‎
#### 6. <u>Remove backing vocals.</u>  
Just like reverb, songs also normally include backing vocals.

a. Go to the main page & input the vocals with no reverb.

b. In `Separation type` select `Ultimate Vocal Remover HQ`.      
In `Model Type` select `UVR-BVE-4B_SN-44100-1`.
c. Click `Separate` and then download the main vocals.      
Download the backing vocals stem too, if you wish to keep them.

    <img src="../uvrmvsep-img/14.png" alt="image" width="420" height="auto">‎   
    ‎     

And that will be all. If it's all clean go ahead and use your audios in RVC.     

!!! *For the best results, follow the pipeline explained before.*      
First, remove instrumental. Second, reverb. And third, backing vocals.   
!!!
***
:::content-center
:icon-heart-fill: If you liked the app, consider supporting the developers: https://mvsep.com/billing :icon-heart-fill:
:::

+++ Only Cleaning Vocals/Datasets 🗣️   
###### ‎     
#### 1. <u>Log in.</u>    
a. First, make an account [<u>here</u>](https://mvsep.com/register).      

b. Once logged in, go to the [<u>main page</u>](https://mvsep.com).

!!!
Logging in is not mandatory, but recommended for **shorter waiting lists**.
!!!
***
###### ‎
#### 2. <u>Select audio & output format.</u>    
a. Click `Browse File` and select your audio. (or just drag the file into the upload box)    
The audio will begin to upload.
    
    <img src="../uvrmvsep-img/9.png" alt="image" width="330" height="auto">‎   
‎       
b. In `Output encoding` select `FLAC`.      
We recommend selecting FLAC from now on. Learn more [<u>here</u>](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/).

    <img src="../uvrmvsep-img/10.png" alt="image" width="420" height="auto">‎    
***
###### ‎
#### 3. <u>Select model.</u>    
In `Separation Type`, select `Ultimate Vocal Remover 5 HQ`. In `Model Type` select the model according to what you need to remove:       
- For **reverb**: `UVR-DeEcho-DeReverb`.        
- For **overlapping voices**: `UVR-BVE-4B_SN-44100-1`.      
- For **noise**: `UVR-DeNoise`.

Then click `Separate` and it will begin to convert. 

!!! Leave ``Vocal model type`` untouched.
!!!
*** 
#### 4. <u>Download output.</u>       
When it's done converting it will redirect you to a page where you can listen the results.          
Tap the three dots of the audio you need and then `Download`.  

If you wish to keep the backing vocals stem, remember to download it too. 

And that will be all. If it's all clean go ahead and use it in RVC.         
‎           
!!! Notes & Tips
**1.** For the best results, follow the pipeline explained before.      
First, remove instrumental. Second, reverb. And third, backing vocals.  

**2.** If you extracted too much/too little</u>, with the `Ultimate Vocal Remover HQ` separation type you can adjust the `Agressiveness` value, which determines the **depth** of the extraction.       
‎ ‎ ‎ • ‎ **Lower** values **softens** the extraction.   
‎ ‎ ‎ • ‎ **Higher** values **deepens** the extraction.    
!!!
***
:::content-center
:icon-heart-fill: If you liked the app, consider supporting the developers: https://mvsep.com/billing :icon-heart-fill:
:::

+++
‎       
:::content-center
### <u>Best Models of MVSEP</u> 💾    
:::
‎       
Although there are plenty of models you could use in MVSEP, these are their best ones for RVC.  

Extraction | Separation Type | Model
:---: | :---: | :---:
Vocals/Instrumental | MDX23C | - 
Reverb | Ultimate Vocal Remover 5 HQ | UVR-DeEcho-DeReverb
Backing Vocals | Ultimate Vocal Remover 5 HQ | UVR-BVE-4B_SN-44100-1
Noise | Ultimate Vocal Remover 5 HQ | UVR-DeNoise
***
:::content-right
||| *Did I miss anything?*        
Send any feedback [<u>here</u>](https://forms.gle/5i6hTJRVkXRohvVF9) 👈
|||
::: 
