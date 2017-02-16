import threading
import time


class mythread(threading.Thread):
    def __init__(self, stopevt=None, File=None, name='subthread', Type='event'):
        threading.Thread.__init__(self)
        self.stopevt = stopevt
        self.name = name
        self.File = File
        self.Type = Type

    def Eventrun(self):
        while not self.stopevt.isSet():
            print self.name + ' alive\n'
            time.sleep(2)
        if self.File:
            print 'close opened file in ' + self.name + '\n'
            self.File.close()
        print self.name + ' stoped\n'

    def run(self):
        if self.Type == 'event':
            self.Eventrun()
        else:
            self.Daemonrun()


def evtstop():
    stopevt = threading.Event()
    FileA = open('testA.txt', 'w')
    FileB = open('testB.txt', 'w')
    A = mythread(stopevt, FileA, 'subthreadA')
    B = mythread(stopevt, FileB, 'subthreadB')
    print repr(threading.currentThread()) + 'alive\n'
    print FileA.name + ' closed? ' + repr(FileA.closed) + '\n'
    print FileB.name + ' closed? ' + repr(FileB.closed) + '\n'
    A.start()
    B.start()
    time.sleep(1)
    print repr(threading.currentThread()) + 'send stop signal\n'
    stopevt.set()
    A.join()
    B.join()
    print  repr(threading.currentThread()) + 'stoped\n'
    print 'after A stoped, ' + FileA.name + ' closed? ' + repr(FileA.closed) + '\n'
    print 'after A stoped, ' + FileB.name + ' closed? ' + repr(FileB.closed) + '\n'

if __name__ == '__main__':
    print '-------stop subthread example with Event:----------\n'
    evtstop()
