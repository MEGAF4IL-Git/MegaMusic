# Music bot
?Help - displays all the available commands.\
?P <YouTube Link> - Finds the song on youtube and plays it in your current channel. Will resume playing the current song if it was paused.\
?Q - Displays the current music queue.\
?Skip - Skips the current song being played.\
?Clear - Stops the music and clears the queue.\
?Leave - Disconnected the bot from the voice channel.\
?Pause - Pauses the current song being played or resumes if already paused.\
?Resume - Resumes playing the current song.\
?Prefix - Change command prefix.\
?Remove - Removes most recently added song from the queue.

# Installation
To run the discord bot all you need is python 3.13 or newer.\
Then run `pip install -r requirements.txt` to install all of the python dependencies.\
Please note that you will also need to have [ffmpeg](https://ffmpeg.org/download.html) installed and make sure that the path to the bin folder is in your environment variables.\
DO NOT FORGET to add a ".env" with the Discord Token. (i.e: "discord_token=TOKEN")
