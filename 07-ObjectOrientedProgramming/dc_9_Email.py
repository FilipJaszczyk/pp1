from dc_9 import Message

class Email(Message):
    def __init__(self, fromUser, toUser, topic, message=''):
        super().__init__(message)
        self.fromUser = fromUser
        self.toUser = toUser
        self.topic = topic
    def send(self):
        return f'''
Wysyłanie emaila...
Od: {self.fromUser}
Do: {self.toUser}
Temat: {self.topic}
Treść: {self.message}'''
    
m1 = Email('jurek@małpa.pl','staszek@małpa.pl', 'Temat debaty')
m1.set_message('aaaaaaaaaaa')
print(m1.send())
