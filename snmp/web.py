from http.server import HTTPServer, BaseHTTPRequestHandler

content = """

<html>
<head>
<title>Configiration Details of HP Laptop</title>
</head>
<table border="2"  cellspacing="4" cellpadding="6">

<tr>

<h1>Configuration Details Of HP Laptop </h1><br><br>

<th>S.no</th>

<th>Description</th>

<th>HP</th>

</tr>

<tr>

<th>1</th>

<th>Processor</th>

<th>Intel core i5</th>

</tr>

<tr>

<th>2</th>

<th>Operating System</th>

<th>Windows 11 Home SL</th>

</tr>

<tr>

<th>3</th>

<th>Graphics</th>

<th>NVIDIA Quadro</th>

</tr>

<tr>

<th>4</th>

<th>Memory</th>

<th>16GB of DDR4</th>

</tr>

<tr>

<th>5</th>

<th>Storage</th> 

<th>512 GB SSD</th>

</tr>

</body>

</html>
"""

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request recieved")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())


server_address = ('', 8080)
httpd = HTTPServer(server_address, HelloHandler)
print("my webserver is running.....")
httpd.serve_forever()