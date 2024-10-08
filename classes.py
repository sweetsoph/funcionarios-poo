from abc import ABC, abstractmethod
import hashlib

class Funcionario(ABC):
    nome : str
    cpf : str
    __senha : int

    def __init__(self, nome : str, cpf : str, senha : int):
        self.nome = nome
        self.cpf = cpf
        senha_bytes = str(senha).encode('utf-8')
        senha_hash = hashlib.md5(senha_bytes)
        self.__senha = senha_hash.hexdigest()

    def get_senha(self):
        return self.__senha

    @abstractmethod
    def autenticar(self):
        pass

    def __str__(self):
        info = (f'Nome: {self.nome}\n'
                f'CPF: {self.cpf}\n')
        return info

class Gerente(Funcionario):

    def autenticar(self, cpf : str, senha : int):
        senha_bytes = str(senha).encode('utf-8')
        senha_hash = hashlib.md5(senha_bytes)
        if self.cpf == cpf and super().get_senha() == senha_hash.hexdigest():
            return "Usuário autenticado com sucesso!"
        else:
            raise Exception("Usuário ou senha incorretos.")

    def cancelar_operacao(self, cpf : str, senha : int):
        try:
            self.autenticar(cpf, senha)
            print("Operação cancelada.")
        except Exception as e:
            print(e)


class Operador_Caixa(Funcionario):
    numero_caixa : int

    def __init__(self, nome : str, cpf : str, senha : int, numero_caixa : int):
        super().__init__(nome, cpf, senha)
        self.numero_caixa = numero_caixa

    def __str__(self):
        info = super().__str__()
        info += (f'Número do Caixa: {self.numero_caixa}')
        return info

    def autenticar(self, numero_caixa : str, senha : int):
        senha_bytes = str(senha).encode('utf-8')
        senha_hash = hashlib.md5(senha_bytes)
        if self.numero_caixa == numero_caixa and super().get_senha() == senha_hash.hexdigest():
            return "Usuário autenticado com sucesso!"
        else:
            raise Exception("Usuário ou senha incorretos.")

    def registrar_produto(self, numero_caixa : str, senha : int):
        try:
            self.autenticar(numero_caixa, senha)
            print("Produto registrado com sucesso!")
        except Exception as e:
            print(e)

class Seguranca(Funcionario):
    posto : int

    def __init__(self, nome: str, cpf : str, senha : int, posto : int):
        super().__init__(nome, cpf, senha)
        self.posto = posto

    def __str__(self):
        info = super().__str__()
        info += (f'Posto: {self.posto}')
        return info

    def autenticar(self, posto : int, senha : int):
        senha_bytes = str(senha).encode('utf-8')
        senha_hash = hashlib.md5(senha_bytes)
        if self.posto == posto and super().get_senha() == senha_hash.hexdigest():
            return "Usuário autenticado com sucesso!"
        else:
            raise Exception("Usuário ou senha incorretos.")

    def acionar_alarme(self):
        return ("UOOUOUOUOUOUOUUOU!!")




