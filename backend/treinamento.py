import json
import logging
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

logging.basicConfig(level=logging.INFO)

CONVERSAS = ["conversas/saudacoes.json", "conversas/informacoes.json"]


def iniciar():
    """
    Inicia o chatbot e retorna o treinador.
    """
    robo = ChatBot("Robô de Atendimento do AgroTech")
    treinador = ListTrainer(robo)
    return treinador


def carregar_conversas():
    """
    Carrega as conversas dos arquivos JSON especificados.
    """
    conversas = []
    for arquivo_conversas in CONVERSAS:
        try:
            with open(arquivo_conversas, "r") as arquivo:
                conversas_para_treinamento = json.load(arquivo)
                conversas.append(conversas_para_treinamento["conversas"])
        except (FileNotFoundError, IOError):
            logging.error(f"Erro ao abrir o arquivo {arquivo_conversas}.")
        except json.JSONDecodeError:
            logging.error(f"Erro decodificar o arquivo {arquivo_conversas}.")
    return conversas


def treinar(treinador, conversas):
    """
    Treina o chatbot com as conversas fornecidas.
    """
    for conversa in conversas:
        for mensagens_resposta in conversa:
            mensagens = mensagens_resposta["mensagens"]
            resposta = mensagens_resposta["resposta"]
            logging.info(f"Treinando o robô. Mensagens: {mensagens}. Resposta: {resposta}")
            for mensagem in mensagens:
                treinador.train([mensagem, resposta])


if __name__ == "__main__":
    treinador = iniciar()
    conversas = carregar_conversas()
    if conversas:
        treinar(treinador, conversas)
