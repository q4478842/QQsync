from twisted.internet import reactor
from twisted.internet.protocol import Protocol , Factory

class SimpleLogger(Protocol):

    fi = open("/temp/31.log","rw+")

    def connectionMade(self):
        print 'got connection from',self.transport.client

    def connectionLost(self,reason):
        print self.transport.client,'disconnected'

    def dataReceived(self,data):
        self.fi.write(data)
        self.fi.flush()

factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(1234,factory)
reactor.run()
