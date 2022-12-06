from telethon import TelegramClient
import time
import schedule
import threading
api_id = 9257340
api_hash = '83f3a9c114640d847a72457b5e4ef724'
client12= TelegramClient('anon12', api_id, api_hash)

client13= TelegramClient('anon13', api_id, api_hash)

client14= TelegramClient('anon14', api_id, api_hash)
client15= TelegramClient('anon15', api_id, api_hash)
client16 = TelegramClient('anon16', api_id, api_hash)
async def main12():
    #FIVERR012
     
    print("CLIENT12 IS RUNNING")
    groups = []
    async for dialog in client12.iter_dialogs():
        if(dialog.id < 0):
                print(dialog.name)
                groups.append(dialog.id)
    print(groups)      
    for group in groups:
        time.sleep(80)
        try:
            await client12.send_file(group, 'pic1.jpg')
            print("CLIENT 12 message sent to group" + str(group))
            
        except Exception as er:
    
            print(er)  
async def main13():
    #FIVERR012
     
    print("CLIENT13 IS RUNNING")
    groups = []
    async for dialog in client13.iter_dialogs():
        if(dialog.id < 0):
                print(dialog.name)
                groups.append(dialog.id)
    print(groups)      
    for group in groups:
        time.sleep(10)
        try:
            await client13.send_message(group,"REDDIT ADVERTISING COURSE AVAILABLE FOR ONLY $20🔥📈\n"+
"\n"+
                                                "We have used reddit advertising for years with many models who started from scratch and others in the top 1%. Reddit is an easy and effective way to gain quality fans because they are SPENDERS and constantly looking 💰\n"+
"\n"+
                                                "There are hundreds of subreddits to post in which gives any girl from thick to thin the ability to gain attention 💕\n"+
"\n"+
                                                "You can implement the strategies right away and start gaining fans within the first week. PLEASE DM me for more details! ⚡️")
            print("CLIENT 13 message sent to group" + str(group))
            
        except Exception as er:
    
            print(er)  
async def main14():
    #FIVERR014
     
    print("CLIENT14 IS RUNNING")
    groups = []
    async for dialog in client14.iter_dialogs():
        if(dialog.id < 0):
                print(dialog.name)
                groups.append(dialog.id)
    print(groups)      
    for group in groups:
        time.sleep(95)
        try:
            await client14.send_file(group, 'pic3.jpg')
            print("CLIENT 14 message sent to group" + str(group))
            
        except Exception as er:
    
            print(er)  
async def main15():
    #FIVERR014
     
    print("CLIENT15 IS RUNNING")
    groups = []
    async for dialog in client15.iter_dialogs():
        if(dialog.id < 0):
                print(dialog.name)
                groups.append(dialog.id)
    print(groups)      
    for group in groups:
        time.sleep(5)
        try:
            await client15.send_file(group, 'pic3.jpg', caption="-quality fans ⚡️\n"+
                                                            "-Grown from socials and ads🔥\n"+
                                                            "-exposed to over 70k fans🤩\n"+
                                                            "Dm me @Baddiprincess to book ✅\n"+
                                                            "\n"+
                                                            "@Baddiprincess❤️‍🔥\n"+
                                                            "\n"+
                                                            "@Baddiprincess❤️‍🔥\n"+
                                                            "\n"+     
                                                            "@Baddiprincess❤️‍🔥")
            print("CLIENT 15 message sent to group" + str(group))
            
        except Exception as er:
    
            print(er)  
async def main16():
    #FIVERR016
     
    print("CLIENT16 IS RUNNING")
    groups = []
    async for dialog in client16.iter_dialogs():
        if(dialog.id < 0):
                print(dialog.name)
                groups.append(dialog.id)
    print(groups)      
    for group in groups:
        time.sleep(60)
        try:
            await client16.send_file(group, 'pic16.png', caption=
            "Selling IG shoutouts🔥\n"+
            "\n"+
            "Dm me to book✅\n"+
            "24 hour posts🚀\n"+
            "All organic followers✨\n"+
            "NO Paid followers⚡️\n"+
            "\n"+
            "💞DM me to book💞")


            print("CLIENT 16 message sent to group" + str(group))
            
        except Exception as er:
    
            print(er)  
while True:
    try:
        # with client16:
        #     client16.loop.run_until_complete(main16())
        # with client15:
        #     client15.loop.run_until_complete(main15())
        # with client12:
        #     client12.loop.run_until_complete(main12())
        with client13:
            client13.loop.run_until_complete(main13())
        with client14:
            client14.loop.run_until_complete(main14())
    except Exception as er:
        print(er)

    time.sleep(1)