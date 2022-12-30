# 입금, 출금, 잔액 조회가 가능한 은행 계좌관리 프로그램을 작성하여라
# 잔액(balance), 입출금액(money), 계좌번호(idNum), 계좌주(idName)
# 입금기능(deposit), 출금기능(withDraw), 잔액조회(getBalance)
# 클래스의 멤버를 선언하여 작동될 수 있도록 할 것.


class Account:
    balance = 0
    money = 0
    idNum = 0
    idName = ""

        def __init__(self, balance, money, idNum, idName):
            self.money = money
            self.balance = balance
            self.idNum = idNum
            self.idName = idName

        def deposit(self):
            money = input(self.money)
            balance = self.money + self.balance
            return balance

        def withDraw(self):
            money = input(self.money)
            balance = self.balance - self.money
            return balance








        def withDraw(self,balance,money):
            balance-=input("출금액>", money)
            return balance

        def getBalance(self,balance):
            print("잔액>", balance)

