==- :icon-terminal: Getting Detailed Server Logs (Debug Mode)
The web interface (client) is just a control panel; the actual voice conversion and backend processes happen on the server. If the cloud server crashes or fails to launch properly, you can enable **Debug Mode** to read the exact error logs directly in your notebook's output cell.

To do this, you need to append the `--log-level debug` argument to the command that launches the server.

+++ Google Colab
1. Scroll to the bottom of your notebook to find the cell that starts the server.
2. Look for the execution command: `!./ML_Program`
3. Add the debug flag to the end of the command so it looks like this:
```bash
!./ML_Program --log-level debug
```
4. Run the cell again.

+++ Kaggle & Lightning.AI
1. Locate the final cell in your notebook/studio that actually starts the server.
2. Look for the execution command: `!./VoiceChanger`
3. Add the debug flag to the end of the command so it looks like this:
```bash
!./VoiceChanger --log-level debug
```
4. Run the cell again.
+++

The notebook output cell will now print detailed debug logs. If the server crashes, **copy the text output from that cell**. Save it to a `.txt` file, or paste it to a site like [Pastebin](https://pastebin.com/) to share with others when asking for support.


!!!info Other Log Levels
By default, the server runs on the `info` log level. While the server also supports `warning`, `error`, and `critical` levels, you should avoid using them for troubleshooting. They filter out background information, hiding the context developers need to figure out why your server crashed.
!!!
===