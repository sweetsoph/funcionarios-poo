from classes import *

gerente = Gerente("José", "50171388895", 12345)
gerente.cancelar_operacao("50171388895", 12345)

caixa = Operador_Caixa("Maria", "50171388896", 23072005, 235)
caixa.registrar_produto(235, 23072005)

seguranca = Seguranca("Sophia", "50171388892", 13092005, 1)
try:
    seguranca.autenticar(1, 13092005)
except Exception as e:
    print(e)

print(seguranca.acionar_alarme())