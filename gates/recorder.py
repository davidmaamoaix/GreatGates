import json

PATH = 'gates/data.json'

class OrderEntry:

	def __init__(self, entryId: int, location: str, time: str, items: dict):
		self.entryId = entryId
		self.location = location
		self.time = time
		self.items = items

	def __str__(self):
		return f'Entry: %d; Location: %s; Time: %s; Data: %s'%\
				(self.entryId, self.location, self.time, self.items)

	def serialize(self) -> dict:
		data = {
			'entryId': self.entryId,
			'location': self.location,
			'time': self.time,
			'items': self.items
		}

		return data

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
		userEntries.append(entry.serialize())
		self.dumps()

	def find(self, userId: str) -> list:
		return self.data.get(userId, [])

	def remove(self, userId: str, entryId: int):
		userEntries = self.data.setdefault(userId, [])
		self.data[userId] = [i for i in userEntries if i['entryId'] != entryId]
		self.dumps()

	def dumps(self):
		with open(PATH, 'w') as f:
			json.dump(self.data, f)

	def genEntryId(self) -> int:
		currId = self.data.setdefault('entryIdGenerator', 0)
		self.data['entryIdGenerator'] += 1
		self.dumps()
		return currId

def add(*args, **kwargs):
	Recorder().add(*args, **kwargs)

def remove(*args, **kwargs):
	Recorder().remove(*args, **kwargs)

def find(*args, **kwargs):
	return Recorder().find(*args, **kwargs)

def genEntryId():
	return Recorder().genEntryId()