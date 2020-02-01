from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


class Graph:
    def __init__(self):
        self.world = {}

    def add_room(self, room_id):
        self.world[room_id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}

    def add_connected_room(self, room1, room2, cardinal_direction, cardinal_direction_inverse):
        if room1 and room2 in self.world:
            self.world[room1][cardinal_direction] = room2
            self.world[room2][cardinal_direction_inverse] = room1

    def bfs(curr_room_id, unexplored_room='?'):
        queue = [curr_room_id]
        visited = set()

        while len(queue) > 0:
            room = queue.pop(0)
            if world[curr_room_id]['n'] == unexplored_room:
                return 'n'
            elif world[curr_room_id]['s'] == unexplored_room:
                return 's'
            elif world[curr_room_id]['w'] == unexplored_room:
                return 'w'
            elif world[curr_room_id]['e'] == unexplored_room:
                return 'e'


# instantiate world graph
world_graph = Graph()
print("curr room:", player.current_room.id)
print("exits:", player.current_room.get_exits())
print("curr room:", player.travel('n'))

# You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.


def world_traversal(starting_room):
    stack = [starting_room]
    visited = set()
    # get an initial array of the possible directions to move in
    initial_move_options = player.current_room.get_exits()
    random.shuffle(initial_move_options)

    while len(stack) > 0:
        room_id = stack.pop()
        if room_id not in visited:
            visited.add(room_id)
            # add the current room to the world_graph room vertices
            world_graph.add_room(room_id)
            # keep a track of the current room ID
            curr_id = room_id
            # move in a random direction
            player.travel(initial_move_options[0])
            traversal_path.append()


dfs(player.current_room.id)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
