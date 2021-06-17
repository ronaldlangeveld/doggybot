# Doggy poop schedule bot.

Built this little telegram bot to remind my parents to take out the dogs at certain times of the day to minimise the risk of accidents in the house.

ENV VARIABLES

```
GROUP_ID=telegram group ID
DEBUG_ID=personal telegram id
BOT_TOKEN=
DEBUG=True

```


#CRON STUFF IN UTC TIME ON MY UBUNTU SERVER

```

# 0 6 * * * /home/ronald/cron/dogpoop/doggybot/venv/bin/python3 /home/ronald/cron/dogpoop/doggybot/bot.py SendMessage "Good Morning. I request you take me out if I haven't been out yet. I've been trying to hold all night."
# 0 7 * * * /home/ronald/cron/dogpoop/doggybot/venv/bin/python3 /home/ronald/cron/dogpoop/doggybot/bot.py SendMessage "Now that I've had my breakfast, please take me out again. 💩"
# 0 10 * * * /home/ronald/cron/dogpoop/doggybot/venv/bin/python3 /home/ronald/cron/dogpoop/doggybot/bot.py SendMessage "I've been sleeping again till now. Let me go out again for a wee."
# 0 12 * * * /home/ronald/cron/dogpoop/doggybot/venv/bin/python3 /home/ronald/cron/dogpoop/doggybot/bot.py SendMessage "Maybe a good idea to go stretch my legs outside, some fresh air and a bit of sun."
# 0 14 * * * /home/ronald/cron/dogpoop/doggybot/venv/bin/python3 /home/ronald/cron/dogpoop/doggybot/bot.py SendMessage "Take me outside quickly before Mom come's home!"
# 0 16 * * * /home/ronald/cron/dogpoop/doggybot/venv/bin/python3 /home/ronald/cron/dogpoop/doggybot/bot.py SendMessage "If there's no monkeys waiting to kill me outside, please may I go outside?"
# 0 18 * * * /home/ronald/cron/dogpoop/doggybot/venv/bin/python3 /home/ronald/cron/dogpoop/doggybot/bot.py SendMessage "Okay, I need to go empty my tummy before dinner. Oh yes!"
# 0 20 * * * /home/ronald/cron/dogpoop/doggybot/venv/bin/python3 /home/ronald/cron/dogpoop/doggybot/bot.py SendMessage "I'm ready to go sleep. Let me out for 15 minutes and then feed me a sausage! Good Night."


```