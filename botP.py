# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 18:16:25 2022

@author: alan

Este es un bot de prueba
"""

#importar bibliotecas
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pytrends.request import TrendReq
#Manipulador de comando START, se activa cuando usuario manda /start
def start(update, context):
    update.message.reply_text("Hola mundo")

#Manipulador de comando END, se activa cuando usuario manda /start
def end(update, context):
    update.message.reply_text("Adios mundo")

#Manipulador tendencias
def tendencias(update, context):
    #Crear un modelo
    pytrend = TrendReq()

    #Obtener datos de google trends
    df = pytrend.trending_searches(pn= "mexico")
    update.message.reply_text(str(df.head(10)))
#Manipulador de suma
def suma(update, context):
    try:
        num1 = int(context.args[0])
        num2 = int(context.args[1])
        num3 = num1 + num2
    
        update.message.reply_text( "La suma es: " + str(num3) )
    except(ValueError):
        update.message.reply_text( "ERROR: Solo se aceptan numeros enteros" )
#Manipulardor de mensajes echo
def echo(update,context):
    if(update.message.text.upper().find("?") >= 0):
        update.message.reply_text( "Estás muy pregunton el día de hoy" )
    else:
        update.message.reply_text( update.message.text )
#Manipulador de HELP
def help1(update, context):
    texto_ayuda="""Lista de comandos:
    
        /start -> inicia la conversación
        /help -> lista de comandos
        /end -> una despedida
        /suma -> suma de dos dígitos (ejemplo: /suma 2 2)
        /tendencias -> muestra el top 10 de busquédas de google
        
        """
    update.message.reply_text(texto_ayuda)
    
#Manipulador secreto
def secreto(update, context):
    update.message.reply_text("Alan dice que te ama mucho mucho mucho")
#----------------------------------------------------
token = os.environ.get("token")
#crear un actualizador para acceder al bot
updater = Updater(token = token, use_context=True)

#agregar el manipulador de comandos star a nuestro bot

updater.dispatcher.add_handler( CommandHandler("start", start) )
updater.dispatcher.add_handler( CommandHandler("end", end) )
updater.dispatcher.add_handler( CommandHandler("tendencias", tendencias) )
updater.dispatcher.add_handler( CommandHandler("suma", suma) )
updater.dispatcher.add_handler( CommandHandler("help",help1) ) 
updater.dispatcher.add_handler(CommandHandler("secret", secreto))

#agregar manipulador de mensaje
updater.dispatcher.add_handler( MessageHandler( Filters.text, echo ) )

#iniciar al bot
updater.start_polling()

#correr el codigo en un loop
updater.idle()

