class Flower:
    def __init__(self, name, petals, price):
        self._name = name
        self._petals = float(petals)
        self._price = float(price)

    def price(self):
        return self._price

    def petals(self):
        return self._petals

    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def set_petals(self, petals):
        self._petals = float(petals)

    def set_price(self, price):
        self._price = float(price)


if __name__ == "__main__":
    bucket = []
    bucket.append(Flower("Rose", "10", "50"))
    bucket.append(Flower("Daisy", "5", "10"))
    bucket.append(Flower("Lavender", "15", "20"))

    for i in range(1, 5):
        bucket[0].set_price(bucket[0].price() * i)
        bucket[1].set_price(bucket[1].price() * i)
        bucket[2].set_price(bucket[2].price() * i)

    print(bucket[0].price())
    print(bucket[1].price())
    print(bucket[2].price())
