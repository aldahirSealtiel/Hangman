def check_email(string):
    if ' ' not in string and '@' in string and '.' in string:
        index_symbol = string.index('@')
        index_dot = string.find('.', index_symbol)
        if -1 < index_dot > index_symbol + 1:
            return True
    return False

