This Discord bot automatically updates a data.json file with a member id, date, and status whenever it sees a change in that member's status.

## Commands include:
* !hello or !ping - Use to check if bot is recieving commands properly. Should return "Hello!".
* !update or !refresh - The bot will update its log with all members with a status not set to offline.
* !lastseen or !ls - The bot will reply with the difference between the current datetime and the last logged datetime for the member(s) mentioned in the command. E.g. `!ls @Dysrhythmic @Ascii` will return how long ago it has been since the bot has logged both users.
* !status - Replies with the last status the bot logged for the given user(s).
* !printlog or !pl - Replies with a list of members that have been logged. E.g. If @Dysrhythmic is the only logged member then `!pl` will have the bot reply with *Dysrhythmic#9317*.