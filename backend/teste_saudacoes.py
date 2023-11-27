import unittest
from unittest.mock import patch, MagicMock
from chatterbot.logic import BestMatch
from main import iniciar, executar_robo


class TestRoboSaudacoes(unittest.TestCase):
    def test_executar_robo_saudacoes(self):
        saudacoes_respostas = [
            (["olá", "ola", "tudo bem?"], "Olá! Sou assistente virtual Bia. Seja bem-vindo ao AgroTech, como posso ajudar?"),
            (["bom dia"], "Bom dia! Sou assistente virtual Bia. Seja bem-vindo ao AgroTech, como posso ser útil?"),
            (["boa tarde"], "Boa tarde! Sou assistente virtual Bia. Seja bem-vindo ao AgroTech, Em que posso ajudar?"),
            (["boa noite"], "Boa noite! Sou assistente virtual Bia. Seja bem-vindo ao AgroTech, como posso te auxiliar?")
        ]

        for saudacoes, resposta in saudacoes_respostas:
            for saudacao in saudacoes:
                with patch('builtins.input', side_effect=[saudacao, KeyboardInterrupt]), patch('main.logging') as mock_logging:
                    robo = MagicMock()
                    robo.get_response.return_value.confidence = 0.65
                    robo.get_response.return_value.text = resposta
                    try:
                        executar_robo(robo)
                    except KeyboardInterrupt:
                        pass
                    robo.get_response.assert_called_once_with(saudacao)
                    mock_logging.info.assert_called_once_with('O valor da confiança é: 0.65')

    def test_executar_robo_mensagem_nao_encontrada(self):
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

    def test_executar_robo_falso_positivo(self):
        with patch('builtins.input', side_effect=['pergunta errada', KeyboardInterrupt]), patch('main.logging') as mock_logging:
            robo = MagicMock()
            robo.get_response.return_value.confidence = 0.0
            robo.get_response.return_value.text = "Resposta errada"
            try:
                executar_robo(robo)
            except KeyboardInterrupt:
                pass
            robo.get_response.assert_called_once_with('pergunta errada')
            self.assertNotEqual(robo.get_response.return_value.text, "Olá! Sou assistente virtual Bia. Seja bem-vindo ao AgroTech, como posso ajudar?")
            mock_logging.info.assert_called_once_with('O valor da confiança é: 0.0')


if __name__ == '__main__':
    unittest.main()
