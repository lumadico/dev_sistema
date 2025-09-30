from sqlalchemy import create_engine, text 

#Banco criado a mão (fazendo o sql dentro do python)
engine = create_engine("sqlite:///teste.db", echo = True, future = True)  # engine pode ser qualquer outro nome

#Criar tabela
with engine.connect() as conn:   # renomeando como 'conn'
    conn.execute(text("""
                    CREATE TABLE IF NOT EXISTS alunos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome VARCHAR (50) NOT NULL,
                        idade INTEGER NOT NULL,
                        email VARCHAR (60) UNIQUE
                      ) 
                       """)) # puxando os comandos do sql (criação tabela); """ é padrão para um texto"
    conn.commit()   # 'fecha' o que vc fez em cima; dando uma espécie de OK - insert, create precisa

#Inserir alunos
with engine.connect() as conn: 
    conn.execute(text("INSERT INTO alunos (nome, idade, email) VALUES (:nome, :idade, :email)"), 
                    [ {"nome":"David", "idade":21, "email":"davidvarao@senai.br"},
                     {"nome":"Geovanni", "idade":23, "email":"geovannicuricica@senai.br"},
                     {"nome":"Silvio", "idade":25, "email":"silviogaladaglobo@senai.br"}   
                    ]
    )
    conn.commit()

#Consulta 1
with engine.connect() as conn: 
    resultado = conn.execute(text("SELECT * FROM alunos"))
    for dado in resultado:   # dado foi o nome colocado para 'a lista de variáveis'
        print(dado.id, dado.nome, dado.email)




