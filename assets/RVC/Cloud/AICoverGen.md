---
icon: chevron-right
order: 2000
---

``Last update: Mar 4, 2024`` 
‎  
***
###### ‎  
:::content-center
## Introduction
:::


- The AICoverGen Colabs are a port of the AICoverGen RVC <u>[fork</u>](https://docs.ai-hub.wtf/essentials/whats-rvc/#forks) to <u>[Google Colab</u>](https://docs.ai-hub.wtf/extra/glossary/#google-colab).

- These are ideal for users who want '***quick & dirty***' AI covers, as the whole process of inputting audio, vocal isolation & song mixing is automated. 

- The pitch control is limiting & inconvenient, so if you want a Colab with more control over it, use <u>[Ilaria RVC](https://docs.ai-hub.wtf/rvc/cloud/ilaria-rvc/)</u> instead.     

- ##### The two versions of the port are: <u>[AICoverGen NO UI](https://docs.ai-hub.wtf/rvc/cloud/aicovergen/#aicovergen-no-ui)</u> and <u>[AICoverGen UI](https://docs.ai-hub.wtf/rvc/cloud/aicovergen/#aicovergen-ui)</u>.
               
***
###### ‎  
:::content-center
## AICoverGen NO UI
:::
###### ‎  
### <u>Description</u> :icon-book:
- This is the version of the port that doesn't have the premade user interface. Credits to Eddy & Raid. Base notebook by <u>[Ardha27</u>](https://github.com/ardha27). 

- It's an upgrade from the original Colab space, bringing bug fixes, improvements, & extra features.    

- The NO UI counterpart is mainly preferred due to being more **stable** compared with the UI version.    
‎   
#### Pros & Cons :icon-tasklist:
==- *Learn more*
!!! *The pros & cons are subjective to your necessities.*      
!!!
||| **✔️ PROS:**       
- Automatic vocal extraction.           
- Song mixing tool.       
- Has Mangio-Crepe.      
- Automatic model upload.               
- Input audio with YouTube links. 
- Can get the stems files.
- More stable.
||| **❌ CONS:**       
- Usage limit for free users.           
- Takes 6 mins to load.        
- UI is incovenient.  
- No control over the stem separation.
- The extraction will always run, you'll waste time if you input clean vocals. 
- Little control of the mixing tools.
- Limited pitch control.
|||     
===

***

###### ‎  
### <u>Setting Up</u> :icon-download:
#### 1. Enter the space
a. Access the Colab space <u>[here</u>](https://colab.research.google.com/drive/1u1brjK8IZt647UsbZuGYfW29oFM2I4tk?usp%3Dsharing&sa=D&source=editors&ust=1704303145687891&usg=AOvVaw3M9tmokG80RXF-GD1LJqCL). Then **Sign in** to your Google account.

    <img src="../aicovergennoui-img/page.png" alt="image" width="500" height="auto">     

***     
###### ‎    
#### 2. Clone and Install    
- Execute the ``Clone and Install``. This will install RVC.      

    <img src="../aicovergennoui-img/cloneandinstall.png" alt="image" width="280" height="auto">‎         
‎    
- It will take around 15 minutes.       
It'll be done when you see a check symbol (✔️) on the corner.        

    <img src="../aicovergennoui-img/check.png" alt="image" width="370" height="auto">‎
‎         
>Don't worry if red text appears, it's normal.          

***
###### ‎  
### <u>Inference</u> :icon-unmute:
#### 1. Download model      
a. Go to **Model Download Function** cell. Paste the <u>[model's link](https://docs.ai-hub.wtf/essentials/voice-models/#how-to-search-voice-models)</u> in the **url** bar.     

b. In **dir_name** name the model. Don't include spaces/special characters.        
           
c. Then execute the cell. 

    <img src="../aicovergennoui-img/model.png" alt="image" width="550" height="auto">‎    

!!!
Downloaded models will be saved until the Colab session ends.  
!!!
***
###### ‎  
#### 2. Input the audio   
- Input the vocals/song in the **Generate Cover** cell.     

- You can go about it with either a <u>**YouTube link**</u> or a <u>**Google Drive file**</u>:     

    +++ :icon-link: ‎ **YouTube link**
    - Copy a YouTube link and paste it in the **SONG_INPUT** bar.

        <img src="../aicovergennoui-img/generatecoveryt.png" alt="image" width="420" height="auto">‎              

    +++ :icon-file: ‎ **Google Drive file**       
    a. Execute the **Mount Drive** cell below.      
    ‎       
     <img src="../aicovergennoui-img/mountdrive.png" alt="image" width="210" height="auto">‎           

    ***      
    ###### ‎  
    b. Click `Connect to Google Drive` & select your Account.   
    ‎        
        <img src="../aicovergennoui-img/connect.png" alt="image" width="280" height="auto"> 
    ***      
    ###### ‎  
    c. Click the folder symbol ( :icon-file-directory: ) on the left.      
    (For mobile users: tap the three lines on the top left & `Show file browser`)

        Go to **drive** & you'll find your GD storage.        
        Right-click your audio & press ``Copy path``.       
        ‎       
        <img src="../aicovergennoui-img/1.png" alt="image" width="320" height="auto">           
    ***        
    ###### ‎  
    d. Paste the path in the **SONG_INPUT** bar.        
    ‎            
        <img src="../aicovergennoui-img/inputaudio.png" alt="image" width="420" height="auto">
    +++
***
###### ‎  
#### 3. Select model   
- In **RVC_DIRNAME** insert the model's name you assigned before.       

    <img src="../aicovergennoui-img/2.png" alt="image" width="400" height="auto">    

***     
###### ‎   
#### 4. Modify settings (optional)        
- Below **RVC_DIRNAME** until **Audio Mixing Options** you'll find the <u>[inference settings</u>](https://docs.ai-hub.wtf/rvc/resources/inference-settings/).     
Tweak them accordingly for better results if you wish.

    <img src="../aicovergennoui-img/3.png" alt="image" width="270" height="auto">‎      

***
###### ‎  
#### 5. Modify mix & reverb (optional)         

- In **Audio Mixing Options** you can modify the values to define the volume of main/backing vocals & instrumental.

    <img src="../aicovergennoui-img/4.png" alt="image" width="240" height="auto">‎                
    ‎     
- In `Reverb Control` you can add reverb to the output vocals.      
    ‎       
<img src="../aicovergennoui-img/6.png" alt="image" width="240" height="auto"> ‎  
 ‎
==- *Reverb Control options:*
**REVERB_SIZE**
:    How "wide" the reverb sounds, like the size of a room.       

**REVERB_WETNESS**
:    Volume of the reverb itself.        

**REVERB_DRYNESS**
:    Volume of the vocals.       

**REVERB_DAMPING**
:    Level of absorption of the reverb's *high frequencies*:       
- Higher values yield a warmer, natural-sounding reverb.       
- Lower ones sound brighter & more present.   
===

***

###### ‎    
#### 6. Begin inferring   
- Execute the **Generate Cover** cell to begin the conversion.      

- It'll be done when the logs say **Cover generated at** followed by the file path.    

    <img src="../aicovergennoui-img/9.png" alt="image" width="850" height="auto">

***
###### ‎   
#### 7. Download output    
a. Click the folder symbol ( :icon-file-directory: ) on the left.      
(For mobile users: tap the three lines on the top left & **Show file browser**)        

    
       
b. Open **song_output** folder & the one inside it. Right-click the first file & press `Download`.      
The other audios are the stems. Download them too if you wish.

    <img src="../aicovergennoui-img/10.png" alt="image" width="550" height="auto">‎   

###### ‎  
- #### If the voice glitches out, click <u>[here</u>](https://docs.ai-hub.wtf/rvc/resources/artifacting/).


***
###### ‎  
:::content-center
## AICoverGen UI
:::
###### ‎  
### <u>Description</u> :icon-book:
- This is the version that's built with the premade user interface. Port by <u>[Hina](https://huggingface.co/HinaBl)</u>. Original repo by <u>[SociallyIneptWeeb</u>](https://github.com/SociallyIneptWeeb/AICoverGen).    

- It's characterized & preferred due to its intuitive UI, ideal for beginners.

- But on the downside, it may be more buggy, so consider using the <u>[NO UI version](https://docs.ai-hub.wtf/rvc/cloud/aicovergen/#aicovergen-no-ui)</u> if issues arise.     
‎          
#### Pros & Cons :icon-tasklist:
==- *Learn more*
!!! *The pros & cons are subjective to your necessities.*      
!!!
||| **✔️ PROS:**       
- Automatic vocal extraction.           
- Song mixing tool.                 
- Has Mangio-Crepe.      
- Automatic model upload.               
- Input audio with YouTube links
- Great UI.
- Can get the stems files.
- Quicker audio file upload.
||| **❌ CONS:**       
- Usage limit for free users.           
- Takes 6 mins to load.        
- No control over the stem separation.
- The extraction will always run, you'll waste time if you input clean vocals. 
- Little control of the mixing tools.
- Inconvenient pitch control.
- More unstable.
|||    

===
***
###### ‎  
### <u>Setting Up</u> :icon-download:

#### 1. Enter the space
- Access the Colab space <u>[here](https://colab.research.google.com/github/hinabl/AICoverGen-Colab/blob/main/Hina_Mod_AICoverGen_colab.ipynb)</u>.
- Then login to your Google account.
***
###### ‎  
#### 2. Define pitch
- In the **Clone Repository** cell, select the pitch change.

    <img src="..\aicovergenui-img\clonerepo.png" alt="image" width="400">‎      
    ‎   
- If you're going to use models of the **same gender** as the vocals, use ``1``.
- If they're of **opposite** gender, use ``12``
- To change this, you'll have to start the Colab from scratch.
***
###### ‎  
#### 3. Run cells
- Then go to **Runtime** on top & press ``Run all``.

    <img src="..\aicovergenui-img\runall.png" alt="image" width="400">

***
###### ‎  
#### 4. Open UI
- After a moment the **Run WebUI** cell will show two links. Open the **public URL** one.

    <img src="..\aicovergenui-img\url.png" alt="image" width="600">‎    

!!!warning Don't close Colab until you're done using it, or it will stop working.
!!!
***
###### ‎  
### <u>Inference</u> :icon-unmute:
#### 1. Upload model
- You can upload it using **its link** or **manually** inputting its files.   
    +++ :icon-link: ‎ Link
    a. Go to the **Download model** tab & paste the <u>[model link](https://docs.ai-hub.wtf/essentials/voice-models/#how-to-search-voice-models)</u> in the bar.

    b. Name it in **Name your model**. Don't introduce spaces/special characters.

    c. Click **Download**.

        <img src="..\aicovergenui-img\modellink.png" alt="image" width="750">

    +++ :icon-file: ‎ Manually
    a. Zip the model into a **.ZIP** file, if you haven't already.

    b. Go to the **Upload model** tab, press the upload box & submit the ZIP.

    c. Name it in **Model name**. Don't introduce spaces/special characters.

    d. Press **Upload model**.

        <img src="..\aicovergenui-img\manualupload.png" alt="image" width="600">

    +++
***
###### ‎  
#### 2. Select model
- Return to the **Generate** tab & press **Refresh Models**. Then select it in the **Voice Models** dropdown.

    <img src="..\aicovergenui-img\selectmodel.png" alt="image" width="400">
***
###### ‎  
#### 3. Select audio
- On its right, input the YouTube link.

    <img src="..\aicovergenui-img\link.png" alt="image" width="380">‎  
‎  
- Or, press **Upload file instead**, click **Upload** & input the audio file.
***
###### ‎  
#### 4. Modify settings (optional)
- Unfold **Voice conversion options** to modify the <u>[inference settings](https://docs.ai-hub.wtf/rvc/resources/inference-settings/)</u> for better results.

***
###### ‎  
#### 5. Select output format
- Unfold **Audio mixing options** & set **Output file type** as ``wav``, for a better quality output.

    <img src="..\aicovergenui-img\wav.png" alt="image" width="600">‎    
‎   
- Modify the mix too if you wish.
***
###### ‎  
#### 6. Convert
- Press **Generate**. The audio will begin processing.
- Once it's done, you can hear the results in the **AI Cover** output box.
- To download it, press the download symbol ( :icon-download: ) on its right.

    <img src="..\aicovergenui-img\output.png" alt="image" width="400">

***
###### ‎  
#### 7. Download stems (optional)
- To download the stems, go to Colab & click the folder symbol ( :icon-file-directory: ) on the left.       
(For mobile users, tap the three lines ( :icon-three-bars: ) on the top left &  **Show File Explorer**)

- Go to **Hina_RVC**, **song_output**, open the new folder, right-click the stem you wish & click `Download`.

    <img src="..\aicovergenui-img\stems.png" alt="image" width="470">‎    
‎    
- #### If the voice glitches out, click <u>[here](https://docs.ai-hub.wtf/rvc/resources/inference-settings/)</u>.

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/rvc/contributions/)
:::