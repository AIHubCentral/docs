---
icon: chevron-right
order: 3000
---

``Last update: Mar 8, 2024``
***
###### ‎
:::content-center
## Introduction :icon-book:
:::
###### ‎              
- RVC Disconnected (or RVC-D) is a port of <u>[Mangio](https://docs.ai-hub.wtf/rvc/local/mangio/)</u> to <u>[Google Colab</u>](https://docs.ai-hub.wtf/extra/glossary/#google-colab), for exclusively training. Notebook made by <u>[Kit Lemonfoot</u>](https://huggingface.co/Kit-Lemonfoot).

- It's free, includes all the necessary tools for a quality model, the <u>[TensorBoard</u>](https://docs.ai-hub.wtf/rvc/resources/training/#tensorboard), & it's the fastest Colab space for training.    

- Making it the go-to method for training for cloud RVC users. Pretty much the only big downside is the time limit (but you can switch to another account & continue).      
‎       
#### Pros & Cons :icon-tasklist:

==- ***Learn more***
!!! *The pros & cons are subjective to your necessities.*        
!!!
||| **✔️ PROS:**  
- Has TensorBoard.    
- Has Mangio-Crepe.     
- Option to save model to HF.  
- Includes the latest *pretrains*.
||| ❌ **CONS**     
- Inconvenient I.   
- Takes some time to set up.      
- You can't leave training unsupervised.
- <u>For free users:</u>     
    - It's slower compared to local RVC.  
    - Can't train long datasets without pausing the process.   
|||
===
***
###### ‎ 
:::content-center
## Setting Up :icon-download:

###### ‎ 
!!!warning WARNING:
1.‎ The guide is centered around the <u>[TensorBoard](https://docs.ai-hub.wtf/rvc/resources/training/#tensorboard)</u>. Read it first if you haven't already.    
2. Turn on <u>[third-party cookies</u>](https://cleeng.zendesk.com/hc/en-us/articles/360009526800-How-to-enable-third-party-cookies-on-my-browser-), or TB might not work.
!!!
:::
###### ‎    
#### 1. Prepare dataset

a. Make a folder named after your model & move the dataset inside of it. Don't include spaces/special characters.     

    <img src="../rvcdisconnected-img/1.png" alt="image" width="210" height="auto">‎                     
‎       
b. Then <u>[zip</u>](https://support.microsoft.com/en-us/windows/zip-and-unzip-files-8d28fa72-f2f9-712f-67df-f80cf89fd4e5) the folder as a `.ZIP` file. .7ZIP and .RAR aren't compatible with RVC-D.

    <img src="../rvcdisconnected-img/2.png" alt="image" width="210" height="auto">‎           
‎       
!!!success
<u>**REMINDER:**</u> With modern versions of RVC, the dataset can be a single audio file. No need to split it.
!!!
***
###### ‎ 
#### 2. Set up Colab     
a. Head over to the <u>[Colab space</u>](https://colab.research.google.com/drive/1XIPCP9ken63S7M6b5ui1b36Cs17sP-NS#scrollTo=ZodNcumpg-JM) & **Sign in** to your Google account.

a. Execute the ``Dependencies`` cell & press `Run anyways`

    <img src="../rvcdisconnected-img/3.png" alt="image" width="280" height="auto">‎  
‎       
b. When this appears, press ``Connect to Google Drive`` & select your account.

    <img src="../rvcdisconnected-img/4.png" alt="image" width="400" height="auto">‎       
‎       
c. Once the cell is done loading, in GD go to the ``rvcDisconnected`` folder, and place the dataset's .ZIP inside of it.

    <img src="../rvcdisconnected-img/5.png" alt="image" width="335" height="auto">‎    

***
###### ‎ 
###### ‎ 
:::content-center
## Training :icon-rocket:
:::
###### ‎ 
#### 1. Training variables    
a. Go to the `Set Training Variables` cell.      

    <img src="../rvcdisconnected-img/18.png" alt="image" width="335" height="auto">‎   
‎   
- #### <u>Define these values:</u>
`experiment_name`   
:    Name your model. Don't include spaces/special characters.

`pretrain_type`
:   If you aren't familiar with pretrains, select `original`.

`target_sample_rate`
:   Select your dataset's <u>[sample rate</u>](https://docs.ai-hub.wtf/rvc/resources/dataset-isolation/#step-1-find-the-sample-rate).

``pitch_extraction_algorithm``
:   The <u>[extraction method](https://docs.ai-hub.wtf/rvc/resources/inference-settings/#pitch-extraction-algorithm)</u>. Don't use Harvest, as it's obsolete.        

`crepe_hop_length`
:   If you chose `Mangio-Crepe`, this defines the <u>[Hop Length](https://docs.ai-hub.wtf/rvc/resources/inference-settings/#mangio-crepe)</u>.

***
###### ‎ 
#### 2. Set the environment      

‎ ‎ ‎ ‎ ‎ ‎ ‎ <img src="../rvcdisconnected-img/8.png" alt="image" width="500" height="auto">‎   
‎   
a. Go to `Load Dataset` cell. In the **dataset** bar type the dataset's .ZIP name followed by **.zip**, then execute the cell.      
Example: ``kalomaze.zip``     

b. Below, execute **Preprocessing, Feature Extraction**, & **Save preprocessed dataset files to Google Drive**.

    <img src="../rvcdisconnected-img/9.png" alt="image" width="335" height="auto">‎   
***
###### ‎ 
#### 3. Train Index  
a. Run **Index Training** to create the model's <u>[.INDEX</u>](https://docs.ai-hub.wtf/essentials/voice-models/#voice-model-files) file.      

    <img src="../rvcdisconnected-img/17.png" alt="image" width="450" height="auto">‎        
‎       
b. To download it, in GD open `rvcDisconnected` & the folder named after the model. Download the .INDEX named `added`.
 
    <img src="../rvcdisconnected-img/13.png" alt="image" width="450" height="auto">‎  
***
###### ‎ 
#### 4. Set Training      
- Go to the **Training** cell.  

    <img src="../rvcdisconnected-img/10.png" alt="image" width="350" height="auto">‎    
‎   
- #### <u>Define these values:</u>

`save_frequency`
:   Frequency of the <u>[saving checkpoints](https://docs.ai-hub.wtf/extra/glossary/#checkpoints)</u>, based on the <u>[epochs](https://docs.ai-hub.wtf/rvc/resources/training/#epochs--overtraining)</u>. If you're a newbie, simply leave it at `15`.      
<u>E.g:</u> with a value of ``10``, it will be saved after the epoch 10, 20, 30, etc.   

`total_epochs`
:   The total amount of <u>[epochs](https://docs.ai-hub.wtf/rvc/resources/training/#epochs--overtraining)</u> for the model. But since we'll use <u>[TensorBoard](https://docs.ai-hub.wtf/rvc/resources/training/#tensorboard)</u>, use an arbitrarily large number like ``2000``.

`batch_size`
:   Use ``8`` if you are a newbie.
But if your dataset is small (around 2 minutes or less), use ``4``.
 
***
###### ‎ 
#### 5. Begin training
- Execute the **Training** cell to begin training. <u>[TB](https://docs.ai-hub.wtf/rvc/resources/training/#tensorboard)</u> will open up after a few seconds, & the graphs will take a minute to appear.         
‎    
- Remember to monitor it, as well as the cell's logs. The latter will show you errors if they happen, and information about the epochs & checkpoints.         
‎       
- **While training, you might get disconnected if you:**      
   - <u>[Stay AFK](https://docs.google.com/document/d/1Pr-AZndodmWgsbOeuHQU4IrgbatFgYc1ChOq_ZAf_5s/edit?usp=sharing)</u> for a long time.     
   - Disconnect from your Internet.       
   - Don't solve the captchas that (might) pop up occasionally.    
   - Run out of <u>[GPU runtime](https://docs.ai-hub.wtf/rvc/extra/glossary/#google-colab)</u>.     

***
###### ‎ 
#### 6. Export model
- If after around 2:30 hours of training you don't detect overtraining, you must save the files so you can resume later, before the GPU runtime ends.    

1. For this, first download the model of the lowest point (**Step 7b**) in case you are already overtraining.

2. Stop training by pressing the stop button of the **Training** cell.

3. Run the **Export Model from Notebook to Drive** cell.

    <img src="../rvcdisconnected-img/22.png" alt="image" width="330" height="auto">‎        
‎       
3. Once your GPU runtime resets, begin the <u>[retraining](https://docs.ai-hub.wtf/rvc/cloud/rvc-disconnected/#resuming-)</U> procedure.

- After exporting, you are free to resume training until runtime is exhausted or close the session.
***
###### ‎ 
#### 7. Download model. 
a. When you're very sure of overtraining, you can stop training by pressing the stop button of the **Training** cell. 

b. Click the folder symbol on the left.     
(For mobile users: tap the three lines on the top left & `Show file browser`)     

    Open the ``Mangio-RVC-Fork`` folder, then `weights`. You'll find the <u>[checkpoints](https://docs.ai-hub.wtf/extra/glossary/#checkpoints)</u>.    

    <img src="../rvcdisconnected-img/20.png" alt="image" width="210" height="auto">‎    
‎   
c. Right-click the one that's **closest** to ***before*** the overtraining point, and press `Download`.     

    The models will be organized with this format: **Name_Epoch_Step.pth**.       
    E.g: `arianagrande_e60_s120.pth`    
‎   
d. And that's all. To test it, do a normal <u>[inference](https://docs.ai-hub.wtf/essentials/how-to-make-ai-cover/)</u> as usual.

***
:::content-center
###### ‎  
###### ‎  
## Resuming :icon-sync:
:::
###### ‎    
- If the training stops but the model still needed training, you don't have to start from scratch.   

- You can resume from the latest checkpoint. But for this, the cell **Save preprocessed dataset files to Google Drive** must have executed prior to training. 

- And if you're resuming from a new session, you should've ran the **Export Model from Notebook to Drive** cell in the previous session.
###### ‎  
#### <ins>Instructions</ins>:
1. Go to the Colab space, input the same criteria as before & execute the cells like normal, <u>**except**</u> Preprocessing & Feature Extraction.    
***
2. Execute the **Load preprocessed dataset files** cell.   

    <img src="../rvcdisconnected-img/14.png" alt="image" width="450" height="auto">‎  
***
3. Go to the **Import Model from Drive to Notebook** cell. In **STEPCOUNT** introduce ``2333333`` & execute it.    

    <img src="../rvcdisconnected-img/16.png" alt="image" width="450" height="auto">‎  

***
4. You can change the **save frequency** or increase the **total epochs**, in case you didn't input enough before.
***
5. Run the **Training** cell to retrain. Remember to monitor <u>[TB</u>](https://docs.ai-hub.wtf/rvc/resources/training/#tensorboard) as before.       

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/rvc/contributions/)
:::