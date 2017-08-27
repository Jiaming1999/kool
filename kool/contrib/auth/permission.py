from kool.db import FlatFileDB


class Permission(FlatFileDB):
	"""Permissions are used to determine actions permitted on a course
	by a user or group"""
	
	_permissions = {}

	def __init__(self, name, course, codename):
		super().__init__()
		self.name = name
		self.course = course
		self.codename = codename

	def save(self):
		pass

	def delete(self):
		pass
