---
icon: chevron-right

order: 2000
---

``Last update: October 20, 2024``

***

:::content-center
## Introduction ‎
:::
To upload your Voice Models in the <u>[AI HUB Discord Server](https://discord.gg/aihub)</u>'s <u>[``#voice-models``](https://discord.com/channels/1159260121998827560/1175430844685484042)</u> forum channel, you need to pass a Quality Control (QC) check to be sure that you post good voice models.

***

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
- A Hugging Face or weights.com account.     
- At least 1 raw audio sample of the model **<u>WITH NO MUSIC</u>**.     
|||
:::


:::content-center
###### ‎ 
## Things to Avoid :icon-x:
##### ``These will disqualify your post``
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
   - Has <u>[artifacting](https://docs.aihub.gg/rvc/resources/dataset-isolation/#artifacts)</u>.
   - Has noise.
***
###### ‎ 
#### :icon-chevron-right: An outdated extraction method was used.
{.list-icon}
- :icon-check-circle: Only **Crepe** & **RMVPE** are allowed. Learn about them <u>[here](https://docs.aihub.gg/rvc/resources/inference-settings/#pitch-extraction-algorithm)</u>

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

:::content-center
###### ‎ 
## How to Submit
:::

#### Step 1: Prepare the submission.
- Once your model is ready, head over to the <u>[AI HUB](https://discord.gg/aihub)</u>'s <u>[`#model-maker-role`](https://discord.com/channels/1159260121998827560/1305524365810470963)</u> channel.  

- Click the `Submit Model` button.    

<img src="../modelmaker-img/submit-model-button.png" alt="Submit Model Button" width="600" height="auto">‎               
‎     
:::content-center
#### ``Now fill up the information about your model:``  
:::

**model-name**
:     Its name.   

**technology**
:     The technology used for its training:
      - RVC
      - GPT-SoVITS

**extraction**
:     The <u>[extraction method](https://docs.aihub.gg/rvc/resources/inference-settings/#pitch-extraction-algorithm)</u> you used:
      - RMVPE
      - Crepe
      - Mangio-Crepe (Obsolete)
      - Harvest (Obsolete)
      - PM (Obsolete)
      - DIO (Obsolete)

**vocoder**
:     The <u>[vocoder](http://docs.aihub.gg/rvc/resources/training/#vocoders)</u> you used:
      - HifiGan
      - RefineGan


**epochs**
:     Total <u>[epochs](https://docs.aihub.gg/rvc/resources/training/#tensorboard)</u> amount.

***

#### Step 2: Complete the submission.
- You will get a DM by **Wally** asking for you to Complete the Submission.

- Click the `Complete Submission` button.    

<img src="../modelmaker-img/complete-submission.png" alt="Complete Submission Button" width="600" height="auto">‎               
‎     
:::content-center
#### ``Now fill up the information about your model:``  
:::

**Embedder**
:     The <u>[Embedder Model](http://docs.aihub.gg/rvc/resources/inference-settings/#embedder-model)</u> you used:
      - ContentVec
      - Spin
      - SpinV2

**Pretrain**
:     The [Pretrain](http://docs.aihub.gg/rvc/resources/training/#pretrains) you used.

**Model Link**
:     Its download link from Hugging Face (right click and copy link the download icon of the model zip, for example https://huggingface.co/Nick088/TADC_Bubble/resolve/main/TADC_Bubble.zip?download=true) or Weights.

**Sample File**
:     An audio sample of it talking/singing.

**Additional Information** 
:   Optional. Add more context about the model if you want.

- Click the `Submit` button.

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
- Now, your model will be posted in ``#model-maker-submissions`` where other model makers will upvote or downvote your model reviewing it. After one week, the model maker submission will be accepted or rejected based on voting.


- If you made a mistake in your submission or you want to change something, you can try to contact staff or talk about in the ``#model-maker-role`` discussion.

- If your model gets approved, you can then repost the model (& future models) to the ``#voice-models`` forum.

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
