from yoko import YokoSync
import random
import _thread as thread


def reader(peer: YokoSync):
    while peer.is_alive:
        status, package = peer.receive()
        if status:
            print('\r<', package, '\n> ', end='')


def main():
    address = ('127.0.0.1', random.randint(1025, 9999))
    peer = YokoSync(address)
    print(f'Current peer token is: {peer.get_token()}')
    peer.connect(input("Enter other peer token here: "))
    thread.start_new_thread(reader, (peer, ))
    while True:
        package = {
            'message': input("> ")
        }
        status = peer.send(package)
        if not status:
            print('[FAILED]')


if __name__ == '__main__':
    main()
