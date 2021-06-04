# Virtual Variables Generator {VVGen - XGen} [0.4.0]    -    By 'Grosse pastèque#6705'
"""Free program used for Multiple Variable Generation (MVG)
You can share this program to whoever you want but don't use it for economics purposes.

Example of how this script can be used for :

    Import project as XGen
    >>> import VVGen

    Define main class method with the virtual file used (create it if doesn't exist)
    >>> VV_main = XGen.VirtualVariable('virtual_file.py')

    Create our first unique variable
    >>> VV_main.create_variable("a_variable", 6, True)

    Create 3 variables with a value = 6
    >>> VV_main.create_many_variables("this_variable_will_be_multiple", 6, 3)

    delete the variable variation 1 or the variable 'this_variable_will_be_multiple' that have the value 6
    >>> VV_main.delete_variable("this_variable_will_be_multiple_1", 6)

    Write a simple script into the virtual variable file and 'auto_run' it (True)
    >>> my_script = '''this_variable_will_be_multiple_2 *= 2\nprint(f'here is a virtual script {this_variable_will_be_multiple_2}')\n'''
    >>> VV_main.write_virtual_script(my_script, auto_run=True)

    Print the content of the Virtual Variables file
    >>> print(VV_main.read_virtual_file())

    Import our virtual variables file
    >>> import virtual_file

    And print the value of 'a_variable' to be sure that it worked
    >>> print(a_variable)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    finnaly we will get :
        The 'auto_run' of our script:   " here is a virtual script 12"


        Our Unique variable:            a_variable = 6
        Our multiple variables:         this_variable_will_be_multiple_0 = 6
                                        this_variable_will_be_multiple_2 = 6

        Our script:                     this_variable_will_be_multiple_2 *= 2
                                        print(f' here is a virtual script {this_variable_will_be_multiple_2}')

        And finaly our import:          6 (is the variable 'a_variable' printed)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WARNING :   The optmization isn't perfect be patient for updates thanks !
            Changes mite arrives soon...
"""
from .UUF import *

# main class
class VirtualVariable:
    # main method
    def __init__(self, **kwargs):
        for key in kwargs:
            if key not in ['save', 'file', 'mode', 'reset']:
                raise AttributeError(
                    f"{key} not valid, valid keys are: save, file, mode, reset.")
        
        if check_type({kwargs['file']: str}):
            self.save = kwargs['save']
            if self.save:
                if check_type({kwargs['file']: str, kwargs['mode']: str, kwargs['reset']: bool}):
                    self.file = kwargs['file']
                    self.mode = kwargs['mode']
                    self.reset = kwargs['reset']

                    if self.reset:
                        with open(self.file, 'w') as f: f.close()

        self.VV_data = {
            'variables': {},
            'scripts': {}
        }            

    # reading VV_data
    def __getitem__(self, item):
        if item == 'all': return self.VV_data
        elif item in ['variables', 'scripts']: return self.VV_data[item]
        return False

    # saving file function
    def vsave(self):
        try: 
            with open(self.file, self.mode) as f: f.write(f"save = {self.VV_data}")
            return True
        except: return False

    # resetting variables file
    def vreset(self, mode):
        if check_type({mode: str}):
            if mode in ['file', 'variables', 'scripts', 'all']:
                if mode == 'file':              
                    try:
                        with open(self.file, 'w') as f: f.close()
                        return True
                    except: return False
                elif mode == 'all': self.VV_data.clear()
                else: self.VV_data[mode].clear()
                return True
            return False

    # create variable function
    def create_variable(self, variable_name: str, variable_value: allt, return_var=False):
        if check_type({variable_name: str, return_var: bool}):
            self.VV_data['variables'][variable_name] = variable_value
            if return_var: return True, variable_name, variable_value
            return True

    # create many variables function
    def create_many_variables(self, variables_names: list, variables_values: list):
        if isinstance(variables_names, list) and isinstance(variables_values, list):
            if len(variables_names) == len(variables_values):
                for key, value in enumerate(variables_names, 0):  # variables numbers
                    try: self.create_variable(value, variables_values[key])
                    except: return False
            else:
                raise LenghtError(
                    "len(variables_names) need to be == to len(variables_values) !")

    # delete variable
    def delete_variable(self, variable_name: str):
        if variable_name in list(self.VV_data['variables'].keys()):
            if check_type({variable_name: str}):
                self.VV_data['variables'].pop(variable_name)
                return True
        return False

    # change variable
    def change_variable(self, variable_name: str, new_value: allt, new_variable_name='current'):
        if check_type({variable_name: str, new_variable_name: str}):
            if new_variable_name == 'current': new_variable_name = variable_name
            self.delete_variable(variable_name)
            self.create_variable(new_variable_name, new_value)
            return True

    # custom script writing
    def write_virtual_script(self, script_name: str, script: str):
        if check_type({script_name: str, script: str}):
            self.VV_data['scripts'][script_name] = script
            return True