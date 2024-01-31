*`Written by Julia`*        
``Last update: Jan 30, 2024``
***
###### ‎
:::content-center
## <u>Introduction</u> 📜
:::
###### ‎
For many, the process of making a (*decent*) voice model can get a little tedious & confusing.        
Let's explain the procedure piece by piece & slowly.

We'll divide the process into 3 chapters:      
**1.** Preparing the dataset      
**2.** Setting up RVC               
**3.** Training the model           

We'll explain as we go along.   
Let's first start by **properly** learning what a model is exactly.
***
###### ‎
### :icon-chevron-down: What is a Voice Model?
- In the field of AI, an AI model is a program that has been trained to recognize certain patterns or make certain decisions.

- In this case, a voice model is an AI model that was trained to replicate a voice, and with AI it applies it to a given audio.

- The best way to make voice models is with the software **RVC**.     
***  
###### ‎  
### :icon-chevron-down: What is RVC?
- RVC (Retrieval-based Voice Conversion) is an advanced AI voice cloning software. It is free and <u>[open-source](https://aihubdocs.github.io/en/other/glossary/#open-source)</u>.

- It was originally designed for desktop, requiring decent <u>[specs</u>] & <u>[GPU](https://aihubdocs.github.io/en/other/glossary/#gpu)</u> to train effectively.

- It can be executed through a cloud server and be used in any device, in case you don't meet the previous requirement.

- It has different versions (known as [<u>forks</u>](https://aihubdocs.github.io/en/other/glossary/#fork)) made by the public, each one with its own features and modifications, and pros and cons, that fulfill different needs for the user.     
***
###### ‎
:::content-center
## <u>Steps</u> 📝
:::
###### ‎
### 1. Prepare dataset.
***In the context of RVC***, the dataset is an **audio** file containing the **voice** the model should replicate. It can be either a speaking or singing voice.

To get the most accurate results, having a **clean** dataset is crucial.        
So be sure to remove any undesired noises.
       
#### Learn everything [<u>here</u>](https://aihubdocs.github.io/en/vocal-isolation--datasets/datasets--how-to-clean-them/).
***
###### ‎ 
### 2. Set up RVC.
With your dataset ready, it's time to set up RVC & train the model. Choose the right one according to your needs.       
Begin using it once you have read chapter 3.               
‎
#### :icon-device-desktop: ‎ <u>For local users:</u>
- We recommend [<u>**Mainline RVC**</u>](https://aihubdocs.github.io/en/rvc/local/mainline-rvc/).     
This is the original version of RVC, being the simplest & quickest to use for training.    
‎    
#### :icon-cloud: ‎ <u>For cloud users:</u>
- We recommend [<u>**RVC Disconnected**</u>](https://aihubdocs.github.io/en/rvc/cloud/training/rvc-disconnected/) or [<u>**Paperspace**</u>](https://aihubdocs.github.io/en/rvc/cloud/paperspace/).   
    - First one is a port of the [Mangio]() fork to <u>[Google Colab](https://aihubdocs.github.io/en/other/glossary/#google-colab)</u> for training.       
    - Second one works similarly except it's much faster. A more convenient option if you don't mind paying a monthly **suscription**. 
***
###### ‎ 
### 3. Train model.
Before you start training, there's something **important** you need to know:        
The training guides are centered around the <u>[**TensorBoard**](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard/#how-to-use-tensorboard)</u>, a tool for determining exactly when to stop training.

A common mistake RVC users make is train the model for a semi-arbitrary amount of time.  
But this isn't a convenient method if you aim towards a quality model, as it can screw up the results.

Go ahead & begin the training process, you'll be adviced when to read/set up TB.       
Good luck & remember to be patient!