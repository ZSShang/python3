#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/10 0:11
#=============================================================
# coding:utf8
import _thread as thread
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec, lock):
    print('start loop', nloop, 'at: ', ctime())
    sleep(nsec)
    print('end loop', nloop, 'at: ', ctime())
    # 释放锁
    lock.release()


def main():
    print('starting at: ', ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        # 分配LockType锁对象
        lock = thread.allocate_lock()
        # 获取锁对象
        lock.acquire()
        locks.append(lock)
        # 启动一个新的线程
        # thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        # 如果获取了锁对象返回True，阻塞主线程，等待子线程完成，释放锁对象
        while locks[i].locked():
            pass
    print('all DONE at: ', ctime())


if __name__ == '__main__':
    main()