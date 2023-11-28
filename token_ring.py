import random

class Node:
    def __init__(self, id):
        self.id = id
        self.is_coordinator = False
        self.neighbor = None

    def start_election(self):
        if not self.is_coordinator:
            election_message = f"Election started by node {self.id}"
            self.neighbor.receive_message(election_message)

    def receive_message(self, message):
        print(message)
        if "Election started" in message:
            sender_id = int(message.split(" ")[-1])
            if sender_id > self.id:
                self.is_coordinator = False
                election_message = f"Election started by node {sender_id}"
                self.neighbor.receive_message(election_message)
            elif sender_id < self.id:
                self.is_coordinator = True
                election_message = f"Election started by node {self.id}"
                self.neighbor.receive_message(election_message)
            else:
                self.is_coordinator = True
                coordinator_message = f"Coordinator is {self.id}"
                self.neighbor.receive_message(coordinator_message)
        elif "Coordinator is" in message:
            self.is_coordinator = False
            coordinator_id = int(message.split(" ")[-1])
            if coordinator_id == self.id:
                self.is_coordinator = True

def simulate_election(nodes):
    for node in nodes:
        node.neighbor = nodes[(nodes.index(node) + 1) % len(nodes)]

    election_node = random.choice(nodes)
    election_node.start_election()

    for node in nodes:
        print(node.id, node.is_coordinator)

if __name__ == "__main__":
    n = 200
    nodes = [Node(i) for i in range(n)]

    simulate_election(nodes)