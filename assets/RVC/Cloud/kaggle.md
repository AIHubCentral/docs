---
icon: chevron-right
order: 4000
---
 
``Last update: Oct 23, 2024``

***
:::content-center
<img src="../kaggle-img/kaggle.png" alt="image" width="600" height="600">        
:::
 
## </u>Introduction</u>
- Kaggle is a cloud platform for using AI apps, powered by virtual machines with powerful GPU's.     

- It's a great alternative for training RVC voice models through the cloud, since it has the best GPUs.

!!!danger
You only get 30 free GPU hours per week.
!!!
    
#### Pros & Cons :icon-tasklist:

==- ***Learn more***
!!! *The pros & cons are subjective to your necessities.*        
!!!
||| **✔️ PROS:**  
- Has good GPU's  
- Has 30 GPU hours
- Fast  
- TensorBoard included
-  You can leave training unsupervised.  
||| ❌ **CONS**       
- Takes some time to set up.      
- Doesn't have Mangio-Crepe
 
|||
===


***
###### ‎   
## How to Setup   
###### ‎   
#### 1. <u>Set up account.</u>
a. Start by making an account <u>[here](https://www.kaggle.com/account/login?phase=startRegisterTab&returnUrl=%2F)</u>.

   <img src="../kaggle-img/kaggle-sign-in.png" alt="image" width="575" height="auto">

b. Verify your acount with a phone number so you can turn on the "internet" option.  

 <img src="../kaggle-img/kaggle-phone.png" alt="image" width="575" height="auto">    
 

***  
######
#### 2. <u>Clone notebook and setup.</u>
a. Go to <u>[Hina's mainline notebook](https://www.kaggle.com/code/hinabl/mainline)</u> and click "Copy and Edit"

   <img src="../kaggle-img/kaggle-copy.png" alt="image" width="1000" height="auto"> 

   
b. Under session settings in the sidebar turn on "internet". Make sure persistance is on for both files and varibles.

   <img src="../kaggle-img/kaggle-Internet.png" alt="image" width="450" height="auto">     
  
c. Turn on T4 X2 GPUs in accelerator.           

   <img src="../kaggle-img/kaggle-gpu.png" alt="image" width="" height=""> 
d: (Optional) Turn on headless mode so you can run so you can run the GPU on all sessions and save your progress. Go to the top right and click "Save version" then open the advanced dropdown.

<img src="../kaggle-img/kaggle-pers.png" alt="image" width="" height=""> 

‎
!!!warning Warning
Your runtime will continue draining when you're not running any cells with this option on. 
!!!

***
###### ‎   
#### 3. <u>Ngrok.</u>
a. Scroll down to the fifth cell and you should see a section where you put your ngrok token. If you dont have a ngrok acount sign up <u>[here](https://ngrok.com/)</u>.       
‎       
     2. Once you have an acount you can authenticate your ngrok tunnel agent here: https://dashboard.ngrok.com/get-started/your-authtoken   
‎       
b. put the Ngrok token in the quotation marks like so:

   <img src="../kaggle-img/kaggle-ngrok.png" alt="image" width="430" height="">  

!!!warning Warning               
There is a monthly limit rate with Ngrok so dont be supprised if training is suddenly interrupted.
!!!

***
######   
#### 3. <u>Starting the Cells.</u>
a. From top to bottom execute all the cells. With first being:

 <img src="../kaggle-img/kaggle-1.png" alt="image" width="600" height=""> 

b. The second cell will take ~5 minutes to load.

<img src="../kaggle-img/kaggle-2.png" alt="image" width="600" height=""> 

- when its finished it will look like this:

<img src="../kaggle-img/kaggle-fin.png" alt="image" width="600" height=""> 

c. If you want to use a pretrain now is the time to download it. Add a new code cell and type this in then run it:

<img src="../kaggle-img/kaggle-pretrain.png" alt="image" width="700" height=""> 

####

`!wget LINK TO PRETRAIN`

d. Run the third cell.

<img src="../kaggle-img/kaggle-3.png" alt="image" width="600" height="">

e. Once you run the final cell it will give you three links.

<img src="../kaggle-img/kaggle-4.png" alt="image" width="600" height=""> 

RVC url: is to open RVC's gui.

File url: is to open Imjoy Elfinder gui.

Tensorboard: is to open the Tensorboard.

***

::: content-center
## The Imjoy Elfinder WebGUI
:::

The interface should look like this with your D and G files being located here. Here you can manage your files within Kaggle. Whenever you want to download files from the Imjoy GUI just double click. Downloading files uses up the Ngrok bandwith data.

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

b. In the file manager create a folder named `dataset` anywhere then drag and drop your dataset in it. Then continue with normal RVC setup and training
***
#### 3. Syncing Graphs. 
a. For syncing graphs you need to train however many epochs you have set you save frequency then go into the file manager and find your model which should be in `assest/weights`, in its name it should have a step count and epoch count like this: `model_name_e(number)_s(number)`.

!!!
E means epochs and S means steps.
!!!

b. Once you know how many steps the model trained for stop training the model by stopping the cell.

<img src="../kaggle-img/stop.png" alt="image" width="600" height="">

c. Then start the same cell and open the file manager and navigate to `assest/weights` and delete all of your previous models.

<img src="../kaggle-img/stop.png" alt="image" width="600" height="">

d. Then navigate to the 32k.json file which is located in the V2 folder of /configs and download it by double clicking it, then delete it. 

<img src="../kaggle-img/v2.png" alt="image" width="600" height="">

e. Open the file you have just downloaded in notepad and edit `log_interval` to the amount of steps your model took, save it then replace the old 32k.json file. 

<img src="../kaggle-img/log.png" alt="image" width="600" height="">

f. Now go to your /logs/ folder and do the same thing. Modify the log interval of the config.json with your step count. Delete the config.json that's already in the /logs/ folder and replace it with your copy.

<img src="../kaggle-img/log2.png" alt="image" width="800" height="">

g. Now delete `Eval folder, tf-events file, G & D_23333333 files and train log file` in /logs/ folder.
***
#### 4. Resuming Training.
a. Do not process and feature extract again because those files are already in the /logs/ folder. Use the same model name, sample rate, batch size, pretrain, and save frequency to train the model again in the RVC GUI.
***

###### ‎   ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/rvc/#contributions)
:::
