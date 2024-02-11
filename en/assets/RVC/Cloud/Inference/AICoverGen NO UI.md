``Last update: Feb 10, 2024`` 
‎  
***
###### ‎  
:::content-center
## Introduction
:::
- AICoverGen NO UI is a port of the AICoverGen RVC <u>[fork</u>](https://aihubdocs.github.io/en/other/glossary/#fork) to <u>[Google Colab</u>](https://aihubdocs.github.io/en/other/glossary/#google-colab). Base notebook by <u>[Ardha27</u>](https://github.com/ardha27).    

- This version (**Eddy's Version**) is an upgrade from the original Colab space, bringing bug fixes, improvements, & extra features. Credits to Eddy & Raid.

- Because of its **quick** <u>[inference](https://aihubdocs.github.io/en/other/glossary/#inference)</u>, automatic vocal extraction, & compatibility with YouTube links, it's considered one of the best Colab spaces for inferencing in RVC.        
‎               
### Pros & Cons :icon-tasklist:
==- ***Unfold***
!!! *The pros & cons are subjective to your necessities.*      
!!!
||| **✔️ PROS:**       
- Automatic vocal extraction.           
- Song mixing tool.            
- Tool to add reverb.       
- Includes Mangio-Crepe algorithm.      
- Model download through links.               
- Can input audio with YouTube links. 
- Automatic stem separation (can get each later).
||| **❌ CONS:**       
- Usage limit for free users.           
- Takes 10-15 mins to load.        
- UI is not great.  
- No control over the stem separation process. Could be a problem.
- Said extraction will always run. You'll waste time if you input clean vocals. 
- Little control of the mixing-reverb tools. Using a DAW is more convenient
|||     
===               
***
###### ‎  
:::content-center
## How to Use
:::
###### ‎  
#### 1. <u>Enter the space.</u>      
a. Log in to Google <u>[here</u>](https://accounts.google.com/).     
b. Then access the Colab space <u>[here</u>](https://colab.research.google.com/drive/1u1brjK8IZt647UsbZuGYfW29oFM2I4tk?usp%3Dsharing&sa=D&source=editors&ust=1704303145687891&usg=AOvVaw3M9tmokG80RXF-GD1LJqCL).    

    <img src="../aicovergen-img/page.png" alt="image" width="500" height="auto">     

***     
‎       
#### 2. <u>Clone and Install.</u>     
- Execute the ``Clone and Install``.     
This will install RVC.      

    <img src="../aicovergen-img/cloneandinstall.png" alt="image" width="280" height="auto">‎         
‎    
- It will take around 15 minutes.       
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
       

b. In `dir_name` name the model. Don't include spaces/special characters.        
           
c. Then execute the cell. 

!!!
The models you download will be saved until the Colab session ends.  
!!!
***
###### ‎  
#### 4. <u>Input the audio.</u>      
Input the vocals/song in the `Generate Cover` cell.     

You have two ways of doing this: using a <u>**YouTube link**</u> or a <u>**Google Drive file**</u>:     

+++ **YouTube link**
Copy a YouTube link, and paste it in the ``SONG_INPUT`` bar.

<img src="../aicovergen-img/generatecoveryt.png" alt="image" width="420" height="auto">‎              

+++ **Google Drive file**       
###### ‎   
a. Execute the cell ``Mount Drive`` that's below `Generate Cover`.      
‎       
     <img src="../aicovergen-img/mountdrive.png" alt="image" width="210" height="auto">‎           

***      
b. Click `Connect to Google Drive` & select your Google Account.   
‎        
    <img src="../aicovergen-img/connect.png" alt="image" width="280" height="auto"> 
***      
c. Click the folder symbol ( :icon-file-directory: ) on the right.      

    Go to ``drive`` folder, then ``MyDrive``, & you'll find your Google Drive storage.        
    Find your audio, right-click it, & press ``Copy path``.       
‎       
    <img src="../aicovergen-img/1.png" alt="image" width="320" height="auto">           
***        
d. Paste the path file in the `SONG_INPUT` bar, located in the `Generate Cover` cell.    
‎            
    <img src="../aicovergen-img/inputaudio.png" alt="image" width="420" height="auto">
+++
###### ‎  
#### 5. <u>Select voice model.</u>        
Under it in ``RVC_DIRNAME`` type the model's name that you have assigned before.       

<img src="../aicovergen-img/2.png" alt="image" width="400" height="auto">    

***     
###### ‎   
#### 6. <u>Modify settings.</u> (optional)        
Below ``RVC_DIRNAME`` until ``Audio Mixing Options`` you'll find the <u>[inference settings</u>](https://aihubdocs.github.io/en/rvc-resources/inference-settings/).     
Tweak them accordingly for better results if you wish.

 <img src="../aicovergen-img/3.png" alt="image" width="270" height="auto">        

‎       
> • ‎ `REMIX_MIX_RATE` works like *Volume Envelope*.        
> • ‎ `FILTER_RADIUS` lowers the volume of breath sounds. (not suppress) 
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
==- <u>*Reverb Control options:*</u>
REVERB_SIZE
:    How "wide" the reverb sounds, like the size of a room.       

REVERB_WETNESS
:    Volume of the reverb itself.        

REVERB_DRYNESS
:    Volume of the vocals.       

REVERB_DAMPING
:    Level of absorption of the reverb's *high frequencies*:       
‎ ‎ ‎ ‎ ‎ ‎ • ‎ Higher values yield a warmer, natural-sounding reverb.       
‎ ‎ ‎ ‎ ‎ ‎ • ‎ Lower ones sound brighter & more present.   
===

***
###### ‎    
#### 8. <u>Begin the inference.</u>      
Once you are ready, execute the `Generate Cover` cell to begin the conversion.      

It'll be done when the last message says "**Cover generated at**" followed by the file path.    

<img src="../aicovergen-img/9.png" alt="image" width="850" height="auto">

***
###### ‎   
#### 9. <u>Download the output.</u>     
a. Click the folder symbol ( :icon-file-directory: ) on the right.      
Open the `content` folder, then `FIX`, `song_output`, & you'll see a folder with a bunch of numbers, containing the results and some stems.

    The inferred vocals will be named with the **algorithm** that you chose (Crepe or RMVPE), followed by "**mixed**" at the end.     

b. Right-click the audio, press `Download` & that's all.       

    <img src="../aicovergen-img/10.png" alt="image" width="550" height="auto">‎   

    !!!
    If you want the output without `REMIX_MIX_RATE`'s influence, use the one without "mixed" at the end.  
    !!!
###### ‎  
- #### If the voice glitches out, click <u>[here</u>](https://aihubdocs.github.io/en/rvc-resources/artifacting/).
***
###### ‎   
:::content-center
``Original guide: Eddy``     
:::
:::content-center
``Redone by: Julia``  
:::
:::content-center
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Send Suggestions"](https://forms.gle/3GVR7opzpQrhgRCj9)
::: 
***