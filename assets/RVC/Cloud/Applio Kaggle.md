---
icon: chevron-right
order: 5000
---
 
``Last update: Jan 13, 2025``

***
:::content-center
<img src="..\appliocolab-img\banner.png" alt="image" width="600">

:::
###### ‎
:::content-center
## Introduction ‎
:::
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
- You can leave training unsupervised.  
||| ❌ **CONS**       
- Takes some time to set up.      
 
|||
===


***
###### ‎   
## Create an Account   
###### ‎   
#### 1. <u>Set up account.</u>
a. Start by making an account <u>[here](https://www.kaggle.com/account/login?phase=startRegisterTab&returnUrl=%2F)</u>.
‎  

   <img src="../kaggle-img/kaggle-sign-in.png" alt="image" width="575" height="auto">

‎  

b. Verify your acount with a phone number so you can turn on the "internet" option.  

 <img src="../kaggle-img/kaggle-phone.png" alt="image" width="575" height="auto">    
 

***  

###### ‎  
## Clone and Notebook Setup
###### ‎  
#### 2. <u>Clone Notebook</u>
a. Go to <u>[Applio's notebook](https://www.kaggle.com/code/deiant/applio)</u> and click "Copy and Edit"

   <img src="../applio-kaggle-img/Applio.png" alt="image" width="1000" height="auto"> 

   
b. Under session settings in the sidebar turn on "internet". Make sure persistance is on for both files and varibles.

   <img src="../applio-kaggle-img/kaggle-Internet.png" alt="image" width="450" height="auto">     
  
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
## Ngrok Setup
###### ‎  
#### 3. <u>Ngrok Setup</u>
a. Scroll down to the fifth cell and you should see a section where you put your ngrok token. If you dont have a ngrok acount sign up <u>[here](https://ngrok.com/)</u>.             
     a2. Once you have an acount you can authenticate your ngrok tunnel agent here: https://dashboard.ngrok.com/get-started/your-authtoken   
‎       
b. put the Ngrok token in the second cell like so:

   <img src="../kaggle-img/ngrok-applio.png" alt="image" width="600" height="">  

c. Once the Ngrok token is there run the cell.

!!!warning Warning               
There is a monthly limit rate with Ngrok so dont be supprised if training is suddenly interrupted.
!!!

***

###### ‎   
## Installation
###### ‎  
#### 4. <u>Installation Cells</u>
a. Starting from the top run all the cells, with the first being:

   <img src="../kaggle-img/install-cell.png" alt="image" width="900" height=""> 

a2. When it's done it will output `Finished`.

b. Now run the last cell which is:

   <img src="../kaggle-img/start-cell.png" alt="image" width="600" height=""> 

***

###### ‎   
## Using Applio
###### ‎  
#### 5. <u>Ngrok Links</u>

a. Click on the Applio URL link to open Applio's UI, click the Tensorboard Url link to open the Tensorboard and click File Url to open the file manager.

   <img src="../applio-kaggle-img/URLs.png" alt="image" width="800" height=""> 

‎

b. Once you've click the Applio Url it will take you to Applio's UI where it operates the same as normal Applio. If you happen to not know how to use Applio you can read about it in their <u>[docs](https://docs.applio.org/applio)</u>.

***

###### ‎   ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/contributions/)
:::