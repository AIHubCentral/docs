==- :icon-terminal: Getting Detailed Server Logs (Debug Mode)
The web interface (client) is just a control panel; the actual voice conversion and backend processes happen on the server. If the server closes unexpectedly or you run into issues, you can launch it in **Debug Mode** to see the exact error logs before the window closes.

To do this, you need to append `--log-level debug` when launching the server.

+++ Windows (Command Prompt)
1. Open your extracted `MMVCServerSIO` folder.
2. Click on the File Explorer's address bar at the top, type `cmd`, and press **Enter**.
3. In the black window that appears, run the following command:
```cmd
MMVCServerSIO.exe --log-level debug
```
*(Alternatively, you can create a shortcut of the `.exe`, open its Properties, and add ` --log-level debug` to the end of the **Target** line).*

+++ Windows (PowerShell)
1. Open your extracted `MMVCServerSIO` folder.
2. Click on the File Explorer's address bar at the top, type `powershell`, and press **Enter**.
3. Run the following command (note the `.\` required by PowerShell):
```powershell
.\MMVCServerSIO.exe --log-level debug
```

+++ Mac & Linux
1. Open your Terminal and navigate to your `MMVCServerSIO` folder.
2. Run the executable with the debug flag:
```bash
./MMVCServerSIO --log-level debug
```
+++

Once the server runs or crashes, **copy all the text from the command line window**. Save it to a `.txt` file, or paste it to a site like [Pastebin](https://pastebin.com/) to share with others when asking for support.


!!!info Other Log Levels
By default, the server runs on the `info` log level. While the server also supports `warning`, `error`, and `critical` levels, you should avoid using them for troubleshooting. They filter out background information, hiding the context developers need to figure out why your server crashed.
!!!
===