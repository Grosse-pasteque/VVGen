from .constants import function

# type checking function
def check_type(config: dict, raiseerror=True):
    if isinstance(config, dict) and isinstance(raiseerror, bool):
        for key in list(config.keys()):
            if str(type(key)) not in str(config[key]):
                if raiseerror:
                    raise TypeError(
                        "{} need to be {}".format(key, str(config[key]).replace("<class '", '').replace("'>", '')))
                return False
        return True
    raise TypeError(
        f"type(config={config}) need to be dict")


# function to make error raising easier
def line_number_error(error):
    return error.__traceback__.tb_lineno

def line_text_error(error, file):
    with open(file, 'r') as f: lines = f.readlines()
    return lines[line_number_error(error) - 1].replace('\n', '').replace(' '*4, '')

def basic_error_message(error, file):
    return f'''\n  File "{file}", line {line_number_error(error)}\n  \t{line_text_error(error, file)}'''