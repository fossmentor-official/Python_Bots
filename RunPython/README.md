# run-py-bot

Run python code from your telegram chat!

## ⚡ Deploy

You can easily *deploy this bot* on [Python Anywhere](https://www.pythonanywhere.com/) or your **local machine** by following the below steps:

> Note: While pasting on your machine terminal you should use `Ctrl+Shift+V` but make sure to use `Ctrl+V` to paste in the Python Anywhere bash console from the browser.

Create a free Python Anywhere account and open a Bash Console, which has everything pre-loaded.

If you are planning to deploy on your **own machine**, make sure to have `Python3+`, `pip`.

The following instructions will work smoothly on *Linux* and *Mac*. If you are on Windows, you may have to make slight modifications. Google is your best friend here.

- Clone this repository and move into this directory which has this README you are reading.

- Now add the token in the first line of `token.txt`.Run `cat > token.txt` -> Paste the token -> Press `Ctrl+D`

- Create a virtual environment and install dependencies.

      python3.8 -m venv venv && source venv/bin/activate
      python3.8 -m pip install -r requirements.txt

- Activate the bot by running `python3.8 start.py`

- You may now close the Python Anywhere bash console window from your browser, but the bot will continue running.

Your bot is now up and running, Enjoy ! 😊

All the logs will have the timestamp in the time-zone specified in the `start.py` file.

To stop the bot, press `Ctrl+C`. You may update the code running in your server by `git fetch && git pull`.

## 😑 Limitations

Currently, the bot is deployed on a Free Tier account of Python Anywhere.

For security and performance reasons, you **cannot** do the following with the bot:

- import any package
- run the `input()` function
- run the `open()` function
- Execute a piece of code which takes longer than *6 seconds* to execute.

You may overcome these limitations by changing the `config.py` file in the `bot` subdirectory and running the bot on your own server.

## Author
[Fossmentor](https://github.com/fossmentorOfficial)