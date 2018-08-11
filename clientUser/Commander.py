class Commander:
    def __init__(self):
        self.commands = []

    def add(self, target, request, **content):
        content['target'] = target
        content['request'] = request
        self.commands.append(content)

    def send(self, com):
        for command in self.commands:
            com.send(**command)
        self.commands = []
