---
icon: chevron-right

order: 1000
---

``Last update: Mar 7, 2024``
***
###### ‎ 
:::content-center
## Requirements

##### ``Before proceeding, ensure you meet these requirements.``
:::
###### ‎
||| <u> REQUIREMENTS </u>
- Model's <u>[**.PTH**](https://docs.aihub.wtf/essentials/voice-models/#voice-model-files)</u> file.        
- Model's <u>[**.INDEX**](https://docs.aihub.wtf/essentials/voice-models/#voice-model-files)</u> file.      
- General information about the model.
- General information about its training process.      
- A Hugging Face account.     
- At least 1 audio sample of the model **<u>WITH NO MUSIC</u>**.     
|||
:::


:::content-center
###### ‎ 
## Things to Avoid :icon-x:
##### ``This will disqualify your post``
:::
‎
:   ‎
:::
#### :icon-chevron-right: It lacks the correct files.
- The .ZIP file must contain both the **correct** `.INDEX` & `.PTH` file. Learn about them <u>[here](https://docs.aihub.wtf/essentials/voice-models/#voice-model-files)</u>.
***
###### ‎ 
#### :icon-chevron-right: Model is low quality.
- <u>**A bad model sounds:**</u>       

   - Scratchy/screechy.
   - Muffled.
   - Inaccurate to the source.
   - Incapable of hitting certain notes.
   - With slurred speech.
   - Unable of pronouncing words correctly in its intended language.
   - With <u>[artifacting](https://docs.aihub.wtf/rvc/resources/artifacting/)</u>.
***
###### ‎ 
#### :icon-chevron-right: An outdated extraction method was used.
{.list-icon}
- :icon-check-circle: Only **Mangio-Crepe** & **RMVPE** are allowed. Learn about them <u>[here](https://docs.aihub.wtf/rvc/resources/inference-settings/#pitch-extraction-algorithm)</u>

- :icon-x-circle: Harvest, Dio, Crepe-Tiny, PM, etc. are obsolete.

***
###### ‎ 
#### :icon-chevron-right: The audio demo has an instrumental.
- Don't include **ANY** music on the audio demo, even if it's not copyrighted. This is due to:
  
     - Concerns over copyright.
     - In many cases, the music can "hide" the flaws of the voice models, making it harder to judge the quality of the model.
***
#### :icon-chevron-right: The audio demo is altered.
- Don't add reverb, equalize, or alter the demo in any way, as that won't be a faithful representation of the model. It must be the raw, unmodified output from RVC.

- Trimming silences at the beginning/end of the audio is valid. :icon-check-circle: 
###### ‎  
***
###### ‎
:::content-center
## Steps
‎
:   ‎
:::
#### Step 1: Zip the model.
- Gather the **.PTH** & **.INDEX** file and <u>[zip</u>](https://support.microsoft.com/en-us/windows/zip-and-unzip-files-8d28fa72-f2f9-712f-67df-f80cf89fd4e5) them into a ``.ZIP`` file.
         
- It must be a **.ZIP** file, not .7ZIP or .RAR.
***
###### ‎
#### Step 2: Upload it.
- The ZIP must be stored in Hugging Face in a **public** repo of `openrail` license.    

- Learn how <u>[here</u>](https://docs.aihub.wtf/essentials/voice-models/#uploading-to-hugging-face).
***
###### ‎
#### Step 3: Prepare the submission.
- Once your model is ready, head over to the **#get-model-maker** channel.  

- Type the `/submit` command of **QCBot** and click the command.       

<img src="../modelmaker-img/submit.png" alt="image" width="600" height="auto">‎               
‎     
:::content-center
#### ``Now fill up the information about your model:``  
:::

**modelname**
:     Its name.   

**rvc**
:     Version of RVC it was trained on (will almost always be v2).

**extraction**
:     The <u>[extraction method](https://docs.aihub.wtf/rvc/resources/inference-settings/#pitch-extraction-algorithm)</u> you used.

**epochs**
:     Total <u>[epochs](https://docs.aihub.wtf/rvc/resources/epochs--tensorboard/)</u> amount.

**link**
:     Its download link from Hugging Face.

**image**
:     Image of what it represents (person/character).   

**demo**
:     Audio sample of it talking/singing.

**note** 
:   Optional. Add more context about the model if you want.

***
!!!success 
You can attach more samples when you repost the model to ``#voice-models``.
!!!
***
###### ‎
#### Step 4: Send submission.
- Once you are done filling the information, send the message.    

- If everything went fine, your submission will be added to the queue & the bot will send a confirmation message, containing your **submission ID**.    
<u>**With the ID you can:**</u>        
   - Check your submission's number in queue with the command ``/queue`` followed by the ID. (e.g ``/queue 251``).        
   - Cancel your submission with the command ``/cancel`` followed by the ID.    
‎     
- Now wait for a **Model QC** (quality checker) to verify your model. You'll be notified once it has been reviewed.   

- If your model gets approved, the bot will notify you with something like this:    

   <img src="../modelmaker-img/approved.png" alt="image" width="" height="auto">‎     
‎    
- You can then repost the model (& future models) to the ``#voice-models`` forum.

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.wtf/rvc/#contributions)
:::