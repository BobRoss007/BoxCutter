import discord
import random

giflist= ['https://media.giphy.com/media/hGLdrItUOxou4/giphy.gif',
          'https://media.giphy.com/media/YknxDq7L5YGe8UiSri/giphy.gif', 
          'https://media.giphy.com/media/l4KibK3JwaVo0CjDO/giphy.gif',
          'https://media.giphy.com/media/1XgHc6zjkSNNPuIY9r/giphy.gif',
          'https://media.giphy.com/media/2zlSwREmLmiQw/giphy.gif',
          'https://media.giphy.com/media/Nong9IGTzi46Y/giphy.gif',
          'https://media.giphy.com/media/l0ExsYAIdFoMqsIp2/giphy.gif',
          'https://media.giphy.com/media/TeinpBGRY5UOc/giphy.gif',
          'https://media.giphy.com/media/l41m5GyLvqR3IESZ2/giphy.gif',
          'https://media.giphy.com/media/1lxkNQ5SDqkEYociFG/giphy.gif',
          'https://media.giphy.com/media/b9TLVAyi8U6wE/giphy.gif',
          'https://media.giphy.com/media/9g99U7FIvhlRK/giphy.gif',
          'https://media.giphy.com/media/ZFXrBOptzMQVi/giphy.gif',
          'https://media.giphy.com/media/NwynINXfQKI4E/giphy.gif',
          'https://media.giphy.com/media/QCHpXmYAYU0TK/giphy.gif',
          'https://media.giphy.com/media/kZDGNBLCIOTmw/giphy.gif',
          'https://media.giphy.com/media/3JQyfGx5tukO4IG6Kz/giphy.gif',
          'https://media.giphy.com/media/MEUb2PZkTPdIc/giphy.gif',
          'https://media.giphy.com/media/y2G0NUuRJPbYQ/giphy.gif',
          'https://media.giphy.com/media/cgGbLeph0usyA/giphy.gif',
          'https://media.giphy.com/media/8uZ5c7IKNTDOM/giphy.gif',
          'https://media.giphy.com/media/11b6KqCRoVtO9y/giphy.gif',
          'https://media.giphy.com/media/acPDlKtyWELAI/giphy.gif',
          'https://media.giphy.com/media/KcxTf64hiTXjO/giphy.gif',
          'https://media.giphy.com/media/UngypwFhpEayI/giphy.gif',
          'https://media.giphy.com/media/GpyyJ3fLHUj1C/giphy.gif',
          'https://media.giphy.com/media/3btc09rgXbMI0/giphy.gif',
          'https://media.giphy.com/media/kvLndz7H41ejm/giphy.gif',
          'https://media.giphy.com/media/8xi9bRpuAPEQw/giphy.gif',
          'https://media.giphy.com/media/y1GC8VzArYSn6/giphy.gif',
          'https://media.giphy.com/media/3t5L3MPSs2Yi4/giphy.gif',
          'https://media.giphy.com/media/REEkKxT7c3RO8/giphy.gif',
          'https://media.giphy.com/media/A1CR5l5xVpQME/giphy.gif',
          'https://media.giphy.com/media/RkDX1g4tF9vYYCKcxg/giphy.gif',
          'https://media.giphy.com/media/13kTeNK71Ca9lm/giphy.gif',
          'https://media.giphy.com/media/9SO5aaN3PF94s/giphy.gif',
          'https://media.giphy.com/media/NIdHOQaDRcwko/giphy.gif',
          'https://media.giphy.com/media/oU1xVGM2Gij3G/giphy.gif',
          'https://media.giphy.com/media/tSZWryfF3SeQg/giphy.gif',
          'https://media.giphy.com/media/56Vd97ywRR2Cs/giphy.gif',
          'https://media.giphy.com/media/BmCoTTCJE7d8Q/giphy.gif',
          'https://media.giphy.com/media/ijKWuLjBoU6v6/giphy.gif',
          'https://media.giphy.com/media/D4dms4FPTZJVm/giphy.gif',
          'https://media.giphy.com/media/RLhTznVNxS4gg/giphy.gif',
          'https://media.giphy.com/media/RLhTznVNxS4gg/giphy.gif',
          'https://media.giphy.com/media/7VUnN0LBp3IIg/giphy.gif',
          'https://media.giphy.com/media/ZPF8pnFRZTT7W/giphy.gif',
          'https://media.giphy.com/media/a3MqlREtKlz1u/giphy.gif',
          'https://media.giphy.com/media/3nCQpjiPXad7q/giphy.gif',
          'https://media.tenor.com/images/a113c67470c544b786cca87f2a163cd3/tenor.gif',
          'https://media.tenor.com/images/ad502ec087982cda920bdd5ef875b313/tenor.gif',
          'https://media.tenor.com/images/a113c67470c544b786cca87f2a163cd3/tenor.gif',
          'https://media.tenor.com/images/d58069718d99f47890bd449d6bcae7bc/tenor.gif',
          'https://media.tenor.com/images/950f7710cf2f80acc91c3869bfe1f973/tenor.gif',
          'https://media.tenor.com/images/6eecea5f246edb1825157e035948c9f7/tenor.gif',
          'https://media.tenor.com/images/2bc82e5a5c7ea2b0687ca3320a7aaf2d/tenor.gif',
          'https://media.tenor.com/images/427e512b268bd5f3a6b4a8bc1b112e1d/tenor.gif',
          'https://media.tenor.com/images/eab0253bde4bf384d2e63c957e871a0a/tenor.gif']
cutterball= ['I could see that',
              'no way!',
              'yes way!',
              'That will happen!!',
              'OOF',
              'EEEWWW',
              'NANI??!!!',
              'ha, okay big mon']

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as: {0.user}, welcome.'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('.rules'):
        embed = discord.Embed(title="Rules", url="https://discordapp.com/terms", description= '''-Post in the appropriate channels.
-No spamming or trolling
-No NSFW images in non NSFW Channels.
-No asking for mod or admin roles.
-No advertising 3rd party games
-No advertising 3rd party Discord channels
-Be respectful of each other
-No advertisements for products or services''' , color=0xFF8000)
        embed.add_field(name="Community Guidelines", value='''While with others in this Discord, you may encounter many others who share different experiences and come from different backgrounds. 
While certain language and images may not be offensive to you, consider the fact that the same language and images may have a completely different effect on someone else. 
The chat moderators shall have full discretion to address any behaviour they feel is inappropriate on a case by case basis.

Repeated offences may result in a ban''', inline=False)
        embed.set_footer(text="- The Box Cutters Team")
        await message.channel.send(embed=embed)

    if message.content.startswith('.banner'):
        embed=discord.Embed(color=0xff8000)
        embed.set_image(url='https://cdn.discordapp.com/attachments/638209719684694016/644404501205352449/rules_banner.png')
        await message.channel.send(embed=embed)

    if message.content.startswith('.box'):
        embed=discord.Embed(color=0xff8000)
        embed.set_image(url=random.choice(giflist))
        await message.channel.send(embed=embed)

    if message.content.startswith('.cutterball'):
        embed=discord.Embed(color=0xff8000)
        embed.add_field(name= 'I have the answer you seek', value=random.choice(cutterball), inline=False)
        await message.channel.send(embed=embed)


client.run('NjgwMjYzNjM1MDUzODM4MzQ0.Xk9Xiw.jm0Nf-n6PPXujpKD21NNiioNME4')