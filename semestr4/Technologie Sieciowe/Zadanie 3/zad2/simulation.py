from models import User, Medium
from random import randint
from time import sleep
import sys

''' generowanie losowego ciągu 0-1 o podanej długości '''
def gen_random_binary_string(leng):
    data = ''
    for _ in range(leng):
        data += str(randint(0,1))

    return data

''' tworzenie obiektu Medium '''
def create_medium(size, nodes_amount, data_length):
    medium = Medium(size)

    for id in range(nodes_amount):
        # generowanie losowego ciągu 0-1 o podanej długości,
        # który zostanie użyty jako dane wysyłane przez usera
        data = gen_random_binary_string(data_length)
        user = User(id, data)
        # dołączenie usera do medium
        connection_address = user.add_to_medium(medium)
        # ustawienie jako maksymalny czas wysyłania
        # maksimum z odległości usera od poczatku i od końca
        max_sending_time = max(abs(size-connection_address), connection_address)
        user.max_sending_time = max_sending_time

    return medium

''' Symulowanie protokołu '''
def simulate(medium):
    while medium.is_working_correctly:
        medium.send_signal()
        sleep(0.5)

    print(medium.time)
    for user in medium.users.values():
        print("User id: %s, liczba kolizji: %s" % (user, user.collisions))


def main():
    args = list(sys.argv)
    try:
        size = int(args[1])
        nodes_amount = int(args[2])
        data_length = int(args[3])
    except:
        print("Wrong arguments provided!")
        return

    medium = create_medium(size=size, nodes_amount=nodes_amount, data_length=data_length)
    simulate(medium)

if __name__ == "__main__":
    main()