---
icon: chevron-right
order: 5000
---

``Last update: March 22, 2026``

***
:::content-center
## Introduction
:::
- This is a [cloud-based](https://docs.aihub.gg/extra/glossary/#cloud-based) alternative to run [Wokada Tg-Develop's Fork](https://docs.aihub.gg/realtime-voice-changer/local/tg-develops-w-okada-fork/#virtual-audio-cable), Realtime Voice Changer for calls/games, only for people who don't have a good PC GPU, via the [Google Colab Service](https://docs.aihub.gg/extra/glossary/#google-colab).

!!!danger Google Colab Service
**Check the [Google Colab Glossary](https://docs.aihub.gg/extra/glossary/#google-colab) for more info on Free Tier, Limits, Verification, Pricing and other things.**
!!!

!!!danger
You need the Google Colab Paid Tier to run this, as it uses a Web User Interface, else you could risk getting disconnected or banned off Colab.
!!!

!!!warning Server Audio not available
**NOTE: ⚠️ "Server audio not available" is normal on cloud platforms as they have no physical sound card. Always use Client mode for audio input/output.**
!!!


***
## Virtual Audio Cable

#### A Virtual Audio Cable (VAC) is what you need to use the realtime voice changer on Discord & Games.

- A VAC (Virtual Audio Cable) makes a fake audio device, used to re-route the audio of different programs.
- In AI Realtime Voice Changing context, it's used to get the output of AI Converted Voice Output as the input in other programs such as Discord.

!!! For Windows
Download this: [VAC Lite (Virtual-Audio-Cable by Muzychenko)](https://software.muzychenko.net/freeware/vac470lite.zip).
(Be sure to not use any toher vac like VB Audio Cable.)
!!!

- Run `setup64`, not 64a, after extracting the zip to a new folder

- After installing the VAC Lite, it changes your default audio system. Click **Yes** when it asks you to open the audio device settings (or press WIN+R, type "mmsys.cpl" if you closed it already), and change your **Recording** and **Playback** devices back to your usual devices. Same for communications device aswell (right click -> set as default communication device)

!!! For Mac
Download either: 
[Blackhole Virtual Audio Cable](https://existential.audio/blackhole)
or
[VB-Audio](https://vb-audio.com/Cable)
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
## Installation
###### ‎  
#### 1. Installation Cells
a. Click [here](https://colab.research.google.com/github/tg-develop/voice-changer/blob/master-custom/Colab_RealtimeVoiceChanger.ipynb) to access the colab. Then starting from the top run the first cell:

   <img src="../colab-img/colab1.png" alt="image" width="900" height=""> 

a2. When it's done, which may take a couple of minutes, it will output `Done! Proceed with the next steps`.

b. Run the second cell:

   <img src="../colab-img/colab2.png" alt="image" width="600" height=""> 

***

###### ‎   
### Ngrok & Sever Setup
###### ‎  
#### 2. Ngrok Setup
a. Scroll down to the last cell and you should see a section where you put your ngrok token. If you dont have a ngrok acount sign up [here](https://ngrok.com/).
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
## Usage
***

Now that you have the web interface running via Kaggle, the rest of the process is **identical to using a local installation.**

For *mostly* all subsequent steps, including audio routing, application settings, and model usage, please continue by following the Local Guide.

[!button text="Continue with the Local Guide" icon="arrow-right" target="blank"](https://docs.aihub.gg/realtime-voice-changer/local/tg-develops-w-okada-fork/#voice-models)


***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/rvc/contributions/)
:::
