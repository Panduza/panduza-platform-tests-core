from panduza import Client, Ping
import time

import random
import string


ADDR="localhost"
PORT=1883

client = Client(url=ADDR, port=PORT)
client.connect()
interfaces = client.scan_all_interfaces()


def generate_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

print("===")
for topic, info in interfaces.items():

    if info["type"] == "ping" :
        print(topic, " - ", info)

        ping = Ping(client=client, topic=topic)
        
        iterations = 5000
        start_time = time.time()
        for i in range(iterations):
            ping.mirror.value.set(generate_random_string(4))
        end_time = time.time()

        elapsed_time = end_time - start_time
        print(f"Le temps écoulé est {elapsed_time} secondes. {iterations/elapsed_time}op/s")

