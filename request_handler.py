from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import response
# from views import get_all_parts, get_single_part, get_all_builds, get_single_build
from views import *
import json

# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.
class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        id = None
        
        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass
        
        return (resource, id)

    # Here's a class function
    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        self._set_headers(200)
        response = {}
        
        (resource, id) = self.parse_url(self.path)
        
        if resource == "parts":
            if id is not None:
                response = f"{get_single_part(id)}"
            else:
                response = f"{get_all_parts()}"
                
        if resource == "builds":
            if id is not None:
                response = f"{get_single_build(id)}"
            else:
                response = f"{get_all_builds()}"
                
        if resource == "partTypes":
            if id is not None:
                response = f"{get_single_partType(id)}"
            else:
                response = f"{get_all_partTypes()}"
                
        if resource == "builders":
            if id is not None:
                response = f"{get_single_builder(id)}"
            else:
                response = f"{get_all_builders()}"
                
        if resource == "userContents":
            if id is not None:
                response = f"{get_single_userContent(id)}"
            else:
                response = f"{get_all_userContents()}"
                
        if resource == "buildParts":
            if id is not None:
                response = f"{get_single_buildPart(id)}"
            else:
                response = f"{get_all_buildParts()}"
                
        self.wfile.write(response.encode())


    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        
        post_body = json.loads(post_body)
        
        (resource, id) = self.parse_url(self.path)
        
        new_part = None
        new_userContent = None
        new_build = None
        
        if resource == "parts":
            new_part = create_part(post_body)
            
        self.wfile.write(f"{new_part}".encode())
            
        if resource == "userContents":
            new_userContent = create_userContent(post_body)
        
        self.wfile.write(f"{new_userContent}".encode())
        
        if resource == "builds":
            new_build = create_build(post_body)
            
        self.wfile.write(f"{new_build}".encode())

    def do_PUT(self):
        """Handles PUT requests to the server
        """
        self.do_POST()

    def do_DELETE(self):
        """Handles DELETE requests to the server
        """
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path)
        
        if resource == "parts":
            delete_part(id)
            
        if resource == "builds":
            delete_build(id)
            
        if resource == "userContents":
            delete_userContent(id)
            
        if resource == "buildParts":
            delete_buildPart(id)
            
        self.wfile.write("".encode())

def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
