def detect_palindrome(str):
    """
    funcion que itera sobre la mitad de la palabra, comparando caracteres desde ambos extremos hacia el centro. 
    Si encuentra al menos una diferencia, la funcion devuelve False, indicando que la palabra no es un palindromo. 
    Si no encuentra ninguna diferencia, devuelve True, indicando que la palabra es un palindromo.
    """
    str = str.lower()
    long = len(str)
    for i in range (long//2):
        if str[i] != str[long-1-i]:
            print(f"la palabra {str} no es un palindromo")
            return False
    return True


def check_parentheses(str):
    """
    funcion que verifica el equilibrio de parentesis contando cuantos parentesis de apertura '(' y cuantos de cierre ')' 
    hay en la cadena. Si al final del recorrido hay mas parentesis de cierre que de apertura, imprime un mensaje indicando 
    cuantos parentesis estan desbalanceados y retorna False. Si los parentesis estan balanceados, retorna True.
    """
    balance = 0 
    for character in str:
        if character == '(':
            balance += 1
        elif character == ')':
            balance -= 1
        
    if balance < 0:
        print(f"Parentesis que no estan equilibrados: {abs(balance)}")
        return False
    return balance == 0


def backwards_text(str):
    """
    funcion que toma una cadena de texto, la divide en palabras, invierte el orden de las palabras y luego las concatena 
    nuevamente en una cadena, la cual se devuelve. El metodo rstrip() se utiliza para eliminar el espacio en blanco adicional 
    al final de la cadena invertida.
    """

    words = str.split()
    inverted_text = ''
    for word in reversed(words):
        inverted_text += f"{word} "
    return inverted_text.rstrip()



if __name__ == '__main__':

    print(detect_palindrome("arad"))

    print(check_parentheses("((()))"))

    print(backwards_text("hola leafnoise soy Joaquin Osorio"))