---
icon: chevron-right
order: 5000
---

``Last update: Apr 01, 2024``

***
:::content-center
<img src="..\applio-img\banner.png" alt="image" width="600">

:::

###### ‎
:::content-center
## Introduction ‎
:::
- Applio is a VITS-based Voice Conversion Tool developed by the <u>[IA Hispano</u>](https://github.com/IAHispano)</u> team.

- It's liked for its great **UI** & **lots** of extra features, such as TTS (with RVC models too), plugins, automatic model upload, customizable theme & more.

- Because of its user-friendly experience & active development, it's considered to be one of the best forks.     

- It also has a <u>[cloud version](https://colab.research.google.com/github/iahispano/applio/blob/master/assets/Applio.ipynb)</u>, in case you don't meet the <u>[requirements](https://docs.aihub.wtf/essentials/whats-rvc/#what-are-the-requirements-for-rvc-locally/)</u> to run it locally.     
‎      
#### Pros & Cons :icon-tasklist:
==- *Learn more*
!!! *The pros & cons are subjective to your necessities.*        
!!! 
||| ✔️ **PROS** 
- Very complete
- Has an active development
- Currently stable
- Very fast
- TTS features            
- Automatic model upload
- Has Mangio-Crepe
- User-friendly UI
- TensorBoard included
- Extra features, (plugins, model fusion, etc)
||| ❌ **CONS** 
- Issues when downloading to external drives
|||
===
***
###### ‎
:::content-center
## Download :icon-download:
:::
###### ‎
!!!warning Before Downloading:
- Make sure that you place Applio inside a folder on C drive.
- Don't put it in a folder with privileged access.
- Don't run the run-install.bat as an administrator.
- Make sure the path does not contain any spaces or special characters.
- Deactivate your antivirus and firewall to avoid missing dependencies.
!!!
***
1. The easiest way to download Applio is by going to Applio's <u>[Hugging Face repo](https://huggingface.co/IAHispano/Applio/tree/main/Compiled)</u>, and clicking the [ :icon-download: **download** ] button on the right-hand side.

    <img src="..\applio-img\2-localappliodl.png" alt="image" width="400">

***
2. Unzip the folder. It may take a few minutes.
***
3. Open Applio's folder & execute ``run-applio.bat``.

    <img src="..\applio-img\2-run-applio.png" alt="image" width="250">‎    
‎       
- A console tab will appear, and after a moment your default browser, with Applio ready to use.     
‎       
!!!warning Don't close the console until you're done using it, or it will stop working.     
!!! 
***
###### ‎       
###### ‎   
:::content-center
## Inference :icon-unmute:   
!!!success
If you encounter an issue, be sure to read the <u>[Troubleshooting](https://docs.aihub.wtf/rvc/local/mainline/#troubleshooting-)</u> chapter.
!!!
:::
###### ‎  
###### ‎   
#### 1. Upload voice model.
- Go to the **Download** tab.       
You have two ways of uploading it: through <u>[**its link**](https://docs.aihub.wtf/essentials/voice-models/#how-to-search-voice-models)</u> or **manually** inputting its files.

    +++ Link
    a. Go to the **Download** tab & paste the link of the model in the `Model Link` bar. It must be from Hugging Face or Google Drive.        
    ‎       
    <img src="..\applio-img\3-download-model.png" alt="image" width="500">    
    ‎       
    b. Press ``Download Model``.
    +++ Manually

    a. Drag & drop the model's .PTH in the **Drop files** box below.    
    ‎       
    <img src="..\applio-img\3-modelupload.png" alt="image" width="800">       
    ‎           
    b. Then drag the .INDEX.
    +++ 

‎  
#### 2. Select voice model.
a. Return to the **Inference** tab & click the ``Refresh`` button on the right.

    <img src="..\applio-img\3-refresh.png" alt="image" width="500">   


    ‎       
b. Select your model in the ``Voice Model`` dropdown.

    <img src="..\applio-img\3-voice-model.png" alt="image" width="500">   

  ***
###### ‎  
#### 3. Input vocals.      
- With Applio you can convert audios individually or in batches:
    +++ Single file
    a. Drag & drop the audio or click the upload box to search it.      
    ‎   
        <img src="..\applio-img/3-upload.png" alt="image" width="600">   
    ‎   
    b. Then select it in the dropdown below.      
    ‎   
        <img src="..\applio-img/3-select-audio.png" alt="image" width="400">   

    +++ In batches
    a. Go to the **Batch** tab.     
    ‎
        <img src="..\applio-img/batchupload.png" alt="image" width="400">    
    
    b. In the `Input Folder` bar, paste the path folder containing the audios.

        In `Output Folder` you can paste a path folder for the results.        
  
        Ensure the paths don't contain spaces/special characters.      
    +++

‎  
#### 4. Modify settings. (optional)      
-  Unfold `Advanced Settings` if you wish to modify the <u>[inference settings](https://docs.aihub.wtf/rvc/resources/inference-settings/)</u> for better results, or to determine the output folder.

    <img src="..\applio-img/3-advanced.png" alt="image" width="600">‎   
***

###### ‎  
#### 5. Convert.
a. Click ``Convert`` at the bottom. The audio will begin to process.       
The processing time will mainly depend on your specs, length of audio & the algorithm picked.

b. Once it's done, you can hear the results in the **Export Audio** box below.

    By default the output files will be in the "**audios**" folder: ``\ApplioV3.0.7\assets\audios``
***
###### ‎     
###### ‎  
:::content-center
## Training :icon-dependabot:
###### ‎   
!!!warning
The training guide will be centered around using <u>[TensorBoard](https://docs.aihub.wtf/rvc/resources/epochs--tensorboard/#tensorboard)</u>. Read about it first if you haven't already.      
If you encounter an issue, be sure to read the <u>[Troubleshooting](https://docs.aihub.wtf/rvc/local/mainline/#troubleshooting-)</u> chapter.
!!!
:::
###### ‎     
:::content-center
:::
==- 1. PREPROCESS
###### ‎      
##### a. Model Name
###### ‎    
- Go to the `Train` tab. Input a name for your model in `Model Name`.       
Don't include spaces/special characters.     

    <img src="..\applio-img\4-modelname.png" alt="image" width="550">‎     

***
###### ‎     
##### b. Dataset Path
###### ‎    
- Paste the path file of your dataset in the **Dataset Path** bar. Ensure the path doesn't contain spaces/special characters.

    <img src="..\applio-img\4-datasetpath.png" alt="image" width="550">‎  

***
###### ‎     
##### c. Sampling Rate
###### ‎    
- Select your dataset's sample rate. If you don't know the amount, click <u>[here](https://docs.aihub.wtf/rvc/local/applio/#extra)</u>.

    <img src="..\applio-img\4-samplerate.png" alt="image" width="300">‎  

***
###### ‎     
##### d. Preprocess Dataset
###### ‎    
- Ensure **RVC Version** is set as `V2` & click `Preprocess Dataset`.       

    It'll finish when the output box says `preprocessed successfully`.

    <img src="..\applio-img\4-preprocessdone.png" alt="image" width="700">

===

==- 2. EXTRACT
###### ‎    
##### a. Pitch extraction algorithm
###### ‎  
- Select the <u>[algorithm](https://docs.aihub.wtf/rvc/resources/inference-settings/#pitch-extraction-algorithm)</u> you want. Use either ``Crepe`` or ``RMVPE``, as the rest are outdated.

    <img src="..\applio-img\4-f0.png" alt="image" width="400">

***
###### ‎  
##### b. Hop Length (optional)
###### ‎  
- If you chose ``Crepe``, you can modify its <u>[hop length](https://docs.aihub.wtf/rvc/resources/inference-settings/#mangio-crepe)</u>.

    <img src="..\applio-img\4-hoplength.png" alt="image" width="900">

***
###### ‎  
##### c. Extract Features
###### ‎  
- Press **Extract Features**.       
It'll finish when it says `extracted successfully`.

    <img src="..\applio-img\4-extractfinish.png" alt="image" width="350">

===

==- 3. TRAIN
###### ‎  
##### a. Batch Size
###### ‎  
- If you are a newbie, use `8`. But in case your dataset is short (around 2 minutes or less), use `4`.

    <img src="..\applio-img\4-batchsize.png" alt="image" width="350">

***
###### ‎  
##### b. Save Every Epoch
###### ‎  
- Frequency of the <u>[saving checkpoints](https://docs.aihub.wtf/extra/glossary/#checkpoints)</u>, based on the <u>[epochs](https://docs.aihub.wtf/rvc/resources/epochs--tensorboard/)</u>.      
‎   
- If you are a newbie, simply leave it at `15`.              

    <img src="..\applio-img\4-freq.png" alt="image" width="420">‎   
‎   
‎   
- E.g: with a value of ``10``, they will be saved after the epoch 10, 20, 30, etc.   
***
###### ‎  
##### c. Total Epoch
###### ‎  
- Input the total amount of <u>[epochs](https://docs.aihub.wtf/rvc/resources/epochs--tensorboard/)</u> (training cycles) for the model.     
‎   
- But since we'll use <u>[TensorBoard](https://docs.aihub.wtf/rvc/resources/epochs--tensorboard/#tensorboard)</u>, use an arbitrarily large value like `1000`

    <img src="..\applio-img\4-epoch.png" alt="image" width="420">‎   
***
###### ‎  
##### d. GPU Settings
###### ‎  
- If you have multiple GPUs, tick `GPU Settings` to use a specific one for the training.

   <img src="../applio-img/4-gpu.png" alt="image" width="440" height="auto">‎ 
***
###### ‎  
##### e. Generate Index
###### ‎  
- Click `Generate Index`. This will create the model's <u>[.INDEX](https://docs.aihub.wtf/essentials/voice-models/#voice-model-files)</u> file.
***
###### ‎  
##### f. Start Training
###### ‎  
- Press `Start Training` to begin the training process.     
‎   
- To open <u>[TB](https://docs.aihub.wtf/rvc/resources/epochs--tensorboard/#tensorboard)</u>, execute `run-tensorboard` in Applio's folder. Remember to monitor it, as well as the console just in case.           
‎   
- The latter will show you errors if they happen, and information about the epochs & checkpoints.   

    <img src="../mainline-img/j.png" alt="image" width="480" height="auto"> 

===

==- 4. FINAL STEP
###### ‎  
##### a. Stop training
###### ‎  
- When you're very sure of overtraining, you can stop training by going to the `Settings` tab & press `Restart Applio`.

    <img src="../applio-img/4-stoptrain.png" alt="image" width="715" height="auto"> ‎ 

***
###### ‎  
##### b. Get the INDEX
###### ‎  
i. Create a new folder anywhere named as the model.     
‎  
ii. Open Applio's folder, go to ``logs``, and open the folder named as the model.      
‎      
iii. Select the **.INDEX** named ``added_`` & move it to your newly made folder.    
‎       
   <img src="../applio-img/4-index.png" alt="image" width="400" height="auto">‎
 ‎    

***
###### ‎  
##### c. Get the PTH
###### ‎  
i. In said folder you'll also find all the <u>[checkpoints](https://docs.aihub.wtf/extra/glossary/#checkpoints)</u>.         
‎  
ii. Select the one **closest** to ***before*** the overtraining point, and move it to the new folder.

    The checkpoints will be organized with this format: **ModelName_Epoch_Step.pth**   
    Example: ``arianagrande_e60_s120.pth``

‎  
    ‎            
iii. And that's all, have fun with your model. To test it, do a normal <u>[inference</u>](https://docs.aihub.wtf/rvc/local/applio/#inference-) as usual.

===

==- 5. RESUMING
- In case the training finished but the model still needed training, you don't have to start from scratch.        
‎     
- Simply enter the **same settings & criteria** that you've previously inserted. You don't have to do the preprocess or train the .INDEX again.      
 ‎     
- You can change the **save frequency**, or increase the **Total Epoch** amount in case you didn't input enough before.      
 ‎     
- Begin training again & remember to monitor TB & console like before.
===

###### ‎  
###### ‎  
###### ‎  
:::content-center
## TTS
*`+ with any RVC model`*
:::
###### ‎  
- Applio is also known for having one TTS tool by default, with **plenty** of voices to choose for.

- You can also use it with **RVC models** & apply the <u>[inference settings](https://docs.aihub.wtf/rvc/resources/inference-settings/)</u> if you wish.

- Aditionally, you can download the **Eleven Labs** TTS <u>[plugin](https://docs.aihub.wtf/rvc/local/applio/#plugins)</u>.       
***
###### ‎  
#### <u>Instructions:</u>
1. Go to the **TTS** tab. 

   <img src="../applio-img/5-ttstab.png" alt="image" width="400" height="auto"> ‎ 

***   
###### ‎   

2. If you want to use an RVC model, <u>[download it](https://docs.aihub.wtf/rvc/local/applio/#1-upload-voice-model)</u>, go to **TTS**, click `Refresh` & select it in **Voice Model** & **Index File**.

   <img src="../applio-img/5-vm.png" alt="image" width="600" height="auto">‎    
‎             
- To modify the <u>[inference settings](https://docs.aihub.wtf/rvc/resources/inference-settings/)</u> or the output folder for the TTS/RVC audio, unfold `Advanced Settings`.

***
###### ‎      
3. In **TTS Voices** select the voice of your desired language, accent & gender.        

    In **Text to Synthesize** input your text. Then click `Convert`.

   <img src="../applio-img/5-voice.png" alt="image" width="500" height="auto">‎     
‎   
- If you are using an RVC model, select a voice that matches the model the most, to guarantee great results.   
***
###### ‎  
4. Once it's done, you'll be able to hear the result in the Export Audio box. By default, the output audio will be in the "**audios**" folder. < ``\ApplioV3.0.7\assets\audios`` >

   <img src="../applio-img/5-ttsoutput.png" alt="image" width="500" height="auto">‎   

***
###### ‎  
###### ‎  
:::content-center
## Extra
:::
###### ‎  
- Applio has an **Extra** menu, containing an **audio analyzer**, originally made by <u>[Ilaria](https://ko-fi.com/ilariaowo)</u>.

- Making it convenient for determining the **sample rate** of datasets when training models.

- It also contains the **model fusion** tool, ideal for advanced users.

***
###### ‎  
#### <u>Audio Analyzer:</u>
1. Go to the **Extra** tab & press the upload box to input your audio. Or simply drag & drop.      

   <img src="../applio-img/6-tab.png" alt="image" width="400" height="auto">‎   
***
###### ‎  
2. Once it's done uploading, click `Get information about the audio`.  

***
###### ‎  
3. In **Sampling rate** you'll see the audio's full sample rate. Use said value for training.

   <img src="../applio-img/6-samplerate.png" alt="image" width="470" height="auto">‎    
###### ‎    
!!!warning <u>WARNING:</u>   
If the frequencies don't reach the top of the spectrogram, see at which number peaks & multiply it by <U>**2**</u>.
!!!

###### ‎
{.list-icon}
- #### <u>Example:</u>
   <img src="../applio-img/6-double.png" alt="image" width="470" height="auto">‎       
‎
>Here it reached 20 kHz. **Doubling** it gives 40kHz. Therefore the ideal target sample rate would be ``40k`` 

***
###### ‎
###### ‎
:::content-center
## Plugins
:::
- Plugins are components that you can add to Applio, that add new features & enhance your experience. 

- These are made by the public, and are free & easy to install. 

- You can find them on their <u>[GitHub page](https://github.com/IAHispano/Applio-Plugins/tree/main)</u>. More will be added in the future.
***
###### ‎
#### <u>Installation:</u>
1. Access their GitHub page & click on the name of the plugin you want.

   <img src="../applio-img/7-repo.png" alt="image" width="470" height="auto">‎ 

***
###### ‎
2. Click on the ZIP file.

   <img src="../applio-img/7-zip.png" alt="image" width="470" height="auto">‎   
‎       
- Click on the download button on the right. This will download the ZIP file of the plugin.

   <img src="../applio-img/7-dl.png" alt="image" width="470" height="auto">‎ 
***
###### ‎
3. Open Applio & head over to the **Plugins** tab. Drag & drop the ZIP file to the upload box.

   <img src="../applio-img/7-plugins.png" alt="image" width="600" height="auto">‎   
‎       
- You will be able to see its installation process in the console.

   <img src="../applio-img/7-plugindl.png" alt="image" width="530" height="auto">‎ 
***
###### ‎
3. Go to the settings tab & click **Restart Applio** at the bottom. 
Then you'll be able to see the plugin in the **Plugins** tab.

   <img src="../applio-img/7-plugindled.png" alt="image" width="420" height="auto">‎ 

***
###### ‎
###### ‎
:::content-center
## Troubleshooting
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
- This a phenomenon called artifacting. To fix it, read <u>[here](https://docs.aihub.wtf/rvc/resources/artifacting/)</u>.

===

==- *I couldn't find my answer.*
###### ‎   
- Report your issue <u>[here](https://docs.aihub.wtf/rvc/#contributions)</u>.
===

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.wtf/rvc/#contributions)
:::