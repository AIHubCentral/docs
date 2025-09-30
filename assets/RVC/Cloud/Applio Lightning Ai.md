---
icon: ":zap:"
order: 6000
---
``Last update: August 8, 2025``
***
:::content-center
<img src="../lightning-applio-img/logo.png" alt="image" width="600">        
:::
## </u>Introduction</u>
- This is a <u>[cloud-based](http://docs.aihub.gg/extra/glossary/#cloud-based)</u> alternative to run [Applio](https://docs.aihub.gg/rvc/local/applio/), RVC Fork, only for people who don't have a good PC GPU, via the <u>[Lightning.AI Service](http://docs.aihub.gg/extra/glossary/#lightningai)</u>. With a Web User Interface.

- It's a great alternative for training RVC voice models through the cloud, since it has the best GPUs with tons of VRAM.

!!!danger Lightning.AI Service
**Check the <u>[Lightning.AI Glossary](http://docs.aihub.gg/extra/glossary/#lightningai)</u> for more info on Free Tier, Limits, Verification, Pricing and other things.**
!!!

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
- Low/Decent GPU time depending on what GPU you choose.
- 2-3 Day verification wait time.
 
|||
===


***
## Create an Account   
### 1. Set up account.
a. First make an account with <u>[Lightning Ai](https://lightning.ai)</u>

<img src="../lightning-applio-img/signup.png" alt="LightningAI Signup" width="300">

b. Make sure you verify yourself with a phone number. Once you've done that you will get an email that looks like this: 

<img src="../lightning-applio-img/verification.png" alt="LightningAI Verification" width="400">

!!!danger
You will need to wait 2-3 business days to become fully verified 
!!!

c. Once you are verified Lightning Ai will send you a email that conatins this: 

<img src="../lightning-applio-img/email-verification.png" alt="LightningAI Email Verification" width="500">


***
## Studio Setup & Installation

#### 2. Access the Notebook
a. After creating your Lightning.AI account, open the [Applio Notebook](https://lightning.ai/nick088/studios/applio-ui?view=public&section=featured) and Clone it.

<img src="../lightning-applio-img/lightning-ai-clone-studio.png" alt="LightningAI Clone Studio" width="300">

#### 3. Activate/Switch GPU
a. If you aren't on a GPU environment by default, you must switch to a GPU environment. This is crucial for performance.
b. On the right-hand lateral menu, click on **Studio Environment** (the processor icon).
<img src="../lightning-applio-img/gpu-setting.png" alt="LightningAI GPU Setting" width="500">
c. Click **Switch To GPU**, select an available GPU, and wait for the environment to restart.
<img src="../lightning-applio-img/gpus-list.png" alt="LightningAI GPUs List" width="500">

!!! Here is a list of how long you can use each GPU before running out of Free credits.
- 75 hours monthly of T4 16gb
- 31 hours monthly of L4 24gb
- 15 hours monthly of L40 48gb
!!!

#### 4. Clone Repository and Install Dependencies
a. Run the first code cell. This will download the latest version of the realtime voice changer and install necessary dependencies.
b. This step may take a few minutes to complete. It will print "Installed!" when finished.


***
### Tunnels

#### 5. Launch the Server via Tunnels
This final code cell is the most important one—it starts the voice changer's server and uses a "tunneling" service to create a secure, public web address (URL) for you to access it from your own computer.

a. Navigate to the third code cell, titled "Start Server **using Tunnels**". This cell boots up the Wokada Deiteris Fork application inside your Lightning.AI Studio.

b. **Select a Tunnel:** A tunnel securely exposes the application running in your private cloud environment to the public internet. The notebook gives you five different services to do this. Choose one from the `Tunnel` code menu in the code cell.

    - **Port Viewer (Recommended & Default method)**
        - **How it works:** This is a built-in Lightning.AI feature. It's one of the most straightforward method as it doesn't require any external accounts or tokens.
        - **Steps:**
            1. Select "Port Viewer" from the `Tunnel` code.
            2. Click the + at the bottom of the right tab, click on Web Apps and install Port Viewer.
            3. Run the code cell. Wait for the output to show that the server is listening.
            4. In the right-hand sidebar of the Lightning.AI interface, click the **Web Apps** tab.
            5. Click on **Port Viewer** and then click **Add a new port**.
            6. Enter `18888` as the Port Number and optionally give it a name (e.g., "Voice Changer").
            7. Click your Port in Port Viewer, you can also click Open to open it in an external tab.
            8. You can optionally go back to the Jupyter session in the right-hand sidebar of the Lightning.AI interface, to check if any error appears in the code output.

    - **Gradio (Fast, Popular & Reliable)**
        - **How it works:** This is a built-in <u>[Gradio](http://docs.aihub.gg/extra/glossary/#gradio)</u> feature. It's one of the most straightforward method as it doesn't require any external accounts or tokens.
        - **Steps:**
            1. Select "Gradio" from the `Tunnel` code.
            2. Run the cell. The public Gradio URL (ending in `gradio.live`) will be printed in the output once the server is ready. Click on it to access the UI.

    - **Ngrok (Fast, Popular & Reliable)**
        - **How it works:** Ngrok is a popular service that creates secure tunnels. It requires a free account and an authentication token. It has a 1GB Bandwidth Free Monthly Limit https://ngrok.com/docs/pricing-limits/free-plan-limits/.
        - **Steps:**
            1. Go to the [Ngrok Dashboard](https://dashboard.ngrok.com/get-started/your-authtoken) to get your free authtoken.
            2. In the notebook cell, paste your token into the `Token` field, replacing `'Ngrok | Horizon TOKEN'`.
            3. (Optional) To potentially reduce latency, select a geographical `Region` from the list of parameter options next to it, that is closest to you.
            4. Run the cell. The public Ngrok URL (ending in `ngrok.io`) will be printed in the output once the server is ready. Click on it to access the UI.

    - **Cloudflare (Easy, No Account Needed)**
        - **How it works:** This option uses Cloudflare's free `trycloudflare` service. It's very easy to use as it requires no accounts or tokens.
        - **Steps:**
            1. Select "Cloudflare" from the `Tunnel` code.
            2. Run the cell. The script will automatically download the necessary tools. After a few moments, a public URL (ending in `trycloudflare.com`) will be printed in the output. Click it to open the interface.

    - **LocalTunnel (No Account, Password Protected)**
        - **How it works:** LocalTunnel is another free service that doesn't require an account. For security, it generates a unique URL that is protected by a password.
        - **Steps:**
            1. Select "LocalTunnel" from the `Tunnel` code.
            2. Run the cell.
            3. The output will display two key pieces of information: the public URL (ending in `loca.lt`) and a `Local Tunnel Password` below it.
            4. Click the URL. A new page will ask for a password.
            5. Copy the password from the notebook output and paste it into the password prompt in your browser to access the voice changer.

    - **Horizon (Fast, Requires Account & ID)**
        - **How it works:** Horizon is another tunneling service that requires a free account and a personal ID for authentication.
        - **Steps:**
            1. Go to the [Horizon Dashboard](https://hrzn.run/dashboard/) and sign up. On the second step of the setup, you will see a command like `hrzn login YOUR_ID`. Copy that `YOUR_ID` part.
            2. In the notebook cell, paste this ID into the `Token` field.
            3. Run the cell. The first time you use it, the output may ask you to authorize the connection by clicking a link (`https://hrzn.run/dashboard/settings/cli-token-requests/...`). Click this link and approve the request in your Horizon dashboard.
            4. The public Horizon URL (ending in `hrzn.run`) will then be printed in the output. Click it to access the UI.

c. After configuring your chosen tunnel, run the cell. The first time you run it, it might download the necessary files, which might take a minute or two.

d. Once the setup is complete, the output will display a message with your public URL. Click this link to open the Applio interface and start using the program.

!!!danger Note:
The server runs in the foreground. If you stop the cell or close the Lightning.AI site, the server will shut down. Keep the cell running to use the program.
!!!

### Server Setup

#### 6. Accessing Files.
b. To upload a dataset, upload audio or anything else find the `Teamspace Drive` button on the right and click it.

<img src="../lightning-applio-img/teamspace-drive.png" alt="LightningAI Teamspace Drive" width="500">‎

!!!
The path to Applio is `Studio > this_studio > Applio > Applio`
!!!

c. Once you're there you can just drag and drop files.

d. To download files click on the file then click the three dots on the right of it and click download

<img src="../lightning-applio-img/teamspace-drive-download.png" alt="Teamspace Drive Download" width="500">

##### 7. Opening the TensorBoard.

a. Find the TensorBoard icon on the right side bar and click it.

<img src="../lightning-applio-img/tensorboard.png" alt="LightningAI TensorBoard" width="500">

b. Once you've clicked it, Start it.

<img src="../lightning-applio-img/run-tensorboard.png" alt="LightningAI Run TensorBoard" width="500">


c. Once you've done that it will open the TensorBoard. you can open it externally in another tab/window via clicking Open. To learn how to use it go <u>[here](https://docs.aihub.gg/rvc/resources/training/#usage-guide)</u>
***

#### 8. Opening the notebook.

a. If you want to go back to the notebook simply click on the `Jupyter` icon on the right. 

<img src="../lightning-applio-img/jupyter.png" alt="LightningAI Jupyter" width="500">


***
## Usage
Now that you have the web interface running via Lightning.AI, the rest of the process is **identical to using a local installation.**

For all subsequent steps, including application settings and model usage, please continue by following the Local PC guide.

[!button text="Continue with the Local PC Guide" icon="arrow-right" target="blank"](https://docs.aihub.gg/rvc/local/applio/#inference)


***
## Maintenance
#### Deleting Everything
If you need to update Applio or start fresh, you can run the final cell in the notebook, "Delete everything". This will remove all downloaded files and configurations from your persistent storage, allowing for a clean installation by re-following the notebook with perhaps a changed branch variable.


***
###### ‎   ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
