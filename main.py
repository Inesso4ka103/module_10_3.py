import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        threading.Thread.__init__(self)
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            y = randint(50, 500)
            with self.lock:
                if self.balance < 500 and self.lock.locked():
                    self.balance += y
                    print(f'Пополнение: {y}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            c = randint(50, 500)
            print(f'Запрос на: {c}')
            with self.lock:
                if c <= self.balance:
                    self.balance -= c
                    print(f'Снятие: {c}. Баланс: {self.balance}')
                else:
                    print(f'Запрос отклонён, недостаточно средств')
            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
