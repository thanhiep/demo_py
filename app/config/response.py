def response_data(status, message, datetime, data):
    return {
        "status": status,
        "message": message,
        "datetime": datetime,
        "content": data
    }