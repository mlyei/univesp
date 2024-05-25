from . import db

class AEEAcompanhamento(db.Model):
    __tablename__ = 'aee acompanhamento'
    idAEE = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(200), nullable=True)

class AssistenteEducacional(db.Model):
    __tablename__ = 'assistente educacional'
    idAssistenteEducacional = db.Column(db.Integer, primary_key=True)
    Nome_da_AE = db.Column(db.String(200), nullable=False)

class Escola(db.Model):
    __tablename__ = 'escola'
    idEscola = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(200), nullable=False)
    Ensino_Fundamental = db.Column(db.Boolean, nullable=True)
    Turmas = db.Column(db.String(90), nullable=False)
    Manha = db.Column(db.Boolean, nullable=True)
    Tarde = db.Column(db.Boolean, nullable=True)

class Professor(db.Model):
    __tablename__ = 'professor'
    idProfessor = db.Column(db.Integer, primary_key=True)
    Nome_professor = db.Column(db.String(200), nullable=False)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idUsuarios = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(200), nullable=False)
    Email = db.Column(db.String(90), nullable=False)
    Senha = db.Column(db.String(45), nullable=False)

class Aluno(db.Model):
    __tablename__ = 'aluno'
    idAluno = db.Column(db.Integer, primary_key=True)
    Nome_aluno = db.Column(db.String(90), nullable=False)
    RA = db.Column(db.Integer, nullable=False)
    Data_de_Nascimento = db.Column(db.Date, nullable=False)
    Responsavel = db.Column(db.String(90), nullable=False)
    Telefone = db.Column(db.Integer, nullable=False)
    Endereco = db.Column(db.String(200), nullable=False)
    Bairro = db.Column(db.String(200), nullable=False)
    Cidade = db.Column(db.String(200), nullable=False)
    Usuarios_idUsuarios = db.Column(db.Integer, db.ForeignKey('usuarios.idUsuarios'), nullable=False)
    Escola_idEscola = db.Column(db.Integer, db.ForeignKey('escola.idEscola'), nullable=False)
    Professor_idProfessor = db.Column(db.Integer, db.ForeignKey('professor.idProfessor'), nullable=False)
    Assistente_Educacional_idAssistente_Educacional = db.Column(db.Integer, db.ForeignKey('assistente educacional.idAssistente Educacional'), nullable=False)
    AEE_acompanhamento_idAEE = db.Column(db.Integer, db.ForeignKey('aee acompanhamento.idAEE'), nullable=False)