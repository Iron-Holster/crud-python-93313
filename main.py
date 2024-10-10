# .txt
# Banco de dados

# S-Q-L
# Linguagem de consulta estruturada

# SELECT * FROM CLIENTES
# nome, sobrenome, idade...

#ORM

import os
os.system("cls || clear") 
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# ORM
# CREATE DATA BASE = meubanco;

# Criando conexão com banco de dados
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# I/O
# I = Input (Entrada)
# O = Output (Saida)

# Criando tabela
Base = declarative_base()

class Usuario (Base):
    __tablename__ = "Usuarios"
    # Criando campos de tabela
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

# Definindo atributos da classe.
def __init__(self, nome: str, email: str, senha: str):
    self.nome = nome
    self.email = email
    self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

# Salvar banco de dados
os.system("cls || clear") 
print("=== Solicitando dados para o Usuario ===")
usuario = Usuario(nome="Marta", email="marta@gmail.com", senha="123")
session.add(usuario)
session.commit()

usuario = Usuario(nome = "Maria", email = "maria@gmail.com", senha = "456")
session.add(usuario)
session.commit()

print("\n Excluindo um usuario")
email_usuario = input("Informe o email do usuario para ser excluido: ")
usuario = session.query(Usuario).filter_by(email = email_usuario).first()
session.delete(usuario)
print(f"Usuario(a) {usuario.nome} excluido com sucesso!")

# Listando todos os usuarios do banco de dados
print("\n=== Exibindo todos os usuarios do banco de dados ===")
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")


# Fechando conexão
session.close()