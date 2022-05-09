from abc import abstractmethod, ABC


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass


class IContent(ABC):
    @abstractmethod
    def set_content(self, content):
        pass


class MyContent(IContent):
    def __init__(self, content_type):
        self.content_type = content_type
        self.__content = None


    def set_content(self, content):
        if self.content_type == 'MyML':
            self.__content = '\n'.join(['<myML>', content, '</myML>'])
        else:
            self.__content = content

    def __repr__(self):

        template = "Content:\n{content}"

        return template.format(content = self.__content)

class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\n"

        return template.format(sender = self.__sender, receiver = self.__receiver)


# email = Email('IM', 'MyML')
# email.set_sender('qmal')
# email.set_receiver('james')
# email.set_content('Hello, there!')
# print(email)

# email = Email('IM')
# email.set_sender('qmal')
# email.set_receiver('james')
# content = MyContent('MyML')
# content_text = 'Hello, there!'
# content.set_content(content_text)
# print(email)
# print(content)

