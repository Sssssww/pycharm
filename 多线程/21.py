from multiprocessing import Process
import os



def info(tittle):
    print(tittle)
    print('moudle name', __name__)
    # 得到父亲进程的id
    print('parent process', os.getpid())
    # 得到本身进程的id
    print('process id',os.getpid())


def f(name):
    info('function f')
    print('hello',name)


if __name__ == '__main__':
    info('main line')
    p = Process(target=f , args=('bob',))
    p.start()
    p.join()