# Wiki-Zulip-Bot

## About 
Bot which sends Wikimedia-specific Zulip welcome messages to newcomers

## Setup
Run the following commands from Your root directory

## Step 1

`git clone https://github.com/spielers/zulip_bot.git`  /* To clone this repository */

`cd zulip-bot ` /* To Navigate to the cloned repo */

`cd python-zulip-api` - navigate into your cloned repository.

`python3 ./tools/provision` - install all requirements in a Python virtualenv.

The output of provision will end with a command of the form source .../activate; run that command to enter the new virtualenv. 


## Step 2 

Go to your Zulip account and add a bot. Use Generic bot as the bot type.

Download the bot's `zuliprc` configuration file to your computer.

Download the `zulip_bots` Python package to your computer using pip3 install zulip_bots.

Note: Click here to install the latest development version of the package.

Start the bot process on your computer.

`Run zulip-run-bot <bot-name> --config-file ~/path/to/zuliprc`
here replace bot name with the generic bot that you created in zulip application above and give the correct path to the zulpric that you have downloaded.

### Step 3
create `keys.yaml` file inside root directory
and add your secret key in it.

### Step 4
```
cd src
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
```

Open http://127.0.0.1:8000/ to see the code in your browser!


