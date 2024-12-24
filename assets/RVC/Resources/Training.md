---
icon: chevron-right
order: 1000
---

``Last update: Dec 24, 2024``
***
:::content-center
## Introduction
:::
- In this guide it will be explained how to **properly** train a model from start to finish.

- **Properly** training a model is just as important as having a great dataset.

- It won't be explained how to prosess a dataset and how to acutally train a model since that is difference from fork to fork, please look at the guide for your fork to find this info. 
***
:::content-center
## Epochs & Overtraining
:::

- "Epoch" is a unit of measuring the training cycles of an AI model.     

- In other words, the amount of times the model went over its <u>[dataset](https://docs.ai-hub.wtf/rvc/resources/datasets/)</u> and learned from it.         
#### *:icon-chevron-right: How many epochs should I use for my dataset?*
- There isn't a way to know the right amount previous to training. It depends on the size, length & quality of the dataset.

- If you aim towards a quality model, it's not convenient to input a semi-arbitrary amount of epochs, as it makes it prone to underfitting/overtraining. (explained later)

- So it's best to use TensorBoard. WIth it you can determine **exactly** for how long you should train. (explained later)  
#### *:icon-chevron-right: Do more epochs equal a better model?*
- It doesn't, since using a disproportionate amount will overtrain the model, which will affect the quality of it.                 
- In the field of AI, is when an AI model learns its <u>[dataset](https://docs.ai-hub.wtf/rvc/resources/datasets/)</u> too well, to the point where it centers too much around it & starts replicating undesired data.

- The model performs very well with data of the dataset, but poorly with new data, as it has lost its ability to replicate anything that deviates from it.

- It happens when the model is trained for **too long**/is too complex. So to avoid this, RVC users use a tool called ***TensorBoard***.

#### *:icon-chevron-right: What is overtraining?*

- Overtraining also know as overfitting is where the model doesn't actually learn the underlying patterns of the data and memorizes them instead. 

- A sign of overfitting is when the sibilances are super robotic or when the graphs in the Tensorboard are going up.


***
:::content-center
## Batch Size & Precision
:::
### Batch Size

- A batch size is the number of training examples used in one iteration before updaing the model's parameters.

- A smaller batch size ( Less then 8 ) is better for smaller datasets, uses less memory, updates parameters more and has noisy gradients.

- A larger batch size ( More then 8 ) is better for large datasets ( over an hour ) uses more memory, has smooth gradients and trains faster. 

- Usually a batch size of 8 is the best for most models with a dataset of around 30 minutes, anything less it is advisable that you use a smaller batch size and for a dataset of 1 hour or more you should increase the batch size.

***
### Precision 

In RVC there are currently two precisions, FP16 and FP32. There is barely an audiable difference between the two so it is up to you on what precision setting you want to use. 

!!!
FP means floating point. 
!!!

||| **FP16's Pros:**
- Faster then fp32
- Less VRAM needed
||| **FP16's Cons:**
- Exploding gradients
- Lots of NaNs
- Unable to train from scratch
||| **FP32 Pros:**
- More stable gradients
- No NaNs
||| **FP32 Cons:**
- Slower then fp16
- Requires more VRAM
|||

***
:::content-center
## Pretrains
:::

Pretrains are an integral part of making a model, they are basically models that have been trained with many different types of voices, genders, ages, languages, manor of speech and are much longer then normal models. The objective of pretrains is to reduce training time and increase the quality of your model.

 <img src="../pretrain-img/pretrain.png" alt="image" width="1000" height="auto">

- There are three types of pretrains:
     - Scratch: Trained with no previous pretrain.
     - Finetune: Trained with a pretrain.
     - Merge: Made by merging pretrains. (These are considered the worst)
***
###### ‎ 
### How do i use Pretrains?

[!badge size="xl" variant="success" text="Applio"]        
- Go into the training tab and check the 'Custom Pretrained' box and use the drop down to select the pretrain's D and G file.
     - If you dont see a pretrain in the dropdown that means you need to download a pretrain, go into the 'Downloads' tab then go to 'Download Pretrained Models' then use the dropdown to select your sample rate and what pretrain you would like to download, then finally click download.
     - If you want to upload pretrains manually go into your Applio folder then go to `rvc\models\pretraineds\pretraineds_custom` and place your D and G files there.

[!badge size="xl" text="Mainline"] 
- Asssuming you have the pretrain you want to use go into your mainline folder then go to `assets\pretrained_v2` and place you D and G files there.
- Then in the 'Train' tab near the train button you can input the location of your pretrain, replace the ending so it's the name of the pretrain you put in `pretrained_v2`. 

<img src="../pretrain-img/pretrain-mainline.png" alt="image" width="200" height="auto">

***
###### ‎ 
### Where do i find Pretrains?       
You can find all of the community made pretrains in the "pretrain-models" channel in AI HUB. 

Here is a quick list of all publicly available pretrains: 

Name   | 32k Download | 40k Downaload | 48k Download
---    | ---
DMR V1 by Razer | [32k](https://huggingface.co/Razer112/DMR_Pretrain/tree/main) | - | - 
Itaila V1.0 by Ilaria | [32k](https://huggingface.co/TheStinger/itaila/tree/main) | - | - 
IMA by Loren85 | [32k](https://huggingface.co/Loren85/IMA-TEST-V1/tree/main) | - | - 
KLM 4.1 by SeoulStreamingStation | [32k](https://huggingface.co/SeoulStreamingStation/KLM4.1/tree/main) | - | [48k](https://huggingface.co/SeoulStreamingStation/KLM4.1/tree/main) 
KLM 4.2 by SeoulStreamingStation | - | [40k](https://huggingface.co/SeoulStreamingStation/KLM4.2_TestVersion/tree/main) | - 
KLM BeatzForge by SeoulStreamingStation | [32k](https://huggingface.co/SeoulStreamingStation/KLM_BEATMASTER/tree/main) | - | [48k](https://huggingface.co/SeoulStreamingStation/KLM_BEATMASTER/tree/main) 
Nanashi V1.7 by shiromiya | [32k](https://huggingface.co/shiromiya/nanashi-pretrain/tree/main/v1.7) | - | - 
Nanashi Anime v1 by shiromiya | [32k](https://huggingface.co/shiromiya/nanashi-pretrain/tree/main/v1_anime) | - | - 
Ov2 Super by SimplCup | [32k](https://huggingface.co/poiqazwsx/Ov2Super32kfix/tree/main) | [40k](https://huggingface.co/ORVC/Ov2Super/tree/main) | [48k](https://huggingface.co/ORVC/Ov2Super/tree/main) 
RIN_E3 by MUSTAR | - | [40k](https://huggingface.co/MUSTAR/RIN_E3/tree/main) | - 
Rigel by MUSTAR | [32k](https://huggingface.co/MUSTAR/Rigel-rvc-base-pretrained-model/tree/main/Rigel_32k_Base_and_FineTuned/FineTuned-model_32k_fp32) | [40k](https://huggingface.co/MUSTAR/Rigel-rvc-base-pretrained-model/tree/main/Rigel_40k_Base_and_FineTuned/FineTuned-model_40k/Alpha) | - 
SingerPreTrain by Sztef | [32k](https://huggingface.co/Sztef/SingerPreTrained/tree/main/update) | - | - 
Snowie by MUSTAR | - | [40k](https://huggingface.co/MUSTAR/SnowyRuPretrain_EnP_40k/tree/main) | [48k](https://huggingface.co/MUSTAR/SnowyRuPretrain_EnP_48k/tree/main) 
SnowieV3 X RIN_E3 by MUSTAR | - | [40k](https://huggingface.co/MUSTAR/SnowieV3.1-X-RinE3-40K/tree/main) | - 
SnowieV3.1 by MUSTAR | [32k](https://huggingface.co/MUSTAR/SnowieV3.1-32k/tree/main) | [40k](https://huggingface.co/MUSTAR/SnowieV3.1-40k/tree/main) | [48k](https://huggingface.co/MUSTAR/SnowieV3.1-48k/tree/main) 
TITAN by blaise-tk | [32k](https://huggingface.co/blaise-tk/TITAN/tree/main/models/medium/32k/pretrained) | [40k](https://huggingface.co/blaise-tk/TITAN/tree/main/models/medium/40k/pretrained) | [48k](https://huggingface.co/blaise-tk/TITAN/tree/main/models/medium/48k/pretrained) 
UKA by PlasmaTi | [32k](https://huggingface.co/Plasmati/Pretrains/tree/main) | - | - 

***
###### ‎ 
### How do i make Pretrain?      
Creating a pretrain is pretty much the same as training a normal model but the dataset is bigger and longer. 

There are two ways of making a pretrain the first being:
- From scratch which means you don't use a pretrain when training this. To make a decent from scratch pretrain you are going to need at **least** 50 hours of low, mid and high quality speech with many different speakers. 
The second way being:
- Finetuning which means you use a pretrain to train this pretrain. To make a good you are going to need at **least** 10 hours of high quality speech with many speakers.
     - The big pro of making a Finetune is that you can tailor it to anything, like you can tailor it to improve a certain language, improve accents, types of speech and more. It can even improve the graphs (like grads, g/total etc.) if trained properly.
***
###### 
### Misc        
This section contains miscellaneous information about pretrains. 

+++ GPU 
To make a pretrain you are going to need a pretty good GPU, because without one it will take a very long time to train. Here is a GPU tier list for training pretrains:
- S Tier:
     - H100
     - A100 (80gb and 40gb)
- A Tier:
     - L40S
     - 4090
     - 4080 (Super)
- B Tier:
     - 4070 (Ti) (Super)
     - V 100
     - 3090 (Ti)
     - A40
- C Tier:
     - 4070 (Ti)
     - 3080 (Ti)
     - 3070 (Ti)
     - P 100
- D Tier:
     - L4
     - A10, T4
     - 4060 (Ti) (8/16gb)
     - 3060 (Ti)

+++ Batch Size
Batch size refers to the amount of samples used in one iteration. Batching is used to improve performence by using parallel processing instead of individual sample processing.

For RVC this means it can influence how well temporal dependencies are captured. A small batch size like 4 and below won't capture the variability in the audio, while a high batch size like 16 and above might smooth out these variations too much causing bad graphs.

Low Batch Size:
- Pros: Less memory consumption, better generalization, less prone to overtraining.
- Cons: Slower training due to reduced parallelism, potentially less stable gradient updates.

High Batch Size:
- Pros: Faster training due to increased parallelism, more stable gradient updates, potentially better convergence.
- Cons: Higher memory requirements, might lead to overtraining if the dataset is small.

+++ Q&A
Q: What is the best pretrain? 

A: There is no "best pretrain" it all depends on your needs and what you're ok with sacrificing to get those benefits.  
+++

***
:::content-center
## Tensorboard
:::

- TensorBoard is a tool that allows you to visualize & measure the training of an AI model, through graphs & metrics.

- It's specially useful for determining when to stop training a voice model, since with it you can detect when the <u><u>[overtraining</u>](https://docs.ai-hub.wtf/rvc/resources/epochs--tensorboard/#overtraining)</u> point begins.    

- Because of this, TB is the most convenient tool for RVC users for perfecting a voice model.     
***
###### ‎
### :icon-chevron-down: Installing & Opening

!!!success
For <u>[RVC Disconnected</u>](https://docs.ai-hub.wtf/rvc/cloud/rvc-disconnected/) users, ignore this, it opens up by itself when you start training.
!!!

###### ‎       
1. Download this file & move it inside RVC's folder. Ensure the file path doesn't contain spaces/special characters.
  
    [!file](./tensorboardfiles/TensorVENV.bat)    
###### ‎
2. Now execute it. It will open a console window & create some folders inside RVC.    
    - If you get the `Windows protected your PC` issue, click <u>**More info**</u> & **Run anyway**.         
‎   
3. Once it's done, your default browser should open with TensorBoard app.           
‎  
    - If it doesn't, copy the address of the console at the bottom, and paste it in your browser.       
    Said address will say "**https://localhost**" followed by some numbers.     
    ‎  
    <img src="../tensorboard-img/11.png" alt="image" width="500" height="auto">

***
###### ‎
### :icon-chevron-down: Usage Guide
    
+++ Simple Guide
###### ‎     
#### :icon-chevron-down: <u>SETTING UP</u>
***
- Open TB & begin training in RVC.     

    - If you get the ``No dashboards are active`` issue, select `SCALARS` in the top right corner dropdown.

        <img src="../tensorboard-img/17.png" alt="image" width="230" height="auto">‎    
‎       
- First ensure **auto-refresh** is on, so the graphs update constantly.    

    Click the gear (:icon-gear:) in the top left corner & turn on **``Reload data``**.      
    You can always manually refresh with the refresh symbol (🔄) in the top right.  
            
    <img src="../tensorboard-img/2.png" alt="image" width="280" height="auto">
       
    ‎       
- Go to the `SCALARS` tab.      
        ‎       
        <img src="../tensorboard-img/12.png" alt="image" width="280" height="auto">     
        ‎        

***
#### :icon-chevron-down: <u>GRAPH</u>
***
- #### In the left panel:  
    1. Activate `Ignore outliers in chart scaling`.  

    2. Set **Smoothing** to ``0.987``.     

    3. Select your model in the `Runs` section below. The models you tick will show in the graphs. (untick `/eval` if you want)        
    ‎       
    <img src="../tensorboard-img/18.png" alt="image" width="240" height="auto">‎      
‎       
- In the search bar, type "**g/total**". This will be the graph you'll monitor.        
    ‎   
        <img src="../tensorboard-img/19.png" alt="image" width="390" height="auto">‎        
‎    
‎  
- Each graph has three buttons in the corner:       
    - Left one is for going **fullscreen**.       
    - Middle one to **disable** Y axis, for a fuller view.       
    - And the right one is to **center** the view.      
        ‎       
        <img src="../tensorboard-img/15.png" alt="image" width="300" height="auto">‎    
‎       
- To **zoom** in & out the graphs, press the ALT key + mouse wheel. Remember to center the view after moving around, and after the graph updates.
***
 #### :icon-chevron-down: <u> MONITORING</u>
***
- Now let the training go for some time.  

- You'll detect **OT** (overtraining) when the graph hits the **lowest point**, then stay **flat**/**rising** indefinitely.  
    ‎       
     **<u>Example of OT:</u>**
        
    <img src="../tensorboard-img/10.png" alt="image" width="370" height="auto">‎     
    ‎    
- There will be various low points, one after the other, so don't get too anxious if it's OT or not. You can always use a previous checkpoint either way.

- If it reaches a low point, let it run for **longer** until it's **very clear** it's OT.

- When you detect OT go into the search bar and look for `mel`, 

    <img src="../tensorboard-img/mel.png" alt="image" width="500" height="auto">‎

- Then zoom out & lower the smoothening to 0. Then look for low points named local minima.

    <img src="../tensorboard-img/min.png" alt="image" width="600" height="auto">‎    

- Then over your mouse over the local minimas and take note of the step counts. Find all of the epochs connected to those step counts and then use them all to find the one that sounds best to you.

> If you want you can just use the lowest mel point.

+++ Advanced Guide ‎     
#### :icon-chevron-down: <u>Other Graphs</u>
***

#### `FM` Feature Matching: 
FM shows how well the generator is able to make synthetic data that has similar features to the dataset.

If the graph is decreasing that indicates that the generator is able to make audio that has similar features to the dataset.

> you can think of this as how well the model can match timbral, spetial, temporal characteristics. 
***

#### `KL` Kullback-Leibler: 
KL makes the generator create similar distribution of latest variables to real data. The KL loss ensures that the generator is not just memorizing real data but it's learning to capture the underlying patterns in the data. 

If the graph is decreasing that shows that the generator is making audio with similar distribution of latent variables to real data.

> You can think of this as how well it can replicate the speakers style. 
***

#### `Mel` Mel Spectrogram: 
 The mel spectrogram loss compares both the real and synthetic mel spectrograms. This loss encourages the generator to produce audio that sounds similar to the dataset.

 If the graph is decreasing that shows that the generator is producing audio with similar spectral distribution to the dataset.

 > you can think of this as clarity / fidelity.
***

#### `d/total` Discriminator Loss: 
d/total shows how well the discriminator is able to differentiate between real and generated audio. 

If the graph is decreasing that means the discriminator is becoming better at distinguishing between real and synthetic data which usually means that the generator is producing realistic audio. 
***

***
#### :icon-chevron-down: <u>Mel Images</u>
***
 While looking through the Tensor Board you may come across `slice/mel_gen` and `slice/mel_org`. 
#### slice/mel_gen: 
Is a mel spectrogram view of audio that the generator created in attempt to make it match `mel_org`.
<img src="../tensorboard-img/mel_gen.png" alt="image" width="700" height="700">‎ 

***

#### slice/mel_org:
Is a mel spectrogram view of audio from your dataset. 
<img src="../tensorboard-img/mel_og.png" alt="image" width="700" height="700">‎ 

***
+++


:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/contributions/)
:::