OK = True

def srv(dato, control=OK):
    print(f"srv: recibido: {dato}")
    return OK

def cli():
    print("cli: begin")
    srv(22)   
    srv(33)
    print("cli: end")

# main --------------------------------
cli()

