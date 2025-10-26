---
icon: chevron-right
order: 7000
---

``Last update: August 7, 2025``

***
:::content-center
<img src="..\appliocolab-img\banner.png" alt="image" width="600">

:::
:::content-center
## Introduction
:::
- This is a <u>[cloud-based](http://docs.aihub.gg/extra/glossary/#cloud-based)</u> alternative to run [Applio](https://docs.aihub.gg/rvc/local/applio/), RVC Fork, only for people who don't have a good PC GPU, via the <u>[Google Colab Service](http://docs.aihub.gg/extra/glossary/#google-colab)</u>. With a Web User Interface.

!!!danger Google Colab Service
**Check the <u>[Google Colab Glossary](http://docs.aihub.gg/extra/glossary/#google-colab)</u> for more info on Free Tier, Limits, Verification, Pricing and other things.**
!!!


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
- Has (not Mangio) Crepe
- User-friendly UI
- TensorBoard included
- Extra features: (plugins, model fusion, etc)
||| ❌ **CONS** 
- Usage limit for free users
||| 
===
***
###### ‎
:::content-center
## Setting Up :icon-download:
:::
###### ‎
1. Access the Colab space <u>[here](https://colab.research.google.com/github/iahispano/applio/blob/master/assets/Applio.ipynb)</u>.
Then log in to your Google account.
***
###### ‎
2. Execute the **Install Applio** cells section. This will take around 2 minutes and will require you to grant permission to use Google Drive to save your models.

    <img src="..\appliocolab-img\install-applio-cell-section.png" alt="Install Applio Cell Section" width="400">
‎   
- It'll finish when you see a tick symbol on the left.

    <img src="..\appliocolab-img\finished-installation.png" alt="Finished Installation" width="400">‎     

***
###### ‎
3. Sync with Google Drive to automatically save or load models.

    <img src="..\appliocolab-img\sync-google-drive-cell.png" alt="Sync with Google Drive" width="500">‎     

***
###### ‎
4. Select a Sharing and Run the Server, using a tunnel that securely exposes the application running in your private cloud environment to the public internet. The notebook gives you 3 different services to do this. Choose one from the `method` dropdown menu in the code cell.

    - **Gradio (Fast, Popular, Reliable & Default)**
        - **How it works:** This is a built-in <u>[Gradio](http://docs.aihub.gg/extra/glossary/#gradio)</u> feature. It's one of the most straightforward method as it doesn't require any external accounts or tokens.
        - **Steps:**
            1. Select "Gradio" from the `method` dropdown menu.
            2. Run the cell. The public Gradio URL (ending in `gradio.live`) will be printed in the output once the server is ready. Click on it to access the UI.

    - **Ngrok (Fast, Popular & Reliable)**
        - **How it works:** Ngrok is a popular service that creates secure tunnels. It requires a free account and an authentication token. It has a 1GB Bandwidth Free Monthly Limit https://ngrok.com/docs/pricing-limits/free-plan-limits/.
        - **Steps:**
            1. Go to the [Ngrok Dashboard](https://dashboard.ngrok.com/get-started/your-authtoken) to get your free authtoken.
            2. In the notebook cell, paste your token into the `ngron_token` field.
            3. (Optional) To potentially reduce latency, select a geographical `Region` from the list of parameter options next to it, that is closest to you.
            4. Run the cell. The public Ngrok URL (ending in `ngrok.io`) will be printed in the output once the server is ready. Click on it to access the UI.

    - **LocalTunnel (No Account, Password Protected)**
        - **How it works:** LocalTunnel is another free service that doesn't require an account. For security, it generates a unique URL that is protected by a password.
        - **Steps:**
            1. Select "LocalTunnel" from the `method` codropdown menude.
            2. Run the cell.
            3. The output will display two key pieces of information: the public URL (ending in `loca.lt`) and a `Local Tunnel Password` below it.
            4. Click the URL. A new page will ask for a password.
            5. Copy the password from the notebook output and paste it into the password prompt in your browser to access the voice changer.


<img src="..\appliocolab-img\start-server-cell.png" alt="Start Serverl Cell" width="550">‎  

!!!warning Don't close Google Colab until you're done using it, or it will stop working.     
!!! 
***
###### ‎       
:::content-center
## Inference :icon-unmute:   
!!!success
Be sure to read the <u>[Troubleshooting](https://docs.aihub.gg/rvc/cloud/applio-colab/#troubleshooting)</u> chapter if any issue arises.
!!!
:::
###### ‎   
#### 1. Upload voice model.
- Go to the **Download** tab.       
You have two ways of uploading it: through <u>[**its link**](https://docs.aihub.gg/essentials/voice-models/#how-to-search-voice-models)</u> or **manually** inputting its files.

    +++ Link
    a. Go to the **Download** tab & paste the link in the `Model Link` bar.     
    It must be from Hugging Face or Google Drive.        
    ‎       
    <img src="..\appliocolab-img\3-download-model.png" alt="image" width="780">    
    ‎       
    b. Press ``Download Model``.
    +++ Manually

    a. Below in **Drop files**, press the upload box & input the model's .PTH.    
    ‎       
    <img src="..\appliocolab-img\3-modelupload.png" alt="image" width="800">       
    ‎           
    b. Then input the .INDEX.
    +++ 

‎  
#### 2. Select voice model.
a. Return to the **Inference** tab & click ``Refresh`` on the right.

    <img src="..\appliocolab-img\3-refresh.png" alt="image" width="500">   


    ‎       
b. Select the model in the ``Voice Model`` & `Index File` dropdown.

    <img src="..\appliocolab-img\3-voice-model.png" alt="image" width="500">   

  ***
###### ‎  
#### 3. Input vocals.      
- With Applio you can convert audios individually or in batches:
    +++ Single
    a. Press the upload box & input your audio.      
    ‎   
        <img src="..\appliocolab-img/3-upload.png" alt="image" width="600">‎      
    ‎       
    ‎   
    b. Then select it in the dropdown below.      
    ‎   
        <img src="..\appliocolab-img/3-select-audio.png" alt="image" width="400">   

    +++ Batch
    a. Go to the **Batch** tab.     
    ‎       
    <img src="..\appliocolab-img/3-batch-upload.png" alt="image" width="360">‎      
    ‎       
    b. Go to the file explorer in Colab. Go to ``drive``, right-click the folder containing the audios & click `Copy Path`.     
    
    c. Paste the path in the `Input Folder` bar.

    - In `Output Folder` you can define the path folder for the results.        
  
    - Ensure the paths don't contain spaces/special characters.      
    +++

‎  
#### 4. Modify settings. (optional)      
-  Unfold `Advanced Settings` if you wish to modify the <u>[inference settings](https://docs.aihub.gg/rvc/resources/inference-settings/)</u> for better results.

    <img src="..\appliocolab-img/3-advanced.png" alt="image" width="550">‎   
***

###### ‎  
#### 5. Convert.
a. Click ``Convert`` at the bottom to process the audio.       

b. Once it's done, you can hear the results in the **Export Audio** box below.      
To download it, press the download symbol on its right.

    <img src="..\appliocolab-img/3-output.png" alt="image" width="450">‎   

***
###### ‎     
###### ‎  
:::content-center
## Training :icon-dependabot:
###### ‎   
:::
:::content-center
:::
==- 1. PREPROCESS
###### ‎      
##### a. Model Name
###### ‎    
- Go to the `Train` tab. Input a name for your model in `Model Name`.       
Don't include spaces/special characters.     

    <img src="..\appliocolab-img\4-modelname.png" alt="image" width="550">‎     

***
###### ‎     
##### b. Dataset Path
###### ‎    
i. Upload your dataset to your GD storage if you haven't already.        
‎       
ii. In Colab click the folder on the left ( :icon-file-directory-fill: ) & click the reload button.     
‎       
   <img src="..\appliocolab-img\4-refresh.png" alt="image" width="220">‎    
‎   
    (For mobile users: tap the three lines on the top left & `Show file browser`)       
‎   
iii. Open `drive`, localize your dataset, right-click it & click `Copy path`, be sure it's only the path folder and not the file with the extension..     
‎   
    <img src="..\appliocolab-img\copy-path-drive-colab.png" alt="Copy the Google Drive Path from Google Colab" width="320">‎    
‎    
‎   
iv. Then paste it on the `Dataset Path` bar.       
‎     
    <img src="..\appliocolab-img\applio-gdrive-dataset-path.png" alt="Applio pasted Google Drive Dataset Path" width="550">‎  

***
###### ‎     
##### c. Sampling Rate
###### ‎    
- Select your dataset's sample rate. If you don't know the amount, click <u>[here](https://docs.aihub.gg/rvc/cloud/applio-colab/#extra)</u>.

    <img src="..\appliocolab-img\4-samplerate.png" alt="image" width="300">‎  

***
###### ‎     
##### d. Preprocess Dataset
###### ‎    
- Ensure **RVC Version** is set as `V2` & click `Preprocess Dataset`.       

    It'll finish when the output box says `preprocessed successfully`.

    <img src="..\appliocolab-img\4-preprocessdone.png" alt="image" width="700">

===

==- 2. EXTRACT
###### ‎    
##### a. Pitch extraction algorithm
###### ‎  
- Select the <u>[algorithm](https://docs.aihub.gg/rvc/resources/inference-settings/#pitch-extraction-algorithm)</u> you want. Use either ``Crepe`` or ``RMVPE``, as the rest are outdated.

    <img src="..\appliocolab-img\4-f0.png" alt="image" width="400">

***
###### ‎  
##### b. Extract Features
###### ‎  
- Press **Extract Features**.       
It'll finish when it says `extracted successfully`.

    <img src="..\appliocolab-img\4-extractfinish.png" alt="image" width="350">

===

==- 3. TRAIN
###### ‎  
##### a. Batch Size
###### ‎  
- If you are a newbie, use `8`. But in case your dataset is short (around 2 minutes or less), use `4`.

    <img src="..\appliocolab-img\4-batchsize.png" alt="image" width="350">

***
###### ‎  
##### b. Save Every Epoch
###### ‎  
- Frequency of the <u>[saving checkpoints](https://docs.aihub.gg/extra/glossary/#checkpoints)</u>, based on the <u>[epochs](https://docs.aihub.gg/rvc/resources/training/#epochs--overtraining)</u>.    
‎   
- If you are a newbie, simply leave it at `15`.              

    <img src="..\appliocolab-img\4-freq.png" alt="image" width="420">‎   
‎   
‎   
- E.g: with a value of ``10``, they will be saved after the epoch 10, 20, 30, etc.   
***
###### ‎  
##### c. Total Epoch
###### ‎  
- Input the total amount of <u>[epochs](https://docs.aihub.gg/rvc/resources/training/#tensorboard)</u> (training cycles) for the model.     
‎   
- But since we'll use <u>[TensorBoard](https://docs.aihub.gg/rvc/resources/training/#tensorboard)</u>, use an arbitrarily large value like `1000`

    <img src="..\appliocolab-img\4-epoch.png" alt="image" width="420">‎   

***
###### ‎  
##### d. Generate Index
###### ‎  
- Click `Generate Index`. This will create the model's <u>[.INDEX](https://docs.aihub.gg/essentials/voice-models/#voice-model-files)</u> file.
***
###### ‎  
##### e. Start Training
###### ‎  
i. Tick **Save Only Latest**

    <img src="..\appliocolab-img\4-savelatest.png" alt="image" width="240">‎    
‎       
‎   
ii.  Press `Start Training` below to begin the training process.     
‎   
    <img src="..\appliocolab-img\4-startraining.png" alt="image" width="520">‎   
***
###### ‎  
##### f. Monitor training 
###### ‎  
i. <u>[TB](https://docs.aihub.gg/rvc/resources/training/#tensorboard)</u> will be available in the Colab. Remember to monitor it, as well as the cell's logs just in case.             

    The latter will show you errors if they happen, and information about the epochs & checkpoints.   
‎  
    <img src="..\appliocolab-img\4-logs.png" alt="image" width="800">‎   
‎  
‎       
ii. If after around 2:30 hours of training you don't detect <u>[OT](https://docs.aihub.gg/rvc/resources/training/#usage-guide)</u> <u>[download the model](https://docs.aihub.gg/rvc/cloud/applio-colab/#c-get-the-pth)</u> of the lowest point, in case it's already OT, and the <u>[.INDEX](https://docs.aihub.gg/rvc/cloud/applio-colab/#b-get-the-index)</u>.     
‎    
iii. Then once your GPU runtime resets, begin the <u>[retraining](https://docs.aihub.gg/rvc/cloud/applio-colab/#5-resuming)</U> procedure.       
***
!!!warning While training, you might get disconnected if you:    
- <u>[Stay AFK](https://docs.google.com/document/d/1Pr-AZndodmWgsbOeuHQU4IrgbatFgYc1ChOq_ZAf_5s/edit?usp=sharing)</u> for a long time.     
- Disconnect from your Internet.       
- Don't solve the captchas that (might) pop up occasionally.    
- Run out of <u>[GPU runtime](https://docs.aihub.gg/rvc/extra/glossary/#google-colab)</u>. 
!!!
===

==- 4. DOWNLOAD
###### ‎  
##### a. Stop training
###### ‎  
- When you're very sure of overtraining, you can stop training by going to the **Settings** tab & press `Restart Applio`.

    <img src="../appliocolab-img/4-stoptrain.png" alt="image" width="715" height="auto"> ‎  
‎       
- Come back to the Colab & open the new public URL.

***
###### ‎  
##### b. Get the INDEX
###### ‎     
i. Open the file explorer, go to ``logs``, and open the folder named as the model.      
‎      
ii. Download the **.INDEX** named ``added_``.    
‎       
   <img src="../appliocolab-img/4-indexdl.png" alt="image" width="400" height="auto">‎
 ‎    

***
###### ‎  
##### c. Get the PTH
###### ‎  
i. In said folder you'll also find all the <u>[checkpoints](https://docs.aihub.gg/extra/glossary/#checkpoints)</u>.         
‎  
ii. Select the one **closest** to ***before*** the overtraining point, and move it to the new folder.

    - The checkpoints will be organized with this format: **ModelName_Epoch.pth**   
    Example: ``arianagrande_60e.pth``       
‎  
        <img src="../appliocolab-img/4-checkpoint.png" alt="image" width="200" height="auto">‎  
‎  
‎  
    - You can determine the Step number of the checkpoints by looking at its epoch number on the logs.

        <img src="../appliocolab-img/4-step.png" alt="image" width="600" height="auto">‎  
    ‎          
    ‎    
iii. And that's all, have fun with your model. To test it, do a normal <u>[inference</u>](https://docs.aihub.gg/rvc/local/applio/#inference-) as usual.

===

==- 5. RESUMING
###### ‎  
- In case the training finished but the model still needed training, you don't have to start from scratch.        
  
1. Simply enter the **same settings & criteria** that you had previously inserted. You don't have to do preprocess, extract feature or train the .INDEX again.      
 ‎     
2. You can change the **save frequency** or increase the **Total Epoch** amount, in case you didn't input enough before.      
 ‎  
3. If you're resuming from a new session, run the "Sync with Google Drive"yy cell again to automatically load your models.
4. Begin training again & remember to monitor <u>[TB</u>]https://docs.aihub.gg/rvc/resources/training/#tensorboard) as before.  
===

###### ‎  
###### ‎  
:::content-center
## TTS
*`+ with any RVC model`*
:::
###### ‎  
- Applio is also known for having one TTS tool by default, with **plenty** of voices to choose for.

- You can also use it with **RVC models** & apply the <u>[inference settings](https://docs.aihub.gg/rvc/resources/inference-settings/)</u> if you wish.

- Additionally, you can download the **Eleven Labs** TTS <u>[plugin](https://docs.aihub.gg/rvc/cloud/applio-colab/#plugins)</u>.       
***
###### ‎  
#### <u>Instructions:</u>
1. Go to the **TTS** tab. 

   <img src="../appliocolab-img/5-ttstab.png" alt="image" width="400" height="auto"> ‎ 

***   
###### ‎   

2. If you want to use an RVC model, <u>[download it](https://docs.aihub.gg/rvc/cloud/applio-colab/#1-upload-voice-model)</u>, go to **TTS**, click `Refresh` & select it in **Voice Model** & **Index File**.

   <img src="../appliocolab-img/5-vm.png" alt="image" width="600" height="auto">‎    
‎             
- To modify the <u>[inference settings](https://docs.aihub.gg/rvc/resources/inference-settings/)</u> or the output folder for the TTS/RVC audio, unfold `Advanced Settings`.

***
###### ‎      
3. In **TTS Voices** select the voice of your desired language, accent & gender.        

    In **Text to Synthesize** input your text. Then click `Convert`.

   <img src="../appliocolab-img/5-voice.png" alt="image" width="500" height="auto">‎     
‎   
- If you are using an RVC model, select a voice that matches the model the most, to guarantee great results.   
***
###### ‎  
4. Once it's done, you'll be able to hear the result in the Export Audio box. To download it, click the download button on its right ( :icon-download: ).

   <img src="../appliocolab-img/5-ttsoutput.png" alt="image" width="500" height="auto">‎   

***
###### ‎  
###### ‎  
:::content-center
## Extra
:::
###### ‎  
- Applio has an **Extra** menu, containing an **audio analyzer**, **F0 Curve** and **Model Information**.

- Making it convenient for determining the <u>[sample rate](https://docs.aihub.gg/rvc/resources/dataset-isolation/#step-1-find-the-sample-rate)</u> of datasets when training models.

- It also contains the **model fusion** tool, ideal for advanced users.

***
###### ‎  
#### <u>Audio Analyzer:</u>
1. Go to the **Extra** tab & press the upload box to input your audio.

   <img src="../appliocolab-img/6-tab.png" alt="image" width="400" height="auto">‎   
***
###### ‎  
2. Once it's done uploading, click `Get information about the audio`.  

***
###### ‎  
3. In **Sampling rate** you'll see the audio's full sample rate. Use said value for training.

   <img src="../appliocolab-img/6-samplerate.png" alt="image" width="470" height="auto">‎    
###### ‎    
!!!warning <u>WARNING:</u>   
If the frequencies don't reach the top of the spectrogram, see at which number peaks & multiply it by <U>**2**</u>.
!!!

###### ‎
{.list-icon}
- #### <u>Example:</u>
   <img src="../appliocolab-img/6-double.png" alt="image" width="470" height="auto">‎       
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

   <img src="../appliocolab-img/7-repo.png" alt="image" width="470" height="auto">‎ 

***
###### ‎
2. Click on the ZIP file.

   <img src="../appliocolab-img/7-zip.png" alt="image" width="470" height="auto">‎   
‎       
- Click on the download button on the right. This will download the ZIP file of the plugin.

   <img src="../appliocolab-img/7-dl.png" alt="image" width="470" height="auto">‎ 
***
###### ‎
3. Open Applio & head over to the **Plugins** tab. Press the upload box & upload the ZIP.

   <img src="../appliocolab-img/7-plugins.png" alt="image" width="600" height="auto">‎   

***
###### ‎
3. Go to the **Settings** tab & click **Restart Applio** at the bottom. Go back to the Colab & open the new public URL. 

    Then you'll be able to see the plugin in the **Plugins** tab.

   <img src="../appliocolab-img/7-plugindled.png" alt="image" width="420" height="auto">‎ 

***
###### ‎
###### ‎
:::content-center
## Troubleshooting
:::
###### ‎ 
==- *There's no public URL.*
###### ‎   

- In case the **public URL** doesn't show up, there might be a problem with <u>[Gradio</u>](https://docs.aihub.gg/extra/glossary/#gradio)</u>, you can check if it's down <u>[here</u>](https://status.gradio.app/)</u>.

- To fix this, instead of waiting until Gradio is back online, just check the **share_tunnel*** checkbox on the Start Applio cell.

    <img src="..\appliocolab-img\2-start-share-tunnel.png" alt="image" width="430">
‎ 
- Applio will use <u>[localtunnel</u>](https://docs.aihub.gg/extra/glossary/#localtunnel) instead of the Gradio Public Share Link now, copy paste the **Password IP** (Don't worry, it's the Google PC's IP, not yours).

- Then open the **Share Link** given by the colab and paste the "Password IP" in "Tunnel Password", finally click Submit.

    <img src="..\appliocolab-img\2-start-share-tunnel-link-localtunnel.png" alt="image" width="430">

===

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
- This a phenomenon called artifacting. To fix it, read <u>[here](https://docs.aihub.gg/rvc/resources/dataset-isolation/#artifacts)</u>.

===

==- *Cannot connect to GPU backend.*
###### ‎   
- You have exhausted the <u>[GPU runtime](https://docs.aihub.gg/rvc/extra/glossary/#google-colab)</u> of Colab.
===

==- *I couldn't find my answer.*
###### ‎   
- Report your issue <u>[here](https://docs.aihub.gg/contributions)</u>.
===
***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
