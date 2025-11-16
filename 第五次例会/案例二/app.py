from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = '123'

# 模拟数据库
users = {
    'user1': {'password': '12345', 'name': '花火'},
    'user2': {'password': '23456', 'name': '张之之'}
}


@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('index'))
    return redirect(url_for('login'))


@app.route('/index')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template("index.html", name=session.get('name'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 验证用户信息
        if username in users and users[username]['password'] == password:
            # 登录成功，设置session
            session['username'] = username
            session['name'] = users[username]['name']
            flash('登录成功！', 'success')
            return redirect(url_for('index'))
        else:
            # 登录失败
            flash('用户名或密码错误！', 'error')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('name', None)
    flash('您已成功退出登录！', 'info')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)