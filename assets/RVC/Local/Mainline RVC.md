``Written by Julia``        
``Images by Poopmaster``    
``Last update: Jan 29, 2024``

***
###### ‎
:::content-center
## Introduction 📜
:::

- Mainline RVC is the base, original, & unmodified version of RVC. Made by the [<u>RVC-Project</u>](https://github.com/RVC-Project) team.

- It has less features compared to other [<u>forks</u>](https://aihubdocs.github.io/en/other/glossary/), but still has the necessary tools to do a decent job.

- It's specially liked because it's a little faster than other forks, as it's less bloated in a way. 

- Its actual name is not "Mainline", but it was given by the public to properly distinguish it from the other versions.     
‎       
### Pros & Cons :icon-tasklist:
==- ***Tap to unfold 👈***
!!! *The pros & cons are subjective to the level of experience and needs of the user.*
You might disagree with some of the points made.
!!!

||| **PROS** ✔️ 
{.list-icon}
:icon-plus: Easy to install.                   
:icon-plus: Simpler to use.     
:icon-plus: A bit faster compared w/ forks. 
||| **CONS** ❌
:icon-dash: Has less features.     
:icon-dash: No [<u>Mangio-Crepe</u>](https://aihubdocs.github.io/en/rvc-resources/inference-settings/#pitch-extraction-algorithm) algorithm.      
:icon-dash: Manual model upload.
||| 
===
***
###### ‎
:::content-center
## How to Install & Open 📥
:::
###### ‎
1.  For **NVIDIA** users, click [<u>here</u>](https://huggingface.co/lj1995/VoiceConversionWebUI/blob/main/RVC1006Nvidia.7z).        
    For **AMD**/**Intel** users, click [<u>here</u>](https://huggingface.co/lj1995/VoiceConversionWebUI/blob/main/RVC1006AMD_Intel.7z).       

3. Click the <u>``Download``</u> word. RVC will begin to download.      
    ‎       
    <img src="../mainline-img/4.png" alt="image" width="550" height="auto">       
    ‎   
3. Once it's done, unzip the folder.

4. Open RVC's folder, find the "``go-web.bat``" file and execute it.        
        ‎       
        <img src="../mainline-img/3.png" alt="image" width="550" height="auto">      
        ‎       
    It will then open a console, & after a moment your default web browser with RVC ready to be used.
    ‎       
    ‎             
    <img src="../mainline-img/inferencetab.png" alt="image" width="450" height="auto">‎   
    ‎       
5. **(Optional)** To access RVC more easily, make a [<u>shortcut</u>](https://desitsupport4u.des.wa.gov/hc/en-us/articles/360000391674-Create-a-Desktop-Shortcut-for-a-File-or-Folder) of the ``go-web`` file.      
‎       
!!! <u> NOTES: </u>
**Don't close the console** until you are done using RVC, or it will stop working.  
Depending on your specs it might take longer to open.                
!!! 
***
###### ‎       
:::content-center
## How to do Inference 🗣️    
:::
###### ‎   
#### 1. <u>Upload voice model.</u>
a. Open RVC's folder, go to the `assets` folder and put your model's [<u>**.PTH**</u>](https://aihubdocs.github.io/en/essentials/voice-models--how-to-search-them/#voice-model-files) file inside the `weights` folder.       
    ‎       
    <img src="../mainline-img/5.png" alt="image" width="520" height="auto">      
‎       
       
b. Return to the previous folder.       
Put the model's [<u>**.INDEX**</u>](https://aihubdocs.github.io/en/essentials/voice-models--how-to-search-them/#voice-model-files) file in the `logs` folder.

    <img src="../mainline-img/6.png" alt="image" width="520" height="auto"> 

***
###### ‎  
#### 2. <u>Select voice model.</u>
a. In RVC, click the ``Refresh voice list and index path`` button.

    <img src="../mainline-img/1.png" alt="image" width="400" height="auto"> 

    ‎       
b. In its left, click `Inferencing voice` & select your model.

    <img src="../mainline-img/7.png" alt="image" width="400" height="auto"> 

***
###### ‎  
#### 3. <u>Select vocals.</u>       
In ``Enter the path of the audio file`` paste the [<u>path file</u>](https://static1.howtogeekimages.com/wordpress/wp-content/uploads/2023/09/shift-right-click-copy-as-path.png?q=50&fit=crop&w=767&dpr=1.5) of your audio.

<img src="../mainline-img/8.png" alt="image" width="650" height="auto"> 

***
###### ‎  
#### 4. <u>Modify settings.</u> (optional)      
If you wish, modify the [<u>inferece settings</u>](https://aihubdocs.github.io/en/rvc-resources/inference-settings/) on display accordingly for better results.
***
###### ‎  
#### 5. <u>Convert.</u>
Click the long ``Convert`` button at the bottom & it will begin to convert.     
 
The processing time will mainly depend on your specs, length of audio, & the algorithm picked.
***
###### ‎  
#### 6. <u>Download output.</u>
Once it's done processing, a playable audio will pop up in the `Export audio` box.      
To download, click the three dots on the right & hit `Download`.

<img src="../mainline-img/9.png" alt="image" width="500" height="auto">‎        
           
#### If the voice glitches out, click [<u>here</u>](https://aihubdocs.github.io/en/rvc-resources/artifacting--how-to-fix-it/).

***
###### ‎     
:::content-center
## How to Train 💾
###### ‎   
!!!warning <u> IMPORTANT NOTES: </u>
- For **AMD/Intel** users, preferably train through the cloud as these GPUs aren't compatible for AI training. [<u>RVC Disconnected</u>](https://aihubdocs.github.io/en/rvc/cloud/training/rvc-disconnected/) & [<u>Paperspace</u>](https://aihubdocs.github.io/en/rvc/cloud/paperspace/) are the best contenders.          

‎ ‎ • ‎ The training process will be centered around the **Tensorboard**.       
‎ ‎ ‎ ‎ ‎ ‎ If you don't know about it, give it a quick read [<u>here</u>](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard/) first.        
!!!
:::
###### ‎     
:::content-center
### <u> Step 1 </u>
:::
###### ‎      
#### 1. <u>Go to training area.</u>
Open RVC & head over to the `Train` tab.      
Here's the section of RVC where you set up the training process.        

<img src="../mainline-img/10.png" alt="image" width="" height="auto">   

***
###### ‎  
#### 2. <u>Name the model.</u>
In `Enter the experiment name` you insert a name for your model.     
Don't include special characters or spaces.     


<img src="../mainline-img/11.png" alt="image" width="300" height="auto">    

‎       
!!!secondary
Example: `ArianaGrande2023` and not ``Ariana Grande 2023 >.< !``.
!!!
***
###### ‎  
#### 3. <u>Select Target Sample Rate.</u>
In `Target sample rate` select the number that matches your datasets' [<u>sample rate</u>](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/#sample-rate).        
Inputting an incorrect one might screw up the final quality.

<img src="../mainline-img/g.png" alt="image" width="" height="auto">         

‎       
!!!
- *If there's no ``32k`` option:* at the right in the `Version` sector, select `v1` & select `v2` again. Ensure to leave it as `v2`.

‎ ‎ ‎ • ‎ *If your sample rate is **44.1k**:* select ``40k``.            

‎ ‎ ‎ • ‎ *If it's lower than **32k**:* select ``32k``.   
!!!
***
###### ‎      
:::content-center
### <u> Step 2a </u>
:::
###### ‎  
#### 4. <u>Select dataset.</u>
In `Enter the path of the training folder` paste the [<u>path file</u>](https://static1.howtogeekimages.com/wordpress/wp-content/uploads/2023/09/shift-right-click-copy-as-path.png?q=50&fit=crop&w=767&dpr=1.5) of your dataset.

Ensure its folder name doesn't include special characters/spaces.

<img src="../mainline-img/13.png" alt="image" width="" height="auto">  

‎       

!!!secondary
If there's any text in the bar, delete it beforehand.
!!!
***
###### ‎  
#### 5. <u>Process data.</u>
Click the `Process Data` button on the center.      

RVC will process the previous criteria for the training.   
But also the dataset file, which might take a moment depending on how big it is.

<img src="../mainline-img/14.png" alt="image" width="450" height="auto">  

‎       

It'll finish when the output box on the right says ``end prepocess``.

<img src="../mainline-img/a.png" alt="testijg" width="" height="auto">  

***
###### ‎     
:::content-center
### <u> Step 2b </u>
:::
###### ‎     
#### 6. <u>Select GPUs.</u>
In `Enter the GPU index(es)` determine which GPU(s) you'll use for training, by indicating the index followed by the dash (e.g: `0`).

<img src="../mainline-img/15.png" alt="image" width="" height="auto">  

***
###### ‎  
#### 7. <u>Select pitch extraction algorithm.</u>
a. At the right select the `Pitch extraction algorithm`.       
Use either ``RMVPE_GPU`` or ``Crepe``, according to your needs.            

    Learn more [<u>here</u>](https://aihubdocs.github.io/en/rvc-resources/inference-settings/).

    <img src="../mainline-img/16.png" alt="image" width="" height="auto"> ‎      

    !!! Only use one of the two, as the other algorithms are obsolete.
    !!! 
###### ‎   
b. Now click the `Feature extraction` button on the right.    

    <img src="../mainline-img/17.png" alt="image" width="370" height="auto">‎        
    ‎      
    ‎   
    It'll finish when the output says ``all-feature-done``.

    <img src="../mainline-img/b.png" alt="image" width="320" height="auto">  

***
###### ‎  
#### 8. <u>Create .INDEX.</u>
Press `Train feature index` at the bottom center.       
This will create the [<u>.INDEX</u>](https://aihubdocs.github.io/en/essentials/voice-models--how-to-search-them/#voice-model-files) file.

<img src="../mainline-img/i.png" alt="image" width="250" height="auto">‎     
‎       
It'll finish when the outbot box says something like this:

<img src="../mainline-img/h.png" alt="image" width="270" height="auto"> 

***
###### ‎     
:::content-center
### <u> Step 3 </u>
:::
###### ‎           
#### 9. <u>Select save frequency.</u>
In `Save frequency` you determine at how many [*<u>epochs</u>*](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard/) the model will saved at.       
If you are a newbie, leave it at `15`.      

- Think of it as how often RVC will make a "saving checkpoint" file of your model.     
- They're useful to resume training starting from where you left. You'll learn more later.          
- Example: with a value of ``10``, RVC will save the model at every 10 epochs (10, 20, 30, etc.)      

‎   
<img src="../mainline-img/18.png" alt="image" width="" height="auto">

***
###### ‎  
#### 10. <u>Input epochs amount.</u>
In `Total training epochs` you determine the total amount of epochs (training cycles) for training.     

But since we'll use TensorBoard, using an arbitrarely large value like `2000` is probably enough, to avoid re-training.

Learn more [<u>here</u>](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard/).

<img src="../mainline-img/19.png" alt="image" width="" height="auto">  

***
###### ‎  
#### 11. <u>Select batch size.</u>
`Batch size per GPU` determines the amount of data that will be processed at once while training.       

If you are a newbie leave it at ``8``.      
If your dataset is short (around 2 minutes or less), use ``4`` instead.

<img src="../mainline-img/20.png" alt="image" width="" height="auto">  

***
###### ‎  
#### 12. <u>Launch TensorBoard.</u>
Now before you start training, open  TB.     

If you havent already, start reading [<u>here</u>](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard/).
***
###### ‎  
#### 13. <u>Begin training.</u>
Start training the model by clicking `Train model`.

Be sure to keep an eye on  TB & the console.

<img src="../mainline-img/21.png" alt="image" width="250" height="auto">  

***
###### ‎  
#### 14. <u>Stop training.</u> 
Once you detect overtraining, stop training by pressing the `Stop training` button, located at the bottom, where `Train model` used to be.

***
###### ‎  
#### 15. <u>Gather model's files.</u>
a. Create a new folder anywhere named as your model.

a. Open RVC's folder, go to ``logs``, and open the folder named with the model.       
Select the `.INDEX` named ``added_`` & move it to your newly made folder.

    <img src="../mainline-img/c.png" alt="image" width="" height="auto">  

‎   

c. Now go to the ``weights`` folder. Here you'll find the "checkpoints", them being usable models.       

    Select the one **closest** to ***before*** the overtraining point, and move it to the new folder      

    These files will be organized with this format: **modelname_epochnumber_stepnumber.pth**   
Example: ``kalomaze_e60_s120.pth``

    <img src="../mainline-img/d.png" alt="image" width="" height="auto"> ‎  
    ‎            

    And that's all. Have fun with your model.

    To test the model, do a normal [<u>inference</u>](https://aihubdocs.github.io/en/essentials/how-to-make-ai-cover/) as usual.
    
    If you were going for a model that hits low/high notes, screams, or other special sounds, ensure your audio sample includes them too.
***
###### ‎   
:::content-center
### <u>How to Re-Train</u>
:::
###### ‎   
If the model still needed some training, you don't have to train from scratch.       
Here's how you do it.

- Simply enter the **same settings and criteria** that you previously inserted.   
Model name, sample rate, dataset, batch size, etc.        

- If you have already done it before, you don't have to press ``Process Data`` or train the [<u>.INDEX</u>](https://aihubdocs.github.io/en/essentials/voice-models--how-to-search-them/#voice-model-files) again.

- If you re-train because you didn't put enough epochs before, increase the total epochs.             
Inserting double the amount should be enough.

- Begin training again & remember to monitor  TB & console like before.
***
:::content-right
||| *Did I miss anything?*        
Send any feedback [<u>here</u>](https://forms.gle/5i6hTJRVkXRohvVF9) 👈
|||
:::
