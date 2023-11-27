import logging
from chatterbot import ChatBot
from difflib import SequenceMatcher

logging.basicConfig(level=logging.INFO)

CONFIANCA_MINIMA = 0.65


def comparar_mensagens(mensagem_digitada, mensagem_candidata):
    digitada = mensagem_digitada.text
    candidata = mensagem_candidata.text
    if digitada and candidata:
        confianca = SequenceMatcher(None, digitada, candidata)
        return round(confianca.ratio(), 2)
    return 0.0


def iniciar():
    robo = ChatBot("Robô de Atendimento da AgroTech",
                   read_only=True,
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch",
                           "statement_comparison_function": comparar_mensagens,
                           "default_response": "Desculpe, eu não entendi. Poderia repetir?",
                           "maximum_similarity_threshold": CONFIANCA_MINIMA
                       }
                   ])

    return robo


def executar_robo(robo):
    while True:
        try:
            mensagem = input("Digite alguma coisa... \n")
            resposta = robo.get_response(mensagem.lower())
            logging.info(f"O valor da confiança é: {resposta.confidence}")
            print(">>", resposta.text)
        except Exception as e:
            logging.error(f"Erro ao executar o robô: {e}")


if __name__ == "__main__":
    robo = iniciar()
    executar_robo(robo)
