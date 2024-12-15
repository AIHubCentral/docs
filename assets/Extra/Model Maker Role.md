---
icon: chevron-right

order: 1000
---

``Last update: October 20, 2024``
***
###### ‎ 
:::content-center
## Requirements

##### ``Before proceeding, ensure you meet these requirements.``
:::
###### ‎
||| <u> REQUIREMENTS </u>
- Model's **.PTH** file.        
- Model's **.INDEX** file.      
- General information about the model.
- General information about its training process.      
- A Hugging Face or Weights.gg account.     
- At least 1 raw audio sample of the model **<u>WITH NO MUSIC</u>**.     
|||
:::


:::content-center
###### ‎ 
## Things to Avoid :icon-x:
##### ``These will disqualify your post``
:::
‎
:   ‎
:::
#### :icon-chevron-right: It lacks the correct files.
- The .ZIP file must contain both the **correct** `.INDEX` & `.PTH` file.

- The correct .index is the one named `added_`. 
     - The added index contains the voice's accent and speech manor.

- The correct .pth is the one that has your model's name, for example: `TylerSwift_e60_s120.pth` 
     - The .pth contains the actual model and pitch data. 
     
***
###### ‎ 
#### :icon-chevron-right: Model is low quality.
- <u>**A bad model:**</u>       

   - Sounds scratchy/screechy.
   - Has a muffled sound.
   - Sounds inaccurate to the source.
   - Is incapable of hitting certain notes.
   - Has slurred speech.
   - Is unable of pronouncing words correctly in its intended language.
   - Has <u>[artifacting](https://docs.ai-hub.wtf/rvc/resources/artifacting/)</u>.
   - Has noise.
***
###### ‎ 
#### :icon-chevron-right: An outdated extraction method was used.
{.list-icon}
- :icon-check-circle: Only **Mangio-Crepe** & **RMVPE** are allowed. Learn about them <u>[here](https://docs.ai-hub.wtf/rvc/resources/inference-settings/#pitch-extraction-algorithm)</u>

- :icon-x-circle: Harvest, Dio, Crepe-Tiny, PM, etc. are obsolete.

***
###### ‎ 
#### :icon-chevron-right: The audio demo contains instrumental.
- Don't include **ANY** music in the audio demo, even if it's not copyrighted. This is due to:
  
     - Concerns over copyright.
     - In many cases, the music can "hide" the flaws of the voice model, making it harder to judge its quality.
***
#### :icon-chevron-right: The audio demo is altered.
- Don't add reverb, equalize, or alter the demo in any way, as it won't be a faithful representation of the model. It must be the raw, unmodified output from the inference.

- Trimming silences at the beginning/end of the audio demo is allowed. :icon-check-circle: 
###### ‎  
***
#### :icon-chevron-right: Is a robotic or non-human voice.
- Robotic, sound effect and drum models will also be rejected, because with these types of voices it is difficult to determine if you know how to clean a dataset properly.

- However once you get model maker you will be able to post robotic, sound effect or drum models.
###### ‎  
***
###### ‎
#### Step 3: Prepare the submission.
- Once your model is ready, head over to the **#model-maker-role** channel.  

- Click the `Submit Model` button.    

<img src="../modelmaker-img/1.png" alt="image" width="600" height="auto">‎               
‎     
:::content-center
#### ``Now fill up the information about your model:``  
:::

**model-name**
:     Its name.   

**technology**
:     The technology used for its training.

**extraction**
:     The <u>[extraction method](https://docs.ai-hub.wtf/rvc/resources/inference-settings/#pitch-extraction-algorithm)</u> you used.

**epochs**
:     Total <u>[epochs](https://docs.ai-hub.wtf/rvc/resources/epochs--tensorboard/)</u> amount.

**link**
:     Its download link from Hugging Face or Weights. 

**demo**
:     An audio sample of it talking/singing.

**note** 
:   Optional. Add more context about the model if you want.

***
!!!success 
You can attach more samples when you repost the model to ``#voice-models``.
!!!
***
###### ‎
#### Step 4: Send submission.
- Once you are done filling the information it will send your model to get QCed   

   <img src="../modelmaker-img/submitted.png" alt="image" width="" height="auto">‎ 
‎     
- Now, wait for a **QC** (quality checker) to verify your model. You'll be notified once it has been reviewed.

- If you made a mistake in your submission or you want to change something you can cancel your submission by clicking on the cancel button that is attatched to the message you get when you send a submission.

  <img src="../modelmaker-img/2.png" alt="image" width="600">‎


- If your model gets approved, the bot will notify you with a message like this:    

   <img src="../modelmaker-img/approved.png" alt="image" width="" height="auto">‎     
‎    
- You can then repost the model (& future models) to the ``#voice-models`` forum.

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/contributions/)
:::
