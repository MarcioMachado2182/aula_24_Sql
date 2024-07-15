import sqlite3

conn =""
def connect_data_base():#caminho do banco
    db_name='minha_loja.db'
    global conn
    conn = sqlite3.connect(db_name)#comando que conecta e cria o banco
    create_table_clientes()
    create_table_mercadorias()

def create_table_clientes():
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nome VARCHAR(50) NOT NULL ,
            cpf INTEGER (11) NOT NULL                 
                   
        )
    ''')
    conn.commit()


def create_table_mercadorias():
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mercadorias (
            id INTEGER PRIMARY KEY,
            nome VARCHAR(50) NOT NULL ,
            valor INTEGER        
        )
    ''')
    conn.commit()

def inserir_clientes(nome, cpf):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO clientes (nome, cpf)
        VALUES (?, ?)
    ''', (nome, cpf))
    conn.commit()

def inserir_mercadorias(nome, valor):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO mercadorias (nome, valor)
        VALUES (?, ?)
    ''', (nome, valor))
    conn.commit()


def selecionar_cliente():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(f"Cliente: {cliente}\n")

def selecionar_mercadoria():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM mercadorias')
    mercadorias = cursor.fetchall()
    for mercadoria in mercadorias:
        print(f"Mercadoria: {mercadoria}\n")

def fechar_conexao():
    conn.close()

def list_all_tables():
    cursor = conn.cursor()
    # Listar todas as tabelas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas = cursor.fetchall()
    for tabela in tabelas:
        print("TABELA: ", tabela[0])
    conn.commit()

connect_data_base()

list_all_tables()

#inserindo Clientes
inserir_clientes('ze', 45237064094)
inserir_clientes('juca', 25225647065)
inserir_clientes('maria', 51096308010)
inserir_clientes('joana', 64487084059)
selecionar_cliente()



#Inserindo Mercadorias
inserir_mercadorias('Deo Colonia Homem Essence', 199)
inserir_mercadorias('Hidratante Corporal Todo Dia', 85)   
inserir_mercadorias('Camiseta Masculina', 49)
inserir_mercadorias("Deo Colonia Homem ELO","199")
inserir_mercadorias("Hidratante Corporal NativaSpa","85")
inserir_mercadorias("Camiseta Feminina","49")
selecionar_mercadoria()
fechar_conexao()

