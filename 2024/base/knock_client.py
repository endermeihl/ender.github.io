from twisted.internet import protocol, reactor


class KnockClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("Knock knock".encode("utf-8"))

    def dataReceived(self, data):
        if data.decode("utf-8").startswith("Who's there?"):
            response = "Banana"
            self.transport.write(response.encode("utf-8"))
        else:
            self.transport.loseConnection()
            reactor.stop()


class KnockFactory(protocol.ClientFactory):
    protocol = KnockClient


def main():
    f = KnockFactory()
    reactor.connectTCP("localhost", 8000, f)
    reactor.run()


if __name__ == "__main__":
    main()
