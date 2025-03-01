def arithmetic_arranger(problems, show_answers=False):
    # Controllo del numero massimo di problemi
    if len(problems) > 5:
        return 'Error: Too many problems.'

    arranged_problems = ['']
    # Inizializzazione delle righe
    first_line = ""
    second_line = ""
    dashes = ""
    results = ""

    for problem in problems:
        # Separazione degli elementi del problema
        
        operand1, operator, operand2 = problem.split()
        
        # Validazioni
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calcolo della larghezza del problema
        width = max(len(operand1), len(operand2)) + 2
        top = operand1.rjust(width)
        bottom = operator + " " + operand2.rjust(width - 2)
        line = "-" * width

        # Calcolo del risultato
        if show_answers:
            if operator == "+":
                result = str(int(operand1) + int(operand2)).rjust(width)
            else:
                result = str(int(operand1) - int(operand2)).rjust(width)

        # Aggiornamento delle righe
        first_line += top + "    "
        second_line += bottom + "    "
        dashes += line + "    "
        if show_answers:
            results += result + "    "

    # Rimuovere gli spazi in eccesso alla fine
    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dashes.rstrip()
    if show_answers:
        arranged_problems += "\n" + results.rstrip()

    return arranged_problems

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
