from socket import *
# We Need This Library To Creat The Web Server
import urllib.request

# we need This Library To defines functions and classes which help in opening URLs (mostly HTTP) in a complex world
# The Server is Working on port 6060
serverPort = 6060
serverSocket = socket(AF_INET, SOCK_STREAM)
# I dont Put Ip To be more General but it can be done with 127.0.0.1
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("The Web Server is Ready .... ")
# mAke the server with infint loop to be ready For any Request From Client-->(Web Browser)
while True:
	# Take the Address of the Client
	connectionSocket, addr = serverSocket.accept()
	# take the massge request
	request_data_from_Brawser = connectionSocket.recv(1024).decode()
	# print the recived request from Client
	print("Received sentence From The Client (web brawser):", request_data_from_Brawser)
	# Save the ip of Client and its  Port
	ip = addr[0]
	port = addr[1]
	# the splitting of the sentence allows the code to extract specific information from the client's request
	sentence_parts = request_data_from_Brawser.split()
	if len(sentence_parts) >= 2:
		# so the object will be -->/resourses-->the place where the server will give me the response
		object = sentence_parts[1]
		print("Requested object:", object)

		if object == '/' or object == '/index.html' or object == '/main_en.html' or object == '/en':
			connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
			connectionSocket.send("Content-Type: text/html \r\n".encode())
			connectionSocket.send("\r\n".encode())
			file1 = open("main_en.html", "rb")
			connectionSocket.send(file1.read())

		elif object == '/ar' or object == '/main_ar.html':
			connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
			connectionSocket.send("Content-Type: text/html \r\n".encode())
			connectionSocket.send("\r\n".encode())
			file2 = open("main_ar.html", "rb")
			connectionSocket.send(file2.read())
		elif object == '/myform.html':
			connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
			connectionSocket.send("Content-Type: text/html \r\n".encode())
			connectionSocket.send("\r\n".encode())
			file2 = open("MyForm.html", "rb")
			connectionSocket.send(file2.read())

		elif object.endswith('.html'):
			connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
			connectionSocket.send("Content-Type: text/html \r\n".encode())
			connectionSocket.send("\r\n".encode())
			file3 = open("main_en.html", "rb")
			connectionSocket.send(file3.read())
		elif object.endswith('.css'):
			connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
			connectionSocket.send("Content-Type: text/css \r\n".encode())
			connectionSocket.send("\r\n".encode())
			file4 = open("Css_File_Style.css", "rb")
			connectionSocket.send(file4.read())

		elif object.endswith('.png'):
			url = "https://e7.pngegg.com/pngimages/423/224/png-clipart-desktop-high-definition-television-forest-1080p-forest-computer-wallpaper-grass-thumbnail.png"
			headers = {
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
			requestFromClient = urllib.request.Request(url, headers=headers)
			content = urllib.request.urlopen(requestFromClient).read()
			connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
			connectionSocket.send("Content-Type: image/png \r\n".encode())
			connectionSocket.send("\r\n".encode())
			connectionSocket.send(content)

		elif object.endswith('.jpg'):
			url = "https://www.w3schools.com/w3css/img_forest.jpg"
			connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
			connectionSocket.send("Content-Type: image/jpg \r\n".encode())
			connectionSocket.send("\r\n".encode())
			urllib.request.urlretrieve(url, "image.jpg")
			# Open the local image file and send its content
			file6 = open("image.jpg", "rb")
			connectionSocket.send(file6.read())

		elif object == '/so':
			connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
			connectionSocket.send("Content-Type: text/html \r\n".encode())
			connectionSocket.send("Location: https://stackoverflow.com \r\n".encode())
			connectionSocket.send("\r\n".encode())

		elif object == '/itc':
			connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
			connectionSocket.send("Content-Type: text/html \r\n".encode())
			connectionSocket.send("Location: https://ritaj.birzeit.edu// \r\n".encode())
			connectionSocket.send("\r\n".encode())
		else:
			error_message = f''' <html> <head> <title>Error 404</title> <style>
                            body {{  
                            background-repeat: no-repeat;
                            background-attachment: fixed;
                            background-size: 100% 100%; 
                            background-color:#5F9EA0; 
                            }}
                            h0{{ margin-top: 80px; color: black; font-weight: bold; text-align: center; }}
                            h1 {{ margin-top: 80px; color: red; font-weight: bold; text-align: center; }}
                            h2 {{background-color:  black; 
                            border-radius: 20px;
                            color:#5F9EA0;
                            font-weight: bold;
                            text-align: center;
                            font-family: "Roboto", Arial, sans-serif;
                            font-size: 18px;
                            padding: 20px;
                            margin: 25px auto;
                            max-width: 10000px;
                            letter-spacing: 1px;}} 
                            </style> </head> <body> 
                            <h0>HTTP/1.1 404 Not Found</h0>
                            <h1>The file is not found</h1>
                            <h2>Nadia Thaer Shaikh  --> Id: 1210021</h2>
                            <h2>Rasha Mohammad Daoud ♡--> Id:1210382</h2>

                            <h2><b>Client IP: {ip}</b></p>
                            <h2><b>Client Port: {port}</b></p> </body> </html> '''.encode('utf-8')
			connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
			connectionSocket.send("Content-Type: text/html\r\n".encode())
			connectionSocket.send("\r\n".encode())
			connectionSocket.send(error_message)
			connectionSocket.close()
	else:
		print("Invalid request format:", request_data_from_Brawser)
		# Add appropriate error handling or send a 400 Bad Request response