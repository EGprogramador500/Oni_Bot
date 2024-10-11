import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
from config import TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("Plantillas SGA ✏️", callback_data='sga'),
        InlineKeyboardButton("Reprogramación 🔄", callback_data='obs')
    )
    bot.send_message(message.chat.id, 
                     "Bienvenido a tu Asistente Virtual Oni 🙌🏻\nSeleccione una opción:", 
                     reply_markup=keyboard)

# Manejador para las opciones de botones
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'sga':
        send_sga(call.message)
    elif call.data == 'obs':
        send_obs(call.message)

# Funciones para enviar las plantillas
def send_sga(message):
    msg = bot.send_message(message.chat.id,
    """
        Plantilla Averias:

        /1 Plantilla Llegada
        /2 Cliente de Baja
        /3 Utiliza Splitter
        /4 Alerta Cliente Desconectado 
        /5 Autoriza  Recableado 
        /6 Validación Llamada
        /7 Validar Casos con Costo
        /8 Cambio de Mesh
        /9 Entrega de Mesh 
        /10 Entrega de Teléfono
        /11 Cambio de Teléfono
        /12 Entrega de Winbox
        /13 Cambio de Winbox
        /14 RX
        /15 Rematriculación
        /16 Cambio de ONT
        /17 RX Para Recableado 
        /18 Reporte a PEXT
        /19 Cambio de CTO, Puerto, Traslado
        /20 Traslado + Cambio de ONT
        /21 Plantilla de Cierre
        /22 Cambio de Ticket
        /23 Plantilla para Supervisor
    """
    )

    time.sleep(10)  # Esperar 10 segundos
    bot.delete_message(message.chat.id, msg.message_id)

@bot.message_handler(commands=["1"])
def send_1 (message):
    bot.reply_to(message,
    """
        1- PLANTILLA DE LLEGADA

        TICKET: 
        DNI: 
        CLIENTE: 
        DIRECCIÓN: 
        CONTRATA: 
        TÉCNICO: 
        PLACA DEL VEHÍCULO: 
        OBSERVACIONES:
    """
    ,)
@bot.message_handler(commands=["2"])
def send_2 (message):
    bot.reply_to(message,
    """
        2- UTILIZACIÓN DE CLIENTE DE BAJA

            TICKET: 
            CLIENTE:
            DNI: 
            CTO O CAJA NAP: 
            PUERTO UTILIZADO: 
            POTENCIA DE PUERTO UTILIZADO: 
            DNI DEL CLIENTE AFECTADO: 
            CONTRATA:
    """
    ,)
@bot.message_handler(commands=["3"])
def send_3(message):
    bot.reply_to(message,
    """
        3- SPLITTER (FOTO DE LA NAP/CTO CERRADA)

        TICKET: 
        CLIENTE COLOCADO EN SPLITTER: 
        DNI DEL CLIENTE COLOCADO: 
        ------------------------------------- 
        DNI DEL CLIENTE AFECTADO: 
        CTO: 
        COORDENADAS CTO: 
        PUERTO UTILIZADO:
        ------------------------------------- 
        POTENCIA EN EL PUERTO: 
        POTENCIA EN EL PUERTO CON SPLITTER: 
        CONTRATA:
    """
    ,)
@bot.message_handler(commands=["4"])
def send_4 (message):
    bot.reply_to(message,
    """
        4- ALERTA POR CLIENTE DESCONECTADO

        TICKET: 
        CLIENTE ATENDIDO: 
        DNI DEL CLIENTE ATENDIDO: 
        CTO o CAJA NAP: 
        PUERTO: 
        DNI DEL CLIENTE CONECTADO ACTUALMENTE EN EL PUERTO: 
        DATOS DEL TÉCNICO QUE REPORTA: 
        CONTRATA:
    """
    ,)
@bot.message_handler(commands=["5"])
def send_5 (message):
    bot.reply_to(message,
    """
        5- AUTORIZACIÓN PARA RECABLEADO MISMA CTO/CAMBIO DE CTO- CAJA NAP / TRASLADO / REINSTALACIÓN 

        TICKET: 
        CLIENTE: 
        DNI: 
        CTO O CAJA NAP: 
        TORRE / PISO DE CAJA NAP: 
        DIRECCIÓN O NOMBRE DE EDIFICIO / CONDOMINIO / RESIDENCIAL: 
        NÚMERO DE PUERTO: 
        POTENCIA DE PUERTO: 
        METRAJE UTILIZADO: 
        NOMBRE DEL TÉCNICO: 
        GESTIÓN A REALIZAR: 
        OBSERVACIONES: 
        MOTIV0 CAMBIO DE CTO O CAJA NAP: (SOLO EN LOS CASOS QUE SE AMERITE CAMBIOS) 
        1. RECABLEADO A LA MISMA CTO O CAJA NAP: 
        2. CAMBIO DE CTO O CAJA NAP: 
        3. TRASLADO: 
        4. REINSTALACIÓN:
    """
    ,)
@bot.message_handler(commands=["6"])
def send_6 (message):
    bot.reply_to(message,
    """
        6- VALIDACIÓN DE LLAMADAS

        CLIENTE/A: 
        DNI: 
        CONTRATA: 
        FECHA Y TRAMO SOLICITADO POR EL CLIENTE: 
        NÚMERO DEL CLIENTE AL CUAL SE COMUNICÓ: 
        MOTIVO: 
        TICKET: 
        OBSERVACIONES:
    """
    ,)
@bot.message_handler(commands=["7"])
def send_7 (message):
    bot.reply_to(message,
    """
        7- VALIDAR CASOS CON COSTO

        NOMBRE DEL CLIENTE(A): 
        DNI: 
        TELÉFONO: 
        DIRECCIÓN: 
        TICKET: 
        SOLICITUD O DAÑO DETECTADO: 
        OBSERVACIONES:
    """
    ,)
@bot.message_handler(commands=["8"])
def send_8 (message):
    bot.reply_to(message,
    """
        8- CAMBIO DE MESH (FOTO DE LA MAC DEL MESH NUEVO Y ANTIGUO) 

        NOMBRE DEL CLIENTE(A):
        DNI:
        SN MESH NUEVO:
        MAC MESH NUEVO:
        SN MESH ACTUAL:
        MAC MESH ACTUAL:
    """
    ,)
@bot.message_handler(commands=["9"])
def send_9 (message):
    bot.reply_to(message,
    """
        9- ENTREGA DE MESH (FOTO DE LA MAC DEL MESH ACTUAL) 

        NOMBRE DEL CLIENTE:
        DNI:
        SN MESH: 
        MAC MESH:
    """
    ,)
@bot.message_handler(commands=["10"])
def send_10 (message):
    bot.reply_to(message,
    """
        10- ENTREGA DE TELEFONO 

        TICKET:
        NOMBRE DEL CLIENTE(A):
        DNI: 
        CODIGO TELEFONO:
    """
    ,)
@bot.message_handler(commands=["11"])
def send_11 (message):
    bot.reply_to(message,
    """
        11- CAMBIO DE TELEFONO (FOTO DE LA MAC DEL TELEFONO NUEVO Y ANTIGUO) 

        NOMBRE DEL CLIENTE: 
        DNI: 
        MAC TELEFONO NUEVO: 
        MAC TELEFONO ACTUAL:
    """
    ,)
@bot.message_handler(commands=["12"])
def send_12 (message):
    bot.reply_to(message,
    """  
        12- ENTREGA DE WINBOX (FOTO DE LA MAC DEL WINBOX ACTUAL) 

        NOMBRE DEL CLIENTE:
        DNI:
        SN WINBOX ACTUAL: 
        MAC WINBOX ACTUAL:
    """
    ,)
@bot.message_handler(commands=["13"])
def send_13 (message):
    bot.reply_to(message,
    """
       13- CAMBIO DE WINBOX (FOTO DE LA MAC DEL WINBOX NUEVO Y ANTIGUO) 

       NOMBRE DEL CLIENTE:
       DNI:
       SN WINBOX NUEVO: 
       MAC WINBOX NUEVO: 
       SN WINBOX ACTUAL: 
       MAC WINBOX ACTUAL:
    """
    ,)
@bot.message_handler(commands=["14"])
def send_14 (message):
    bot.reply_to(message,
    """
        14- RX 

        TICKET: 
        NOMBRE DEL CLIENTE(A): 
        DNI: 
        SN DEL ONT ACTUAL: 
        PRODUCT ID ONT NUEVA: 
        TECNICO: 
        CONTRATA: 
        TIPO DE TRABAJO:
    """
    ,)
@bot.message_handler(commands=["15"])
def send_15 (message):
    bot.reply_to(message,
    """
        15- REMATRICULACION 

        TICKET:
        CODIGO DEL CLIENTE:
        NOMBRE DEL CLIENTE(A): 
        DNI: 
        SN DEL ONT ACTUAL:
        PRODUCT ID ONT ACTUAL:
        CONTRATA:
        TECNICO:
        DISTRITO:
        MOTIVO DE LA REMATRICULACION:
    """
    ,)
@bot.message_handler(commands=["16"])
def send_16 (message):
    bot.reply_to(message,
    """
        16- CAMBIO DE ONT 

        TICKET: 
        CLIENTE: 
        DNI:
        SN ONT ANTIGUO: 
        SN ONT NUEVO:  
        PRODUCT ID ONT NUEVA:
        CONTRATA: 
        TECNICO:
        DISTRITO:
        OBSERVACION:
    """
    ,)
@bot.message_handler(commands=["17"])
def send_17 (message):
    bot.reply_to(message,
    """
        17- RX PARA RECABLEADO MISMA CTO / CAMBIO DE CTO- CAJA NAP / TRASLADO / REINSTALACION 

        TICKET: 
        CLIENTE: 
        DNI: 
        SN DEL ONT ACTUAL: 
        CTO O CAJA NAP: 
        TORRE/ PISO DE CAJA NAP: 
        NUMERO DE PUERTO: 
        DIRECCION O NOMBRE DE EDIFICIO / CONDOMINIO / RESIDENCIAL: 
        NOMBRE DEL TECNICO: 
        CONTRATA: 
        TIPO DE TRABAJO:
    """
    ,)
@bot.message_handler(commands=["18"])
def send_18 (message):
    bot.reply_to(message,
    """
        18- PLANTILLA DE REPORTE PEXT 

        TICKET: 
        NOMBRE DEL CLIENTE: 
        DNI: 
        DISTRITO: 
        COORDENADAS DE LA CTO: 
        CTO: 
        NOMBRE Y APELLIDO DEL TEC: 
        CONTRATA: 
        NUMERO DE PUERTO DEGRADADO: 
        OBS:
    """
    ,)
@bot.message_handler(commands=["19"])
def send_19 (message):
    bot.reply_to(message,
    """
        19- CAMBIO DE CTO / CAMBIO DE PUERTO / TRASLADO 

        TICKET:
        NOMBRE DEL CLIENTE: 
        DNI: 
        SN DEL ONT ACTUAL:
        DIRECCION:
        CTO:
        PUERTO:
        CONTRATA:
        TECNICO:
        DISTRITO:
        OBSERVACION:
        MOTIVO DEL CAMBIO:
    """
    ,)
@bot.message_handler(commands=["20"])
def send_20 (message):
    bot.reply_to(message,
    """
        20- TRASLADO + CAMBIO DE ONT 

        TICKET: 
        NOMBRE DEL CLIENTE: 
        DNI: 
        SN DEL ONT ANTIGUO: 
        SN DEL ONT NUEVO: 
        PRODUCT ID ONT NUEVA: 
        DIRECCION: 
        CONDOMINIO/PISO: 
        DISTRITO: 
        CTO: 
        PUERTO: 
        CONTRATA: 
        TECNICO:
    """
    ,)
@bot.message_handler(commands=["21"])
def send_21 (message):
    bot.reply_to(message,
    """
        21- PLANTILLA DE CIERRE 

        TICKET: 
        DNI: 
        CLIENTE: 
        TRABAJO REALIZADO:
    """
    ,)
@bot.message_handler(commands=["22"])
def send_22 (message):
    bot.reply_to(message,
    """
        22- CAMBIO DE TICKET

        NOMBRE DEL CLIENTE(A): 
        DNI: 
        TELÉFONO: 
        DIRECCIÓN: 
        TICKET: 
        SOLICITUD O DAÑO DETECTADO: 
        OBSERVACIONES:
    """
    ,)
@bot.message_handler(commands=["23"])
def send_23 (message):
    bot.reply_to(message,
    """
        23- /*PLANTILLA PARA SUPERVISORES*/

        CLIENTE:
        DNI:
        CONTACTO:
        DIRECCION:
        DISTRITO:
        CONTRATA:
        TICKET:
        TIPO DE ATENCION (RECABLEADO/TRASLADO/OTRO.):
        OBS:
    """
    ,)
#plantillas para observados
def send_obs(message):
    msg = bot.send_message(message.chat.id,
    """
        Plantilla Observados: 
        /24 Ticket Observados
    """
    )

    time.sleep(10)  # Esperar 10 segundos
    bot.delete_message(message.chat.id, msg.message_id)

@bot.message_handler(commands=["24"])
def send_24 (message):
    bot.reply_to(message,
    """
        24- TICKET OBSERVADOS 
        NOMBRE: 
        DNI: 
        TICKET: 
        MOVIL: 
        MOTIVO: 
        OBS:
    """
    ,)


# Empezar a recibir mensajes
bot.polling()

