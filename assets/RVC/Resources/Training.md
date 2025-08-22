---
icon: chevron-right
order: 1000
---

``Last update: May 5, 2025``
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

- In other words, the amount of times the model went over its <u>[dataset](https://docs.aihub.gg/rvc/resources/datasets/)</u> and learned from it.         
#### *:icon-chevron-right: How many epochs should I use for my dataset?*
- **There isn't a way to know the right amount previous to training.** It depends on the length, quality and diversity of the dataset.

- If you aim towards a quality model, it's not convenient to input a semi-arbitrary amount of epochs, as it makes it prone to underfitting/overtraining. (explained later)

- So it's best to use TensorBoard. With it you can determine **exactly** for how long you should train. (explained later)  
#### *:icon-chevron-right: Do more epochs equal a better model?*
- **No it doesn't**, since using a disproportionate amount will overtrain the model, which will affect the quality of it.                 
- In the field of AI, is when an AI model learns its <u>[dataset](https://docs.aihub.gg/rvc/resources/datasets/)</u> too well, to the point where it centers too much around it & starts replicating undesired data.

- The model performs very well with data of the dataset, but poorly with new data, as it has lost its ability to replicate anything that deviates from it.

- It happens when the model is trained for **too long**/is too complex. So to avoid this, RVC users use a tool called ***TensorBoard***.

#### *:icon-chevron-right: What is overtraining?*

- Overtraining also know as overfitting is where the model doesn't actually learn the underlying patterns of the data and memorizes them instead. 

- Some signs of overfitting are when the sibilances are robotic, when the graphs in the <u>[Tensorboard](https://docs.aihub.gg/rvc/resources/training/#tensorboard)</u> are going up or when the model is unable to produce high end harmonics because it's learning your dataset to well and your dataset doesn't have these high end harmonics. 

<img src="../tensorboard-img/overtrained.png" alt="image" width="1000" height="700">‎

This image is a bit extreme but it gives you a good idea. If you notice your model is poorly creating high end harmonics try using a model several epochs back.



***
:::content-center
## Batch Size
:::
A batch size is the number of training examples used in one iteration before updaing the model's parameters. For 30+ minutes of data batch size 8 is recommended and for less than 30 minutes batch size 4 is recommended.

- Smaller batch size:
    - Promotes noisier, less stable gradients.
    - More suitable when your dataset is small, less diverse or repetitive.
    - Can lead to instability / divergence or noisy graphs.
    - Generalization might be improved.
‎ 
- Bigger batch size:
    - Promotes smoother, more stable gradients.
    - Can beneficial in cases where your dataset is big and diverse.
    - Can lead to early overtraining or flat / 'stuck' graphs.
    - Generalization might be worsened.

***
:::content-center
## Pretrains
:::

Pretrains are an integral part of making a model, they are basically models that have been trained with many different types of voices, genders, ages, languages, manor of speech and are much longer then normal models. The objective of pretrains is to reduce training time and increase the quality of your model. To make a model without a pretrain you would need several hours of data to make anything decent. 

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

You can find all of the community made pretrains in the "pretrain-models" channel in <u>[AI HUB](https://discord.gg/aihub)</u>. 

Here is a list of all publicly available pretrains: 

||| TITAN by blaise-tk
TITAN is a fine-tuned based on the original RVC V2 pretrained, leveraging an 11.15-hours dataset sourced from Expresso. It gives cleaner results compared to the original pretrained, also handles the accent and noise better due to its robustness, being able to generate high quality results. Like Ov2 Super, it allows models to be trained with few epochs.

- **32k Download:**
    - <u>[**D Download**](https://huggingface.co/blaise-tk/TITAN/resolve/main/models/medium/32k/pretrained/D-f032k-TITAN-Medium.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/blaise-tk/TITAN/resolve/main/models/medium/32k/pretrained/G-f032k-TITAN-Medium.pth?download=true)</u>
- **40k Download:**
    - <u>[**D Download**](https://huggingface.co/blaise-tk/TITAN/resolve/main/models/medium/40k/pretrained/D-f040k-TITAN-Medium.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/blaise-tk/TITAN/resolve/main/models/medium/40k/pretrained/G-f040k-TITAN-Medium.pth?download=true)</u>
- **48k Download:**
    - <u>[**D Download**](https://huggingface.co/blaise-tk/TITAN/resolve/main/models/medium/48k/pretrained/D-f048k-TITAN-Medium.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/blaise-tk/TITAN/resolve/main/models/medium/48k/pretrained/G-f048k-TITAN-Medium.pth?download=true)</u>
|||
||| Nanashi V1.7 by shiromiya
Nanashi V1.7 is a fine-tuned based on TITAN pretrained and made with 11 hours of Brazilian music, so it will work better with this language but it can work with other languages without any problems, like TITAN, it allows models to be trained with few epochs and handles the noise better.

- **32k Download:**
    - <u>[**D Download**](https://huggingface.co/shiromiya/nanashi-pretrain/resolve/main/v1.7/D_nanashi_v1_7.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/shiromiya/nanashi-pretrain/resolve/main/v1.7/G_nanashi_v1_7.pth?download=true)</u>
|||
||| Legacy Core by lyery
This is a perfect recreation of the original pretrain of RVC, which means you can train both speech datasets and singing datasets while also enjoying the benefits of the [Spin Embedder Model](http://docs.aihub.gg/rvc/resources/inference-settings/#spin). Every language supported, english pronunciation is vastly improved compared to the original pretrain, potential improvements in other languages as well. This recreation also has higher singing range than the og pretrain, and better generation of both speech and singing.


- Training Info:
    - dataset: vctk + m4singer
    - batch size: 32 x 2
    - f0: rmvpe
    - sample rate: 32k
    - embedder: SPIN
    - vocoder: hifigan 


<br>

- **32k Download:**
    - <u>[**D Download**](https://huggingface.co/lyery/legacy-core/resolve/main/D_lcore.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/lyery/legacy-core/resolve/main/G_lcore.pth?download=true)</u>
|||
||| KLM 4.1 by SeoulStreamingStation
KLM 4.1 is a fine-tuned based on KLM V7 pretrained and made with around 100 hours dataset (Korean vocal/speech, Japanese vocal/speech and English speech), so it will work better with those languages. Unlike typical pretrained models KLM is a pretrained model created to make vocal guides using short voice recordings from a studio, this means that even with short dataset high pitch information it is possible to implement high-pitched sounds but it is sensitive to noise so it is recommended to use it with high quality datasets

- **32k Download:**
    - <u>[**D Download**](https://huggingface.co/SeoulStreamingStation/KLM4.1/resolve/main/D_KLM41_32k.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/SeoulStreamingStation/KLM4.1/resolve/main/G_KLM41_32k.pth?download=true)</u>

- **48k Download:**
    - <u>[**D Download**](https://huggingface.co/SeoulStreamingStation/KLM4.1/resolve/main/D_KLM41_48k.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/SeoulStreamingStation/KLM4.1/resolve/main/G_KLM41_48k.pth?download=true)</u>
|||
||| KLM 4.2 by SeoulStreamingStation
KLM 4.2 maintains the same highly extensive pitch range as before and was developed to be able to handle high-pitched vocal inference even without having the corresponding vocal data of the model you wish to generate. KLM 4.2 was trained with 146 hours of data which mostly contains Korean, Japanese and some English.

- **32k Download:**
    - <u>[**D Download**](https://huggingface.co/SeoulStreamingStation/KLM4.2/resolve/main/D_KLM42_32k_x10.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/SeoulStreamingStation/KLM4.2/resolve/main/G_KLM42_32k_x10.pth?download=true)</u>

|||
||| KLM 4 by SeoulStreamingStation :icon-star-fill:
KLM 4 is the final HiFi-GAN pretrain that is going to be made by SSS. This version of klm is like all of the others but it follows the original structure of training and contains noise in the dataset so it can handle it better. This was trained with 800 hours of data, with a large portion of it being in Korean.

- **32k Download:**
    - <u>[**D Download**](https://huggingface.co/SeoulStreamingStation/KLM49_HFG/resolve/main/D_KLM_HFG_32k.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/SeoulStreamingStation/KLM49_HFG/resolve/main/G_KLM_HFG_32k.pth?download=true)</u>
- **40k Download:**
    - <u>[**D Download**](https://huggingface.co/SeoulStreamingStation/KLM49_HFG/resolve/main/D_KLM_HFG_40k.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/SeoulStreamingStation/KLM49_HFG/resolve/main/G_KLM_HFG_40k.pth?download=true)</u>
- **48k Download:**
    - <u>[**D Download**](https://huggingface.co/SeoulStreamingStation/KLM49_HFG/resolve/main/D_KLM_HFG_48k.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/SeoulStreamingStation/KLM49_HFG/resolve/main/G_KLM_HFG_48k.pth?download=true)</u>

|||
||| DMR V2 by Razer
This is a fine-tuned based on the original RVC V2 pretrained and made with 22 hours of dataset aimed towards e-girl, soft male/female and deep male/female voices.

- **32k Download:**
    -  <u>[**D Download**](https://huggingface.co/Razer112/DMR_Pretrain/resolve/main/D_DMR-V2.pth?download=true)</u>
    -  <u>[**G Download**](https://huggingface.co/Razer112/DMR_Pretrain/resolve/main/G_DMR-V2.pth?download=true)</u> 
|||
||| GuideVocalPretrain by Essid
GuideVocalPretrain is a fine-tuned pretrain based on the original pretrain. This contains 58 hours of Korean speech with the goal being to improve Korean speech.  

- **48k Download:**
    - <u> [**D Download**](https://huggingface.co/Essid/GuideVocalPretrain/resolve/main/D_GuideVocalPretrain.pth?download=true)</u> 
    - <u> [**G Download**](https://huggingface.co/Essid/GuideVocalPretrain/resolve/main/G_GuideVocalPretrain.pth?download=true)</u> 
|||
||| Itaila V1.0 by Ilaria
This is a fine-tuned pretrain based on the original pretrains and was made with 10 hours of Italian speech. Itaila was made to improve Italian speech.

- **32k Download:**
    - <u>[**D Download**](https://huggingface.co/TheStinger/itaila/resolve/main/ItaIla_32k_D.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/TheStinger/itaila/resolve/main/ItaIla_32k_G.pth?download=true)</u>
|||
||| IMA by Loren85
This is a fine-tuned pretrain based on the original pretrains and was made with 2 hours of robotic speech which aims to make robotic voices better.

- **32k Download:**
    - <u>[**D Download**](https://huggingface.co/Loren85/IMA-TEST-V1/resolve/main/D_2333333.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/Loren85/IMA-TEST-V1/resolve/main/G_2333333.pth?download=true)</u>
|||
||| KLM BeatzForge by SeoulStreamingStation
This is a fine-tuned pretrain based on the original pretrain that improves drum models. 

- **32k Download:**
    - <u>[**D Download**](https://huggingface.co/SeoulStreamingStation/KLM_BEATMASTER/resolve/main/D_BeatzForge_V2_32k.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/SeoulStreamingStation/KLM_BEATMASTER/resolve/main/G_BeatzForge_V2_32k.pth?download=true)</u>
|||
||| Nanashi Anime v1 by shiromiya
This is a fine-tuned pretrain based off of the original pretrain which aims to improve anime-style speech. This was train with 11 hours of speech.

- **32k Download:**
    - <u>[**D Download**](https://huggingface.co/shiromiya/nanashi-pretrain/resolve/main/v1_anime/normal/D_nanashi_anime_384e.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/shiromiya/nanashi-pretrain/resolve/main/v1_anime/normal/G_nanashi_anime_384e.pth?download=true)</u>
|||
||| Nezox V1 by noxty
Nezox is a fine-tuned pretrain based on the original pretrain. This pretrain contains 43 hours of Indonesian speech with the goal of the pretrain to make Indonesian speech better. 

- **32k Download:**
    - <u>[**D Download**](https://huggingface.co/theNeofr/Nezox/resolve/main/Nezox_32k_D.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/theNeofr/Nezox/resolve/main/Nezox_32k_G.pth?download=true)</u>
|||
||| OV2 Super by SimplCup
Ov2Super is a fine-tuned based on the original RVC V2 pretrained and made with 30 minutes dataset, works well for small datasets and English language, this pretrained was trained on a precisely chosen clean speech and singing dataset, with bright and emotional voices. Additionally, it allows models to train with very few epochs compared to regular pretrains.

- **32k Download:**
    - <u>[**D Download**](https://huggingface.co/poiqazwsx/Ov2Super32kfix/resolve/main/f0Ov2Super32kD.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/poiqazwsx/Ov2Super32kfix/resolve/main/f0Ov2Super32kG.pth?download=true)</u>
- **40k Download:**
    - <u>[**D Download**](https://huggingface.co/ORVC/Ov2Super/resolve/main/f0Ov2Super40kD.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/ORVC/Ov2Super/resolve/main/f0Ov2Super40kG.pth?download=true)</u>
|||
||| RIN_E3 by MUSTAR
This pretrain is made from scratch with a 140 hour dataset. It is suggested to use this with high quality datasets due to its sensitivity to noise.

- **40k Download:**
    - <u>[**D Download**](https://huggingface.co/MUSTAR/RIN_E3/resolve/main/RIN_E3_D.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/MUSTAR/RIN_E3/resolve/main/RIN_E3_G.pth?download=true)</u>
|||
||| Rigel by MUSTAR
Rigel is a fine-tuned pretrain based on Rigel Base. Rigel Base has 1921 of speech from most langauges, Rigel fine-tuned has 102 of high quality speech also from a ton of langauges. The goal of this pretrain is to be a better base then the original pretrain.

- **Base 32k Download:**
    - <u>[**D Download**](https://huggingface.co/MUSTAR/Rigel-rvc-base-pretrained-model/resolve/main/Rigel_32k_Base_and_FineTuned/Base-model_32k_fp32/D_Rigel_32k_3890220.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/MUSTAR/Rigel-rvc-base-pretrained-model/resolve/main/Rigel_32k_Base_and_FineTuned/Base-model_32k_fp32/G_Rigel_32k_3890220.pth?download=true)</u>
- **Fine-Tuned 32k Download:**
    - <u>[**D Download**](https://huggingface.co/MUSTAR/Rigel-rvc-base-pretrained-model/resolve/main/Rigel_32k_Base_and_FineTuned/FineTuned-model_32k_fp32/D_Rigel_32k_fp32_2854856.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/MUSTAR/Rigel-rvc-base-pretrained-model/resolve/main/Rigel_32k_Base_and_FineTuned/FineTuned-model_32k_fp32/G_Rigel_32k_fp32_2854856.pth?download=true)</u>

|||
||| SingerPreTrain by Sztef
SingerPetrain is a fine-tuned based on Ov2 Super pretrained and made with 14 hours dataset (English singers). It is most suitable for training singers but it works for everything, the vocal range dataset is c1 to db7 so it works well with bass, baritone, tenor, alto, mezzo-soprano, soprano voices.

- **32k Download:**
    - <u>[**D Download**](https://huggingface.co/Sztef/SingerPreTrained/resolve/main/update/f0D_SingerPreTrain.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/Sztef/SingerPreTrained/resolve/main/update/f0G_SingerPreTrain.pth?download=true)</u>
|||
||| SnowieV3 X RIN_E3 by MUSTAR
SnowieV3 X RIN_E3 continues the training with Snowie dataset and then finetuned with additional data, so it will work better with English, Russian and Japanese language and also helps models of other languages to pronounce them well.

- **40k Download:**
    - <u>[**D Download**](https://huggingface.co/MUSTAR/SnowieV3.1-X-RinE3-40K/resolve/main/D_Snowie-X-Rin_40k.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/MUSTAR/SnowieV3.1-X-RinE3-40K/resolve/main/G_Snowie-X-Rin_40k.pth?download=true)</u>
|||
||| SnowieV3.1 by MUSTAR
SnowieV3.1 is a fine-tuned based on Snowie base pretrained (not publicly available) and made with 58 hours dataset (Russian and Japanese), so it will work better with those languages and also helps models of other languages to pronounce them well. 

- **32k Download:**
    - <u>[**D Download**](https://huggingface.co/MUSTAR/SnowieV3.1-32k/resolve/main/D_SnowieV3.1_32k.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/MUSTAR/SnowieV3.1-32k/resolve/main/G_SnowieV3.1_32k.pth?download=true)</u>
- **40k Download:**
    - <u>[**D Download**](https://huggingface.co/MUSTAR/SnowieV3.1-40k/resolve/main/D_SnowieV3.1_40k.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/MUSTAR/SnowieV3.1-40k/resolve/main/G_SnowieV3.1_40k.pth?download=true)</u>
- **48k Download:**
    - <u>[**D Download**](https://huggingface.co/MUSTAR/SnowieV3.1-48k/resolve/main/D_SnowieV3.1_48k.pth?download=true)</u>
    - <u>[**G Download**](https://huggingface.co/MUSTAR/SnowieV3.1-48k/resolve/main/G_SnowieV3.1_48k.pth?download=true)</u>
|||
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
     
+++ Q&A
Q: What is the best pretrain? 

A: There is no "best pretrain" it all depends on your needs and what you're ok with sacrificing to get those benefits.  
+++

***
:::content-center
## Vocoders
:::

-   In Applio you are given the choice between three vocoders:
    - HiFi-GAN
    - MRF HiFi-GAN
    - RefineGAN

Each of these are different in fidelity and require their own pretrains to use.

### HiFI-GAN

The first vocoder choice is HiFi-GAN the original GAN used in RVC which is combatible with all version of RVC and forks. HiFI-GAN is pretty basic and has muddy high ends.

### MRF HiFI-GAN

The second choice is MRF HiFI-GAN, this is a modfied version of HiFi-GAN with MRF instead of MPD, new loss functions and non-simplified version of the resolution block. 

- Pros:
    - Higher fidelity
    - 44.1k Training
- Cons:
    - Only a slight upgrade from Hifi-GAN
    - Not many pretrains for it

### RefineGAN

The third and final choice is RefineGAN, this is an entirely different GAN then HiFi. This GAN uses noise to fill in the gaps and has a different resolution block.

- Pros:
    - Higher fidelity and quality
    - 44.1k Training

***
:::content-center
## Tensorboard
:::

- TensorBoard is a tool that allows you to visualize & measure the training of an AI model, through graphs & metrics.

- It's specially useful for determining when to stop training a voice model, since with it you can detect when the <u><u>[overtraining</u>](https://docs.aihub.gg/rvc/resources/training/#epochs--overtraining)</u> point begins.    

- Because of this, TB is the most convenient tool for RVC users for perfecting a voice model.     
***
###### ‎
### :icon-chevron-down: Installing & Opening

!!! Applio Users 
#### If you use Applio you don't have to follow these installation steps. Just run `run-tensorboard.bat`. These installation steps are only for local mainline RVC users.
!!!

###### ‎       
1. Download this file & move it inside mainline RVC's folder. Ensure the file path doesn't contain spaces/special characters.
  
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
- In the search bar, type "**g/total**" then look for the avg graph. This will be the graph you'll monitor.        
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

- Then zoom out & lower the smoothening. Then in the avg graph look for low points around where it started to overtrain.

- Then over your mouse over these low points and take note of the step counts. Since this is using the avg graphs you may not find the exact epoch connected to the step count so just choose the closest point.

    <img src="../tensorboard-img/avg.png" alt="image" width="1000" height="auto">‎ 

- As you can see in the image above there is an area with several low points, so in this scenario you would try several epochs in that area to find the best sounding epoch.

> If you want you can just use the lowest avg g/total point.

+++ Advanced Guide ‎     
#### :icon-chevron-down: <u>Other Graphs</u>
***

#### `FM` Feature Matching: 
FM shows how well the generator is able to make synthetic data that has similar features to the dataset.

If the graph is increasing that indicates that the generator is able to make audio that has similar features to the dataset.

> you can think of this as how well the model can match timbral, spatial and temporal characteristics. 
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

#### `grad_norm_g` Gradient norm for the generator: 
grad_norm_g shows the magnitude of gradients during training. If the gradients are becoming too large (over 1,000 for fintuning) that can cause some training instabilities and if they are becoming small that can lead to slow learning.

> If you're fintuning it's best if the gradients don't go above 1,000. 
***

#### `grad_norm_d` Gradient norm for the discriminator: 
grad_norm_d shows the magnitude of gradients during training. If the gradients are becoming too large (over 100 for fintuning) that can cause some training instabilities and if they are becoming small that can lead to slow learning.

> If you're fintuning it's best if the gradients don't go above 100. 
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

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
