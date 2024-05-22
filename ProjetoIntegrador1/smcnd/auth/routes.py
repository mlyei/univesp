from flask import Blueprint, request, redirect, url_for, render_template, flash
from werkzeug.security import check_password_hash, generate_password_hash
from smcnd.models import Usuario
from smcnd import db

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])

def auth_login():

    if request.method == ['POST']:
    usuario = request.from['Usuario']
    senha = request.from['Senha']

    usuario = Usuario.query.filter_by(usuario = Usuario).first()

    #usuário existente
    if usuario and check_password_hash(usuario.senha, senha):
        flash('Acesso aprovado', 'success')
        return redirect(url_for(render_template('dashboard.html')))
    
    #usuario inexistente
    elif usuario is None:
        flash('Usuário não encontrado. Por favor, registre-se.', 'warning')
        return redirect(url_for('auth.signup'))
    
    #usuario ou senha errados
    else:
        flash('Usuário ou Senha incorretos', 'danger')
        return render_template('login.html', message = 'usuario ou senha inválidos')


#inscrição na plataforma
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['Email']
        senha = request.form['Senha']
        usuario = request.from['Usuario']
        nome = request.form['Nome']

        # Verifica se o usuário já existe
        usuario = Usuario.query.filter_by(email=email).first()

        if usuario:
            flash('Email já existente', 'danger')
            return redirect(url_for('auth.login'))

        # Cria um novo usuário
        new_user = Usuario(nome=nome, email=email)
        new_user.senha = generate_password_hash(password, method='sha256')

        # Adiciona o novo usuário ao banco de dados
        db.session.add(new_user)
        db.session.commit()

        flash('Usuário Registrado! Por favor realize o login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('signup.html')