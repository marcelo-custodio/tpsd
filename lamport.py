import random

class Process:
    def __init__(self, id):
        self.id = id
        self.clock = 0
        return
    
    def send_message(self, message):
        self.clock += 1
        timestamp_message = (self.clock, message, self.id)

        receiver_id = random.randint(0, len(processes) - 1)
        if receiver_id == self.id: receiver_id = (receiver_id + 1) % (len(processes) - 1)
        receiver = processes[receiver_id]

        print(f"Processo {self.id} enviou mensagem {timestamp_message} para o processo {receiver_id} no tempo {self.clock}")
        receiver.receive_message(timestamp_message)
        return
    
    def receive_message(self, timestamp_message):
        timestamp, message, sender = timestamp_message

        print(f"Processo {self.id} tinha tempo {self.clock}")
        self.clock = max(self.clock, timestamp) + 1

        print(f"Processo {self.id} recebeu mensagem {timestamp_message} do processo {sender} no tempo {self.clock}")
        return

def simulate(processes, num_messages):
    for _ in range(num_messages):
        sender_id = random.randint(0, len(processes) - 1)
        sender = processes[sender_id]

        message = f"Mensagem do processo {sender_id}"
        sender.send_message(message)
    return

if __name__ == "__main__":
    n = 4
    processes = [Process(i) for i in range(n)]

    num_messages = 80
    simulate(processes, num_messages)