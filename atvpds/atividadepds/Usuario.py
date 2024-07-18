class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self._email = email
        self.__senha = senha
    
    def consultar_nome(self):
        return self.nome
    
    def consultar_email(self):
        return self._email

    def consultar_senha(self):
        return self.__senha
    
    def modificar_nome_privado(self, nova_senha):
        self.__senha = nova_senha

class Pessoa(Usuario):
    def __init__(self,nome,_email,__senha, idade):
        super().__init__(nome,_email, __senha)
        self.idade = idade

    def consultar_idade(self):
        return self.idade