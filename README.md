# Music bot

?help - displays all the available commands\
?p <YouTube Link> - finds the song on youtube and plays it in your current channel. Will resume playing the current song if it was paused\
?q - displays the current music queue\
?skip - skips the current song being played\
?clear - Stops the music and clears the queue\
?leave - Disconnected the bot from the voice channel\
?pause - pauses the current song being played or resumes if already paused\
?resume - resumes playing the current song\
?prefix - Change command prefix\
?remove - Removes most recently added song from the queue

# Installation
To run the discord bot all you need is python 3.13 or newer.\
Then run `pip install -r requirements.txt` to install all of the python dependencies.\
Please note that you will also need to have [ffmpeg](https://ffmpeg.org/download.html) installed and make sure that the path to the bin folder is in your environment variables.\
DO NOT FORGET to add a ".env" with the Discord Token. (i.e: "discord_token=TOKEN")
