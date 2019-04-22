import json

PATH = '/data.json'

class Recorder:

	def __init__(self):
		with open(PATH, 'r') as f:
			self.data = json.loads(f)

	def add(self, entry: OrderEntry):
		pass

	def dumps(self):
		with open(PATH, 'w') as f:
			json.dumps(self.data, f)

class OrderEntry:

	def __init__(self, location: str, time: str, items: dict):
		self.location = location
		self.time = time
		self.items = items

	def serialize(self) -> dict:
		data = {
			'location': self.location,
			'time': self.time,
			'items': self.items
		}

	@classmethod
	def deserialize(cls, data: dict):
		return cls(
			data.get('location', ''),
			data.get('time', ''),
			data.get('items', {})
		)

current = Recorder()