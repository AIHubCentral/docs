---
icon: chevron-right
order: 5000
---

``Last update: Jan 31, 2025``

***
:::content-center
<img src="..\appliocolab-img\banner.png" alt="image" width="600">

:::
###### ‎
:::content-center
## Introduction ‎
:::
- Applio is a VITS-based Voice Conversion Tool developed by the <u>[IA Hispano</u>](https://github.com/IAHispano)</u> team.

- It's liked for its great **UI** & **lots** of extra features, such as TTS (with RVC models too), plugins, automatic model upload, customizable theme & more.

- Because of its user-friendly experience & active development, it's considered to be one of the best forks.     

- As this cloud version is hosted in <u>[Google Colab](https://docs.ai-hub.wtf/extra/glossary/#google-colab)</u>, remember that you have a limited runtime of around 4 hours.       
‎         
#### Pros & Cons :icon-tasklist:
==- *Learn more*
!!! *The pros & cons are subjective to your necessities.*        
!!! 
||| ✔️ **PROS** 
- Very complete
- Has an active development
- Currently stable
- Very fast
- TTS features            
- Automatic model upload
- Has Mangio-Crepe
- User-friendly UI
- TensorBoard included
- Extra features: (plugins, model fusion, etc)
||| ❌ **CONS** 
- Usage limit for free users
||| 
===


***
###### ‎   
## Installation   
###### ‎   
#### 1. <u>Running cells.</u>
a. Start by accessing the colab <u>[here](https://colab.research.google.com/github/IAHispano/Applio/blob/main/assets/Applio_NoUI.ipynb)</u>.

b. Then run the `Installation` cell to install all the requirements.

<img src="../applio-no-ui-img/one.png" alt="image" width="800" height="">

***
###### ‎   
## Training     
#### 2. <u>Preprocess Dataset.</u>
1. Name your model whatever you want. 

2. Then upload your dataset to your google drive.

3. Type in the path to your dataset into `dataset_path`. 

<img src="../applio-no-ui-img/two.png" alt="image" width="1200" height="">
‎ 

4. Select your <u>[sample rate](https://docs.aihub.gg/rvc/resources/dataset-isolation/#step-1-find-the-sample-rate)</u>.

5. Run the cell.
###### ‎   
#### 3. <u>Extract Features.</u>
1. Choose the f0 method you want, usually RMVPE is the best.

2. If you chose Crepe set your hop length to 32, 64 or 128. If you chose RMVPE ignore this option.

<img src="../applio-no-ui-img/three.png" alt="image" width="1500" height="">
‎ 

3. Run the cell. 
###### ‎   
#### 4. <u>Training.</u>
1. Set the total number of epoch you want to train for. 

2. Choose your <u>[batch size](https://docs.aihub.gg/rvc/resources/training/#batch-size)</u>, 8 is the best for most cases. 

3. Enable `cleanup` if this is your first time training a model and you're not resuming. 

4. Set how many epochs you are going to save. If you want to get the best epoch set this to 1 but if you're ok with close enough you can set this to a higher number. 

5. Turn on `save_only_latest`.

<img src="../applio-no-ui-img/four.png" alt="image" width="1000" height="">
‎

6. Run the cell to start training!
###### ‎   
##### 5. <u>Resuming Training.</u>

1. Set the model names to **exactly** what you had before.

2. Run the first cell.

3. Select your sampe rate and f0 method in the second cell.

4. Run the final cell.

<img src="../applio-no-ui-img/five.png" alt="image" width="1000" height="">
‎ 

5. Then run the training cell again.


***

###### ‎   ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/contributions/)
:::