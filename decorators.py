import logging

def log_message(func):
    def wrapper(message, *args, **kwargs):
        logging.info(f"Received message: {message.text} from user {message.chat.id}")
        return func(message, *args, **kwargs)
    return wrapper
