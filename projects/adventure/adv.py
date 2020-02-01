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

    def add_connected_room(self, room1, room2, cardinal_direction):
        if room1 and room2 in self.world:
            self.world[room1][cardinal_direction] = room2
            cardinal_direction_inverse = self.cardinal_direction_inverse(
                cardinal_direction)
            self.world[room2][cardinal_direction_inverse] = room1

    def cardinal_direction_inverse(self, cardinal_direction):
        if cardinal_direction == 'n':
            return 's'
        if cardinal_direction == 's':
            return 'n'
        if cardinal_direction == 'w':
            return 'e'
        if cardinal_direction == 'e':
            return 'w'

    def bfs(self, curr_room_id, unexplored_room='?'):
        queue = [curr_room_id]

        while len(queue) > 0:
            curr_room_id = queue.pop(0)
            if self.world[curr_room_id]['n'] == unexplored_room:
                return 'n'
            elif self.world[curr_room_id]['s'] == unexplored_room:
                return 's'
            elif self.world[curr_room_id]['w'] == unexplored_room:
                return 'w'
            elif self.world[curr_room_id]['e'] == unexplored_room:
                return 'e'


# instantiate world graph
world_graph = Graph()
print("curr room:", player.current_room.id)
print("exits:", player.current_room.get_exits())
print("curr room:", player.travel('n'))

# You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.


def world_traversal(starting_room):
    move_options = player.current_room.get_exits()
    random.shuffle(move_options)
    initial_direction = move_options[0]
    # stack will hold tuples of the room_id and a cardinal direction, to let us know what direction we need to move in still)
    stack = [(starting_room, initial_direction)]
    visited = set()

    while len(stack) > 0:
        room_id = stack.pop()
        # move_options is an array of the possible directions to move in
        move_options = player.current_room.get_exits()
        if room_id not in visited:
            visited.add(room_id)
            # add the current room to the world_graph room vertices
            world_graph.add_room(room_id)
            # keep a track of the current room ID
            old_id = room_id
            # move in a random direction
            player.travel()
            # append traveled direction to traveral_path
            traversal_path.append()
            # add connected room paths to world_graph dictionary
            world_graph.add_connected_room(
                old_id, player.current_room.id, )


world_traversal(player.current_room.id)

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
