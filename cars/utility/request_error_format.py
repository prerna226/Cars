def request_error_messages_formate(params):
    
    try:
        for x in params:
            val = params[x]
            return {'error':str(x)+' '+str(val[0])}
    except Exception as e:
        print('................requestErrorMessagesFormate.........',str(e))
        return {'error': 'Invalid Request'}

