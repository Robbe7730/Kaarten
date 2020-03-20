from faker import Faker
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

from models import Game

FAKER = Faker()

CURRENT_GAMES = {}

@app.route('/')
def root():
    return "I am root"

@app.route("/new_game")
def new_game_invalid():
    return "Try /new_game/(number of players)"

@app.route("/new_game/<int:num_players>")
def new_game(num_players):
    game_id = FAKER.bs().replace(" ", "-").lower()
    players = [FAKER.color_name().lower() for _ in range(int(num_players))]
    CURRENT_GAMES[game_id] = Game(game_id, players)
    return game_id

@app.route("/games/<gameid>")
def game_detail(gameid):
    return render_template("game.html", game=CURRENT_GAMES[gameid])

@app.route("/games/<gameid>/<playerid>")
def playerview(gameid, playerid):
    return render_template("player.html", game=CURRENT_GAMES[gameid], playerid=playerid)

@app.route("/games/<gameid>/<playerid>/pickup")
def pickup(gameid, playerid):
    g = CURRENT_GAMES[gameid]
    g.pickup(playerid)
    return redirect(url_for('playerview', gameid=gameid, playerid=playerid))

@app.route("/games/<gameid>/<playerid>/undo")
def undo(gameid, playerid):
    g = CURRENT_GAMES[gameid]
    g.undo(playerid)
    return redirect(url_for('playerview', gameid=gameid, playerid=playerid))

@app.route("/games/<gameid>/<playerid>/play/<card>")
def play(gameid, playerid, card):
    g = CURRENT_GAMES[gameid]
    g.play(playerid, card)
    return redirect(url_for('playerview', gameid=gameid, playerid=playerid))

@app.route("/games/<gameid>/<playerid>/give/<victim>")
def give(gameid, playerid, victim):
    g = CURRENT_GAMES[gameid]
    g.pickup(victim)
    return redirect(url_for('playerview', gameid=gameid, playerid=playerid))

@app.route("/games/<gameid>/<playerid>/shuffle_deck")
def shuffle_deck(gameid, playerid):
    g = CURRENT_GAMES[gameid]
    g.shuffle_deck()
    return redirect(url_for('playerview', gameid=gameid, playerid=playerid))
