from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<HTML>
    <HEAD>
    </HEAD>
    <BODY bgcolor="cyan">
        <table border="1" align="center" bgcolor="blue" cellpadding="10"
        <caption><h1><center>List of protocols+</center></h1></caption>
        <tr><th>S.No</th><th>Name of the layers</th>
        <th>Name of the protocols</th>
    </tr>
    <tr>
        <td>1</td><td>Application layer</td><td>HTTP,FTP,RDP</td>
    </tr>
    <tr>
        <td>2</td><td>Transport Layer</td><td>TCP & UDP</td>
    </tr>
    <tr>
        <td>3</td><td>Internet Layer</td><td>ICMP,ARP,IGMP</td>
    </tr>
    <tr>
        <td>4</td><td>Network access Layer</td><td>Ethernet,FDDI,Frame Relay,Token Ring</td>
    </tr>
    </table>
    </BODY>
</HTML>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()