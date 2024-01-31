‎   
*``Originally written by Eddy. Re-written by Julia``*         
``Last update: Jan 29, 2024`` 
‎  
***
###### ‎  
:::content-center
## Introduction 📜
:::
###### ‎    
- AICoverGen NO UI is a port of the AICoverGen RVC [<u>fork</u>](https://aihubdocs.github.io/en/other/glossary/#fork) to [<u>Google Colab</u>](https://aihubdocs.github.io/en/other/glossary/#google-colab).        
Base notebook by [<u>Ardha27</u>](https://github.com/ardha27).    

- This version (**Eddy's Version**) is an upgrade from the original Colab space, bringing bug fixes, improvements, & extra features.   
Credits to Eddy & Raid.

- It's liked for being fairly **quick**, having the necessary tools for a **great inference**, & being able to input audio through YouTube links. 

- Because of this, it's seen as one of the **best** Colab spaces for inferencing in RVC. Pretty much its only real downside is the **usage limit** for free users.       
‎               
### Pros & Cons :icon-tasklist:
==- ***Tap to unfold*** 👈
!!! *Pros & cons are subjective to your level of experience & needs.*      
You might disagree with some of the points.        
!!!
||| **✔️ PROS:**       
{.list-icon}
- :icon-plus: Faster than Hugging Face.      
- :icon-plus: Automatic vocal isolation.           
- :icon-plus: Song mixing tool.            
- :icon-plus: Tool to add reverb.            
- :icon-plus: Includes Mangio-Crepe algorithm.      
- :icon-plus: Model download through links.               
- :icon-plus: Can input audio with YouTube links. 
- :icon-plus: Automatic stem separation.        
(can get each after inferencing) 
||| **❌ CONS:**       
{.list-icon}
- :icon-dash: 6 hour daily use limit for free users.                   
- :icon-dash: Takes 10-15 mins to load.        
- :icon-dash: UI not user-friendly for free users.  
- :icon-dash: No control over the stem separation process. Could be a problem.
- :icon-dash: Stem separation process will always run. You'll waste time if inputting already clean vocals. 
- :icon-dash: Little control of the mixing-reverb tools. Using a DAW is more convenient
|||     
===               
***
###### ‎  
:::content-center
## How to Use 📝
:::
###### ‎  
#### 1. <u>Enter the space.</u>      
a. If you haven't already, first log in to your Google account [<u>here</u>](https://accounts.google.com/).     
b. Then access the Colab space [<u>here</u>](https://www.google.com/url?q=https://colab.research.google.com/drive/1u1brjK8IZt647UsbZuGYfW29oFM2I4tk?usp%3Dsharing&sa=D&source=editors&ust=1704303145687891&usg=AOvVaw3M9tmokG80RXF-GD1LJqCL).    

    <img src="../aicovergen-img/page.png" alt="image" width="500" height="auto">     

***     
‎       
#### 2. <u>Clone and Install.</u>     
- Execute the ``Clone and Install`` cell by pressing the play button :icon-play:.     
This will install RVC.      

    <img src="../aicovergen-img/cloneandinstall.png" alt="image" width="280" height="auto">‎         
‎    
- It will take around 10 - 15 minutes to load.       
It'll be done when you see a check symbol (✔️) on the corner.        

    <img src="../aicovergen-img/check.png" alt="image" width="370" height="auto">‎
‎         
>Don't worry if red text appears, it's normal.          

***
‎       
#### 3. <u>Download voice model.</u>    
<img src="../aicovergen-img/model.png" alt="image" width="550" height="auto">‎       
‎ 
a. Go to `Model Download Function` cell.        
Paste the model's link in the ``url`` bar.     
       

b. In `dir_name` name the model.      
Don't include spaces/special characters.       
(e.g "**ArianaGrande2023**" and not "Ariana Grande 2023 :3!")       
           
c. Then execute the cell. 

>The models you download will be saved until the   Colab session ends.  
***
###### ‎  
#### 4. <u>Input the audio.</u>      
Input the vocals/song in the `Generate Cover` cell.     
You have two ways of doing this: using a <u>**YouTube link**</u> or a <u>**Google Drive file**</u>:     

+++ **YouTube link**
a. In ``SONG_INPUT`` paste the YouTube link.

<img src="../aicovergen-img/generatecoveryt.png" alt="image" width="420" height="auto">‎              

+++ **Google Drive file**       
a. Execute the cell ``Mount Drive`` that's below `Generate Cover`.      
‎       
     <img src="../aicovergen-img/mountdrive.png" alt="image" width="210" height="auto">        
‎
‎       
‎       
b. Click `Connect to Google Drive`, select your Google Account & then `Allow`.   
‎        
    <img src="../aicovergen-img/connect.png" alt="image" width="280" height="auto"> 
‎       
‎       
‎           
c. Click the folder symbol on the right. Go to ``drive``, then ``MyDrive``, & you'll find your Google Drive storage.        
Find your audio, right-click it, & select ``Copy path``.       
‎       
    <img src="../aicovergen-img/1.png" alt="image" width="320" height="auto">           
‎       
‎       
d. Now paste the path file in `SONG_INPUT`, located in the `Generate Cover` cell.    
‎            
    <img src="../aicovergen-img/inputaudio.png" alt="image" width="420" height="auto">
+++
***
###### ‎  
#### 5. <u>Select voice model.</u>        
Under it in ``RVC_DIRNAME`` type the model's name that you have **assigned** before.       

<img src="../aicovergen-img/2.png" alt="image" width="400" height="auto">    

***     
###### ‎   
#### 6. <u>Modify settings.</u> (optional)        
Below ``RVC_DIRNAME`` until ``Audio Mixing Options`` you'll find the [<u>inference options</u>](https://aihubdocs.github.io/en/rvc-resources/inference-settings/).     
Tweak them accordingly for better results if you wish.

 <img src="../aicovergen-img/3.png" alt="image" width="270" height="auto">        

‎       
> • ‎ `REMIX_MIX_RATE` works like *Volume Envelope*.        
> • ‎ `FILTER_RADIUS` lowers the volume of breath sounds. (not supress) 
***
###### ‎  
#### 7 . <u>Modify mix & reverb.</u> (optional)         

- In ``Audio Mixing Options``, you can change the values to determine the volume of main vocals, backing vocals, & instrumental.      

    <img src="../aicovergen-img/4.png" alt="image" width="240" height="auto">‎                
    ‎     
- In `Reverb Control`, you can add reverb to the output vocals.      
    ‎       
<img src="../aicovergen-img/6.png" alt="image" width="240" height="auto"> ‎  
 ‎      
!!! <u>Reverb Control options:</u>     
:icon-chevron-right: **REVERB_SIZE**: how "wide" the reverb sounds, like the size of a room.        
:icon-chevron-right: **REVERB_WETNESS**: volume of the reverb itself.        
:icon-chevron-right: **REVERB_DRYNESS**: volume of the vocals.       
:icon-chevron-down: **REVERB_DAMPING**: level of absorption of the reverb's *high frequencies*:       
‎ ‎ ‎ ‎ ‎ ‎ • ‎ Higher values yield a warmer, natural-sounding reverb.       
‎ ‎ ‎ ‎ ‎ ‎ • ‎ Lower values yield brighter, more present reverb.   
!!!
***
###### ‎    
#### 8. <u>Begin the inference.</u>      
Once you are ready, execute the `Generate Cover` cell to begin the conversion.      

It'll be done when the last message says "**Cover generated at**" followed by the file path.    

<img src="../aicovergen-img/9.png" alt="image" width="850" height="auto">

***
###### ‎   
#### 9. <u>Download the output.</u>     
a. Click the folder symbol on the right. Open the `content` folder, then `FIX`, `song_output` and you'll find the output inside a folder with numbers.     

    You'll find the stems too.        
    The inferred vocals will be named with the *pitch extraction algorithm* that you chose, followed by "**mixed**" at the end.     

b. Right-click the audio, press `Download` and that's all.       

    <img src="../aicovergen-img/10.png" alt="image" width="550" height="auto">
>If you want the output without `REMIX_MIX_RATE`'s influence, use the one without "mixed" at the end.  


- #### If the voice glitches out, click [<u>here</u>](https://aihubdocs.github.io/en/rvc-resources/artifacting--how-to-fix-it/).
***
:::content-right
||| *Did I miss anything?*        
Send any feedback [<u>here</u>](https://forms.gle/5i6hTJRVkXRohvVF9) 👈
|||
:::
