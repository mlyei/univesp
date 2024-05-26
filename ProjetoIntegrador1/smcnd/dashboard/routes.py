from flask import Blueprint, render_template, jsonify
from smcnd.models import Escola, Aluno

bp = Blueprint('dashboard', __name__, template_folder='templates/dashboard')

@bp.route('/dashboard')
def dashboard_home():
    total_escolas = Escola.query.count()
    total_alunos = Aluno.query.count()

    alunos_laudados = Aluno.query.filter(Aluno.AEE_acompanhamento_idAEE.isnot(None)).count()
    alunos_sem_laudo = total_alunos - alunos_laudados

    alunos_assistidos = Aluno.query.filter(Aluno.Assistente_Educacional_idAssistente_Educacional.isnot(None)).count()
    alunos_nao_assistidos = total_alunos - alunos_assistidos

    data = {
        'total_escolas': total_escolas,
        'total_alunos': total_alunos,
        'alunos_laudados': alunos_laudados,
        'alunos_sem_laudo': alunos_sem_laudo,
        'alunos_assistidos': alunos_assistidos,
        'alunos_nao_assistidos': alunos_nao_assistidos
    }

    return render_template('dashboard.html', data=data)