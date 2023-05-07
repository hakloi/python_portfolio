import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print("logged on as {0}!".format(self.user))
        
    async def on_message(self, message):
        print("message from {0.author}: {0.content}".format(message))
        
client = MyClient()
client.run('token')