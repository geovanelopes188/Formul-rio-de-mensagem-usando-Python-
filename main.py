from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']

        # Aqui você pode adicionar a lógica para enviar o email, salvar em um banco de dados, etc.
        print(f"Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}")

        return redirect(url_for('success'))
    return render_template('index.html')

@app.route('/success')
def success():
    return 'Mensagem enviada com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)