class CsrfProcessor:
    """
    File with processors that will process
    request until he got to a specific controller.
    Pattern FRONT CONTROLLER
    Check csrf_token
    """

    def process(self, request):
        if request['method'] == 'POST':
            params = request['params']
            if b'csrf_token' in params:
                csrf = params[b'csrf_token']
                csrf = csrf[0]
                csrf = csrf.decode(encoding='utf-8')
                if csrf != '123':
                    raise Exception('Wrong csrf_token')
            else:
                raise Exception('In request no csrf_token')
