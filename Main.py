import discord

# Diccionario con objetos y tiempos de descomposición
decomposition_data = {
    "botella de plástico": "450 años",
    "botella de vidrio": "1 millón de años",
    "lata de aluminio": "80-200 años",
    "colilla de cigarrillo": "1-5 años",
    "bolsa de plástico": "10-20 años",
    "papel": "2-6 semanas",
    "cáscara de plátano": "2-5 semanas",
    "corazón de manzana": "2 meses",
    "suela de bota de caucho": "50-80 años",
    "lata de conservas": "50 años",
    "pañal desechable": "500 años",
    "línea de pesca": "600 años",
    "vaso de unicel": "500 años o más",
    "camiseta de algodón": "5 meses",
    "calcetín de lana": "1-5 años",
    "zapatos de cuero": "25-40 años",
    "tela de nylon": "30-40 años",
    "pajilla de plástico": "200 años",
    "chicle": "5 años",
    "tetra pak": "30 años",
    "cartón de leche": "5 años",
    "periódico": "6 semanas",
    "cuerda (fibra natural)": "3-14 meses",
    "cuerda (fibra sintética)": "30-40 años",
    "muebles acolchonados": "50-75 años",
    "baterías": "100 años",
    "llantas": "500 años",
    "utensilios de plástico": "1,000 años",
    "bandeja de espuma de poliestireno": "50 años",
    "poliestireno (espuma plástica)": "500 años o más",
    "cepillo de dientes": "500 años",
    "red de pesca": "600 años",
    "alfombra": "1,000 años",
    "tetrabrik": "30 años",
    "corcho": "200 años",
    "colchón de látex": "50 años",
    "bolsas de patatas fritas": "75-80 años",
    "pañuelos de papel": "2-4 semanas",
    "tapones de corcho": "3 años",
    "botellas de detergente": "500 años",
    "cápsulas de café": "150-500 años",
    "latas de refresco": "200 años",
    "envoltorios de dulces": "50 años",
    "cepillos de cabello": "500 años",
    "guantes de goma": "1-3 años",
    "tarjetas de crédito": "1,000 años",
    "envoltorios de plástico": "500 años",
    "tapas de plástico": "400-500 años",
    "televisores": "1,000,000 años (si no son reciclados)",
    "refrigeradores": "hasta 1,000 años",
    "vasos de papel con revestimiento plástico": "5-30 años"
}

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$info'):
        await message.channel.send("Este bot ha sido creado para compartir información acerca de algunos objetos utilizados en su día a día y sus tiempos de descomposición.")
        
        with open('Reciclaje.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)

    elif message.content.startswith('$descomposicion'):
        objeto = message.content[len('$descomposicion '):].strip()  
        
        if objeto in decomposition_data:
            tiempo = decomposition_data[objeto]
            await message.channel.send(f"El tiempo de descomposición de una {objeto} es: {tiempo}.")
        else:
            await message.channel.send("Lo siento, no tengo información sobre ese objeto.")
client.run("token here")
