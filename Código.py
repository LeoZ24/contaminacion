# contaminacion
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def Hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def CambioClimatico(ctx):
    await ctx.send("Es el aumento del calor (temperatura) en nuestro planeta, el cual es producido por el exceso de GEI en la atmósfera. Así es, el humo de los carros, la basura, los gases de los aerosoles (desodorante) y el corte de árboles son demasiados para nuestro planeta y producen muchísimos GEI.")

tips = [
    "Reducir el consumo de energía",
    "Reducir el uso de combustibles fósiles",
    "Usar energías renovables",
    "Consumir menos y reutilizar más",
    "Reducir el desperdicio de agua",
    "Adoptar una alimentación sostenible",
    "Apoyar la reforestación y proteger los ecosistemas",
    "Reducir el uso de plásticos y desechables",
    "Participar en iniciativas ecológicas y activismo",
    "Educar y concienciar",
    "Utilizar transporte público, bicicleta o caminar en lugar de autos particulares",
    "Comprar productos locales y de temporada para reducir la huella de carbono",
    "Evitar el desperdicio de alimentos planificando las compras y almacenando bien los alimentos",
    "Plantar árboles y apoyar proyectos de reforestación",
    "Ahorrar agua cerrando el grifo mientras te cepillas los dientes o lavas los platos",
    "Usar bolsas reutilizables en lugar de bolsas de plástico",
    "Reducir el consumo de carne y optar por dietas más vegetales",
    "Utilizar baterías recargables en lugar de desechables",
    "Reparar y reutilizar objetos antes de desecharlos",
    "Reciclar correctamente separando los residuos según el material",
    "Optar por ropa sostenible y evitar la moda rápida",
    "Usar menos papel y optar por versiones digitales siempre que sea posible",
    "Optar por cosméticos y productos de higiene ecológicos y sin microplásticos",
    "Desconectar aparatos electrónicos cuando no se usen para evitar el consumo en modo espera",
    "Usar electrodomésticos eficientes y aprovechar programas ecológicos",
    "Evitar el uso excesivo de calefacción y aire acondicionado",
    "Utilizar energías limpias como la solar o eólica en el hogar",
    "Participar en campañas de limpieza de playas, ríos y bosques",
    "Promover el uso de empaques biodegradables",
    "Reducir el consumo de productos desechables como vasos y cubiertos de plástico",
    "Evitar productos con exceso de embalaje",
    "Usar bombillas LED en lugar de incandescentes",
    "Incentivar a empresas a adoptar prácticas sostenibles",
    "Apoyar marcas y negocios comprometidos con el medio ambiente",
    "Crear un huerto en casa o participar en huertos urbanos",
    "Fomentar el compostaje para reducir residuos orgánicos",
    "No arrojar basura en la calle, ríos o mares",
    "Promover la educación ambiental en la comunidad",
    "Compartir conocimientos sobre sostenibilidad con familiares y amigos",
    "Evitar comprar agua embotellada y usar botellas reutilizables",
    "No desperdiciar papel, reutilizar hojas y reciclarlas",
    "Apagar las luces al salir de una habitación",
    "Utilizar cortinas o persianas para regular la temperatura en casa",
    "Evitar el uso de globos y confeti plástico en celebraciones",
    "Hacer turismo ecológico y respetuoso con la naturaleza",
    "Usar medios digitales para facturas y documentos en lugar de impresiones",
    "Apoyar iniciativas de reducción de emisiones de carbono",
    "No tirar aceite usado por el desagüe, reciclarlo correctamente",
    "Elegir productos con certificaciones ecológicas",
    "No comprar productos hechos con pieles de animales o materiales no sostenibles"
]

datos_curiosos = [
    "El 20% de las emisiones de gases de efecto invernadero provienen de la deforestación.",
    "El nivel del mar ha aumentado aproximadamente 20 cm desde 1880.",
    "Las olas de calor extremas están aumentando en frecuencia y duración debido al cambio climático.",
    "El 97% de los científicos climáticos están de acuerdo en que el cambio climático es causado por la actividad humana.",
    "El Ártico se está calentando dos veces más rápido que el resto del planeta.",
    "En 2020, las temperaturas globales fueron las más altas registradas en la historia.",
    "El cambio climático puede aumentar la frecuencia de fenómenos meteorológicos extremos como huracanes y sequías.",
    "La agricultura es responsable de aproximadamente el 25% de las emisiones globales de gases de efecto invernadero.",
    "La acidificación de los océanos está afectando a los ecosistemas marinos debido al aumento del CO2 en la atmósfera.",
    "Las capas de hielo en la Antártida y Groenlandia están perdiendo masa a una tasa acelerada.",
    "El 70% de las emisiones globales de gases de efecto invernadero provienen de 100 empresas multinacionales.",
    "El cambio climático está afectando a las especies animales, provocando la extinción de algunas y el desplazamiento de otras.",
    "Las zonas urbanas contribuyen significativamente al cambio climático debido al uso intensivo de energía y el transporte.",
    "El cambio climático podría desplazar a más de 200 millones de personas para el año 2050 debido a la subida del nivel del mar.",
    "Cada año se pierden alrededor de 13 millones de hectáreas de bosques en todo el mundo debido a la deforestación y el cambio climático."
]

@bot.command()
async def Tip(ctx):
    tip = random.choice(tips)
    await ctx.send(f"🌱 Sugerencia ecológica: {tip}")

@bot.command()
async def DatoCurioso(ctx):
    dato = random.choice(datos_curiosos)
    await ctx.send(f"🌍 Dato curioso sobre el cambio climático: {dato}")

bot.run("TU TOKEN AQUI")
