from twisted.internet import protocol, reactor


class Knock(protocol.Protocol):
    def dataReceived(self, data):
        print("Client:", data)
        if data.decode("utf-8").startswith("Knock knock"):
            response = "Who's there?"
        else:
            response = data.decode("utf-8") + " who?"
        print("Server:", response)
        self.transport.write(response.encode("utf-8"))


class KnockFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Knock()


reactor.listenTCP(8000, KnockFactory())
reactor.run()
