from flask import Blueprint, render_template, request, redirect, url_for
from smcnd.models import Aluno
from smcnd import db
from datetime import datetime

bp = Blueprint('aluno', __name__)

@bp.route('/aluno', methods=['GET', 'POST'])
def manage_alunos():
    if request.method == 'POST':
        nome = request.form.get('nome')
        ra = request.form.get('ra')
        data_de_nascimento = request.form.get('data_de_nascimento')
        responsavel = request.form.get('responsavel')
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')
        bairro = request.form.get('bairro')
        cidade = request.form.get('cidade')
        usuarios_idusuarios = request.form.get('usuarios_idusuarios')
        escola_idescola = request.form.get('escola_idescola')
        professor_idprofessor = request.form.get('professor_idprofessor')
        assistente_educacional_idassistente_educacional = request.form.get('assistente_educacional_idassistente_educacional')
        aee_acompanhamento_idaee = request.form.get('aee_acompanhamento_idaee')

        novo_aluno = Aluno(
                Nome_aluno=nome,
                RA=ra,
                Data_de_Nascimento=datetime.strptime(data_de_nascimento, '%Y-%m-%d'),
                Responsavel=responsavel,
                Telefone=telefone,
                Endereco=endereco,
                Bairro=bairro,
                Cidade=cidade,
                Usuarios_idUsuarios=usuarios_idusuarios,
                Escola_idEscola=escola_idescola,
                Professor_idProfessor=professor_idprofessor,
                Assistente_Educacional_idAssistente_Educacional=assistente_educacional_idassistente_educacional,
                AEE_acompanhamento_idAEE=aee_acompanhamento_idaee
        )
        db.session.add(novo_aluno)
        db.session.commit()
        return redirect(url_for('aluno.manage_alunos'))
    
    alunos = Aluno.query.all()
    return render_template('aluno.html', alunos=alunos)

@bp.route('/aluno/<int:id_aluno>/detalhes', methods=['GET'])
def detalhes_aluno(id_aluno):
    aluno = Aluno.query.get_or_404(id_aluno)
    return jsonify({
        'Nome_aluno': aluno.Nome_aluno,
        'RA': aluno.RA,
        'Data_de_Nascimento': aluno.Data_de_Nascimento.isoformat(),
        'Responsavel': aluno.Responsavel,
        'Telefone': aluno.Telefone,
        'Endereco': aluno.Endereco,
        'Bairro': aluno.Bairro,
        'Cidade': aluno.Cidade,
        'Usuarios': aluno.Usuarios_idUsuarios,
        'Escola': aluno.Escola_idEscola,
        'Professor': aluno.Professor_idProfessor,
        'Assistente_Educacional': aluno.Assistente_Educacional_idAssistente_Educacional,
        'Aee_acompanhamento': aluno.AEE_acompanhamento_idAEE
    })
