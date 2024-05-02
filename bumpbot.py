import discord
import asyncio

# Configura el cliente de Discord
client = discord.Client()

# Token de tu bot (reemplaza 'TU_TOKEN' con el token de tu bot real)
TOKEN = 'TU_TOKEN'

# ID del canal donde quieres que el bot haga bump
CANAL_ID = 'https://discord.com/channels/1191792395457679381/1226931635505725584'

# Función para hacer bump cada 2 horas
async def hacer_bump():
    await client.wait_until_ready()
    canal = client.get_channel(CANAL_ID)
    while not client.is_closed():
        await canal.send('/bump')
        await asyncio.sleep(2)  # Esperar 2 segundos antes de enviar otro mensaje

# Evento de inicio del bot
@client.event
async def on_ready():
    print('Bot conectado como {0.user}'.format(client))
    # Comienza el ciclo de bumping
    client.loop.create_task(hacer_bump())

# Ejecutar el bot
client.run(TOKEN)
