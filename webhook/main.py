import time
from flask import Flask, request
from chatterbot import ChatBot
import json
from chatterbot.trainers import ListTrainer

time.clock = time.time()

chatbot = ChatBot('Vore')

# trainer = ListTrainer(chatbot)
#
# trainer.train([
#     "testando",
#     "funcionou"
# ])

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent_name = req.get('queryResult')['intent']['displayName']
    match intent_name:
        case 'restrição_alimentar':
            global fd_restrict
            fd_restrict = req.get('queryResult')['queryText']
        case 'tempo':
            global time
            time = req.get('queryResult')['queryText']
        case 'gosto':
            global taste
            taste = req.get('queryResult')['queryText']
        case 'celebridades':
            global portions
            portions = req.get('queryResult')['queryText']
        case 'ingredientes':
            global ingredients
            ingredients = req.get('queryResult')['queryText']
            return {
                "fulfillmentText": f"""Então você é {fd_restrict}, tem até {time} para receitas, não tem preferência por tamanho de porção, não tem preferência por canal ou celebridade Globo e têm {ingredients.lower()} na cozinha?""",
                "source": 'webhook'
            }


if __name__ == '__main__':
    app.run(debug=True)
