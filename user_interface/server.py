from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from cgi import parse_header, parse_multipart
from urllib.parse import parse_qs

HOST_NAME = "localhost"
PORT_NUMBER = 80


class SchoolHttpProcessor(BaseHTTPRequestHandler):

    urls = {}
    processors = []

    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        url = self.get_url()
        self.postvars = None  # parameters
        # process the found address
        self.process_url(url)

    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        url = self.get_url()
        # Получаем параметры запроса
        self.postvars = self.parse_POST()
        self.process_url(url)

    def parse_POST(self):
        # Parsing parameters post request
        content_type, data_dict = parse_header(self.headers['content-type'])
        if content_type == 'multipart/form-data':
            postvars = parse_multipart(self.rfile, data_dict)
        elif content_type == 'application/x-www-form-urlencoded':
            length = int(self.headers['content-length'])
            postvars = parse_qs(
                self.rfile.read(length),
                keep_blank_values=1)
        else:
            postvars = {}
        return postvars

    def process_url(self, url):
        request = {
            'method': self.command,
            'params': self.postvars
        }

        # Pattern FRONT CONTROLLER
        for processor in self.processors:
            processor.process(request)

        if url in self.urls:
            # get view, Pattern PAGE CONTROLLER
            view = self.urls[url]
            result = view(request)
            self.show_result(result)
        else:
            self.show_result('404 Not Found')
            self.send_response(404)

    def get_url(self):
        # Get the address from the request body
        command, url, data = self.requestline.split()
        return url

    def show_result(self, result):
        if isinstance(result, str):
            self.wfile.write(result.encode(encoding='utf-8'))


def run(urls, processors):
    """Start server"""
    SchoolHttpProcessor.urls = urls  # urls for PAGE CONTROLLER
    SchoolHttpProcessor.processors = processors  # for FRONT CONTROLLER
    # create server
    serv = ThreadingHTTPServer((HOST_NAME, PORT_NUMBER), SchoolHttpProcessor)
    serv.serve_forever()


if __name__ == '__main__':
    server = ThreadingHTTPServer((HOST_NAME, PORT_NUMBER), SchoolHttpProcessor)
    server.serve_forever()

