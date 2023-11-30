import dis

def print_names_from_pyc(pyc_file):
    with open(pyc_file, 'rb') as f:
        code = f.read()
        bytecode = dis.Bytecode(code)
        names = {i.argval for i in bytecode if isinstance(i.argval, str) and not i.argval.startswith('__')}
        for name in sorted(names):
            print(name)

# Replace 'hidden_4.pyc' with the actual path to your downloaded file
print_names_from_pyc('hidden_4.pyc')
