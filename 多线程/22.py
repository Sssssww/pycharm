import multiprocessing
from time import ctime


def consumer(input_q):
    print("Into consumer:",ctime())
    while True:
        # 处理项
        item = input_q.get()
        print ("pull",itemm,"out of q")#此处代替为有用的工作
        input_q.tast_done()#发出信号通知任务完成
    print("Out of consumer:",ctime())##此句末执行，因为q.join()信号后，主进程启动，为等到print此语句完


def prodeuce(sequence,out_q):
    print("Inpo producer ",ctime())
    for item in sequence:
        output_q.put(item)
        print("put",item,"into q")
    print("Out of producer",ctime())


if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    #运行消费者进程
    cons_p = multiprocessing.Process(target= consumer, args = (q,1))
    cons_p.daemon = True
    cons_p.start()

    #在生产多个项，sqeuence代表要发送个消费者的项的序列
    #在实践中，这可能是生成器的输出或通过一些其他生产方式出来
    sequence = [1,2,3,4]
    prodeuce(sequence,q)
    q.join()


