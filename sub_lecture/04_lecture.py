# 이메일을 보내면 이메일을 보냈다라고 True를 출력해주는 send_eamil() 메서드를 가진 Email 클래스를 작성하시오



# class Email:
#     def __init__(self):
#         self.is_sent = False

#     def send_email(self):
#         self.is_sent = True
          
# my_email = Email()
# print(my_email.is_sent) # ===> False
# my_email.send_email()
# print(my_email.is_sent) # ===> True


# 아래처럼 리스트에 단일 값을 넣는 add() 메서드와 값을 두번 넣어주는 add_twice() 메서드를 가진 Bag 클래스를 작성하시오

class Bag:
    def __init__(self):
        self.data = []
    
    def add(self, a):
        self.data += [a]
    
    def add_twice(self, b):
        self.data += [b,b]



bag = Bag()
bag.add(1)
bag.add_twice(5)
print(bag.data)

