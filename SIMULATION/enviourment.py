class Environment:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def limit_position(self, position):
		"""Ensure the agent's position stays within the environment
		boundaries."""
		x, y = position
		x = max(0, min(x, self.width - 1))
		y = max(0, min(y, self.height - 1))
		return [x, y]

	def display(self):
		"""Display environment details."""
		print(f"Environment size: {self.width}x{self.height}")