---
icon: chevron-right
order: 6000
---
``Last update: September 6, 2025``
***
:::content-center
<img src="..\kaggle-img\kaggle.png" alt="image" width="600">
:::

###### ‎
:::content-center
## Introduction ‎
:::
- This is a <u>[cloud-based](http://docs.aihub.gg/extra/glossary/#cloud-based)</u> alternative to run [Wokada Tg-Develop's Fork](https://docs.aihub.gg/realtime-voice-changer/local/tg-develops-w-okada-fork/#virtual-audio-cable), Realtime Voice Changer for calls/games, only for people who don't have a good PC GPU, via the <u>[Kaggle Service](http://docs.aihub.gg/extra/glossary/#kaggle)</u>.

!!!danger Kaggle Service
**Check the <u>[Kaggle Glossary](http://docs.aihub.gg/extra/glossary/#kaggle)</u> for more info on Free Tier, Limits, Verification, Pricing and other things.**
!!!


***
## Virtual Audio Cable

#### A Virtual Audio Cable (VAC) is what you need to use the realtime voice changer on Discord & Games.

- A VAC (Virtual Audio Cable) makes a fake audio device, used to re-route the audio of different programs.
- In AI Realtime Voice Changing context, it's used to get the output of AI Converted Voice Output as the input in other programs such as Discord.

!!! For Windows
Download this: <u>[VAC Lite (Virtual-Audio-Cable by Muzychenko)](https://software.muzychenko.net/freeware/vac470lite.zip)</u>.
(Be sure to not use any toher vac like VB Audio Cable.)
!!!

- Run `setup64`, not 64a, after extracting the zip to a new folder

- After installing the VAC Lite, it changes your default audio system. Click **Yes** when it asks you to open the audio device settings (or press WIN+R, type "mmsys.cpl" if you closed it already), and change your **Recording** and **Playback** devices back to your usual devices. Same for communications device aswell (right click -> set as default communication device)

!!! For Mac
Download either: 
<u>[Blackhole Virtual Audio Cable](https://existential.audio/blackhole)</u>
or
<u>[VB-Audio](https://vb-audio.com/Cable)</u>
!!!

!!! For Linux
For Debian / Ubuntu-based Systems (Ubuntu, Mint, Pop!_OS), run in the terminal:
```bash
sudo apt-get update && sudo apt-get install -y portaudio19-dev
```


For Fedora / RHEL-based Systems (CentOS, Rocky Linux), run in the terminal:
```bash
sudo yum install -y portaudio
```

For Arch / Arch-based Systems (Endeavour, Manjaro Linux), run in the terminal:
```bash
sudo pacman -Syu portaudio
```
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
## Notebook Creation & Setup
###### ‎  
#### 2. <u>Clone Notebook</u>
a. Go to <u>[Kaggle](https://www.kaggle.com)</u> and click "Create" then "New Notebook" at the top left. 

   <img src="../kaggle-img/new.png" alt="image" width="400" height="auto"> 

‎ 
b. Under your session's name click "File" then "Import Notebook".

   <img src="../kaggle-img/import.png" alt="image" width="450" height="auto">     

‎   

c. On the new window that appeared on the right click "Link" then type in the box this link `https://github.com/tg-develop/voice-changer/blob/master-custom/Kaggle_RealtimeVoiceChanger.ipynb`.

   <img src="../kaggle-img/link.png" alt="image" width="700" height="auto"> 

Click "Import" on the bottom right once you've done this.

d. When it's done importing it will display this text window.

   <img src="../kaggle-img/settings-updated.png" alt="image" width="600" height="auto">

‎  
e. Under "Session options" in the sidebar turn on "internet". Make sure persistance is on for both files and varibles.

   <img src="../kaggle-img/kaggle-internet.png" alt="image" width="" height=""> 

f. Turn on T4 X2 GPUs in accelerator.           

   <img src="../kaggle-img/kaggle-gpu.png" alt="image" width="" height=""> 

‎ 
g: (Optional) Turn on headless mode so you can run so you can run the GPU on all sessions and save your progress. Go to the top right and click "Save version" then open the advanced dropdown.

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
## Usage
***

Now that you have the web interface running via Kaggle, the rest of the process is **identical to using a local installation.**

For *mostly* all subsequent steps, including audio routing, application settings, and model usage, please continue by following the Local PC guide.

[!button text="Continue with the Local PC Guide" icon="arrow-right" target="blank"](https://docs.aihub.gg/realtime-voice-changer/local/tg-develops-w-okada-fork/#voice-models)



***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/rvc/contributions/)
:::
