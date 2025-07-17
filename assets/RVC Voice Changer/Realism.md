---
icon: person
order: 1000
visibility: private
---
``Last update: July 4, 2025``

:::content-center
## Introduction
:::
- In this guide it will be explained how to increase the realism of a RVC model while using W-Okada.

- We will go over installing and setting up Voicemeeter, adding VST's using Light Host and how to make your voice sound more convincing. 

***

## Good Practices

- Using a model that is similar to your voice helps a bit. Best case scenario you have the pitch set to 0 and you don't have to act like the voice.

- Index can help a bit by adding some of the models accent into the converted voice. 

- Acting like the voice you are trying to be also helps. 

- Some users think that models trained on the f0 extractors crepe and fcpe give models a "human softness" to them while rmvpe can sometimes give a "metalic sound" to them. It would be good to try models trained on rmvpe or fcpe to see which one you think sounds more real.


***
## Installing Voicemeeter
***

1. Download Voicemeeter from <u>[here](https://download.vb-audio.com/Download_CABLE/VoicemeeterSetup_v2119.zip)</u>. You can either install Voicemeeter Banana or Potato. 

2. Unzip the folder then run `voicemeeterprosetup.exe`. 

3. Once you run it you should get this popup. Click install.

<img src="../realism-img/meeter.png" alt="image" width="700" height="">

It's already installed for me so that is why it says "Remove".

4. Restart your computer once you have finished downloading it.

***
### Voicemeeter Setup
***

1. Open Voicemeeter and in the top right "Hardware Out" should be flashing red, if it's not you can skip these 2 steps. 

<img src="../realism-img/hardware.png" alt="image" width="500" height="">

2. Click A1 and set it to your headphones then click A1 again then click remove selection. If your Hardware Out isn't flashing anymore that's good. We do not want voicemeeter removing our system sounds so that is why we do this step.

3. Go to "Stereo Input 1"

<img src="../realism-img/stereo.png" alt="image" width="400" height="">

4. Click it and select `Line 1` so whatever is sent through line 1 is sent to voicemeeter. If you want you can also right click "Stereo Input 1" to rename it to something.

<img src="../realism-img/inputs.png" alt="image" width="700" height="">

5. Once you have done that set it to output to B1.

<img src="../realism-img/b2.png" alt="image" width="200" height="">

6. Then go here and set both the outputs to B1.

<img src="../realism-img/b1virt.png" alt="image" width="300" height="">


7. Once you have completed all of the above steps you can now go into anything and set the mic input to "Voicemeeter Out B1". You will not be able to hear whatever is sent through B1 so you will have to use whatever game's or discord's mic test to hear it. 

<img src="../realism-img/discord1.png" alt="image" width="700" height="">


8. (Optional) If you want to decrees delay press `ctrl + ,` and a menu should open. In the menu go down to where the buffer settings are and set the samples to 480. If you hear crackling or audio bugs increase the buffer size and if there is no crackling and you want less delay you can lower the buffer size more.

<img src="../realism-img/buffer.png" alt="image" width="600" height="">


***

### W-Okada Setup

This is pretty simple.


Set `Input:` Your mic

Set `Output:` Line 1

Set `Monitor:` Your headphones if you want to hear the model



***
## Installing Light Host
***

1. Download <u>[Light Host](https://github.com/rolandoislas/LightHost/releases/download/v1.2.1/Light.Host.1.2.1.Win64.zip)</u>.

2. Unzip the folder then run `Light Host.exe`


***
### Light Host Setup
***

1. Open Light Host and go into 'Preferences'

<img src="../realism-img/pref.png" alt="image" width="300" height="">

‎

2. Set your 'Audio device type' to "DirectSound"

<img src="../realism-img/sound.png" alt="image" width="600" height="">

‎

3. Set your output to "Voicemeeter Input" And your input to "Line 1"

<img src="../realism-img/light.png" alt="image" width="400" height="">

‎

4. In advanced settings set your "Sample rate" to 44.1k and the "Audio buffer size" to 480. If you hear crackling increase the buffer size and if there is no crackling and you want less delay you can lower the buffer size more.

<img src="../realism-img/adv.png" alt="image" width="500" height="">

***
## VSTs & Background Noise
***

### VSTs

- First you will need some VST's, you can find plenty of free ones at <u>[Kilohearts website](https://kilohearts.com/products/kilohearts_essentials)</u>. I suggest their Bitcrush, Filter and Phase Distortion but you can use whatever VSTs you want.

- There is no "prefect setting" for these VSTs so set their settings to whatever you think sounds good.


!!!danger
The more VSTs you add the more delay there is going to be.
!!!

***

1. To add a VST to Light Host open it then click "Edit Plugins".

<img src="../realism-img/pref-vst.png" alt="image" width="300" height="">

‎

2. Go down to options, click it and then click scan for VST or VST3 plugins.


<img src="../realism-img/scan.png" alt="image" width="500" height="">

‎

- It should compile a list of all your plugins. At that point you can close that menu, reopen Light Host and there should be a "Available Plugins" section. Just click plugin and it should open a sub-menu where you can add plugins.

3. To edit them click on the plugin then click 'Edit'. It will open the plugin's menu so you can edit it.

<img src="../realism-img/plugins.png" alt="image" width="500" height="">

***
### Background Noise

- First you are going to need noise to play, you can get those at <u>[freesound](https://freesound.org/)</u> or just record your own room noise using Audacity.


1. When you have the noise you want you are going to need to open "Windows Media Player" then drag the audio you downloaded into it. 

2. Then you are going to need to go into windows "Sound Settings" then "Advanced sound options".

<img src="../realism-img/sounds.png" alt="image" width="500" height="">

‎

3. Scroll until you see "Windows Media Player" and set its output to "Voicemeeter AUX Input".

<img src="../realism-img/volume.png" alt="image" width="500" height="">

‎

4. Then go back in "Windows Media Player" and hit play on your noise. Don't forget to turn on repeat so it doesn't randomly stop.

***
### VST & Bg Noise Examples

Here are some examples of what you can do with Kilohearts VSTs and Bg noise.
Here is the clean audio for reference. 

<audio controls>
  <source src="../audio/clean-sample.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

‎

- **Remember that these are just examples and you can change them to fit your needs or wants.**

***

#### Bitcrush
- Here is what you can do with these bitcrush settings. 

<img src="../realism-img/bitcrush-ex.png" alt="image" width="250" height="">

<audio controls>
  <source src="../audio/bitcrush-sample.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

***
#### Phase Distortion 
- Here is what you can do with these phase distortion settings. 

<img src="../realism-img/phasedistortion-ex.png" alt="image" width="250" height="">

<audio controls>
  <source src="../audio/phase-sample.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

***
#### Bg Noise
- Here is what you can do with adding background noise. 

<audio controls>
  <source src="../audio/bgnoise-sample.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

***
#### Filter
- Here is what you can do with this filter setting. 

<img src="../realism-img/filter-ex.png" alt="image" width="250" height="">

<audio controls>
  <source src="../audio/filter-sample.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>



***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::