import discord
import requests  # Do wysyłania żądań HTTP
from discord.ext import commands

# Ustawienia uprawnień
intents = discord.Intents.default()
intents.reactions = True

# Tworzymy bota
bot = commands.Bot(command_prefix="!", intents=intents)

# Adres webhooka n8n, który będzie odbierał dane
n8n_webhook_url = "https://primary-production-7ddc.up.railway.app/webhook-test/2a9ab676-ad9c-42b4-8a84-26872a7efc02"  # Zastąp tym URL swojego webhooka z n8n

# Event - dodanie reakcji
@bot.event
async def on_reaction_add(reaction, user):
    # Jeśli reakcja została dodana przez bota, ignorujemy ją
    if user.bot:
        return

    # Tworzymy dane, które będą wysyłane do n8n (możesz dostosować dane w zależności od potrzeb)
    data = {
        "user": user.name,
        "emoji": str(reaction.emoji),
        "message_id": reaction.message.id,
        "channel_id": reaction.message.channel.id,
        "reaction_count": len(reaction.users)
    }

    # Wysyłamy dane do webhooka n8n
    response = requests.post(n8n_webhook_url, json=data)

    # Jeśli chcesz, możesz dodać logowanie odpowiedzi
    if response.status_code == 200:
        print("Dane wysłane do n8n.")
    else:
        print(f"Nie udało się wysłać danych do n8n. Status: {response.status_code}")

# Uruchamiamy bota
bot.run("MTM2MTg0OTk1NTMwNzg4NDYzNQ.G_g6fW.XHZBtoD1SxDjF4lQWUVUsQr2eSDAZcIilpJX14")  # Wstaw tutaj swój token bota
