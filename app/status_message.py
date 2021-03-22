STATUS_MSG = {
    200: 'Result is success',
    201: 'Resource is created',
    400: 'Request is not valid',
    401: 'Request is unauthorized',
    403: 'Request is forbidden',
    404: 'Resource is not found',
    500: 'Request is failed to process'
}


def get_status_message(status_code, default=''):
    return STATUS_MSG.get(status_code, default)


def get_data_status_message(rv):
    data = None
    status = 200
    message = None

    if type(rv) is not tuple:
        data = rv
    elif len(rv) == 1:
        data = rv[0]
    elif len(rv) == 2:
        (data, status) = rv
    elif len(rv) > 2:
        (data, status, message) = rv

    if message is None:
        message = get_status_message(status)
    return data, status, message


def get_data_page_data_status_message(rv):
    message = None
    if len(rv) == 2:
        status = 200
        (data, page_data) = rv
    elif len(rv) == 3:
        (data, page_data, status) = rv
    else:
        (data, page_data, status, message) = rv
    if message is None:
        message = get_status_message(status)
    return data, page_data, status, message
