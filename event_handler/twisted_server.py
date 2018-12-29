from twisted.internet import protocol, reactor
class Knock(protocol.Protocol):
    def dataReceived(self, data):
        print('Client', data)
        data_as_string = data.decode("utf-8")

        if data_as_string == "Knock knock":
            response_string = "Who's there?"
        else:
            response_string = data_as_string + " who?"

        print('Server:', response_string)
        self.transport.write(bytes(response_string,'utf-8'))

class KnockFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Knock()

reactor.listenTCP(8000, KnockFactory())
reactor.run()
