# Shock Over Ethernet

This repository contains the code for a Python based Discord bot called "Dr. Trainer". This bot lets users control the Dr. Trainer shock collar through Discord commands. This bot can also be adapted and used outside of Discord to control the shock collar through other mechanisms.

## Ethical Disclaimer

This project is meant for educational and experimental purposes only. The creators and contributors of this repository are in no way responsible or liable for any harm, damage, or injury caused as a result of using this software with the Dr. Trainer shock collar. Any form of misuse is entirely at the user's own risk.

## Technical Disclaimer

We acknowledge that this is not the most elegant or efficient solution to control the shock collar. As at the moment of writing this, the exact Bluetooth signals sent by the Dr. Trainer app are unknown. This project is a workaround till a better solution is found.

## Prerequisites

Before getting started, ensure you have:

- Dr. Trainer shock collar, which can be found on Amazon. Make sure it is the model that supports app control and shock functionality.
- An Android device running Android 4.0 or greater that has a stable internet connection.
- A spare Windows machine capable of running Python 11, preferably Windows 10/11, with a stable internet connection.

## Installation and Setup

Follow these steps to set up the system:

1. **Download Apps**
    - Download the "AirDroid" and "Dr. Trainer" apps from the Google Play Store onto your Android device.
    - Install the "AirDroid" app on the spare Windows machine and follow the steps provided by the app to configure remote desktop access to the Android device.
   
2. **Set up Python Code**
   - Download 'Shock Over Ethernet.py' from this repository and load it into your preferred code editor.
   - On line 7 of the code, replace the placeholder with your Discord bot token.

3. **Install Python Libraries**
   - Open the terminal on your Windows machine and run the following commands to install the necessary Python libraries:
       ```
       pip install pyautogui
       pip install discord
       ```

4. **Pair the Shock Collar and Run the Bot**
   - Pair the shock collar with the Dr. Trainer Android app.
   - On your Windows machine, run the Python file, then enter full-screen remote desktop mode.
   - Go to the 'remote' section of the app on the Android device.
   - In the Discord chat where the bot is present, type `!shock` to send a command to the bot.
   - If your Android device has different dimensions than those used during the development of this project, you might need to adjust the coordinates of the click on line 21 of the Python code.

5. **Optimization**
   - For the best integration experience, set both the Android device and Windows machine to never enter sleep or idle mode.

Congratulations, you've set up your Dr. Trainer shock collar Discord bot. Please remember to use this responsibly and at your own risk!

## Contributing
If you have ideas about how to improve this project or have discovered the exact Bluetooth signals sent by the Dr. Trainer app, please feel free to make a pull request. Your contributions will be greatly appreciated.
