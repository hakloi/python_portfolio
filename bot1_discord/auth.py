import discord
import config
from discord import utils


class MyClient(discord.Client):
    async def on_ready(self):
        print("logged on as {0}!".format(self.user))
        
    async def on_raw_reaction_add(self, payload):
        channel = self.get_channel(payload.channel_id) #объект канала
        message = await channel.fetch_message(payload.message_id) #объект сообщения
        member = utils.get(message.guild.members, id=payload.user_id) #объект пользователя с реакцией
    
        try:
            emoji = str(payload.emoji)
            role = utils.get(message.guild.roles, id=config.ROLES[emoji] )
            
            if(len([i for i in member.roles if i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
                await member.add_roles(role)
                print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
            else:
                await message.remove_reaction(payload.emoji, member)
                print('[ERROR] Too many roles for user {0.display_name}'.format(member))
            
        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))
    
    async def on_raw_reaction_remove(self, payLoad):
        pass
        
client = discord.Client(intents=discord.Intents.default())
client.run(config.TOKEN)