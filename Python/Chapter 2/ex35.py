class Sender:
    def __init__(self, name):
        self._name = name
        self._packets = {}

    def _process_data_to_packets(self, data):
        result = set()
        for word in data:
            result.add(word)
        # Do stuff with data
        return result

    def add_data(self, data):
        print("Alice: Im hoping he will read this soon")
        self._packets = self._process_data_to_packets(data)

    def get_packets(self):
        return self._packets

    def clear_packets(self):
        self._packets = {}


class Reader:
    def __init__(self, name):
        self._name = name
        self._receivedPackets = {}

    def receive_packets(self, packets):
        self._receivedPackets = packets

    def check_packets(self):
        return self._receivedPackets != {}

    def read_packets(self):
        if self.check_packets():
            print("Im done reading this awful message", self._receivedPackets, sep="\n")
            self._receivedPackets = {}


class Internet:
    def __init__(self):
        print("Beep Boop... Internet is booting")

    def deliver_packets(self, sender, receiver):
        send_packets = sender.get_packets()
        if len(send_packets) > 0:
            print("Sending...")
            receiver.receive_packets(send_packets)
            print("Sent.")
            sender.clear_packets()
        else:
            print("Nothing to do boo-hoo-hoo...")


if __name__ == "__main__":
    import random
    import time

    Alice = Sender("Alice")
    Bob = Reader("Bob")
    awesomeInternet = Internet()

    while True:
        possibility = random.randint(0, 100)
        packetLength = len(Alice.get_packets())
        if possibility < 20 and packetLength == 0:
            Alice.add_data("Hello Bob, I love you %d" % random.randint(1000, 3000))
        if packetLength > 0:
            awesomeInternet.deliver_packets(Alice, Bob)
        possibility = random.randint(0, 100)
        if possibility < 50:
            Bob.read_packets()
        time.sleep(2)

