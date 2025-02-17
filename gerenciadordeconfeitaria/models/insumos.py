from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 📌 Modelo de Categoria (usado nos insumos)
class Categoria(db.Model):
    __tablename__ = "categorias"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    insumos = db.relationship("Insumo", backref="categoria", lazy=True)

# 📌 Modelo de Insumo
class Insumo(db.Model):
    __tablename__ = "insumos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Float, nullable=False)
    unidade = db.Column(db.String(20), nullable=False)
    preco_unitario = db.Column(db.Float, nullable=False)
    quantidade_minima = db.Column(db.Float, nullable=False, default=10)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categorias.id"), nullable=True)

    def get_status(self):
        """Retorna o status do estoque baseado na quantidade mínima."""
        if self.quantidade < 0.1 * self.quantidade_minima:
            return "Crítico"
        elif self.quantidade < 0.4 * self.quantidade_minima:
            return "Atenção"
        return "Estável"
