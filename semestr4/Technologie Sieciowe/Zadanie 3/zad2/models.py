from random import randint
from numpy.random import choice
import os

''' 
klasa sygnału, który zawiera dane do wysłania
'''
class Signal():
    def __init__(self, direction, data, state='normal'):
        self.direction = direction
        self.data = data
        self.state = state

    def __str__(self):
        if self.state == 'jamming':
            return 'jam'
        return str(self.data)

''' 
medium informacyjne, które obsługuje userów
i przesyła dane 
'''
class Medium:

    def __init__(self, size):
        self.size = size
        self.signals = [[] for _ in range(size)]
        self.users = {}
        self.time = 0
        self.is_working_correctly = True

    def __str__(self):
        temp = []
        for i in self.signals:
            temp.append([str(j) for j in i])
        return str(temp)

    ''' dodanie usera do sieci '''
    def add_user(self, user):
        new_address = -1
        while new_address < 0 or new_address in list(self.users.keys()):
            new_address = randint(0, self.size-1)
        
        self.users[new_address] = user
        return new_address

    ''' przesyłanie sygnałów i obsługa userów '''
    def send_signal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.time += 1

        print(self.time)
        # przesuwanie sygnałów
        new_signals = [[] for _ in range(self.size)]
        for i, signal in enumerate(self.signals):
            if len(signal) > 0:
                for s in signal:
                    if s.direction == 'left':
                        if i > 0:
                            new_signals[i-1].append(s)
                    elif s.direction == 'right':
                        if i < self.size - 1:
                            new_signals[i+1].append(s)

        self.signals = new_signals                

        print(self)
        for user in self.users.values():
            
            if user.left_punishment_seconds == 0 or user.is_sending_jamming:
                user.do_something(self.time, self.signals[user.connection_address])

                if user.status == 2:
                    # tworzenie i wysyłanie zwykłego sygnału z danymi
                    right_signal = Signal('right', user.data)
                    left_signal = Signal('left', user.data)
                    self.signals[user.connection_address].append(right_signal)           
                    self.signals[user.connection_address].append(left_signal)

                elif user.status == 3:
                    # tworzenie i wysyłanie jam signal
                    jamming_signal_left = Signal('left', user.data, state='jamming')
                    jamming_signal_right = Signal('right', user.data, state='jamming')
                    self.signals[user.connection_address].append(jamming_signal_left)
                    self.signals[user.connection_address].append(jamming_signal_right)

                elif user.status == 4:
                    self.is_working_correctly = False
        
            else:
               
                user.do_something(self.time, self.signals[user.connection_address])
                user.left_punishment_seconds -= 1
 

            print("User id: %s, received data: %s, user status: %s, user data: %s, user connection address: %s" % (user, user.received_data, user.status, user.data, user.connection_address))

        


# status = 1 - słuchanie
# status = 2 - wysyłanie
# status = 3 - kolizja
# status = 4 -  > 15 prób wysłania
class User():
    def __init__(self, username, data):
        self.username = username
        self.status = 1
        self.data = data
        self.connection_address = None
        self.curr_sending_time = 0
        self.max_sending_time = None
        self.received_data = []
        self.curr_received_data = ''
        self.sending_attempts = 0
        self.left_punishment_seconds = 0
        self.collisions = 0
        self.is_sending_jamming = False

    def __str__(self):
        return str(self.username)

    def add_to_medium(self, medium):
        self.connection_address = medium.add_user(self)
        return self.connection_address

    def do_something(self, time, channel):

        # czy podczas słuchania twój kanał jest zajęty
        if self.status == 1 and len(channel) > 0:
            singal_states = [channel[i].state for i in range(len(channel))]
            # czy odebrałeś jakiś jam signal
            if 'jamming' in singal_states:
                self.curr_received_data = ''
            elif len(channel) == 1:
                if channel[0].data != self.curr_received_data and self.curr_received_data != '':
                    self.received_data.append(self.curr_received_data)
                self.curr_received_data = channel[0].data

        # jeśli słuchasz i nie otrzymujesz żadnych danych
        elif self.status == 1:
            # jeśli otrzymałeś jakąś wiadomość której jeszcze nie dodałeś do listy received_data
            if len(self.curr_received_data) > 0:
                self.received_data.append(self.curr_received_data)
                self.curr_received_data = ''
            if self.left_punishment_seconds == 0:
                # 10% na to, że zaczniesz coś wysyłać
                self.status = choice([1, 2], 1, [1,9])[0]

        # jeśli wysyłasz i twój kanał jest pusty
        elif self.status == 2 and len(channel) == 0:
            self.curr_sending_time += 1
            # sprawdzenie czy wysłałeś wystarczająco dużo sygnałów by być pewnym, że kolizja nie nastąpiła
            if self.curr_sending_time == self.max_sending_time * 2:
                self.status = 1
                self.curr_sending_time = 0
                self.sending_attempts = 0
                
        # jeśli wysyłasz, a twój kanał nie jest pusty to znaczy, że nastąpiła kolizja
        elif self.status == 2 and len(channel) > 0:
 
            self.status = 3
            self.curr_sending_time = 0
            self.is_sending_jamming = True
            self.collisions += 1
            self.collision_handling()

        # jeśli miałeś kolizję i jesteś w trakcie wysyłania jam singal
        elif self.status == 3:
            self.curr_sending_time += 1
            if self.curr_sending_time == self.max_sending_time * 2:
                self.status = 1
                self.curr_sending_time = 0
                self.is_sending_jamming = False
   

        
    def collision_handling(self):
        self.sending_attempts += 1

        # jeśli 16 razy pod rząd nie udało się wysłać wiadmości to znaczy, że sieć jest zła i trzeba przerwać symulację
        if self.sending_attempts == 16:
            self.status = 4
            return

        if self.sending_attempts > 10:
            exponent = 10
        else:
            exponent = self.sending_attempts

        random_Number = randint(1, 2**exponent - 1)
        self.left_punishment_seconds = random_Number * self.max_sending_time