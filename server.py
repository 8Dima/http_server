import socket

sock = socket.socket()

try:
	sock.bind(('',80))
	print("Using port 80")
except OSError:
	sock.bind(('', 8080))
	print("Using port 8080")

sock.listen(5)
while True:
	conn, addr = sock.accept()
	print("Connected", addr)



	data = conn.recv(8192)
	msg = data.decode()
	print(msg)

	resp = """HTTP/1.1 200 OK
	Server: SelfMadeServer v0.0.1
	Content-type: text/html

	"""

	if ("GET /index.html" in msg):
		with open('index.html', 'r') as file:
			for line in file.readlines():
				resp+=line

	if ("GET /1.html" in msg):
		with open('1.html', 'r') as file:
			for line in file.readlines():
				resp+=line
	
	if ("GET /2.html" in msg):
		with open('2.html', 'r') as file:
			for line in file.readlines():
				resp+=line

	if ("GET /style.css" in msg):
		with open('style.css', 'r') as file:
			for line in file.readlines():
				resp+=line									

	if ("/favicon.ico" in msg):
		resp = """HTTP/1.1 404 Not Found
		Server: SelfMadeServer v0.0.1
		Content-type: text/html

		"""



	conn.send(resp.encode())
	conn.close()