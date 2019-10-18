import socket
import multiprocessing

def read_file():
	print('Reading... IP from file')
	r = open('ip.txt', mode='rt')
	f = open('result.txt','w')
	f.close()
	read_result = [line.strip() for line in r.readlines()]
	return read_result

def reverse_dns(ip_addr):
	print(ip_addr)
	reverse_dns = socket.gethostbyaddr(ip_addr)
	print(reverse_dns[0])
	f = open('result.txt','a')
	f.write(ip_addr+'^'+reverse_dns[0]+'\n')


a = read_file()

pool = multiprocessing.Pool(processes=10)
pool.map(reverse_dns,a)
pool.close()
pool.join()
