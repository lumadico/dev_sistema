from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, CheckConstraint         # importando os tipos de variáveis 
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


# Criando a classe base/mãe e a partir dela serão criadas as tabelas do banco, sem precisar fazer a mão
Base = declarative_base()  # ao lado esquerdo do = é uma variável sendo declarada, então pode mudar pro que achar melhor

# Criar a classe "real"
class Aluno(Base):
    __tablename__ = 'alunos'       # Tudo da classe Alunos vai ser convertido na tabela alunos

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(62), nullable=False)    #nullable = notnull quando False
    idade = Column(Integer, nullable=False)
    email = Column(String(62), unique=True, nullable=False)

    # backpopulate - associação mútua 'Aluno' com 'AlunoDisciplina' - volta / relationship - ida
    disciplinas = relationship('AlunoDisciplina', back_populates='aluno')

    # Método Mágico pra um obj ser impresso (visto que teoricamento um objt não pode ser impresso)
    def __repr__(self):
        return f"<Aluno(id={self.id}, nome='{self.nome}',idade={self.idade}, email='{self.email}')>" # <> formatação
    
#--------------------------------------------------------------------------

class Disciplina(Base):
    __tablename__ = 'disciplinas'

    id = Column(Integer, primary_key=True,  autoincrement=True)
    nome = Column(String(62), nullable=False, unique=True)
    carga_horaria = Column(Integer, nullable=False)

    alunos = relationship('AlunoDisciplina', back_populates='disciplina') # pensar como uma chave estrangeira 

    def __repr__(self):
        return f"<Disciplina(id={self.id}, nome='{self.nome}', carga_horaria={self.carga_horaria})>"


# --------------------------------------------------------------------------

class AlunoDisciplina(Base):
    __tablename__ = 'aluno_disciplina'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_aluno_fk = Column(Integer, ForeignKey('alunos.id'),  nullable=False)
    id_disciplina_fk = Column(Integer, ForeignKey('disciplinas.id'), nullable=False)

    aluno = relationship('Aluno', back_populates='disciplinas')
    disciplina = relationship('Disciplina', back_populates='alunos')   # classe com a tabela


# Criar engine (cria conexão com o BD)
engine = create_engine("sqlite:///tecdev_py.db", echo=False, future=True)

# Criar sessão (conexção engine com ORM)
Session = sessionmaker(bind=engine,future=True)    # o bind 'enraiza' sessão com seu banco (no caso: engine)

# Criar as tabelas
Base.metadata.create_all(engine)


# Insert nas tabelas 
##with Session() as session:    # renomeando -> vai ser usando Session pq agr o engine está nela
 ##   alunos = [
  ##      Aluno(nome='David', idade=21, email='davidvarao@senai.br'),
   ##     Aluno(nome='Geovanni', idade=23, email='geovannicuricica@senai.br'),
   ##     Aluno(nome='Silvio', idade=25, email='silviogaladaglobo@senai.br')
   ## ]
    ## session.add_all(alunos)     # pegando e salvando os criados acima no BD
   ## session.commit()

# Fazendo select (consulta)
## with Session() as session:
   ## resultado = session.query(Aluno).all()

   ## for aluno in resultado:
       ## print(aluno.id, aluno.nome, aluno.idade, aluno.email)


# Criar alunos
with Session() as session:
    raphamel = Aluno(nome='Raphamel', idade=24, email='raphamel@senai.br')
    silvio = Aluno(nome='Silvio', idade=25, email='silviogaladaglobo@senai.br')
    presidente = Aluno(nome='Presidente', idade=18, email='presidente@senai.br')
    eriquison = Aluno(nome='Erick', idade=39, email='erickazeite@senai.br')
    
    
    # Criar disciplinas
    alg = Disciplina(nome='Algoritmo', carga_horaria=180)
    dev = Disciplina(nome='Desenvolvimento de Sistemas', carga_horaria=180)
    
    session.add_all([raphamel, silvio, presidente, eriquison, alg, dev])
    session.commit()

    # Conexão entre Aluno e Disciplina
    cone = [
        AlunoDisciplina(aluno=raphamel, disciplina=alg),
        AlunoDisciplina(aluno=presidente, disciplina=alg),
        AlunoDisciplina(aluno=eriquison, disciplina=dev),
        AlunoDisciplina(aluno=silvio, disciplina=alg),
        AlunoDisciplina(aluno=silvio, disciplina=dev)
    ]
    session.add_all(cone)
    session.commit()

    # Consulta 1
    print('Disciplinas cursadas pelo Silvio')
    for vinculo in silvio.disciplinas:
        print(vinculo.disciplina.nome)

    # Consulta 2
    print(20*'-')
    print('Todos alunos em Dev de Sistemas')
    for vinculo in dev.alunos:
        print(f'{vinculo.aluno.nome}')

        
