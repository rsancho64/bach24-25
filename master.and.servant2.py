INCREMENTA = 1
DOBLA = 2

def operacion(dato, op = INCREMENTA):
    print(f"srv: recibido: {dato} y {op}")
    if op == INCREMENTA:
        return dato + 1
    if op == DOBLA:
        return dato * 2

def cli():
    print("cli: begin")

    retorno = operacion(22,INCREMENTA)   
    print(f"cli: recibido: {retorno}")
    
    retorno = operacion(33,DOBLA)
    print(f"cli: recibido: {retorno}")

    print("cli: end")

# main --------------------------------
cli()

