*`Originally written by FDG`*       
*`Re-written by Julia`*  
``Last update: Jan 28, 2024``
***
###### ‎ 
:::content-center
## Requirements 📜
:::
######
:::content
#### Before proceeding, make sure you meet these requirements:
||| <u> REQUIREMENTS </u>
- Model's <u>[**.PTH**](https://aihubdocs.github.io/en/essentials/voice-models--how-to-search-them/#section-1)</u> file.        
- Model's [**.INDEX**](https://aihubdocs.github.io/en/essentials/voice-models--how-to-search-them/#section-1) file.      
- General information about the <u>[model](https://aihubdocs.github.io/en/essentials/how-to-make-an-rvc-voice-model/#what-is-a-voice-model).</u>
- General information about the training process.      
- A <u>[Hugging Face](https://aihubdocs.github.io/en/other/glossary/#hugging-face)</u> account.     
- At least 1 audio sample of the model **<u>WITH NO MUSIC</u>**.     
|||
:::

***
:::content-center
###### ‎ 
## What Will Reject Your Model ❌
:::
###### ‎
#### If your submission/model meets any of these points, it will get invalidated:   
###### ‎ 
#### :icon-chevron-right: <u>It lacks one of the two crucial files.</u>
- The `.ZIP` file must contain both the correct `.INDEX` file and its final `.PTH` file:       

   - The **.INDEX** must be the one named ``added_``.  
   - The **.PTH** shouldn't be the `D_` or `G_` ones, as these aren't usable models. 
***
#### :icon-chevron-right: <u>Model is low quality.</u>
- **A poorly trained model sounds:**       

   - Scratchy/screechy
   - Muffled
   - Inaccurate to the source
   - Incapable of hitting certain notes
   - With slurred speach
   - Unable of pronouncing words correctly in its intended language
   - Has [<u>artifacting</u>](https://aihubdocs.github.io/en/rvc-resources/artifacting--how-to-fix-it/)
***
#### :icon-chevron-right: <u>You used an outdated extraction method.</u>
{.list-icon}
- :icon-x-circle: **Don't** use obsolete ones like Harvest, Dio, Crepe-Tiny, PM, etc.         
- :icon-check-circle: Use one of the 3 main ones **Crepe, Mangio-Crepe**, or **RMVPE**. Learn more [<u>here</u>](https://aihubdocs.github.io/en/rvc-resources/inference-settings/#pitch-extraction-algorithm)
***
#### :icon-chevron-right: <u>The audio demo has an instrumental.</u>
- Due to concerns over copyright, do **NOT** include **ANY** music on the audio demo, even if it's not copywritten.
***
#### :icon-chevron-right: <u>The audio demo is altered.</u>
- Don't add <u>[reverb](https://aihubdocs.github.io/enther/glossary/#reverb)</u>, equalize, or alter the demo in any way, as that isn't a faithful representation of the model.     
- It must be the raw, unmodified output from [<u>RVC</u>](https://aihubdocs.github.io/en/essentials/how-to-make-an-rvc-voice-model/#what-is-rvc).              
- Trimming silences at the beginning or end of the audio is okay. ✔️
***
###### ‎
:::content-center
## Tutorial 📝
:::
###### ‎
#### Step 1: <u>Zip the model.</u>
Gather the **.PTH** & **.INDEX** file and [<u>zip</u>](https://support.microsoft.com/en-us/windows/zip-and-unzip-files-8d28fa72-f2f9-712f-67df-f80cf89fd4e5) them into a ``.ZIP`` file.         
It must be a **.ZIP** file, not .7ZIP or .RAR files.
***
###### ‎
#### Step 2: <u>Upload model to Hugging Face.</u>
The ZIP must be stored in Hugging Face in a **public** repo of `openrail` license.    

If you don't know how, click [<u>here</u>](https://aihubdocs.github.io/en/essentials/how-to-upload-models-to-hugging-face/).
***
###### ‎
#### Step 3: <u>Prepare the model submission.</u>
Once your model is ready, head over to the **#get-model-maker** channel.        
Type the `/submit` command of **QCBot** and click the command.       

<img src="../modelmaker-img/1.png" alt="image" width="800" height="auto">‎               
‎     
Now fill up the information about your model:  

1. **<u>modelname:</u>** The name of your model.   

2. **<u>rvc:</u>** The version of RVC it was trained on (will almost always be 2)          
3. **<u>extraction:</u>** The <u>[extraction method](https://aihubdocs.github.io/en/rvc-resources/inference-settings/#pitch-extraction-algorithm)</u> used for training.         
:icon-check-circle: Use **only** **Crepe**, **Mangio-Crepe**, or **RMVPE**.             
:icon-x-circle: Obsolete algorithms like Harvest & others are not permitted.         
4. **<u>epochs:</u>** Number of epochs the model was trained for.      
5. **<u>link:</u>** The model's download link from Hugging Face.      
6. **i<u>mage:</u>** An image of what your model represents (character/person).       
7. **<u>demo:</u>** An audio demo of your model speaking/singing (as explained earlier, **<u>no</u>** music/post-processing).     
   You can only attach 1 demo with the command. You can include more after the bot confirmation response.  
8. **<u>note:</u>** This is optional. Here you can include an additional note.
***
###### ‎
#### Step 4: <u>Send submission.</u>
Once you are done filling the information, send the message.    

If everything went fine, your submission will be added to the queue and the bot will send a confirmation message, containing your **submission ID**.    

<u>**With the ID you can:**</u>        
1. Check your submission's number in queue with the command ``/queue`` followed by the ID. (for example, ``/cancel 251``)        
2. Cancel your submission with the command ``/cancel`` followed by the ID.    
‎     

From here, you can wait for a **Model QC** (quality checker) to verify your model. You'll be notified once it has been reviewed.   
You can then re-post your model (and any future models) to the forum ``#voice-models``.

If your model gets approved, the bot will notify you with something like this:    

<img src="../modelmaker-img/2.png" alt="image" width="" height="auto">  

***
:::content-right
||| *Did I miss anything?*        
Send any feedback [<u>here</u>](https://forms.gle/5i6hTJRVkXRohvVF9) 👈
|||
:::
