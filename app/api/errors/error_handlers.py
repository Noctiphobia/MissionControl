from collections import Callable

from flask import jsonify

from app.api.errors.duplicate_error import DuplicateError
from app import app
from werkzeug.http import HTTP_STATUS_CODES


def error_with_code(error_code: int) -> Callable:
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            result = jsonify({
                'message': str(func(*args, **kwargs)),
                'error': HTTP_STATUS_CODES[error_code]
            })
            result.status_code = error_code
            return result
        return wrapper
    return decorator


@app.errorhandler(KeyError)
@error_with_code(404)
def handle_key_error(error: KeyError) -> KeyError:
    return error


@app.errorhandler(AttributeError)
@error_with_code(400)
def handle_attribute_error(error: KeyError) -> KeyError:
    return error


@app.errorhandler(DuplicateError)
@error_with_code(409)
def handle_duplicate_error(error: KeyError) -> KeyError:
    return error
