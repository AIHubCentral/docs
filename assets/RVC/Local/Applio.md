---
icon: chevron-right
order: 3000
---

``Last update: March 7, 2026``

***
:::content-center
<img src="..\applio-img\banner.png" alt="Applio Banner Logo" width="600">

:::

:::content-center
## Introduction ‎
:::
- Applio is a <u>[Fork</u>](https://docs.aihub.gg/essentials/whats-rvc/#forks) of <u>[Original/Mainline RVC](https://docs.aihub.gg/rvc/local/mainline/)</u>, developed by the <u>[IA Hispano</u>](https://github.com/IAHispano)</u> team.

- It's liked for its great **UI**, **performance** improvements and **lots** of extra features, such as TTS (with RVC models too), plugins, automatic model upload, customizable theme & more.

- Because of its user-friendly experience & active development, it's considered to be one of the best forks.     

- Applio has <u>[it's own Applio Docs](https://docs.applio.org/)</u>, which may have more info about the tool.


***
#### Are RVC Models Safe?

RVC Models are PyTorch Models, a Python library used for AI.
PyTorch uses serialization via Pythons' Pickle Module, converting the model to a file.
Since pickle can execute arbitrary code when loading a model, it could be theoretically used for malware, but this fork has a **built-in feature to prevent code execution along the model.**
Also, **HuggingFace has a <u>[Security Scanner](https://huggingface.co/docs/hub/security-pickle#hubs-security-scanner)</u>** which scans for any unsafe pickle exploits and uses also ClamAV for scanning dangerous files.
***

‎      
#### Pros & Cons :icon-tasklist:
==- *Learn more*
!!! *The pros & cons are subjective to your necessities.*        
!!! 
||| ✔️ **PROS** 
- Very complete
- Has an active development
- Currently stable
- Faster interface
- TTS features            
- Automatic model upload
- User-friendly UI
- TensorBoard included
- Extra features: (plugins, model fusion, etc)
||| ❌ **CONS** 
- None :smile:
|||
===
***


## System & Hardware Requirements

Check if you meet the <u>[requirements](https://docs.aihub.gg/essentials/whats-rvc/#what-are-the-requirements-for-rvc-locally/)</u> to run it locally.

If you don't meet the requirements, there are 4 Cloud Versions:
- <u>[Applio UI Kaggle](https://docs.aihub.gg/rvc/cloud/applio-kaggle/)</u>
- <u>[Applio UI Google Colab](https://docs.aihub.gg/rvc/cloud/applio-colab/)</u>
- <u>[Applio NO UI Google Colab](https://docs.aihub.gg/rvc/cloud/applio-no-ui-colab/)</u>
- <u>[Applio UI Lightning.AI](https://docs.aihub.gg/rvc/cloud/applio-lightning-ai/)</u>


###### ‎
:::content-center
## Download & Installation :icon-download:
:::
###### ‎
!!!warning Before Downloading:
- Don't put it in a folder with privileged access.
- Don't run the run-install.bat as an administrator.
- Make sure the path does not contain any spaces or special characters.
- Deactivate your antivirus and firewall to avoid missing dependencies.
!!!
***

### Nvidia on Windows (Precompiled)

RTX 5000 Series Users require version 3.3.0 or newer.

1. The easiest way to download Applio is by going to Applio's <u>[Hugging Face repo](https://huggingface.co/IAHispano/Applio/tree/main/Compiled)</u>, and clicking the [ :icon-download: **download** ] button on the right-hand side.

    <img src="..\applio-img\2-localappliodl.png" alt="image" width="400">

***
2. Unzip the folder. This may take a few minutes.
***
3. Open Applio's folder & execute ``run-applio.bat``.

    <img src="..\applio-img\2-run-applio.png" alt="image" width="250">‎    
‎       
- A console tab will appear, and after a moment your default browser, with Applio ready to use.     
‎       
!!!warning Don't close the console until you're done using it, or it will stop working.     
!!! 


***

### Linux & macOS

1. The easiest way to download Applio is by going to Applio's <u>[Hugging Face repo](https://huggingface.co/IAHispano/Applio/tree/main/Compiled)</u>, and clicking the [ :icon-download: **download** ] button on the right-hand side.

    <img src="..\applio-img\2-localappliodl.png" alt="image" width="400">

***
2. Unzip the folder. This may take a few minutes.
***

3. Make sure you have **Python 3.10.12** or 3.11.x installed. You can check your version by running `python --version`.
4. Open a terminal in the Applio directory you just extracted.
5. Run the commands corresponding to your Linux distribution:

==- Debian/Ubuntu
```bash
apt install python3.10-venv -y
python -m venv .venv
find ".venv" -type f -exec sed -i -e 's/\r$//' -e "s|/home/runner/work/Applio/Applio|$(pwd)|g" -e "s|/.venv/bin/python|/.venv/bin/$(basename $(which python))|g" {} +
```
===
==- Arch
```bash
sudo pacman -S python-virtualenv --noconfirm
python -m venv .venv
find ".venv" -type f -exec sed -i -e 's/\r$//' -e "s|/home/runner/work/Applio/Applio|$(pwd)|g" -e "s|/.venv/bin/python|/.venv/bin/$(basename $(which python))|g" {} +
```
===
==- Fedora
```bash
sudo dnf install python3-virtualenv -y
python -m venv .venv
find ".venv" -type f -exec sed -i -e 's/\r$//' -e "s|/home/runner/work/Applio/Applio|$(pwd)|g" -e "s|/.venv/bin/python|/.venv/bin/$(basename $(which python))|g" {} +
```
===

6. Run Applio
- In the terminal, run the following commands to make the script executable and launch the application:
```bash
chmod +x run-applio.sh
./run-applio.sh
```

‎       
- A console tab will appear, and after a moment your default browser, with Applio ready to use.     
‎       
!!!warning Don't close the console until you're done using it, or it will stop working.     
!!! 

***

### AMD on Windows (Precompiled Fix)

!!!info "Unofficial Method"
These guides are for AMD GPU users on Windows using Zluda to enable CUDA compatibility. Select the tab corresponding to your driver version.
!!!

+++ Adrenalin 25.5.1+ (Newer)
**For Adrenalin 25.5.1 driver or newer**

1. Download a compiled version of Applio **v3.5.0 or newer** from the <u>[Hugging Face repo](https://huggingface.co/IAHispano/Applio/tree/main/Compiled)</u>, and unzip it to your desired folder.

2. Download **HIP SDK 6.2.4** from the <u>[AMD ROCm Hub](https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html)</u>.
    - Run the installer.
    - **Important:** Install the components but **exclude/deselect the video driver** at the bottom of the installer list.

3. Add the following path to your System Environment Variables (Path):
   `C:\Program Files\AMD\ROCm\6.2\bin`

4. Open a command line (CMD) inside the Applio folder and run the following commands to update PyTorch:
   ```bash
   env\python -m pip uninstall torch torchvision torchaudio
   env\python -m pip install torch torchvision torchaudio --upgrade --index-url https://download.pytorch.org/whl/cu118
   ```

5. Download the necessary patch files into your Applio root folder:
    - <u>[patch-zluda-hip62.bat](https://github.com/IAHispano/Applio/blob/main/assets/zluda/patch-zluda-hip62.bat)</u>
    - <u>[run-applio-amd.bat](https://github.com/IAHispano/Applio/blob/main/assets/zluda/run-applio-amd.bat)</u>

6. Edit the file located at `rvc/lib/zluda.py`. Replace the content with the following:
   ```python
   import torch

   if torch.cuda.is_available() and torch.cuda.get_device_name().endswith("[ZLUDA]"):
       # disabling unsupported cudnn
       torch.backends.cudnn.enabled = False
       torch.backends.cuda.enable_flash_sdp(False)
       torch.backends.cuda.enable_math_sdp(True)
       torch.backends.cuda.enable_mem_efficient_sdp(False)
   ```

7. Run `patch-zluda-hip62.bat`.

8. Run `run-applio-amd.bat` to start Applio.

+++ Older Drivers / Legacy
1. Download and install the <u>[VC++ Runtime](https://aka.ms/vs/17/release/vc_redist.x64.exe)</u>.

***

2. First, check the official <u>[System Requirements](https://rocm.docs.amd.com/projects/install-on-windows/en/develop/reference/system-requirements.html)</u> on the AMD ROCm™ documentation site. In the "Windows-supported GPUs" section, determine which steps to follow below.

==- GPU has a green check in the HIP SDK column
- Install either v6.1.2 or v5.7.1 HIP SDK from the <u>[AMD ROCm Hub](https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html)</u>.
===
==- GPU is RX 6600, 6600XT, 6650XT, 6700, 6700XT, or 6750XT
1. Install **v5.7.1** HIP SDK from the <u>[AMD ROCm Hub](https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html)</u>.
2. Download the correct archive for your GPU:
    - For 6700, 6700XT, 6750XT, download the <u>[gfx1031 archive](https://github.com/brknsoul/ROCmLibs/raw/main/Optimised_ROCmLibs_gfx1031.7z)</u>.
    - For 6600, 6600XT, 6650XT, download the <u>[gfx1032 archive](https://github.com/brknsoul/ROCmLibs/raw/main/Optimised_ROCmLibs_gfx1032.7z)</u>.
3. Navigate to `C:\Program Files\AMD\ROCm\5.7\bin\rocblas\` and rename the `library` folder to `library.old`.
4. Create a new, empty folder named `library` in its place.
5. Unzip the content of the archive you downloaded into this new `library` folder.
===
==- All other AMD GPUs
1. Find your GPU's `gfxNNNN` value. You can do this by searching "techpowerup *your_gpu_name*" (e.g., "techpowerup RX 7900 XTX") and finding the "Shader ISA" on the specifications page.
2. Follow the steps for your corresponding `gfx` value:

    +++ `gfx803, gfx900, gfx906, gfx1010, gfx1011, gfx1012, gfx1030, gfx1100, gfx1101, gfx1102`
    1. Install **v5.7.1** HIP SDK from the <u>[AMD ROCm Hub](https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html)</u>.
    2. Download <u>[this archive](https://github.com/brknsoul/ROCmLibs/raw/main/ROCmLibs.7z)</u>.
    3. Navigate to `C:\Program Files\AMD\ROCm\5.7\bin\rocblas\` and rename the `library` folder to `library.old`.
    4. Unzip the content of the archive directly into the `C:\Program Files\AMD\ROCm\5.7\bin\rocblas\` folder.
    +++ Other GPUs
    - Visit <u>[this repository](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU)</u> and follow the specific instructions provided there.
    +++
===

***

3. Download a <u>[compiled version of Applio](https://huggingface.co/IAHispano/Applio/tree/main/Compiled)</u> (v3.2.5 or higher) and unzip it to your desired folder.

    <img src="..\applio-img\2-localappliodl.png" alt="image" width="400">

4. Open a Command Prompt in the Applio folder (type `CMD` in the address bar and press Enter). Run the following commands to install the correct version of PyTorch for Zluda.
   ```bash
   env\python -m pip uninstall torch torchvision torchaudio
   env\python -m pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --upgrade --index-url https://download.pytorch.org/whl/cu118
   ```

***

5. Navigate to the `assets\zluda` folder inside your Applio directory.
6. Move all `.bat` files from this folder to the main (root) Applio folder.
7. Run the patch file that corresponds to your HIP SDK version:
    - **For HIP SDK 5.7:** Run `patch_zluda_hip57.bat`.
    - **For HIP SDK 6.1:** Run `patch_zluda_hip61.bat`.
8. Add the `bin` directory of your HIP SDK installation to your system's Path environment variables.
    - For HIP SDK 5.7: `C:\Program Files\AMD\ROCm\5.7\bin`
    - For HIP SDK 6.1: `C:\Program Files\AMD\ROCm\6.1\bin`

***

9.  Run `run-applio-amd.bat` to start Applio.
+++


!!!warning "Check your GPU Index"
It's assumed your primary AMD GPU has an index of **0**. If you have an iGPU that is listed first in Device Manager (under 'Display Adapters'), you must edit the `run-applio-amd.bat` file and change the value from `"0"` to `"1"`.
!!!

!!!info "Initial Compilation Will Be Slow"
The very first time you run a task (like inference or training), Applio may appear to freeze for **15-20 minutes**. This is normal. Zluda is compiling the necessary kernel code in the background. Subsequent runs will be fast.
!!!


‎       
- A console tab will appear, and after a moment your default browser, with Applio ready to use.     
‎       
!!!warning Don't close the console until you're done using it, or it will stop working.     
!!! 


***
###### ‎       
###### ‎   
:::content-center
## Upload Models
:::
###### ‎  
###### ‎   
#### 1. Upload voice model.
- Go to the **Download** tab.       
You have two ways of uploading it: through <u>[**its link**](https://docs.aihub.gg/essentials/voice-models/#how-to-search-voice-models)</u> or **manually** inputting its files.

    +++ Link
    a. Go to the **Download** tab & paste the link of the model in the `Model Link` bar. It must be from Hugging Face or Google Drive.        
    ‎       
    <img src="..\applio-img\3-download-model.png" alt="image" width="500">    
    ‎       
    b. Press ``Download Model``.
    +++ Manually

    a. Drag & drop the model's .PTH in the **Drop files** box below.    
    ‎       
    <img src="..\applio-img\3-modelupload.png" alt="image" width="800">       
    ‎           
    b. Then drag the .INDEX.
    +++ 



***
###### ‎       
###### ‎   
:::content-center
## Inference :icon-unmute:   
:::
###### ‎  
###### ‎   
#### 1. Select voice model.
a. Return to the **Inference** tab & click the ``Refresh`` button on the right.

    <img src="..\applio-img\3-refresh.png" alt="image" width="500">   


    ‎       
b. Select your model in the ``Voice Model`` dropdown.

    <img src="..\applio-img\3-voice-model.png" alt="image" width="500">   

  ***
#### 2. Input vocals.      
- With Applio you can convert audios individually or in batches:
    +++ Single file
    a. Drag & drop the audio or click the upload box to search it.      
    ‎   
        <img src="..\applio-img/3-upload.png" alt="image" width="600">   
    ‎   
    b. Then select it in the dropdown below.      
    ‎   
        <img src="..\applio-img/3-select-audio.png" alt="image" width="400">   

    +++ In batches
    a. Go to the **Batch** tab.     
    ‎
        <img src="..\applio-img/batchupload.png" alt="image" width="400">    
    
    b. In the `Input Folder` bar, paste the path folder containing the audios.

        In `Output Folder` you can paste a path folder for the results.        
  
        Ensure the paths don't contain spaces/special characters.      
    +++

‎  
#### 3. Modify settings. (optional)      
-  Unfold `Advanced Settings` if you wish to modify the <u>[inference settings](https://docs.aihub.gg/rvc/resources/inference-settings/)</u> for better results, or to determine the output folder.

    <img src="..\applio-img/3-advanced.png" alt="image" width="600">‎   
***

###### ‎  
#### 4. Convert.
a. Click ``Convert`` at the bottom. The audio will begin to process.       
The processing time will mainly depend on your specs, length of audio & the algorithm picked.

b. Once it's done, you can hear the results in the **Export Audio** box below.

    By default the output files will be in the "**audios**" folder: ``\ApplioV3.0.7\assets\audios``


***
###### ‎     
###### ‎  
:::content-center
## Training :icon-dependabot:
###### ‎   
!!!warning
The training guide will be centered around using <u>[TensorBoard](https://docs.aihub.gg/rvc/resources/training/#tensorboard)</u>. Read about it first if you haven't already.      
If you encounter an issue, be sure to read the <u>[Troubleshooting](https://docs.aihub.gg/rvc/local/mainline/#troubleshooting-)</u> chapter.
!!!
:::
###### ‎     
:::content-center
:::
==- 1. PREPROCESS
###### ‎      
##### a. Model Name
###### ‎    
- Go to the `Train` tab. Input a name for your model in `Model Name`.       
Don't include spaces/special characters.     

    <img src="..\applio-img\4-modelname.png" alt="image" width="550">‎     

***
###### ‎     
##### b. Dataset Path
###### ‎    
- Paste the path file of your dataset in the **Dataset Path** bar. Ensure the path doesn't contain spaces/special characters.

    <img src="..\applio-img\4-datasetpath.png" alt="image" width="550">‎  

***
###### ‎     
##### c. Sampling Rate
###### ‎    
- Select your dataset's sample rate. If you don't know the amount, click <u>[here](https://docs.aihub.gg/rvc/local/applio/#extra)</u>.

    <img src="..\applio-img\4-samplerate.png" alt="image" width="300">‎  

***
###### ‎     
##### d. Preprocess Dataset
###### ‎    
- Ensure **RVC Version** is set as `V2` & click `Preprocess Dataset`.       

    It'll finish when the output box says `preprocessed successfully`.

    <img src="..\applio-img\4-preprocessdone.png" alt="image" width="700">

===

==- 2. EXTRACT
###### ‎    
##### a. Pitch extraction algorithm
###### ‎  
- Select the <u>[algorithm](https://docs.aihub.gg/rvc/resources/inference-settings/#pitch-extraction-algorithm)</u> you want. Use either ``RMVPE`` (most suggested) or ``Crepe``. Applio removed pm. dio and harvest as they are outdated.

    <img src="..\applio-img\pitch-extraction-algorithms.png" alt="image" width="400">

***
###### ‎  
##### b. Embedder Model
###### ‎  
- Select the <u>[Embedder Model](https://docs.aihub.gg/rvc/resources/inference-settings/#embedder-model)</u> you want. Contentvec is the most used.

    <img src="..\applio-img\embedder.png" alt="image" width="400">

***
###### ‎  
##### c. Custom Embedder Model
###### ‎  
- If you select "custom" for embedders, you can add your own, like [Spin](https://docs.aihub.gg/rvc/resources/inference-settings/#spin) or [Spin V2](https://docs.aihub.gg/rvc/resources/inference-settings/#spin-v2) (which seems to have better pronunciation than contentvec and better for realtime as it handles context differently)

    <img src="..\applio-img\embedder-custom-option.png" alt="image" width="400">

- Give it a Folder Name, like "spin".
- Upload the .bin and .json files, which for example you can find them at https://huggingface.co/IAHispano/Applio/tree/main/Resources/embedders/spin for spin.
- Click "Move files to custom embedder folder".

- After you added your custom embedder, Refresh Embedders and select it from the Dropdown menu at the left of the refresh embedders button.
    <img src="..\applio-img\custom-embedder.png" alt="image" width="600">


***
###### ‎  
##### d. Extract Features
###### ‎  
- Press **Extract Features**.       
It'll finish when it says `extracted successfully`.

    <img src="..\applio-img\4-extractfinish.png" alt="image" width="350">

===

==- 3. TRAIN
###### ‎  
##### a. Batch Size
###### ‎  
- If you are a newbie, use `8`. But in case your dataset is short (around 2 minutes or less), use `4`.

    <img src="..\applio-img\4-batchsize.png" alt="image" width="350">

***
###### ‎  
##### b. Save Every Epoch
###### ‎  
- Frequency of the <u>[saving checkpoints](https://docs.aihub.gg/extra/glossary/#checkpoints)</u>, based on the <u>[epochs](https://docs.aihub.gg/rvc/resources/training/#epochs--overtraining)</u>.      
‎   
- If you are a newbie, simply leave it at `15`, but if you wish to be percise set it to `1`.              

    <img src="..\applio-img\4-freq.png" alt="image" width="420">‎   
‎   
‎   
- E.g: with a value of `10`, they will be saved after the epoch 10, 20, 30, etc.   
***
###### ‎  
##### c. Total Epoch
###### ‎  
- Input the total amount of <u>[epochs](https://docs.aihub.gg/rvc/resources/training/#epochs--overtraining)</u> (training cycles) for the model.     
‎   
- But since we'll use <u>[TensorBoard](https://docs.aihub.gg/rvc/resources/training/#tensorboard)</u>, use an arbitrarily large value like `1000`

    <img src="..\applio-img\4-epoch.png" alt="image" width="420">‎   
***
###### ‎  
##### d. Use Pretrained Models
###### ‎  
- RVC uses the Orignal [Pretrain](https://docs.aihub.gg/rvc/resources/training/#pretrains) by default (`Pretrained` is always checked, unchecking it is highly not recommended as you won't use even the Original Pretrain and train from scratc) to significantly reduce training duration and enhance overall quality. You can use the original pretrain, or community made models downloaded via the Download tab or upload them yourself.

<img src="..\applio-img\advanced-settings-pretrain.png" alt="Pretrained and Custom Pretrained options in Applio" width="600">

- Download Custom Pretrained Models (Optional):
    - Go to the **Download** tab, go to the download custom pretrain, and select the community made ones like TITAN and for which sample rate you need.
    - To use a pretrained model that you downloaded from the **Download** tab, simply check the `Pretrained` box.
    - If you can't find the pretrain you want, you can check [AI HUB](https://discord.gg/invite/aihub)'s [`#pretrain-models`](https://discord.com/channels/1159260121998827560/1235952130855010365) or [here](https://docs.aihub.gg/rvc/resources/training/#where-do-i-find-pretrains)
- Use Custom Pretrained Models (Optional):
    - Check the `Custom Pretrained` box to use your own files. This will open the `Pretrained Custom Settings` section.

    <img src="..\applio-img\custom-pretrain.png" alt="Uploading a custom pretrained model in Applio" width="700">

    - **Upload:** Click `Upload Pretrained Model` to open a file dialog. Here, you can drag and drop your files or click to upload the Generator (`G`) and Discriminator (`D`) `.pth` files. This is for when you want to upload your own pretrains which aren't in the community download pretrains tab.
    - **Select:** After uploading, click `Refresh Custom Pretraineds`. Then, select your custom generator and discriminator from the `Custom Pretrained G` and `Custom Pretrained D` dropdown menus. These dropdowns will also show any custom pretrained models you have downloaded from the Download tab.

***
###### ‎  
##### e. Sync Graphs
###### ‎  
- Sync graphs trains a single epoch and sets the log interval to the amount of steps that epoch trained for.     
‎   
- Doing this makes the Tensor Board's graphs accurate.

    <img src="..\applio-img\sync-graph.png" alt="image" width="420">‎   
***
###### ‎  
##### f. GPU Settings
###### ‎  
- If you have multiple GPUs, tick `GPU Settings` to use a specific one for the training.

   <img src="../applio-img/4-gpu.png" alt="image" width="440" height="auto">‎ 
***
###### ‎  
##### g. Generate Index
###### ‎  
- Click `Generate Index`. This will create the model's <u>[.INDEX](https://docs.aihub.gg/essentials/voice-models/#voice-model-files)</u> file.
***
###### ‎  
##### h. Start Training
###### ‎  
- Press `Start Training` to begin the training process.     
‎   
- To open <u>[TB](https://docs.aihub.gg/rvc/resources/training/#tensorboard)</u>, execute `run-tensorboard` in Applio's folder. Remember to monitor it, as well as the console just in case.           
‎   
- The latter will show you errors if they happen, and information about the epochs & checkpoints.   

    <img src="../mainline-img/j.png" alt="image" width="480" height="auto"> 

===

==- 4. FINAL STEP
###### ‎  
##### a. Stop training
###### ‎  
- When you're very sure of overtraining, you can stop training by going to the `Settings` tab & press `Restart Applio`.

    <img src="../applio-img/4-stoptrain.png" alt="image" width="715" height="auto"> ‎ 

***
###### ‎  
##### b. Get the INDEX
###### ‎  
i. Create a new folder anywhere named as the model.     
‎  
ii. Open Applio's folder, go to ``logs``, and open the folder named as the model.      
‎      
iii. Select the **.INDEX** named ``added_`` & move it to your newly made folder.    
‎       
   <img src="../applio-img/4-index.png" alt="image" width="400" height="auto">‎
 ‎    

***
###### ‎  
##### c. Get the PTH
###### ‎  
i. In said folder you'll also find all the <u>[checkpoints](https://docs.aihub.gg/extra/glossary/#checkpoints)</u>.         
‎  
ii. Select the one **closest** to ***before*** the overtraining point, and move it to the new folder.

    The checkpoints will be organized with this format: **ModelName_Epoch_Step.pth**   
    Example: ``arianagrande_e60_s120.pth``

‎  
    ‎            
iii. And that's all, have fun with your model. To test it, do a normal <u>[inference</u>](https://docs.aihub.gg/rvc/local/applio/#inference-) as usual.

===

==- 5. RESUMING
- In case the training finished but the model still needed training, you don't have to start from scratch.        
‎     
- Simply enter the **same settings & criteria** that you've previously inserted. You don't have to do the preprocess or train the .INDEX again.      
 ‎     
- You can change the **save frequency**, or increase the **Total Epoch** amount in case you didn't input enough before.      
 ‎     
- Begin training again & remember to monitor TB & console like before.
===

###### ‎  
###### ‎  
###### ‎  
:::content-center
## TTS
*`+ with any RVC model`*
:::
###### ‎  
- Applio is also known for having one TTS tool by default, with **plenty** of voices to choose for.

- You can also use it with **RVC models** & apply the <u>[inference settings](https://docs.aihub.gg/rvc/resources/inference-settings/)</u> if you wish.

- Aditionally, you can download the **Eleven Labs** TTS <u>[plugin](https://docs.aihub.gg/rvc/local/applio/#plugins)</u>.       
***
###### ‎  
#### <u>Instructions:</u>
1. Go to the **TTS** tab. 

   <img src="../applio-img/5-ttstab.png" alt="image" width="400" height="auto"> ‎ 

***   
###### ‎   

2. If you want to use an RVC model, <u>[download it](https://docs.aihub.gg/rvc/local/applio/#1-upload-voice-model)</u>, go to **TTS**, click `Refresh` & select it in **Voice Model** & **Index File**.

   <img src="../applio-img/5-vm.png" alt="image" width="600" height="auto">‎    
‎             
- To modify the <u>[inference settings](https://docs.aihub.gg/rvc/resources/inference-settings/)</u> or the output folder for the TTS/RVC audio, unfold `Advanced Settings`.

***
###### ‎      
3. In **TTS Voices** select the voice of your desired language, accent & gender.        

    In **Text to Synthesize** input your text. Then click `Convert`.

   <img src="../applio-img/5-voice.png" alt="image" width="500" height="auto">‎     
‎   
- If you are using an RVC model, select a voice that matches the model the most, to guarantee great results.   
***
###### ‎  
4. Once it's done, you'll be able to hear the result in the Export Audio box. By default, the output audio will be in the "**audios**" folder. < ``\ApplioV3.0.7\assets\audios`` >

   <img src="../applio-img/5-ttsoutput.png" alt="image" width="500" height="auto">‎   



***
###### ‎  
###### ‎  
:::content-center
## Update :icon-download:
:::
###### ‎  
To Update Applio, you need to firstly Save your audios and models, then Delete the current Applio folder and reinstall the latest version.


***
###### ‎  
###### ‎  
:::content-center
## Voice Blender :icon-git-merge:
:::
###### ‎  
The Voice Blender (also known as Model Fusion) allows you to combine the weights of two different RVC models to create an entirely new, hybrid voice. This is ideal for creating unique characters or fine-tuning a model's tonal characteristics.

#### 1. Setup Models
- Go to the **Voice Blender** tab.
- **Model Name:** Enter the name for your new hybrid model.
- **Upload Models:** You can either drag and drop the two `.pth` files into the upload boxes or paste their local file paths in the "Path to Model" bars.

<img src="../applio-img/voice-blender-1.png" alt="Applio Voice Blender Model Setup" width="800" height="auto">

***

#### 2. Blend & Fuse
- **Blend Ratio:** Adjust the slider to determine the influence of each model. 
    - A value of `0.5` is a perfect 50/50 split. 
    - Moving it closer to `0` favors the first model, while `1` favors the second.
- **Fusion:** Click the `Fusion` button to begin the process.

<img src="../applio-img/voice-blender-2.png" alt="Applio Voice Blender Fusion" width="800" height="auto">

***

#### 3. Export Information
- **Output Information:** Once finished, the console log and the output box will confirm the successful creation of the model.
- **Download/Save:** The new fused model will be generated and can be found in your Applio `logs` or downloaded directly from the interface.

!!!danger Index Blending
Note that Voice Blender only merges the **.pth** (weight) files. It does **not** merge `.index` files. To get the best results with a fused model, you may need to use it without an index or create a new index using the training tab with a combined dataset.
!!!


***
###### ‎     
###### ‎  
:::content-center
## Realtime Voice Conversion :icon-broadcast:
###### ‎   

Beyond offline inference, Applio features a powerful built-in **Realtime** tab, allowing you to convert your voice live during calls, streaming, or recordings.

- It uses the same RVC technology but is optimized for low-latency performance.
- Features include Voice Activity Detection (VAD), input/output device selection, and advanced performance tweaking.

For a full step-by-step setup and configuration guide, please visit the <u>[Applio Realtime Guide](https://docs.aihub.gg/realtime-voice-changer/local/applio-realtime/)</u>.


***
###### ‎  
###### ‎  
:::content-center
## Extra
:::
###### ‎  
- Applio has an **Extra** menu, containing an **audio analyzer**.

- Making it convenient for determining the **sample rate** of datasets when training models.

- It also contains the **model fusion** tool, ideal for advanced users.

***
###### ‎  
#### <u>Audio Analyzer:</u>
1. Go to the **Extra** tab & press the upload box to input your audio. Or simply drag & drop.      

   <img src="../applio-img/6-tab.png" alt="image" width="400" height="auto">‎   
***
###### ‎  
2. Once it's done uploading, click `Get information about the audio`.  

***
###### ‎  
3. In **Sampling rate** you'll see the audio's full sample rate. Use said value for training.

   <img src="../applio-img/6-samplerate.png" alt="image" width="470" height="auto">‎    
###### ‎    
!!!warning <u>WARNING:</u>   
If the frequencies don't reach the top of the spectrogram, see at which number peaks & multiply it by <U>**2**</u>.
!!!

###### ‎
{.list-icon}
- #### <u>Example:</u>
   <img src="../applio-img/6-double.png" alt="image" width="470" height="auto">‎       
‎
>Here it reached 20 kHz. **Doubling** it gives 40kHz. Therefore the ideal target sample rate would be ``40k`` 

***
###### ‎
###### ‎
:::content-center
## Plugins
:::
- Plugins are components that you can add to Applio, that add new features & enhance your experience. 

- These are made by the public, and are free & easy to install. 

- You can find them on their <u>[GitHub page](https://github.com/IAHispano/Applio-Plugins/tree/main)</u>. More will be added in the future.
***
###### ‎
#### <u>Installation:</u>
1. Access their GitHub page & click on the name of the plugin you want.

   <img src="../applio-img/7-repo.png" alt="image" width="470" height="auto">‎ 

***
###### ‎
2. Click on the ZIP file.

   <img src="../applio-img/7-zip.png" alt="image" width="470" height="auto">‎   
‎       
- Click on the download button on the right. This will download the ZIP file of the plugin.

   <img src="../applio-img/7-dl.png" alt="image" width="470" height="auto">‎ 
***
###### ‎
3. Open Applio & head over to the **Plugins** tab. Drag & drop the ZIP file to the upload box.

   <img src="../applio-img/7-plugins.png" alt="image" width="600" height="auto">‎   
‎       
- You will be able to see its installation process in the console.

   <img src="../applio-img/7-plugindl.png" alt="image" width="530" height="auto">‎ 
***
###### ‎
3. Go to the settings tab & click **Restart Applio** at the bottom. 
Then you'll be able to see the plugin in the **Plugins** tab.

   <img src="../applio-img/7-plugindled.png" alt="image" width="420" height="auto">‎ 


***
:::content-center
## Troubleshooting
:::
==- *There's no option for my sample rate.*
- **If it's lower than <u>32k**</u>: select ``32k``.       

- **If it's <u>44.1k**</u>: select ``40k``.   

- **If i'ts higher than <u>48k</u>**: select ``48k``.

===

==- *The voice glitches out.*
- This a phenomenon called artifacting. To fix it, read <u>[here](https://docs.aihub.gg/rvc/resources/dataset-isolation/#artifacts)</u>.

===

==- *Shoul.*
- This a phenomenon called artifacting. To fix it, read <u>[here](https://docs.aihub.gg/rvc/resources/dataset-isolation/#artifacts)</u>.

===

==- *I couldn't find my answer.*
- Report your issue <u>[here](https://docs.aihub.gg/contributions)</u>.
===


***
:::content-center
## Communities :icon-people:
:::

<div style="display: flex; flex-direction: column; gap: 1rem; align-items: center; padding: 1rem 0;">
    <a href="https://discord.gg/aihub" style="display: inline-flex; align-items: center; gap: 0.5rem; background-color: #1a1c1d; color: white; padding: 0.6rem 1.2rem; border-radius: 9999px; text-decoration: none; font-weight: bold; font-size: 1rem; min-width: 150px; justify-content: center; border: 1.5px solid #555;">
        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjcuMTQgOTYuMzYiPgogICAgPHBhdGggZmlsbD0iIzU4NjVmMiIKICAgICAgICBkPSJNMTA3LjcsOC4wN0ExMDUuMTUsMTA1LjE1LDAsMCwwLDgxLjQ3LDBhNzIuMDYsNzIuMDYsMCwwLDAtMy4zNiw2LjgzQTk3LjY4LDk3LjY4LDAsMCwwLDQ5LDYuODMsNzIuMzcsNzIuMzcsMCwwLDAsNDUuNjQsMCwxMDUuODksMTA1Ljg5LDAsMCwwLDE5LjM5LDguMDlDMi43OSwzMi42NS0xLjcxLDU2LjYuNTQsODAuMjFoMEExMDUuNzMsMTA1LjczLDAsMCwwLDMyLjcxLDk2LjM2LDc3LjcsNzcuNywwLDAsMCwzOS42LDg1LjI1YTY4LjQyLDY4LjQyLDAsMCwxLTEwLjg1LTUuMThjLjkxLS42NiwxLjgtMS4zNCwyLjY2LTJhNzUuNTcsNzUuNTcsMCwwLDAsNjQuMzIsMGMuODcuNzEsMS43NiwxLjM5LDIuNjYsMmE2OC42OCw2OC42OCwwLDAsMS0xMC44Nyw1LjE5LDc3LDc3LDAsMCwwLDYuODksMTEuMUExMDUuMjUsMTA1LjI1LDAsMCwwLDEyNi42LDgwLjIyaDBDMTI5LjI0LDUyLjg0LDEyMi4wOSwyOS4xMSwxMDcuNyw4LjA3Wk00Mi40NSw2NS42OUMzNi4xOCw2NS42OSwzMSw2MCwzMSw1M3M1LTEyLjc0LDExLjQzLTEyLjc0UzU0LDQ2LDUzLjg5LDUzLDQ4Ljg0LDY1LjY5LDQyLjQ1LDY1LjY5Wm00Mi4yNCwwQzc4LjQxLDY1LjY5LDczLjI1LDYwLDczLjI1LDUzczUtMTIuNzQsMTEuNDQtMTIuNzRTOTYuMjMsNDYsOTYuMTIsNTMsOTEuMDgsNjUuNjksODQuNjksNjUuNjlaIiAvPgo8L3N2Zz4=" alt="Discord Icon" style="width: 20px; height: 20px;"/>
        <span>AI HUB's Discord</span>
    </a>
    <a href="https://discord.gg/urxFjYmYYh" style="display: inline-flex; align-items: center; gap: 0.5rem; background-color: #1a1c1d; color: white; padding: 0.6rem 1.2rem; border-radius: 9999px; text-decoration: none; font-weight: bold; font-size: 1rem; min-width: 150px; justify-content: center; border: 1.5px solid #555;">
        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjcuMTQgOTYuMzYiPgogICAgPHBhdGggZmlsbD0iIzU4NjVmMiIKICAgICAgICBkPSJNMTA3LjcsOC4wN0ExMDUuMTUsMTA1LjE1LDAsMCwwLDgxLjQ3LDBhNzIuMDYsNzIuMDYsMCwwLDAtMy4zNiw2LjgzQTk3LjY4LDk3LjY4LDAsMCwwLDQ5LDYuODMsNzIuMzcsNzIuMzcsMCwwLDAsNDUuNjQsMCwxMDUuODksMTA1Ljg5LDAsMCwwLDE5LjM5LDguMDlDMi43OSwzMi42NS0xLjcxLDU2LjYuNTQsODAuMjFoMEExMDUuNzMsMTA1LjczLDAsMCwwLDMyLjcxLDk2LjM2LDc3LjcsNzcuNywwLDAsMCwzOS42LDg1LjI1YTY4LjQyLDY4LjQyLDAsMCwxLTEwLjg1LTUuMThjLjkxLS42NiwxLjgtMS4zNCwyLjY2LTJhNzUuNTcsNzUuNTcsMCwwLDAsNjQuMzIsMGMuODcuNzEsMS43NiwxLjM5LDIuNjYsMmE2OC42OCw2OC42OCwwLDAsMS0xMC44Nyw1LjE5LDc3LDc3LDAsMCwwLDYuODksMTEuMUExMDUuMjUsMTA1LjI1LDAsMCwwLDEyNi42LDgwLjIyaDBDMTI5LjI0LDUyLjg0LDEyMi4wOSwyOS4xMSwxMDcuNyw4LjA3Wk00Mi40NSw2NS42OUMzNi4xOCw2NS42OSwzMSw2MCwzMSw1M3M1LTEyLjc0LDExLjQzLTEyLjc0UzU0LDQ2LDUzLjg5LDUzLDQ4Ljg0LDY1LjY5LDQyLjQ1LDY1LjY5Wm00Mi4yNCwwQzc4LjQxLDY1LjY5LDczLjI1LDYwLDczLjI1LDUzczUtMTIuNzQsMTEuNDQtMTIuNzRTOTYuMjMsNDYsOTYuMTIsNTMsOTEuMDgsNjUuNjksODQuNjksNjUuNjlaIiAvPgo8L3N2Zz4=" alt="Discord Icon" style="width: 20px; height: 20px;"/>
        <span>IA Hispano (Applio)' Discord</span>
    </a>
</div>


***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
