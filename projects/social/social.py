import random


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i + 1}")
            # Create friendships
            # total_friendships = avg_friendships * num_users

        # create a list with all possible friendship combinations
        possible_friendships = []
        for user_id in self.users:
            # the counter starts at user_id + 1 and ends at last_id + 1 BECAUSE...
            # friend_id needs be in the correct number range. User_IDs start at 1 AND...
            # python's range() doesn't end at the last number, so last_id needs to be + 1 as well
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

            # shuffle the list
        random.shuffle(possible_friendships)
        # then grab the first N elements from the list
        # number of times to add_friendships = avg_friendships * num_users / 2
        # for i in range(num_users * avg_friendships // 2):
        for i in range(num_users):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = [[user_id]]

        while len(queue) > 0:
            path = queue.pop(0)
            latest_vertex = path[-1]
            if latest_vertex not in visited:
                visited[path[-1]] = path
                for neighbor in self.friendships[path[-1]]:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    queue.append(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    print("-----")
    connections = sg.get_all_social_paths(1)
    print(connections)
