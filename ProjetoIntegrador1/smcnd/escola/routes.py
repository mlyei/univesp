from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from smcnd.models import Escola
from smcnd import db

bp = Blueprint('escola', __name__,)

@bp.route('/escola', methods=['GET', 'POST'])
def manage_escola():
    if request.method == 'POST':
        nome = request.form.get('nome')
        ensino_fundamental = request.form.get('ensino_fundamental')
        turmas = request.form.get('turmas')
        manha = request.form.get('manha')
        tarde = request.form.get('tarde')

        nova_escola = Escola(
            Nome=nome,
            Ensino_Fundamental=ensino_fundamental == 'on',
            Turmas=turmas,
            Manha=manha == 'on',
            Tarde=tarde == 'on'
        )

        db.session.add(nova_escola)
        db.session.commit()
        return redirect(url_for('escola.manage_escola'))

escolas = Escola.query.all()
return render_template('escola.html')

@bp.route('/escola/<int:id_escola>/detalhes', methods=['GET'])
def detalhes_escola(id_escola):
    escola = Escola.query.get_or_404(id_escola)
    return jsonify({
        'Nome': escola.Nome,
        'Ensino_Fundamental': escola.Ensino_Fundamental,
        'Turmas': escola.Turmas,
        'Manha': escola.Manha,
        'Tarde': escola.Tarde
    })