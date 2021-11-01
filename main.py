from discord_webhook import DiscordWebhook

lol=["webhook link"]

webav = ("image link")

webhook = DiscordWebhook(url=lol,content="Send Send Send", username="Sended", avatar_url=(webav))

while True:
 response = webhook.execute()
