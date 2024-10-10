---
icon: chevron-right
order: 2000
---

``Last update: Mar 8, 2024``   
 
***
###### ‎ 
:::content-center
## Introduction ‎ :icon-book:
:::   
- Mangio RVC is a <u>[fork</u>](https://docs.ai-hub.wtf/essentials/whats-rvc/#forks) of RVC, [Mangio621](https://github.com/Mangio621), [Kalomaze](https://github.com/kalomaze), & [Alexolotl](https://github.com/alexlnkp)

- Considered one of the best forks out there. Mainly because of it's extra features, inclusion of <u>[Mangio-Crepe](https://docs.ai-hub.wtf/rvc/resources/inference-settings/#pitch-extraction-algorithm)</u>, & its stability.

- The project nowadays is a little abandoned, so don't expect many updates from the developers soon, unfortunately.     

‎           
#### Pros & Cons :icon-tasklist:
==- ***Unfold***
!!! *The pros & cons are subjective to your necessities.*       
!!!

||| ✔️ **PROS** 
- Easy to install.      
- Includes Mangio-Crepe algorithm.        
- Nicer UI.       
- More features than <u>[Mainline</u>](https://docs.ai-hub.wtf/rvc/local/mainline/).        
- Has hybrid training.        
- Lighter storage-wise if you install the <u>[inference</u>](https://docs.ai-hub.wtf/extra/glossary/#inference)</u>)-only version.
||| ❌ **CONS** 
- A little slower than Mainline, since it's more bloated.     
- Will likely remain with no updates for a long time.      
- Manual model upload.
||| 
===
***
###### ‎   
###### ‎   
:::content-center
## Installing & Opening :icon-download:
:::
###### ‎   

1. For exclusively <u>[**inferencing**](https://docs.ai-hub.wtf/extra/glossary/#inference)</u>, click <u>[here</u>](https://huggingface.co/MangioRVC/Mangio-RVC-Huggingface/resolve/main/Mangio-RVC-v23.7.0_INFER.7z).      
    For both inferencing **& training**, click <u>[here</u>](https://huggingface.co/MangioRVC/Mangio-RVC-Huggingface/resolve/main/Mangio-RVC-v23.7.0_INFER_TRAIN.7z).     

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
5. **(Optional)** To access RVC more easily, make a shortcut of the ``go-web`` file. 

!!!warning Don't close the console until you're done using RVC, or it will stop working.        
!!! 
***
###### ‎      
###### ‎       
:::content-center
## Inference :icon-unmute:
###### ‎       
!!!success
If you encounter an issue, be sure to read the <u>[Troubleshooting](https://docs.ai-hub.wtf/rvc/local/mangio/#troubleshooting-)</u> chapter.
!!!
:::
###### ‎    
#### 1. Upload voice model.
a. Open Mangio's folder & put your model's <u>[**.PTH**](https://docs.ai-hub.wtf/essentials/voice-models/#voice-model-files)</u> file inside the `weights` folder.

    <img src="../mangio-img/g.png" alt="image" width="500" height="auto"> 
###### ‎       
b. Put the model's **.INDEX** file in the `logs` folder.

    <img src="../mangio-img/h.png" alt="image" width="500" height="auto"> 
***
###### ‎  
#### 2. Select voice model.
a. In RVC, click the upper ``Refresh voice list`` button.

    <img src="../mangio-img/1.png" alt="image" width="400" height="auto">     
    
‎   
b. In its left, click `Inferencing voice` & select your model.

    <img src="../mangio-img/b.png" alt="image" width="400" height="auto">    

***
###### ‎  
#### 3. Select vocals.       
In ``Specify path to an audio file`` paste the <u>[path file</u>](https://static1.howtogeekimages.com/wordpress/wp-content/uploads/2023/09/shift-right-click-copy-as-path.png?q=50&fit=crop&w=767&dpr=1.5) of your audio.        

<img src="../mangio-img/2.png" alt="image" width="400" height="auto"> 

‎       

!!!
If there are multiple audios in said path, click `Select audio path from the dropdown` & select the one you want.
!!!
***
###### ‎  
#### 4. Modify settings. (optional)      
If you wish, modify the <u>[inference settings](https://docs.ai-hub.wtf/rvc/resources/inference-settings/)</u> on display accordingly for better results.
***
###### ‎  
#### 5. Convert.
Click the long ``Convert`` button at the bottom & it will begin to convert.     
 
The processing time will mainly depend on your specs, length of audio, & the algorithm picked.
***
###### ‎  
#### 6. Locate the output.
Once it's done processing, a playable audio will pop up in the `Export audio` box.      
Your output audios will be located in Mangio's `audio-outputs` folder.

<img src="../mangio-img/a.png" alt="image" width="" height="auto"> 

***
###### ‎     
###### ‎      
:::content-center
## Training :icon-dependabot:
###### ‎     
!!!warning <u> NOTES: </u>
The training guide will be centered around using <u>[TensorBoard](https://docs.ai-hub.wtf/rvc/resources/epochs--tensorboard/#tensorboard)</u>. Read about it first if you haven't already.      

If you encounter an issue, be sure to read the <u>[Troubleshooting](https://docs.ai-hub.wtf/rvc/local/mangio/#troubleshooting-)</u> chapter.
!!!
:::
###### ‎    
###### ‎    
:::content-center
### <u> Step 1 </u>
:::
###### ‎   
#### 1. Go to training area.
Open RVC & head over to the `Train` tab.          

<img src="../mangio-img/4.png" alt="image" width="" height="auto">   

***
###### ‎  
#### 2. Name the model.
In `Enter the experiment name` you insert a name for your model. Don't include special characters or spaces.     

<img src="../mangio-img/5.png" alt="image" width="300" height="auto">    

***

###### ‎  
#### 3. Select Target Sample Rate.
In `Target sample rate` select the number that matches your dataset's [<u>sample rate</u>](https://docs.ai-hub.wtf/rvc/resources/datasets/#sample-rate).        
Inputting an incorrect one might screw up the final quality.

<img src="../mangio-img/6.png" alt="image" width="" height="auto">         

***
###### ‎       
:::content-center
### <u>Step 2a</u>
:::
###### ‎     
#### 4. Select dataset.
Open Mangio's folder, go to `datasets` folder & move your dataset there.      

<img src="../mangio-img/c.png" alt="image" width="550" height="auto"> 

‎       
!!!warning *Once training is done, be sure to remove the dataset from there.*     
!!!
***
###### ‎  
#### 5. Process data.
Click the `Process Data` button on the center.      

RVC will process the previous criteria for the training.   
But also the dataset file, which might take a moment depending on how big it is.

<img src="../mangio-img/8.png" alt="image" width="370" height="auto"> 

‎       

It'll finish when the output box on the right says ``end preprocess``.

<img src="../mangio-img/17.png" alt="image" width="380" height="auto"> 

***
‎   
:::content-center
### <u>Step 2b</u>
:::
###### ‎  
#### 6. Select GPUs.
In `Enter the GPU index(es)` determine which GPU(s) you'll use for training, by indicating the index followed by the dash (e.g: `0`).

<img src="../mangio-img/9.png" alt="image" width="300" height="auto"> 

***
###### ‎  
#### 7. Select pitch extraction algorithm.
a. At the right select the <u>[**Pitch extraction algorithm**](https://docs.ai-hub.wtf/rvc/resources/inference-settings/#pitch-extraction-algorithm)</u>.       
Only use ``RMVPE``, ``Crepe`` or `Mangio-Crepe`, as the rest are obsolete.            

    <img src="../mangio-img/10.png" alt="image" width="270" height="auto"> 

    ###### ‎   
b. Now click the `Feature extraction` button on the right.    

    <img src="../mangio-img/11.png" alt="image" width="320" height="auto">‎        
    ‎      
    ‎   
    It'll finish when the output says ``all-feature-done``.

    <img src="../mangio-img/18.png" alt="image" width="320" height="auto">  

***
###### ‎  
#### 8. Create .INDEX file.
Now click the `Train feature index` button on the bottom.         
This will create the <u>[.INDEX</u>](https://docs.ai-hub.wtf/essentials/voice-models/#voice-model-files) file.       

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
#### 9. Select save frequency.
Frequency of the <u>[saving checkpoints](https://docs.ai-hub.wtf/extra/glossary/#checkpoints)</u>, based on the <u>[epochs](https://docs.ai-hub.wtf/rvc/resources/epochs--tensorboard/)</u>.       

If you are a newbie, simply leave it at `15`.    
    
E.g: with a value of ``10``, they will be saved after the epoch 10, 20, 30, etc.              
‎   

<img src="../mangio-img/12.png" alt="image" width="250" height="auto"> 

***
###### ‎  
#### 10. Input epochs amount.
In `Total training epochs` you determine the total amount of <u>[epochs](https://docs.ai-hub.wtf/rvc/resources/epochs--tensorboard/)</u> (training cycles) for the model.     

But since we'll use <u>[TensorBoard](https://docs.ai-hub.wtf/rvc/resources/epochs--tensorboard/#tensorboard)</u>, use an arbitrarily large value like `2000`.


<img src="../mangio-img/13.png" alt="image" width="250" height="auto">

***
###### ‎  
#### 11. Select batch size.
Leave `Batch size per GPU` at `8` if you aren't familiar with it.
  
If your dataset is short (around 2 minutes or less), use ``4`` instead.


<img src="../mangio-img/14.png" alt="image" width="250" height="auto"> 

***
###### ‎  
#### 12. Launch TensorBoard.
Now before you start training, open TB.     

If you haven't already, start reading about it here <u><u>[here</u>](https://docs.ai-hub.wtf/rvc/resources/epochs--tensorboard/#tensorboard)</u>.
***
###### ‎  
#### 13. Begin training.
Start training the model by clicking `Train model`.

<img src="../mangio-img/16.png" alt="image" width="290" height="auto"> 

‎ 
‎ 

Remember to monitor TB, & also the console just in case.    
The latter will show you errors if they happen, and information about the epochs & checkpoints.happen.       
‎   
<img src="../mainline-img/j.png" alt="image" width="550" height="auto"> 

***
###### ‎  
#### 14. Stop training.
When you are very sure of overtraining, you can stop training by pressing the `Stop training` button where `Train model` used to be. 

<img src="../mangio-img/d.png" alt="image" width="290" height="auto"> 

***
###### ‎      
#### 15. Gather model's files.
a. Create a new folder anywhere named as your model.

a. Open RVC's folder, go to ``logs``, and open the folder named with the model.       
Select the `.INDEX` named ``added_`` & move it to your newly made folder.

    <img src="../mangio-img/e.png" alt="image" width="470" height="auto"> 

    ‎       
c. Now go to the ``weights`` folder. Here you'll find the model's checkpoints.         

    Select the one **closest** to ***before*** the overtraining point, and move it to the new folder      

    These files will be organized with this format: **ModelName_Epoch_Step.pth** 

    Example: ``kalomaze_e60_s120.pth``

    <img src="../mangio-img/f.png" alt="image" width="500" height="auto">‎ 
    ‎      

    And that's all. Have fun with your model.   
    To test the model, do a normal <u>[inference</u>](https://docs.ai-hub.wtf/essentials/how-to-make-ai-cover/) as usual.
***
###### ‎   
:::content-center
### <u>Resuming</u> :icon-sync:
:::
###### ‎       
If the training finished but the model still needed training, you don't have to start from scratch.       
**Follow this procedure:**

- Simply enter the **same settings and criteria** that you previously inserted. Model name, sample rate, dataset, batch size, etc. You don't have to press ``Process Data`` or train the .INDEX again.

- You can change the **save frequency**, or increase the **epochs** amount in case you didn't input enough before.

- Begin training again & remember to monitor TB & console like before.
***
###### ‎   
###### ‎ 
:::content-center
## Troubleshooting :icon-tools:
:::
###### ‎ 
==- *There's no option for my sample rate.*
###### ‎   

- **If it's lower than <u>32k**</u>: select ``32k``.       
‎   
- **If it's <u>44.1k**</u>: select ``40k``.   
‎   
- **If i'ts higher than <u>48k</u>**: select ``48k``.

===

==- *The voice glitches out.*
###### ‎   
- This a phenomenon called artifacting. To fix it, read <u>[here](https://docs.ai-hub.wtf/rvc/resources/artifacting/)</u>.

===

==- *I couldn't find my answer.*
###### ‎   
- Report your issue <u>[here](https://docs.ai-hub.wtf/rvc/#contributions)</u>.
===

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/rvc/#contributions)
:::