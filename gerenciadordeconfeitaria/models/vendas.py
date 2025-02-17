from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# 📌 Modelo de Venda
class Venda(db.Model):
    __tablename__ = "vendas"
    
    id = db.Column(db.Integer, primary_key=True)
    data_venda = db.Column(db.DateTime, default=datetime.utcnow)
    produto_id = db.Column(db.Integer, db.ForeignKey("produtos.id"), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    total_venda = db.Column(db.Float, nullable=False)  # Preço total da venda
    
    produto = db.relationship("Produto", backref="vendas")

    def __repr__(self):
        return f"<Venda {self.id} - Produto {self.produto_id} - {self.quantidade}>"
