class Email:
    def __init__(self, sender, receiver, content) -> None:
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


email_info = {}
num = 0

while True:

    command = input().split()

    if command[0] == "Stop":
        break

    else:
        email_info[num] = Email(command[0], command[1], command[2])
        num += 1


indices_sent = [int(x) for x in input().split(", ")]

for key, email in email_info.items():
    if key in indices_sent:
        email.send()
        print(email.get_info())
    else:
        print(email.get_info())
