This Discord bot automatically updates a data.json file with a member id, date, and status whenever it sees a change in that member's status.

## Commands include:
* !hello or !ping - Use to check if bot is recieving commands properly. Should return "Hello!".
* !update or !refresh - The bot will update its log with all members with a status not set to offline.
* !lastseen or !ls - The bot will reply with the difference between the current datetime and the last logged datetime for the member(s) mentioned in the command. E.g. `!ls @Dysrhythmic @Ascii` will return how long ago it has been since the bot has logged both users.
* !status - Replies with the last status the bot logged for the given user(s).
* !printlog or !pl - Replies with a list of members that have been logged. E.g. if @Dysrhythmic is the only logged member then `!pl` will have the bot reply with *Dysrhythmic#9317*.

## Setup:
* Go to the [Discord developer portal](https://discord.com/developers/applications), create a new application, name it, go to the bot tab, and add bot.
* You get your bot's token from the bot tab, which you will need for logging in your bot. Don't share the token with others.
* Your bot token should be stored in a *.env* file as `BOT_TOKEN=YOUR_TOKEN_HERE`.
* Since this bot tracks presence data of server members you will also need to enable "Presence Intent" and "Server Members Intent" settings in the bot tab.
* Set whatever permissions you want the bot to have in the "Bot Permissions" section (e.g. view channels, send messages, etc.).
* Go to the OAuth2 tab and check the box next to "bot" in the "Scopes" section.
* Copy the URL generated at the bottom of the "Scopes" section. Go to the URL in a new tab or window.
* This will take you to a page where you log into your Discord account and choose which of your servers you want the bot to be added to.
* Authorize the bot and it will join the server in offline mode. It will not be online until you run the Python file.
* The Discord API can be found [here](https://discordpy.readthedocs.io/en/stable/api.html), and it's extension can be found [here](https://discordpy.readthedocs.io/en/stable/ext/commands/index.html).
