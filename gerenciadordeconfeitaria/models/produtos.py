from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 📌 Modelo de Produto
class Produto(db.Model):
    __tablename__ = "produtos"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    preco_venda = db.Column(db.Float, nullable=False)

    # Relacionamento com os insumos usados na receita
    receita = db.relationship("ProdutoInsumo", backref="produto", lazy=True)

    def __repr__(self):
        return f"<Produto {self.nome}>"

# 📌 Modelo de relação entre Produto e Insumos
class ProdutoInsumo(db.Model):
    __tablename__ = "produto_insumos"
    
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey("produtos.id"), nullable=False)
    insumo_id = db.Column(db.Integer, db.ForeignKey("insumo.id"), nullable=False)  # 🔹 Correção aqui!
    quantidade_usada = db.Column(db.Float, nullable=False)  # Quantidade do insumo necessária para o produto

    def __repr__(self):
        return f"<ProdutoInsumo {self.produto_id} - {self.insumo_id}>"
