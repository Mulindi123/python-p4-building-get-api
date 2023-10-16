# app/app.py

from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, User, Review, Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "Index for Game/Review/User API"

@app.route('/games')
def games():

    games = []
    for game in Game.query.all():
        game_dict = {
            "title": game.title,
            "genre": game.genre,
            "platform": game.platform,
            "price": game.price,
        }
        games.append(game_dict)

    response = make_response(
        jsonify(games),
        200
    )

    return response

@app.route("/games/<int:id>")
def game_by_id(id):
    game = Game.query.filter_by(id=id).first()
    

    # game_dict ={
    #     "title": game.title,
    #     "genre": game.genre,
    #     "platform": game.platform,
    #     "price": game.price
    # }

    game_dict = game.to_dict()
    
    response = make_response(jsonify(game_dict), 200)

    response.headers["Content_Type"] = "application/json"
    return response

#Show games sorted by title
# @app.route('/games')
# def games():
#     games = Game.query.order_by(Game.title).all()  # Sort games by title
#     games_list = [
#         {
#             "title": game.title,
#             "genre": game.genre,
#             "platform": game.platform,
#             "price": game.price,
#         }
#         for game in games
#     ]

#     response = make_response(
#         jsonify(games_list),
#         200
#     )

#     return response

#Only show the first 10 games
# @app.route('/games')
# def games():
#     games = Game.query.limit(10).all()  # Sort games by title and limit to 10
#     games_list = [
#         {
#             "title": game.title,
#             "genre": game.genre,
#             "platform": game.platform,
#             "price": game.price,
#         }
#         for game in games
#     ]

#     response = make_response(
#         jsonify(games_list),
#         200
#     )

#     return response







if __name__ == '__main__':
    app.run(port=5555, debug=True)