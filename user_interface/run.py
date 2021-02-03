from user_interface.server import run
from user_interface.urls import urls
from user_interface.processors import CsrfProcessor

if __name__ == '__main__':
    processors = [CsrfProcessor()]
    run(urls, processors)
