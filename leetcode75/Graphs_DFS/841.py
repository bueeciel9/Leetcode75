class Solution(object):
    def canVisitAllRooms(self, rooms):
        # Keep track of visited rooms
        visited = set()

        def dfs(room):
            # If the room is already visited, do nothing
            if room in visited:
                return
            # Mark the current room as visited
            visited.add(room)
            # Use the keys in the current room to visit other rooms
            for key in rooms[room]:
                dfs(key)

        # Start the DFS from room 0
        dfs(0)

        # If the number of visited rooms equals the total number of rooms,
        # it means we can visit all rooms
        return len(visited) == len(rooms)
