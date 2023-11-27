from flask import Flask
from flask_cors import CORS
from main import *

VERSAO = "0.1"


robo = iniciar()
servico_robo = Flask(__name__)
CORS(servico_robo)


@servico_robo.route("/versao")
def get_versao():
    return VERSAO


@servico_robo.route("/resposta/<mensagem>")
def get_resposta(mensagem):
    resposta = robo.get_response(mensagem)
    return resposta.text


if __name__ == "__main__":
    servico_robo.run()
