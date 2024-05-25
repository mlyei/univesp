from flask import Blueprint, render_template, request, redirect, url_for
from smcnd.models import Aluno
from smcnd import db

bp = Blueprint('aluno', __name__)

@bp.route('/aluno', methods=['GET', 'POST'])
def manage_alunos():
    if request.method == 'POST':
        # Lógica para processar o formulário de cadastro de alunos
        nome = request.form.get('nome')
        # ... outros campos
        novo_aluno = Aluno(nome=nome)
        db.session.add(novo_aluno)
        db.session.commit()
        return redirect(url_for('aluno.manage_alunos'))
    
    alunos = Aluno.query.all()
    return render_template('aluno.html', alunos=alunos)
