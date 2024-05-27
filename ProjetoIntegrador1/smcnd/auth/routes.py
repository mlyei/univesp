from flask import Blueprint, request, redirect, url_for, render_template, flash
from werkzeug.security import check_password_hash, generate_password_hash
from smcnd.models import Usuario
from smcnd import db

bp = Blueprint('auth', __name__)

@bp.route('/signin', methods=['GET', 'POST'])
def auth_login():
    if request.method == 'POST':
        usuario = request.form['Usuario']
        senha = request.form['Senha']
        user = Usuario.query.filter_by(usuario=usuario).first()

        #usuário existente
        if user and check_password_hash(user.Senha, senha):
            flash('Acesso aprovado', 'success')
            return redirect(url_for('dashboard.dashboard_home'))
        
        #usuario inexistente
        elif user is None:
            flash('Usuário não encontrado. Por favor, registre-se.', 'warning')
            return redirect(url_for('auth.signup'))
        
        #usuario ou senha errados
        else:
            flash('Usuário ou Senha incorretos', 'danger')
            return render_template('signin.html', message='Usuário ou senha inválidos')

#inscrição na plataforma
@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['Email']
        senha = request.form['Senha']
        usuario = request.form['Usuario']
        nome = request.form['Nome']

        #Verifica se o usuário já existe
        user = Usuario.query.filter_by(Email=email).first()

        if user:
            flash('Email já existente', 'danger')
            return redirect(url_for('auth.signin'))

        # Cria um novo usuário
        new_user = Usuario(Nome=nome, Email=email)
        new_user.Senha = generate_password_hash(senha, method='sha256')

        # Adiciona o novo usuário ao banco de dados
        db.session.add(new_user)
        db.session.commit()

        flash('Usuário Registrado! Por favor realize o login.', 'success')
        return redirect(url_for('auth.signin'))

    return render_template('signup.html')