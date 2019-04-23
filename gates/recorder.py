import json

PATH = 'gates/data.json'

class OrderEntry:

	def __init__(self, entryId: int, location: str, time: str, items: dict):
		self.entryId = entryId
		self.location = location
		self.time = time
		self.items = items

	def serialize(self) -> dict:
		data = {
			'entryId': self.id,
			'location': self.location,
			'time': self.time,
			'items': self.items
		}

	@classmethod
	def deserialize(cls, data: dict):
		return cls(
			data.get('entryId', 0),
			data.get('location', ''),
			data.get('time', ''),
			data.get('items', {})
		)

class Recorder:

	def __init__(self):
		with open(PATH, 'r') as f:
			self.data = json.load(f)

	def add(self, userId: str, entry: OrderEntry):
		userEntries = self.data.setdefault(userId, [])
		userEntries.append(entry)

	def remove(self, userId: str, entryId: int):
		userEntries = self.data.setdefault(userId, [])
		self.data[userId] = [i for i in userEntries if i['entryId'] != entryId]

	def dumps(self):
		with open(PATH, 'w') as f:
			json.dump(self.data, f)

current = Recorder()