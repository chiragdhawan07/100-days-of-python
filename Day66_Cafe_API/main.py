from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
from sqlalchemy.exc import IntegrityError
import random

# ---------------------- #
#   Flask App Setup
# ---------------------- #
app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# ---------------------- #
#   Cafe Model
# ---------------------- #
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        """Convert SQLAlchemy object to dictionary."""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    
    def __repr__(self):
        return f"<Cafe {self.name} - {self.location}>"


# ---------------------- #
#   Create Database
# ---------------------- #
with app.app_context():
    db.create_all()


# ---------------------- #
#   Routes
# ---------------------- #
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# Random Cafe
@app.route("/random", methods=["GET"])
def get_random_cafe():
    random_cafe = db.session.execute(
        db.select(Cafe).order_by(func.random())
    ).scalar()
    return jsonify(success=True, cafe=random_cafe.to_dict()), 200


# All Cafes
@app.route("/all", methods=["GET"])
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return jsonify(success=True, cafes=[cafe.to_dict() for cafe in all_cafes]), 200


# Search Cafe by Location
@app.route("/search", methods=["GET"])
def get_cafe_at_location():
    query_location = request.args.get("loc")
    if not query_location:
        return jsonify(success=False, error="Missing 'loc' parameter"), 400

    result = db.session.execute(
        db.select(Cafe).where(Cafe.location == query_location)
    )
    all_cafes = result.scalars().all()

    if all_cafes:
        return jsonify(success=True, cafes=[cafe.to_dict() for cafe in all_cafes]), 200
    else:
        return jsonify(success=False, error="No cafe found at that location"), 404


# Add New Cafe
@app.route("/add", methods=["POST"])
def post_new_cafe():
    try:
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify(success=False, error="Cafe with that name already exists"), 409

    return jsonify(success=True, message="Successfully added the new cafe"), 201


# Update Price by ID
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    if not new_price:
        return jsonify(success=False, error="Missing 'new_price' parameter"), 400

    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(success=True, message="Price updated successfully"), 200
    else:
        return jsonify(success=False, error="Cafe not found"), 404


# Delete Cafe (with API Key)
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key != "TopSecretAPIKey":
        return jsonify(success=False, error="Invalid API Key"), 403

    cafe = db.session.get(Cafe, cafe_id)
    if not cafe:
        return jsonify(success=False, error="Cafe not found"), 404

    db.session.delete(cafe)
    db.session.commit()
    return jsonify(success=True, message="Cafe deleted successfully"), 200


# ---------------------- #
#   Run Flask App
# ---------------------- #
if __name__ == '__main__':
    app.run(debug=True)
