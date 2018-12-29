from twisted.internet import reactor, protocol
class KnockClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write(bytes("Knock knock",'utf-8'))
    def dataReceived(self, data):
        data_as_string = data.decode("utf-8")
        if data_as_string == "Who's there?":
            response_as_string = "Disappearing client"
            self.transport.write(bytes(response_as_string,'utf-8'))
        else:
            self.transport.loseConnection()
            reactor.stop()

class KnockFactory(protocol.ClientFactory):
    protocol = KnockClient

def main():
    f = KnockFactory()
    reactor.connectTCP("localhost", 8000, f)
    reactor.run()
if __name__ == '__main__':
    main()