import webapp2
import itertools
import random
from games import GameModel

class MainPage(webapp2.RequestHandler):

    def get(self):
    	self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('TEST TEST TEST!')

class DrawCardHandler(webapp2.RequestHandler):
	def get(self, game_id, player_id):
		pass

class PeekCardHandler(webapp2.RequestHandler):
	def get(self, game_id, player_id):
		pass

class PlayCardHandler(webapp2.RequestHandler):
	def post(self, game_id, player_id):
		pass

class GameHandler(webapp2.RequestHandler):
	def get(self, game_id):
		game = GameModel.get_by_id(game_id)
		if game:
			# Second player joined, make the game
			deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
			random.shuffle(deck)

	def respond(self, data, content_type='application/json')

application = webapp2.WSGIApplication([
	('/game/\w+/draw/\w+', DrawCardHandler),
	('/game/\w+/peek/\w+', PeekCardHandler),
	('/game/\w+/play/\w+', PlayCardHandler),
	('/game/\w*', GameHandler),	
    ('/', MainPage),
], debug=True)