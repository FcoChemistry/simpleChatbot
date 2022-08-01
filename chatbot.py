import re
import random
import datetime

#recibe la entrada del usuario y se remueven los signos de puntuación con expresiones regulares
#receives user input and removes punctuation with regular expressions
def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

#función para verificar la probabilidad de un mensaje
#function to check the probability of a message
def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def localtime():
    now = datetime.datetime.now()
    timenow = int(datetime.datetime.strftime(now, '%H'))
    message_hour = ''
    if timenow < 5:
        message_hour = 'Buenas noches'
    elif timenow < 12:
        message_hour = 'Buenos días'
    elif timenow < 19:
        message_hour = 'Buenas tardes'
    else:
        message_hour = 'Buenas noches'
    return message_hour

#Listas de preguntas y respuestas
greetings = [('Hola, ' + localtime() + ', me llamo Tobias y soy una creacion de Francisco Villalba'), ('Hola, es un gusto en presentarme. Me llamo Tobias y soy un chatbot creado por Francisco Villalba, usando operaciones recurrentes')]
greetingsr = ['hola', 'saludos', 'buenas', 'buenos', 'buen', 'días', 'día', 'tardes', 'noches']
greetings1 = ['Por ahora estoy bien, me siento muy contento por ir recibiendo nuevas actualizaciones ¿y tú?', 'Estoy bien y usted ¿cómo se encuentra?']
greetingsr1 = ['como', 'estas', 'cómo', 'sientes', 'vas']
thanks = ['Siempre a la orden para servirte', 'Me alegra mucho haberte podido ayudar', 'Me hace feliz poder ayudarte']
thanksr1 = ['gracias', 'agradecido', 'thanks', 'agradecida', 'te lo agradezco']

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response(greetings[random.randrange(len(greetings))], greetingsr, single_response = True)
        response(greetings1[random.randrange(len(greetings1))], greetingsr1, single_response= True)
        response(thanks[random.randrange(len(thanks))], thanksr1, single_response=True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob) #elimina el primer hashtag para probar el algoritmo, remove the first hashtag to test the algorithm

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'puedes probar a buscarlo en google a ver que tal', 'puedes ayudarme un poco, no te estoy entiendiendo'][random.randrange(4)]
    return response

#bucle para pedir siempre las preguntas al usuario
while True:
    print("My Bot: " + get_response(input('You/tú: ')))
