:::
*``Written by Julia``*    
*``A thanks to Poopmaster, Eddy, Raid, SimplCup for helping.``*   
``Last update: Jan 29, 2024``   
 
***
###### ‎ 
:::content-center
## Introduction 📜
:::   
- Mangio RVC is a [<u>fork</u>](https://aihubdocs.github.io/en/other/glossary/#fork) of RVC, made by Mangio621, Kalomaze, & Alex.

- Considered one of the best forks out there. Mainly because of it's extra features, inclusion of [<u>Mangio-Crepe</u>](https://aihubdocs.github.io/en/rvc-resources/inference-settings/#pitch-extraction-algorithm), & its stability.

- The project nowadays is a little abandoned, so don't expect many updates from the developers soon, unfortunately.     

‎           
### Pros & Cons :icon-tasklist:
==- ***Tap to unfold 👈***
!!! *Pros & cons are subjective to your level of experience & needs.*
You might disagree with some of the points.
!!!

||| **PROS** ✔️ 
{.list-icon}
:icon-plus: Easy to install.      
:icon-plus: Includes Mangio-Crepe algorithm.        
:icon-plus: Nicer UI.       
:icon-plus: More features than [<u>Mainline</u>](https://aihubdocs.github.io/en/rvc/local/mainline-rvc/).        
:icon-plus: Has hybrid training.        
:icon-plus: Lighter storage-wise if you install the [<u>inference</u>](https://aihubdocs.github.io/en/other/glossary/#inference)-only version.
||| **CONS** ❌
:icon-dash: A little slower than Mainline, since it's more bloated.     
:icon-dash: Will likely remain with no updates for a long time.      
:icon-dash: Manual model upload.
||| 
===
***
:::content-center
## How to Install & Open 📥
:::
‎   

1. For exclusively **inferencing**, click [<u>here</u>](https://huggingface.co/MangioRVC/Mangio-RVC-Huggingface/resolve/main/Mangio-RVC-v23.7.0_INFER.7z).      
    For both inferencing **& training**, click [<u>here</u>](https://huggingface.co/MangioRVC/Mangio-RVC-Huggingface/resolve/main/Mangio-RVC-v23.7.0_INFER_TRAIN.7z).     

2. Once it's done downloading, unzip the folder.

3. Open RVC's folder, find the "``go-web.bat``" file and execute it.        
    ‎       
    <img src="../mangio-img/k.png" alt="" width="600" height="auto">‎ 

    ‎       
    It will then open a console, & after a moment your default web browser with RVC ready to be used.
    ‎       
    ‎             
    <img src="../mangio-img/inferencetab.png" alt="image" width="500" height="auto">  
    ‎       
5. **(Optional)** To access RVC more easily, make a [<u>shortcut</u>](https://desitsupport4u.des.wa.gov/hc/en-us/articles/360000391674-Create-a-Desktop-Shortcut-for-a-File-or-Folder) of the ``go-web`` file. 

!!!warning <u> NOTES: </u>
Don't close the console until you are done using RVC, otherwise the app will stop working.  
Depending on your specs it might take longer to open.                
!!! 
***
:::content-center
###### ‎      
## How to do Inference 🗣️     
:::
###### ‎    
#### 1. <u>Upload voice model.</u>
a. Open Mangio's folder & put your model's [<u>**.PTH**</u>](https://aihubdocs.github.io/en/essentials/voice-models--how-to-search-them/#voice-model-files) file inside the `weights` folder.

    <img src="../mangio-img/g.png" alt="image" width="500" height="auto"> 
###### ‎       
b. Put the model's **.INDEX** file in the `logs` folder.

    <img src="../mangio-img/h.png" alt="image" width="500" height="auto"> 
***
###### ‎  
#### 2. <u>Select voice model.</u>
a. In RVC, click the upper ``Refresh voice list`` button.

    <img src="../mangio-img/1.png" alt="image" width="400" height="auto">     
    
‎   
b. In its left, click `Inferencing voice` & select your model.

    <img src="../mangio-img/b.png" alt="image" width="400" height="auto">    

***
###### ‎  
#### 3. <u>Select vocals.</u>       
In ``Specify path to an audio file`` paste the [<u>path file</u>](https://static1.howtogeekimages.com/wordpress/wp-content/uploads/2023/09/shift-right-click-copy-as-path.png?q=50&fit=crop&w=767&dpr=1.5) of your audio.        

<img src="../mangio-img/2.png" alt="image" width="400" height="auto"> 

‎       

!!!
If there are multiple audios in said path, click `Select audio path from the dropdown` & select the one you want.
!!!
***
###### ‎  
#### 4. <u>Modify settings.</u> (optional)      
If you wish, modify the [<u>inference settings</u>](https://aihubdocs.github.io/en/rvc-resources/inference-settings/) on display accordingly for better results.
***
###### ‎  
#### 5. <u>Convert.</u>
Click the long ``Convert`` button at the bottom & it will begin to convert.     
 
The processing time will mainly depend on your specs, length of audio, & the algorithm picked.
***
###### ‎  
#### 6. <u>Locate the output.</u>
Once it's done processing, a playable audio will pop up in the `Export audio` box.      
Your output audios will be located in Mangio's `audio-outputs` folder.

<img src="../mangio-img/a.png" alt="image" width="" height="auto"> 

###### ‎           
#### If the voice glitches out, click [<u>here</u>](https://aihubdocs.github.io/en/rvc-resources/artifacting--how-to-fix-it/).
***
###### ‎       
:::content-center
## How to Train 💾
:::
:::content-center
!!!warning <u> IMPORTANT NOTES: </u>
- For **AMD/Intel** users, it's best if you train through the cloud as these GPUs aren't compatible for AI training.        
[<u>RVC Disconnected</u>](https://aihubdocs.github.io/en/rvc/cloud/training/rvc-disconnected/) & [<u>Paperspace</u>](https://aihubdocs.github.io/en/rvc/cloud/paperspace/) are the best contenders.         

‎ ‎ • ‎ The training process will be centered around the **Tensorboard**.       
‎ ‎ ‎ ‎ ‎ ‎ If you don't know about it, give it a quick read [<u>here</u>](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard/).        
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

<img src="../mangio-img/4.png" alt="image" width="" height="auto"> 

***
###### ‎  
#### 2. <u>Name the model.</u>
In `Enter the experiment name` you insert a name for your model.     
Don't include special characters or spaces.       

<img src="../mangio-img/5.png" alt="image" width="340" height="auto"> 

***
###### ‎  
#### 3. <u>Select Target Sample Rate.</u>
In `Target sample rate` select the number that matches your datasets' [<u>sample rate</u>](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/#sample-rate).        
Inputting an incorrect one might screw up the final quality.

<img src="../mangio-img/6.png" alt="image" width="" height="auto"> 

‎       
!!!
‎ ‎ • ‎ *If your sample rate is **44.1k**:* select ``40k``.            

‎ ‎ • ‎ *If it's lower than **32k**:* select ``32k``.    
!!!
***
###### ‎       
:::content-center
### <u>Step 2a</u>
:::
###### ‎     
#### 4. <u>Select dataset.</u>
Open Mangio's folder, go to `datasets` folder & move your dataset there.      

<img src="../mangio-img/c.png" alt="image" width="550" height="auto"> 

‎       
!!!warning *Once training is done, be sure to remove the dataset from there.*     
That way next time you train there won't be two datasets conflicting.
!!!
***
###### ‎  
#### 5. <u>Process data.</u>
Click the `Process Data` button on the center.      

RVC will process the previous criteria for the training.   
But also the dataset file, which might take a moment depending on how big it is.

<img src="../mangio-img/8.png" alt="image" width="370" height="auto"> 

‎       

It'll finish when the output box on the right says ``end prepocess``.

<img src="../mangio-img/17.png" alt="image" width="380" height="auto"> 

‎    

!!!
RVC will also process the dataset file, which might take a moment depending on how big it is.
!!!
***
‎   
:::content-center
### <u>Step 2b</u>
:::
###### ‎  
#### 6. <u>Select GPUs.</u>
In `Enter the GPU index(es)` determine which GPU(s) you'll use for training, by indicating the index followed by the dash (e.g: `0`).

<img src="../mangio-img/9.png" alt="image" width="300" height="auto"> 

***
###### ‎  
#### 7. <u>Select pitch extraction algorithm.</u>
a. At the right select the [<u>Pitch extraction algorithm</u>](https://aihubdocs.github.io/en/rvc-resources/inference-settings/).       
Use either ``RMVPE``, ``Crepe``, or `Mangio-Crepe` according to your needs.            

    <img src="../mangio-img/10.png" alt="image" width="270" height="auto"> 

    ‎   
    !!! Only use one of the three, as the rest are obsolete.
    !!!
    ###### ‎   
b. Now click the `Feature extraction` button on the right.    

    <img src="../mangio-img/11.png" alt="image" width="320" height="auto">‎        
    ‎      
    ‎   
    It'll finish when the output says ``all-feature-done``.

    <img src="../mangio-img/18.png" alt="image" width="320" height="auto">  

***
###### ‎  
#### 8. <u>Create .INDEX file.</u>
Now click the `Feature extraction` button on the bottom.         
This will create the [<u>.INDEX</u>](https://aihubdocs.github.io/en/essentials/voice-models--how-to-search-them/#voice-model-files) file.       

<img src="../mangio-img/11.png" alt="image" width="280" height="auto"> 

‎       

It'll finish when the output box says `Successful index Construction`.

<img src="../mangio-img/i.png" alt="image" width="280" height="auto"> 

***
###### ‎     
:::content-center
### <u> Step 3 </u>
:::
###### ‎         
#### 9. <u>Select save frequency.</u>
In `Save frequency` you determine at how many [<u>epochs</u>](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard/) the model will saved at.       
If you are a newbie, leave it at `15`.      

Think of it as how often RVC will make a "saving checkpoint" file of your model.     
They're useful to resume training starting from where you left. You'll learn more later.                 
‎   

<img src="../mangio-img/12.png" alt="image" width="250" height="auto"> 

‎       

!!!secondary
Example. With a value of ``10``, RVC will save the model at every 10 epochs.
!!!
***
###### ‎  
#### 10. <u>Input epochs amount.</u>
In `Total training epochs` input the total amount of epochs (training cycles) used for the training.    

Though since we'll use a TensorBoard, using an arbitrarely large value like `2000` is probably enough, to avoid re-training.       

Learn more [<u>here</u>](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard/).     


<img src="../mangio-img/13.png" alt="image" width="250" height="auto">

***
###### ‎  
#### 11. <u>Select batch size.</u>
`Batch size per GPU` determines the amount of data that will be processed at once while training.

If you are a newbie leave it at ``8``.      
If your dataset is short, (around 2 minutes or less) use ``4`` instead.

<img src="../mangio-img/14.png" alt="image" width="250" height="auto"> 

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

<img src="../mangio-img/16.png" alt="image" width="290" height="auto"> 

***
###### ‎  
#### 14. <u>Stop training.</u> 
When you detect overtraining, stop training by clicking the `Stop training` button, located at the bottom.

<img src="../mangio-img/d.png" alt="image" width="290" height="auto"> 

***
###### ‎      
#### 15. <u>Gather model's files.</u>
a. Create a new folder anywhere named as your model.

a. Open RVC's folder, go to ``logs``, and open the folder named with the model.       
Select the `.INDEX` named ``added_`` & move it to your newly made folder.

    <img src="../mangio-img/e.png" alt="image" width="470" height="auto"> 

    ‎       
c. Now go to the ``weights`` folder. Here you'll find the "checkpoints", them being usable models.       

    Select the one **closest** to ***before*** the overtraining point, and move it to the new folder      

    These files will be organized with this format: **modelname_epochnumber_stepnumber.pth**   
Example: ``kalomaze_e60_s120.pth``

    <img src="../mangio-img/f.png" alt="image" width="500" height="auto">
‎      

And that's all. Have fun with your model.

To test the model, do a normal [<u>inference</u>](https://aihubdocs.github.io/en/essentials/how-to-make-ai-cover/) as usual.
    
If you were going for a model that hits low/high notes, screams, or other special sounds, ensure your audio sample includes them too.
***
###### ‎   
:::content-center
### <u>How To Re-Train</u>
:::
###### ‎       
If the model still needed some training, you don't have to train from scratch.       
Here's how you do it.

- Simply enter the **same settings and criteria** that you previously inserted.   
Model name, sample rate, dataset, batch size, etc.        

- If you have already done it before, you don't have to Process Data or train the .INDEX again.

- If you re-train because you didn't put enough epochs before, increase the total epochs.             
Inserting double the amount should be enough.

- Begin training again & remember to monitor  TB & console like before.
***
:::content-right
||| *Did I miss anything?*        
Send any feedback [<u>here</u>](https://forms.gle/5i6hTJRVkXRohvVF9) 👈
|||
:::
