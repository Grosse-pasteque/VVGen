import VVGen

VV_main = VVGen.VirtualVariable(save=True, file='datatest.py', mode='a', reset=True)

print(VV_main.create_variable("a_variable", 6, return_var=True))
print(VV_main.create_many_variables(['hey', 'test'], [8, 'test 1212']))
print(VV_main.delete_variable('test'))
print(VV_main.change_variable('hey', 10))

script = "print('hey boiiiiiii !')"
print(VV_main.write_virtual_script('test', script))

print('_'*100)
VV_data = VV_main['all']
print(VV_data)
print(globals())
print('_'*100)

print(VV_main.vsave())
print(VV_main.vreset('variables'))
print(VV_main['variables'])