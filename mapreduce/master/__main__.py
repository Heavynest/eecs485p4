import sys
import click, time
import mapreduce.helper as helper
import os
import socket
from threading import Thread
import time
import sh


class Master:
	def kill(self):
		time.sleep(2)
		print("5second")
		hello=os.getpid()
		a=sh.kill()
		a(_in=hello)

	def jinghan(self):
		time.sleep(10)
		print(10)
		exit(1)
		while True:
			print("sb")
		print("10 second")

	def __init__(self):
		print("wo hai huo zhe")
		self.new=Thread(target=self.kill,args=())
		self.old=Thread(target=self.jinghan,args=())
		self.new.start()
		self.old.start()
		return

@click.command()
@click.argument("port_num", nargs=1, type=int)
def main(port_num):
    # TODO: you should remove this. This is just so the program doesn't 
    #       exit immediately!
    server=Master()
    time.sleep(15)
    print(15)

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    main()
