---
icon: chevron-right
order: 1000
---

``Last update: August 7, 2025``

***
:::
:::content-center
## Introduction
:::
- This is a <u>[cloud-based](http://docs.aihub.gg/extra/glossary/#cloud-based)</u> alternative to run [Mainline/Original RVC](https://docs.aihub.gg/rvc/local/mainline/), RVC Fork, only for people who don't have a good PC GPU, via the <u>[Google Colab Service](http://docs.aihub.gg/extra/glossary/#google-colab)</u>. With a Web User Interface.

!!!danger Google Colab Service
**Check the <u>[Google Colab Glossary](http://docs.aihub.gg/extra/glossary/#google-colab)</u> for more info on Free Tier, Limits, Verification, Pricing and other things.**
!!!

!!!danger End Of Life
The Hina Modified Mainline Google Colab has reached EOL (End Of Life), meaning it has had it's last update, it won't be suggested anymore nor fixed for any future issues. We would suggest users to use other alternatives if it breaks, and if it breaks this guide will be removed in the future.
!!!
     
‎       
#### Pros & Cons :icon-tasklist:

==- ***Learn more***
!!! *The pros & cons are subjective to your necessities.*        
!!!
||| **✔️ PROS:**  
- Has TensorBoard.    
||| ❌ **CONS**     
- Reached End Of Life.
- Inconvenient.   
- Takes some time to set up.      
- You can't leave training unsupervised.
- Doesn't have Mangio-crepe.
|||
===
***


***
###### ‎   
## How to Setup   
###### ‎   
#### 1. <u>Running cells.</u>
a. Start by accessing the colab <u>[here](https://colab.research.google.com/github/hinabl/RVC-Online/blob/main/Mainline_Colab_Full.ipynb)</u>.

b. Then run the first two cells to install all the requirements.
 
***  
######
#### 2. <u>Installing Pretrains.</u>
a. If you wish to install a custom pretrain go to the 'Download Custom Pretrains' cell and go into the dropdown menu and find the pretrain you want.

   <img src="../mainline-img/1.png" alt="image" width="600" height="auto"> 

   
b. If the pretrain you want isn't there go to the top left and click '+ Code'.

   <img src="../mainline-img/2.png" alt="image" width="600" height="auto">     
  
c. Then in the new cell type in `!wget LINK TO PRETRAIN`           

<img src="../mainline-img/3.png" alt="image" width="1500" height="auto"> 
 

***
###### ‎   
#### 3. <u>Ngrok.</u>
a. Scroll down to the fifth cell and you should see a section where you put your ngrok token. If you don't have a ngrok acount sign up <u>[here](https://ngrok.com/)</u>.       
‎       
     2. Once you have an acount you can authenticate your ngrok tunnel agent here: https://dashboard.ngrok.com/get-started/your-authtoken   
‎       
b. put the Ngrok token in like so:

<img src="../mainline-img/4.gif" alt="image" width="700" height="auto"> 

‎
!!!warning Warning               
There is a monthly limit rate with Ngrok so don't be supprised if training is suddenly interrupted.
!!!

***
######   
::: content-center
#### 3. <u>The Imjoy Elfinder WebGUI.</u>
:::

The interface should look like this with your D and G files being located here. Here you can manage your files. Whenever you want to download files from the Imjoy GUI just double click. Downloading files uses up the Ngrok bandwith data.

<img src="../kaggle-img/gui.png" alt="image" width="900" height=""> 

***
###### ‎   
## Starting RVC   
###### ‎   
#### 1. Click the RVC link.
 It should take you to the GUI where you can then go to the top and click the 'Train' tab. 

 <img src="../kaggle-img/train.png" alt="image" width="900" height="">

***
#### 2. Setup.
a. Run through the normal RVC setup with setting your model name, sample rate and such. If you are unable to see the 32k sample rate click on V1 then swap back to V2.

!!!warning
Only use V2 Don't use V1 or you will get an error.
!!!

b. In google drive create a folder named `training` and inside it make another folder named`dataset` then drag and drop your dataset in it. Then continue with normal RVC setup and training

!!!
Make sure you use WAV or Flac files inside. Do not zip the folder.
!!!

***
#### 3. Syncing Graphs. 
a. For syncing graphs you need to train however many epochs you have set you save frequency then go into the file manager and find your model which should be in `training/weights`, in its name it should have a step count and epoch count like this: `model_name_e(number)_s(number)`.

!!!
E means epochs and S means steps.
!!!

b. Once you know how many steps the model trained for stop training the model by stopping the cell.

<img src="../mainline-img/4.png" alt="image" width="600" height="">

c. Then start the same cell and open then navigate to `assest/weights` in google colab and delete all of your previous models.

d. Then navigate to the 32k.json file which is located in the V2 folder of /configs and edit `log_interval` to the amount of steps your model took, save it. 

<img src="../kaggle-img/log.png" alt="image" width="600" height="">

f. Now go to your /logs/ folder and do the same thing. Modify the log interval of the config.json with your step count.

<img src="../kaggle-img/log2.png" alt="image" width="800" height="">

g. Now delete `Eval folder, tf-events file, G & D_23333333 files and train log file` in /logs/ folder.
***
#### 4. Resuming Training.
a. Do not process and feature extract again because those files are already in the /logs/ folder. Use the same model name, sample rate, batch size, pretrain, and save frequency to train the model again in the RVC GUI.
***

###### ‎   ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
