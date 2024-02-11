
``Last update: Feb 9, 2024``
***
###### ‎
:::content-center
## Introduction
:::
###### ‎              
- RVC Disconnected (or RVC-D) is a port of <u>[Mangio](https://aihubdocs.github.io/en/rvc/local/mangio/)</u> to <u>[Google Colab</u>](https://aihubdocs.github.io/en/other/glossary/#google-colab), for exclusively training. Notebook made by <u>[Kit Lemonfoot</u>](https://huggingface.co/Kit-Lemonfoot).

- It's free, includes all the necessary tools for a quality model, the <u>[TensorBoard</u>](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard/#tensorboard), & it's the fastest Colab space for training.    

- Making it the go-to method for training for cloud RVC users. Pretty much the only big downside is the time limit (but you can switch to another account & continue).      
‎       
### Pros & Cons :icon-tasklist:

==- ***Unfold***
!!! *The pros & cons are subjective to your necessities.*        
!!!
||| **✔️ PROS:**  
- Has TensorBoard.    
- Has Mangio-Crepe.     
- Option to save model to HF.  
- Includes the latest *pretrains*.
    Speeds up the process.
||| ❌ **CONS**     
- Doesn't have a great UI.   
- Takes some time to set up.      
- You can't leave training unsupervised.
- <u>For free users:</u>     
    - It's slower compared to local RVC.  
    - Can't train long datasets without having to pause the process.   
|||
===
***
###### ‎ 
:::content-center
## How to Train

###### ‎ 
!!!warning IMPORTANT NOTE:
1.‎ This guide is centered around the <u>[TensorBoard](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard/#tensorboard)</u>. Read it first if you haven't already.    
2. Turn on <u>[third-party cookies</u>](https://cleeng.zendesk.com/hc/en-us/articles/360009526800-How-to-enable-third-party-cookies-on-my-browser-), or TB might not work.
!!!
:::
###### ‎    
#### 1. Prepare the dataset

a. First make a folder named after your model & move your dataset inside of it. 
Don't include spaces/special characters.     

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
#### 2. Set up the Colab space.     
a. Log in to Google account & head over to the <u>[Colab space</u>](https://colab.research.google.com/drive/1XIPCP9ken63S7M6b5ui1b36Cs17sP-NS#scrollTo=ZodNcumpg-JM).

a. Execute the ``Dependencies`` cell & press `Run anyways`

    <img src="../rvcdisconnected-img/3.png" alt="image" width="280" height="auto">‎  
‎       
b. When this appears, press ``Connect to Google Drive`` & select your Google account.

    <img src="../rvcdisconnected-img/4.png" alt="image" width="400" height="auto">‎       
‎       
c. Once the cell is done loading, in Google Drive go to the ``rvcDisconnected`` folder, and place the dataset's .ZIP inside said folder.

    <img src="../rvcdisconnected-img/5.png" alt="image" width="335" height="auto">‎    

***
###### ‎ 
#### 3. Set Training Variables.     
a. Go to the `Set Training Variables` cell.      

    <img src="../rvcdisconnected-img/18.png" alt="image" width="335" height="auto">‎   
‎   
- #### <u>Define these values:</u>
`experiment_name`   
:    Name your model. Don't include spaces/special characters.

`pretrain_type`
:   If you aren't familiar with pretrains, select `original`.

`target_sample_rate`
:   Select your dataset's <u>[sample rate</u>](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/#sample-rate).

``pitch_extraction_algorithm``
:   Learn about them <u>[here](https://aihubdocs.github.io/en/rvc-resources/inference-settings/#pitch-extraction-algorithm)</u>. Don't use Harvest, it's obsolete.        

`crepe_hop_length`
:   Works if you use `Mangio-Crepe`. Modifies its Hop Length.

***
###### ‎ 
#### 4. Set the environment.        

‎ ‎ ‎ ‎ ‎ ‎ ‎ <img src="../rvcdisconnected-img/8.png" alt="image" width="500" height="auto">‎   

a. Go to `Load Dataset` cell, and in the `dataset` bar type the dataset's .ZIP name followed by ".zip". Example: `kalomaze:zip`.        
Then execute the cell.

b. Below, execute `Preprocessing`, ``Feature Extraction``, & ``Save preprocessed dataset files to Google Drive``.

    <img src="../rvcdisconnected-img/9.png" alt="image" width="335" height="auto">‎   
***
###### ‎ 
#### 5. Train Index.  
a. Run ``Index Training`` to create the model's <u>[.INDEX</u>](https://aihubdocs.github.io/en/essentials/voice-models/#voice-model-files) file.      

    <img src="../rvcdisconnected-img/17.png" alt="image" width="450" height="auto">‎        
‎       
b. To download it, open `rvcDisconnected` in GD. Open the folder named after the model and download the .INDEX named `added`.
 
    <img src="../rvcdisconnected-img/13.png" alt="image" width="450" height="auto">‎  
***
###### ‎ 
#### 6. Set Training.       
- Go to the `Training` cell.  

    <img src="../rvcdisconnected-img/10.png" alt="image" width="350" height="auto">‎    
‎   
- #### <u>Define these values:</u>

`save_frequency`
:   At how many <u>[epochs](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard/)</u> the model will be saved at. These saved models are known as the "checkpoints". If you are a newbie, leave it at `15`.      
<u>E.g:</u> with a value of ``10``, it will save after 10, 20, 30, 40 epochs, etc.    

`total_epochs`
:   The total amount of <u>[epochs](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard//)</u> for the model. But since we'll use <u>[TensorBoard](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard/#tensorboard)</u>, use an arbitrarily large number like ``2000``.

`batch_size`
:   Use ``8`` if you are a newbie.
But if your dataset is small (around 2 minutes or less), usa ``4``.
 
***
###### ‎ 
#### 7. Begin training
- Execute the `Training` cell to begin the training. Be patient, it may take hours.

- <u>[TB](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard/#tensorboard)</u> will open up after a few seconds, remember to monitor it.             

- The cell will be showing you information about the epochs & when the checkpoints happen.      
‎   
!!!warning <u>While training, you might get disconnected if you:</u>
• Ran out of usage time.       
• Didn't interact with the space for a long time (staying AFK).     
• Get disconnected from your Internet.       
• Don't solve the captchas that (might) pop up occasionally. 
!!!
***
###### ‎ 
#### 8. Download model. 
- Once you are sure of overtraining, you can stop training by pressing the stop button of the ``Training`` cell.     

- Click the folder symbol on the right, open the ``Mangio-RVC-Fork`` folder, then `weights`. There you'll find the model's checkpoints.    

    <img src="../rvcdisconnected-img/20.png" alt="image" width="210" height="auto">‎    
‎   
- Right-click the one that's **closest** to ***before*** the overtraining point, and press `Download`.     

- The models will be organized with this format: **Name_Epoch_Step.pth**.       
E.g: `arianagrande_e60_s120.pth`

‎   
And that's all. Have fun with your model. Remember to move them to a new folder to stay organized.

To test it, do a normal <u>[inference](https://aihubdocs.github.io/en/essentials/how-to-make-ai-cover/)</u> as usual.

***
###### ‎  
### Retraining

If the training finished but the model still needed training, you don't need to start from scratch.     

##### <u>Instructions:</u>

1. Go to the Colab space & input the same data as before, & execute the cells like normal, <u>except</u> ``Preprocessing`` & ``Feature Extraction``.    

2. Execute the `Load preprocessed dataset files` cell.   

    <img src="../rvcdisconnected-img/14.png" alt="image" width="450" height="auto">‎  
‎       
3. Go to the `Import Model from Drive to Notebook` cell. In `STEPCOUNT` introduce ``2333333`` & execute it.    

    <img src="../rvcdisconnected-img/16.png" alt="image" width="450" height="auto">‎  
    ‎       
4. You can change the `save_frequency` or increase the `total_epochs`, in case you didn't input enough before.

5. Run the `Training` cell to retrain. Remember to monitor <u>[TB</u>](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard/#tensorboard) as before.
***
###### ‎
:::content-center
``Original guide: Angetyde``     
:::
:::content-center
``Re-done by: Julia, Eddy, Poopmaster & Light``      
:::
:::content-center
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Send Suggestions"](https://forms.gle/3GVR7opzpQrhgRCj9)
:::  
***