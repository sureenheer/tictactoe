from flask import Flask, render_template, request, jsonify
from tictactoe import Game

app = Flask(__name__)
game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    x, y = data['x'], data['y']
    success, message = game.make_move(x, y)
    if success:
        response = {
            'success': True,
            'board': game.board,
            'current_player': game.current_player,
        }
        if game.game_finished:
            response['winner'] = game.current_player
        return jsonify(response)
    else:
        return jsonify(success=False, message=message)

@app.route('/reset', methods=['POST'])
def reset():
    game.reset()
    return jsonify(success=True, board=game.board, current_player=game.current_player)

if __name__ == '__main__':
    app.run(debug=True, port=5501)
