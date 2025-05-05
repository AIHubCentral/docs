---
icon: chevron-right
order: 2000
---
``Last update: Nov 21, 2024`` 
***
:::content-center
<img src="../lighting.ai/logo.png" alt="image" width="600">        
:::
## </u>Introduction</u>
- Lightning.Ai is a cloud platform for using AI apps, powered by virtual machines with powerful GPU's.     

- It's a great alternative for training RVC voice models through the cloud, since it has the best GPUs with tons of VRAM.

- Lightning doesn't have the best GPU hours but it does have the best GPUs out of all the other cloud options. 

#### Pros & Cons :icon-tasklist:

==- ***Learn more***
!!! *The pros & cons are subjective to your necessities.*        
!!!
||| **✔️ PROS:**  
- Has good GPU's.  
- Has lots of VRAM  
- TensorBoard included.
- You can leave training unsupervised.  
||| ❌ **CONS**       
- Takes some time to set up.      
- Needs a phone number.
- Low GPU time depending on what GPU you choose.
- 2-3 Day verification wait time.
 
|||
===


***
###### ‎   
## How to Setup    
***
### 1. Set up Account.
a. First make an acount with <u>[Lightning Ai](https://lightning.ai)</u>

<img src="../lighting.ai/1.png" alt="image" width="300">‎ 

b. Make sure you verify yourself with a phone number. Once you've done that you will get an email that looks like this: 

<img src="../lighting.ai/2.png" alt="image" width="400">‎   

!!!danger
You will need to wait 2-3 business days to become fully verified 
!!!

c. Once you are verified Lightning Ai will send you a email that conatins this: 

<img src="../lighting.ai/3.png" alt="image" width="500">‎   

***  
######
### 2. Notebook and Setup.
a. Once you have become verified click this <u>[link](https://lightning.ai)</u> and it should take you to your home page so you can create a notebook.

b. In the top right click `New Studio` 

<img src="../lighting.ai/studio.png" alt="image" width="1400">‎ 

c. Set the studio type to code, teamspace to vision model and select any gpu you want for the machine. Click create when you've selected everything

<img src="../lighting.ai/setting.png" alt="image" width="400">‎ 

d. Once you are in the notebook go to the left side right under `main.py` and right click. Select `New Notebook`. 

<img src="../lighting.ai/notebook.png" alt="image" width="400">‎ 

e. Select python 3 for your kernal. 

<img src="../lighting.ai/python.png" alt="image" width="400">‎ 

f. In the first cell paste in the code from this code block:


==- Code Block 1
```py
import sys
from IPython.display import clear_output
import codecs
import os

encoded_url = "uggcf://tvguho.pbz/VNUvfcnab/Nccyvb/"
decoded_url = codecs.decode(encoded_url, "rot_13")

repo_name_encoded = "Nccyvb"
repo_name = codecs.decode(repo_name_encoded, "rot_13")

!pip install -q uv

!git clone --depth 1 {decoded_url} --branch 3.2.9 --single-branch
%cd {repo_name}
clear_output()

print("Installing requirements...")
!uv pip install torch==2.7.0 torchvision torchaudio==2.7.0 \
  --index-url https://download.pytorch.org/whl/cu128 \
  -q
!uv pip install -r requirements.txt -q
!uv pip install pyngrok -q

clear_output()
print("✅ Finished installing requirements!")
```
===

- Click the run button once you've pasted the code.

<img src="../lighting.ai/block1.png" alt="image" width="600">‎ 


g. When it's done it will say `Finished installing requirements!`. When it says that paste in this second code block in another cell.

==- Code Block 2
```py
import codecs
import threading
import urllib.request
import time
import ipywidgets as widgets
from IPython.display import display
import os
from pyngrok import ngrok
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

method = "gradio"  # @param ["gradio", "localtunnel", "ngrok"]
ngrok_token = "If you selected the 'ngrok' method, obtain your auth token here: https://dashboard.ngrok.com/get-started/your-authtoken" # @param {type:"string"}
tensorboard = True #@param {type: "boolean"}

def start_gradio():
    !python app.py --listen --share

def start_localtunnel():
    !npm install -g localtunnel &>/dev/null
    with open('url.txt', 'w') as file:
        file.write('')
    get_ipython().system_raw('lt --port 6969 >> url.txt 2>&1 &')
    time.sleep(2)
    endpoint_ip = urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip("\n")

    with open('url.txt', 'r') as file:
        tunnel_url = file.read()
        tunnel_url = tunnel_url.replace("your url is: ", "")

    print(f"Share Link: \033[0m\033[93m{tunnel_url}\033[0m", end="\033[0m\n")

    password_endpoint_widget = widgets.Text(
    value=endpoint_ip,
    description='Password IP:',
    disabled=True
    )
    display(password_endpoint_widget)
    !python app.py --listen


def start_ngrok():
    try:
        ngrok.set_auth_token(ngrok_token)
        ngrok.kill()
        tunnel = ngrok.connect(6969)
        print(f"Ngrok URL: \033[0m\033[93m{tunnel.public_url}\033[0m", end="\033[0m\n")
        !python app.py --listen
    except Exception as e:
        print(f"Error starting ngrok: {e}")

def start_applio():
    if method == 'gradio':
        start_gradio()
    elif method == 'localtunnel':
        start_localtunnel()
    elif method == 'ngrok':
        start_ngrok()

if tensorboard:
    %load_ext tensorboard
    %reload_ext tensorboard
    %tensorboard --logdir logs --bind_all

if "autobackups" not in globals():
    autobackups = False

if autobackups:
    thread = threading.Thread(target=backup_files)
    thread.start()

thread_applio = threading.Thread(target=start_applio)
thread_applio.start()


while True:
    time.sleep(5)
```
===

- Once again click the run button when you've pasted this code in another cell. 



***
###### ‎   
## Using Applio   
###### ‎   
#### 1. Open the Gardio link.
a. To access Applio's UI click on the link next to `Running on public URL:`, after that it is basically the same as using Applio locally or on other cloud platforms.

#### 2. Accessing Files.
b. To upload a dataset, upload audio or anything else find the `Teamspace Drive` button on the right and click it.

<img src="../lighting.ai/8.png" alt="image" width="500">‎

!!!
The path to Applio is `Studio > this_studio > Applio > Applio`
!!!

c. Once you're there you can just drag and drop files.

d. To download files click on the file then click the three dots on the right of it and click download

<img src="../lighting.ai/13.png" alt="image" width="500">‎

#### 3. Opening the Tensor Board.

a. Find the Tensor board icon on the right side bar and click it.

<img src="../lighting.ai/10.png" alt="image" width="500">‎

b. Once you've done that it will open the Tensor board. To learn how to use it go <u>[here](https://docs.ai-hub.wtf/rvc/resources/training/#usage-guide)</u>
***

#### 4. Opening the notebook.

a. If you want to go back to the notebook simply click on the `Jupyter` icon on the right. 

<img src="../lighting.ai/14.png" alt="image" width="500">‎

***
###### ‎   
## How to use Better GPUs    
###### ‎   
#### 1. Swapping GPUs.
a. To swap GPUs go to the GPU icon the the righ and click it. 

<img src="../lighting.ai/11.png" alt="image" width="500">‎

b. Then click on `GPU` and it will show you a list of GPUs you can use by clicking on them and then clicking request.

<img src="../lighting.ai/12.png" alt="image" width="500">‎

!!! Here is a list of how long you can use each GPU before running out of hours.
- 22 hours monthly of T4 16gb
- 21 hours monthly of L4 24gb
- 8 hours monthly of A10G 24gb
- 6 hours monthly of L40 48gb
!!!

***




***
###### ‎   ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/contributions/)
:::