from collections import deque

class Solution:
	def __init__(self):
		pass
	

	def place_buildings(self, W, H, n):
		"""
		Place buildings into a grid.
		"""
		# directions array
		self.dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
		# buildings array
		self.buildings = [[-1 for _ in range(W)] for _ in range(H)]
		# visited array
		self.visited = [[False for _ in range(W)] for _ in range(H)]
		# variable to hold the max distance
		self.min_distance = float('inf')

		self.rec(W, H, 0, 0, n)


	def rec(self, W, H, r, c, n):
		# base case - bfs
		if n==0:
			self.bfs(W, H)

		if c==W and r!=H:
			r+=1
			c=0

		# recursion relation
		for i in range(r, H):	# for row
			for j in range(c, W):	# for col
				# set the building
				self.buildings[i][j] = 0
				# make a recursive call.
				self.rec(W, H, r, c+1, n-1)
				# reset the building
				self.buildings[i][j] = -1

			# reset the column to 0 from the next row.
			j=0


	def bfs(self, w, h):
		"""
			Breadth first search to find the maximum distance between building and parking lot.
		"""
		q = deque()
		for i in range(h):
			for j in range(w):
				if self.buildings[i][j]==0:
					q.append((i, j, 0))
					self.visited[i][j] = True

		while q:
			i, j, dist = q.popleft()
			for dir in self.dirs:
				curr = (i+dir[0], j+dir[1])
				if 0<=curr[0]<w and 0<=curr[1]<h and not self.visited[curr[0]][curr[1]]:
					q.append((curr[0], curr[1], dist+1))
					self.visited[curr[0]][curr[1]] = True # mark as visited
	
		# compare the minimum distance with the maximum distance
		self.min_distance = min(self.min_distance, dist)

		# reset the visited array
		for i in range(h):
			for j in range(w):
				self.visited[i][j] = False


def main():
	W, H = 4, 4
	n = 3 
	s = Solution()
	s.place_buildings(W, H, n)


if __name__=="__main__":
	main()