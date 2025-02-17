from flask import Flask, render_template, request, redirect, url_for
from models import db
from models.produtos import Produto, ProdutoInsumo
from models.vendas import Venda
from models.insumos import Insumo, Categoria

app = Flask(__name__, static_folder="static")

# 📌 Configuração do banco de dados SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 📌 Inicializa o banco de dados
db.init_app(app)

# 📌 Criar as tabelas no banco de dados (se ainda não existirem)
with app.app_context():
    db.create_all()

# ✅ Rota para visualizar produtos
@app.route("/produtos")
def produtos():
    produtos = Produto.query.all()
    insumos = Insumo.query.all()
    return render_template("produtos.html", produtos=produtos, insumos=insumos)

# ✅ Rota para adicionar produtos e associar insumos
@app.route("/add_produto", methods=["POST"])
def add_produto():
    nome = request.form.get("nome")
    preco_venda = float(request.form.get("preco_venda"))
    insumo_ids = request.form.getlist("insumos[]")  # Pega a lista de insumos selecionados
    quantidades = request.form.getlist("quantidades[]")  # Pega a lista de quantidades usadas

    # Criar o novo produto
    novo_produto = Produto(nome=nome, preco_venda=preco_venda)
    db.session.add(novo_produto)
    db.session.commit()

    # Associar os insumos selecionados ao produto
    for insumo_id, quantidade in zip(insumo_ids, quantidades):
        produto_insumo = ProdutoInsumo(
            produto_id=novo_produto.id,
            insumo_id=int(insumo_id),
            quantidade_usada=float(quantidade)
        )
        db.session.add(produto_insumo)

    db.session.commit()
    return redirect(url_for("produtos"))

# ✅ Rodar a aplicação
if __name__ == "__main__":
    app.run(debug=True)
