import unittest
from unittest.mock import patch, MagicMock
from chatterbot.logic import BestMatch
from main import iniciar, executar_robo


perguntas_fertilizantes = [
    "quais são os tipos de fertilizantes disponíveis na loja?",
    "tem fertilizantes?",
    "tem fertilizante?",
    "vocês vendem fertilizantes?",
    "vocês tem fertilizantes?",
    "vocês tem fertilizante?",
    "quais fertilizantes disponíveis"
]

resposta_fertilizantes = "Na nossa loja, temos uma variedade de fertilizantes disponíveis, incluindo fertilizantes orgânicos e químicos. Temos opções para diferentes tipos de culturas e necessidades específicas."

perguntas_controle_pragas = [
    "Vocês oferecem produtos para o controle de pragas e doenças nas plantações?",
    "tem produtos para o controle de pragas",
    "vocês tem produtos para o controle de pragas?",
    "vocês vendem produtos para o controle de pragas?",
    "vocês tem produtos para o controle de doenças?",
    "vocês vendem produtos para o controle de doenças?"
]

resposta_controle_pragas = "Sim, oferecemos uma ampla gama de produtos para o controle de pragas e doenças nas plantações. Temos defensivos agrícolas eficazes para ajudar a proteger suas culturas."

perguntas_racao = [
    "quais são as opções de ração para animais de criação que vocês têm disponíveis?",
    "vocês tem ração para animais de criação?",
    "vocês vendem ração para animais de criação?",
    "vocês tem ração para animais?",
    "tem ração",
    "vocês vendem ração?"
]

resposta_racao = "Temos diversas opções de ração para animais de criação, como bovinos, suínos, aves e outros. Nossas rações são formuladas para atender às necessidades nutricionais específicas de cada espécie."

perguntas_equipamentos = [
    "vocês vendem equipamentos agrícolas, como tratores e implementos?",
    "vocês tem equipamentos agrícolas?",
    "tem equipamentos agrícolas?"
]

resposta_equipamentos = "Sim, oferecemos uma variedade de equipamentos agrícolas, incluindo tratores, implementos e máquinas para auxiliar nas atividades agrícolas. Entre em contato conosco para mais informações sobre os produtos disponíveis."

perguntas_sementes_mudas = [
    "quais são as opções de sementes e mudas que posso encontrar na loja?",
    "vocês tem sementes e mudas?",
    "vocês vendem sementes e mudas?",
    "vocês tem sementes?",
    "vocês vendem sementes?",
    "vocês tem mudas?",
    "vocês vendem mudas?",
    "tem sementes?",
    "tem mudas?"
]

resposta_sementes_mudas = "Em nossa loja, você encontrará uma ampla variedade de sementes e mudas de diferentes culturas. Temos opções de alta qualidade e variedades adaptadas às condições locais. Venha nos visitar para conhecer todas as opções disponíveis."


class TestRobo(unittest.TestCase):
    def test_executar_robo(self):
        perguntas_respostas = [
            (perguntas_fertilizantes, resposta_fertilizantes),
            (perguntas_controle_pragas, resposta_controle_pragas),
            (perguntas_racao, resposta_racao),
            (perguntas_equipamentos, resposta_equipamentos),
            (perguntas_sementes_mudas, resposta_sementes_mudas)
        ]

        for perguntas, resposta in perguntas_respostas:
            for pergunta in perguntas:
                with patch('builtins.input', side_effect=[pergunta, KeyboardInterrupt]), patch('main.logging') as mock_logging:
                    robo = MagicMock()
                    robo.get_response.return_value.confidence = 0.7
                    robo.get_response.return_value.text = resposta
                    try:
                        executar_robo(robo)
                    except KeyboardInterrupt:
                        pass
                    robo.get_response.assert_called_once_with(pergunta.lower())
                    mock_logging.info.assert_called_once_with('O valor da confiança é: 0.7')

    def test_executar_robo_mensagem_nao_reconhecida(self):
        with patch('builtins.input', side_effect=['mensagem não reconhecida', KeyboardInterrupt]), patch('main.logging') as mock_logging:
            robo = MagicMock()
            robo.get_response.return_value.confidence = 0.0
            robo.get_response.return_value.text = "Desculpe, não entendi o que você disse. Poderia repetir, por favor?"
            try:
                executar_robo(robo)
            except KeyboardInterrupt:
                pass
            robo.get_response.assert_called_once_with('mensagem não reconhecida')
            mock_logging.info.assert_called_once_with('O valor da confiança é: 0.0')


if __name__ == '__main__':
    unittest.main()
