from google.appengine.ext import ndb

class GameModel(ndb.Model):
	date_modified = ndb.DateTimeProperty(auto_now_add=True)
	player_one = ndb.StringProperty()
	player_two = ndb.StringProperty()
	observer_ids = ndb.StringProperty(repeated=True)
	hand_one = ndb.StringProperty(repeated=True)
	hand_two = ndb.StringProperty(repeated=True)
	board = ndb.StringProperty(repeated=True)
	tokens = ndb.IntegerProperty(repeated=True)
	deck = ndb.StringProperty(repeated=True)
	finished = ndb.BooleanProperty()



