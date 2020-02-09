def tres_recursiones(k):
    if(k>0):
        resultado = k + tres_recursiones(k-1)
        print(resultado)
    else:
        resultado = 0
    return resultado
    
print("\n\nRecursion")
tres_recursiones(6)
