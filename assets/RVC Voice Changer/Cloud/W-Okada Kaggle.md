---
icon: chevron-right
order: 4000
---
``Last update: Feb 19, 2025``
***
:::content-center
<img src="..\kaggle-img\kaggle.png" alt="image" width="600">
:::

###### ‎
:::content-center
## Introduction ‎
:::
- Kaggle is a cloud platform for using AI apps, powered by virtual machines with powerful GPU's.     

- It's a good cloud alternative for W-Okada for those who don't have good enough GPUs.

!!!danger
You only get 30 free GPU hours per week.
!!!

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
a. Go to the <u>[voice changer notebook](https://www.kaggle.com/code/suneku/voice-changer-public)</u> and click "Copy and Edit"

   <img src="../kaggle-img/vc.png" alt="image" width="1000" height="auto"> 

   
b. Under session settings in the sidebar turn on "internet". Make sure persistance is on for both files and varibles.

   <img src="../kaggle-img/kaggle-internet.png" alt="image" width="450" height="auto">     
  
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
### Installation
###### ‎  
#### 3. <u>Installation Cells</u>
a. Starting from the top run the first cells, with the first being:

   <img src="../kaggle-img/install-1.png" alt="image" width="900" height=""> 

a2. When it's done, which may take a couple of minutes, it will output `Done! Proceed with the next steps`.

b. Run the third cell which is:

   <img src="../kaggle-img/install-2.png" alt="image" width="600" height=""> 

***

###### ‎   
### Ngrok & Sever Setup
###### ‎  
#### 4. <u>Ngrok Setup</u>
a. Scroll down to the last cell and you should see a section where you put your ngrok token. If you dont have a ngrok acount sign up <u>[here](https://ngrok.com/)</u>.             
     a2. Once you have an acount you can authenticate your ngrok tunnel agent here: https://dashboard.ngrok.com/get-started/your-authtoken   
‎       
b. put the Ngrok token in the last cell like so:

   <img src="../kaggle-img/token.png" alt="image" width="600" height="">  

c. Once the Ngrok token is there run the cell and let it download what it needs then you can click on the ngork link and start using W-Okada.

!!!warning Warning               
There is a monthly limit rate with Ngrok so dont be supprised if training is suddenly interrupted.
!!!

d. (Optional) Directly under where you put your ngrok token there is region selection. You can change it to any of these servers to get less latency:
- us -> United States (Ohio)
- ap -> Asia/Pacific (Singapore)
- au -> Australia (Sydney)
- eu -> Europe (Frankfurt)
- in -> India (Mumbai)
- jp -> Japan (Tokyo)
- sa -> South America (Sao Paulo)

c. From here it's pretty much the same as using local W-Okada.


***

## Virtual Audio Cable

#### A Virtual Audio Cable (VAC) is what you need to use the voice changer on Discord & Games.

!!! For Windows
Download this: <u>[VAC Lite (Virtual-Audio-Cable by Muzychenko)](https://software.muzychenko.net/freeware/vac470lite.zip)</u>
!!!

- Run `setup64`, not 64a, after extracting the zip to a new folder

- After installing the Virtual Cable, it changes your default audio system. Click **Yes** when it asks you to open the audio device settings (or press WIN+R, type "mmsys.cpl" if you closed it already), and change your **Recording** and **Playback** devices back to your usual devices. Same for communications device aswell (right click -> set as default communication device)

!!! For Mac
Download either: 
<u>[Blackhole Virtual Audio Cable](https://existential.audio/blackhole)</u>
or
<u>[VB-Audio](https://vb-audio.com/Cable)</u>
!!!


***
## Audio Setup
***

### Discord & Games

On the voice changer app wokada, you select:

- Input: Your microphone
- Output: Virtual Cable
- Monitor (if you wish to hear the voice changer on your headphones aswell): Your headphones

On discord and games, you select:

- Input: Virtual Cable
- Output: Your headphones


***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/rvc/contributions/)
:::
