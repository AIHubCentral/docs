---
icon: chevron-right
order: 4000
---

``Last update: May 5, 2025``

***
:::
###### ‎
:::content-center
## Introduction ‎
:::
- This cloud version is hosted in <u>[Google Colab](https://docs.aihub.gg/extra/glossary/#google-colab)</u>, remember that you have a GPU runtime of 4 hours.
- **YOU WILL NEED TO HAVE A COLAB PAID TIER SUBSCRIPTION TO USE THIS AS WEB UIS AREN'T ALLOWED IN THE FREE TIER**

***

###### ‎   
### Installation
###### ‎  
#### 1. <u>Installation Cells</u>
a. Click <u>[here](https://colab.research.google.com/github/deiteris/voice-changer/blob/master-custom/Colab_RealtimeVoiceChanger.ipynb)</u> to access the colab. Then starting from the top run the first cell:

   <img src="../colab-img/colab1.png" alt="image" width="900" height=""> 

a2. When it's done, which may take a couple of minutes, it will output `Done! Proceed with the next steps`.

b. Run the second cell:

   <img src="../colab-img/colab2.png" alt="image" width="600" height=""> 

***

###### ‎   
### Ngrok & Sever Setup
###### ‎  
#### 2. <u>Ngrok Setup</u>
a. Scroll down to the last cell and you should see a section where you put your ngrok token. If you dont have a ngrok acount sign up <u>[here](https://ngrok.com/)</u>.             
     a2. Once you have an acount you can authenticate your ngrok tunnel agent here: https://dashboard.ngrok.com/get-started/your-authtoken   
‎       
b. When you have your ngrok token place it in the text box that says `TOKEN_HERE`

   <img src="../colab-img/colab3.png" alt="image" width="600" height="">  

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

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/rvc/contributions/)
:::
