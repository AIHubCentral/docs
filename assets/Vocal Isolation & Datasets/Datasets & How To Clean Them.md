*``Written by Julia``*      
``Last update: Jan 27, 2024``   
***
###### ‎
:::content-center
## What's a Dataset?
:::
- In the field of AI, it's the collection of data used to train an AI model.        
It contains examples of the inputs the model is expected to handle, along with the correct outputs.

- In the context of **RVC**, it's an audio file that is fed to RVC, containing the voice the model is going to replicate. It can be either a speaking or singing voice.

- Overall, the **quality** & **length** of the dataset are the biggest determining factors of the final quality of the model.     
Let's explain.
***
###### ‎
:::content-center
## About Length
:::
###### ‎
- For beginners we recommend sticking with **10 minutes**, or 20 if you want it very high quality.        

- If you wish to go for more, keep in mind, usually anything further than 40 minutes isn't necessary.      

- With modern versions of RVC, the dataset can be just a single audio file, no need to split it in multiple files.  


***
###### ‎
:::content-center
## About Quality
:::
###### ‎
Here are some general recommendations/requirements for a quality dataset:   
‎   
#### :icon-chevron-down: Great range.
- Vocals must be clear, hit low/high notes, & pronounce every vowel correctly. And of course, the dataset must contain the voice of a single person, not multiple ones.

#### :icon-chevron-down: Clean vocals.
- Ensure there isn't background noise, reverb, overlapping voices, music, distortion, or small silences. You'll learn more in the **Cleaning Datasets** section below.

#### :icon-chevron-down: Good audio quality.
- It's better if the audio format is a [<u>lossless</u>](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/) one like **WAV** or **FLAC**, not a lossy one like MP3.

#### :icon-chevron-down: No silibance/popping.
- Additionally, it's best if they don't include harsh silibance (loud "S" & "SH" pronounciation) or popping sounds (loud "P" sound).
***
###### ‎
:::content-center
## Cleaning Datasets
:::
*`Credits to Litsa & Faze Masta`*     
*`for the information`*      

‎   
First, clean the undesired noises explained before using an **audio isolation** software. Learn more [<u>here</u>](https://aihubdocs.github.io/en/vocal-isolation--datasets/uvr5--mvsep/).       
Keep reading once you're done.          

‎       
Now, to minimize (even more) background noise, remove silences & distorsion, we'll use tools from Audacity. A free, simple & very light-weighted [<u>DAW</u>](https://aihubdocs.github.io/enother/glossary/#daw).       
Download [<u>here</u>](https://www.audacityteam.org/download/).

Here's how you use it:  
‎   
#### Step 1: <u>Noise Gate.</u>     
- First input your dataset by dragging the audio file into the app.       
- Press CTRL + A to select the whole audio.       
- Navigate to the ``Effect`` menu at the top, go to `Noise removal and Repair` and select ``Noise Gate``,   
Use these exact settings:      
‎       
 <img src="../datasets-img/1.png" alt="image" width="420" height="auto">   

‎
#### Step 2: Truncating Silence.    

Again go to Effect, Special, & select ``Truncate Silence``.     
Use the following settings:         

 <img src="../datasets-img/6.png" alt="image" width="420" height="auto">    

‎
#### Step 3: Audio Normalization.    
And finally go to Effects, Volume and Compression, ``Normalization``, & use the following settings:

 <img src="../datasets-img/3.png" alt="image" width="420" height="auto">  

‎
#### Step 4: Export.
a. Go to File and click ``Export Audio``.       
‎   
 <img src="../datasets-img/4.png" alt="image" width="370" height="auto"> 
‎       
‎       
b. In **Save As Type** select ``FLAC``.     
**Level** must be ``8``.         
And **Bit depth** of ``24 bit``.            

    <img src="../datasets-img/5.png" alt="image" width="650" height="auto">

And that's all! You have now cleaned your dataset.      
***
###### ‎
:::content-center
## Tips for Recording Yourself
:::
If you are making a model of yourself, here are some **<u>tips</u>** (not requirements):
- Record while reading anything, like a book.
- Warm up your voice.
Clear your throat & read out loud before starting.
- Make it natural, not robotic. 
- Pronounce every vowel correctly.
- Hit low & high notes. Don't have to exaggerate it if you don't need to.
- Get close to the mic, not too much to avoid silibances/popping
- Avoid background noise. Close windows, door, turn off the computer, unplug fridge, etc.
- Don't be in a room with reverb.
- Be in a small-to-medium sized room with lots of stuff in it, specially soft like beds, couches, pillows, etc.
- Have a good posture, it's good for breath support.
- Have a drink at your side to not dehydrate.
***
:::content-right
||| *Did I miss anything?*        
Send any feedback [<u>here</u>](https://forms.gle/5i6hTJRVkXRohvVF9) 👈
|||
::: 
