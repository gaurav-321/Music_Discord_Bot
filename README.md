# Discord Music Bot

This is a simple Discord bot that can play music and manage a queue of songs.

## Installation

1. Clone this repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Create a Discord bot and get its token. Follow [these instructions](https://discordpy.readthedocs.io/en/stable/discord.html) for more information.
4. Add the bot to your Discord server using the OAuth2 URL. Follow [these instructions](https://discordpy.readthedocs.io/en/stable/discord.html#inviting-your-bot) for more information.
5. Set the `DISCORD_TOKEN` environment variable to your bot's token.
6. Run the bot using `python bot.py`.

## Usage

1. Type `/play <url>` to add a song to the queue and start playing music.
2. Type `/skip` to skip the current song and play the next song in the queue.
3. Type `/emptyqueue` to empty the queue.
4. Type `/stop` to stop playing music and disconnect the bot from the voice channel.
5. Type `/listqueue` to list the songs in the queue.
6. Type `/help` to show a list of available commands.

## License

This project is licensed under the [MIT License](LICENSE).
