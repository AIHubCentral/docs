# :icon-dependabot: Voice Models

``Last update: April 19, 2026``        

***

:::   
:::content-center
## What is a Voice Model
:::
- ***In the field of AI***, is a program that was trained to recognize certain patterns or make certain decisions.

- **In this case**, voice models are models trained to **replicate** a voice, and with AI they apply it to the input audio.

- There are plenty of them uploaded to the internet, made by the public. And the best way to make them is with [RVC</u>](https://docs.aihub.gg/essentials/how-to-make-voice-models/).   

###### ‎   
### Voice Model Files 
==- *They are made up of two files:*       
###### ‎    
##### :icon-triangle-down: <u>PTH:</u>   
- This file is the model itself.
- Contains data regarding pitch.     
- While training, RVC generates other .PTHs named `D_` and `G_`, but these are the [checkpoints](https://docs.aihub.gg/extra/glossary/#checkpoints), not usable models.  
###### ‎       
##### :icon-triangle-down: <u>INDEX:</u>
- Contains data regarding the voice's accent and speech manner.       
- File is additional, but usually **crucial** for the **quality** of the model.        
- While training, RVC generates two .INDEX file, but the right one will be named ``added_`` by default.         
***
!!!warning *Be sure to upload the correct files mentioned before.*
As people sometimes upload them incorrectly.
!!!
===

***
###### ‎
:::content-center
## How to Search Voice Models
#### *``Methods to find one online.``*
:::
###### ‎  

+++ Voice Models channel     
:::content-center
<img src="../searchrvcmodels-img/aihub.png" alt="image" width="200" height="auto">        
:::
‎   

- This is a forum channel in **AI Hub** where people upload their own voice models.       
- Searching here is specially useful if you need the model as a link, as the posts include one.       
***
###### ‎   
#### 1. Enter the channel   
- If you haven't already, join AI Hub [here</u>](https://discord.gg/mmRR2TUJF5).         
- Then go to the [``#voice-models``](https://discord.com/channels/1159260121998827560/1175430844685484042) forum channel.       
       
<img src="../searchrvcmodels-img/5.png" alt="image" width="480" height="auto"> 

***
###### ‎
#### 2. Search    
- In the upper search bar, search your model & click the post.
***
###### ‎
#### 3. Download   
- Click the Hugging Face link to download the model, or copy it if that's what you need.      
- You can listen to the audio sample to get a preview of the it.

    <img src="../searchrvcmodels-img/6.png" alt="image" width="480" height="auto"> 

+++ Hugging Face search
:::content-center
<img src="../searchrvcmodels-img/11.png" alt="image" width="510" height="auto">       
:::
‎   

- This is a free & open-source platform for storing Any Type AI models, interactive AI apps, & datasets.
!!!
**Reminder:** This is a General AI Platform, not every model is an RVC one.
!!!           
***
###### ‎
1. Go to the [models page](https://huggingface.co/models) & search the model in the ``Filter by name`` bar.

    <img src="../searchrvcmodels-img/9.png" alt="image" width="" height="auto">‎                   
‎       
2. Click the model & go to the ``Files and versions`` tab.

3. To download it, click the download symbol ( :icon-download: ) on the right of the .ZIP file.     
    If you need its link, right-click it and copy the address.

    <img src="../searchrvcmodels-img/10.png" alt="image" width="530" height="auto">         
  
###### ‎   

!!! In case there isn't a .ZIP.
Download the [correct files](https://docs.aihub.gg/essentials/voice-models/#voice-model-files) of the model. Then if you need its **link**, [upload it to HF</u>](https://docs.aihub.gg/essentials/voice-models/#uploading-to-hugging-face).
!!!

+++

##### ‎ 
#### If you couldn't find one, you have 3 options:   
- [Make the model yourself](https://docs.aihub.gg/essentials/how-to-make-voice-models/)
- Pick a different one.
- Request a **free** model via [AI HUB](https://discord.gg/mmRR2TUJF5)'s [``#request-models``](https://discord.com/channels/1159260121998827560/1159289738314919936) forum channel. Be aware that **we don't allow paid commissions**

##### ‎
***
:::content-center
## Uploading to Hugging Face
:::
‎
:   ‎

#### 1. Zip the model        
- Select the correct [.PTH & .INDEX](https://docs.aihub.gg/essentials/voice-models/#voice-model-files) & [zip</u>](https://support.microsoft.com/en-us/windows/zip-and-unzip-files-8d28fa72-f2f9-712f-67df-f80cf89fd4e5) them into a **.ZIP** file.       

- Ensure it's .ZIP & not .RAR or .7ZIP.

***
###### ‎ 
#### 2. Log in
- If you haven't already, [create an account</u>](https://huggingface.co/join) & log in.
***
###### ‎  
#### 3. Make repository
a. Once logged in, tap your profile on the upper right corner, & then `New Model`.       

    <img src="../hfupload-img/1.png" alt="image" width="200" height="auto">

    ‎

b.  In `Model name` you name the repo as you want.   

c.  Make sure **License** is set as `openrail` & the repo is set as `Public`.     

d.  Once done, hit `Create model`.

    <img src="../hfupload-img/2.png" alt="image" width="480" height="auto"> ‎                
***
###### ‎ 
#### 4. Upload model
a. It will redirect you to the repo.        
Go to the `Files and versions` tab on the center, click `+ Add file` on the right & then ``Upload files``.

    <img src="../hfupload-img/3.png" alt="image" width="350" height="auto">‎    
‎                         
b. Tap the upload box & submit the ZIP. Or just drag & drop.       

    <img src="../hfupload-img/4.png" alt="image" width="" height="auto">‎       
‎       
c. Tap on `Commit changes to main` & the model will begin to upload.
***
###### ‎ 
#### 5. Copy link (optional)
- Once it's done, it will redirect you to the files list.       

- So if you need its link, right-click the download button ( :icon-download: ) of the .ZIP file on the right, and click `Copy Link`.

    <img src="../hfupload-img/5.png" alt="image" width="610" height="auto">
           
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
