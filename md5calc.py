import hashlib

class md5code():
	md5hex = ""
	byte1 = ""
	byte2 = ""
	def __init__(self,s):
		m = hashlib.md5()
		m.update(s.encode())
		self.md5hex = m.hexdigest()
		self.byte1 = self.md5hex[0:2]
		self.byte2 = self.md5hex[2:4]
