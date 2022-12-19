# Cvicenia z labakov.
# Den - 11.11.2022 ; Skupina - II

# +++> Info:
#
# - V pythone definovanie viacerych variabilit SUCASNE je
#   totalne jednoduche. Pre oddelenie staci na oboch stranach
#   pouzit ',' separator.
#   @ Priklad:
#       a, b = 22667121, "Foo"
#       ( Do variability 'a' sme vlozili integer 22667121 a do 'b' String "Foo". )
#
# - Pokial chceme do variability zadefinovat xy argumentov
#   mozeme pouzit "*arg" parameter. Data budu vo variabilite
#   v liste.
#   @ Priklad:
#       a, *b = 2423, 4232, "Foo", "Bar", 43923
#       ( Do variability 'a' sa vlozi iba int 2423, ostatne data si pozbiera variabilita 'b' )

# ++ Zadanie k prvemu cviceniu:
#   Napis program, ktory prehodi hodnoty
#   dvoch variabilit.
# ++ Obmedzenia:
#   Keep it simple, Jakub, Jakub!

# Mozne riesenie:
def prve_cvicenie():

    a = 4239
    b = 12
    a, b = b, a

    return print(f"Prehodene hodnoty: \n a = {a} \n b = {b}")

prve_cvicenie()

# ++ Zadanie k druehmu cviceniu:
#    Napis parser s prikazmi: print / plus / minus
#    + print: vypise kazdy argument za prikazom.
#    + plus: scita vsetkych n argumentov.
#    + minus: odcita vsetky argumenty od prveho

# Mozne riesenie:
def druhe_cvicenie():

    def are_integers(arr) -> bool:
        try:
            [int(i) for i in arr]
            return True
        except ValueError:
            return False

    while True:

        cmd_args = input("> ").split()
        while len(cmd_args) < 1: cmd_args = input("> ").split()

        main_arg, *args = cmd_args
        match main_arg:

            case "print":
                if len(args) != 0: print( " ".join(args) )
                else: print("++ Few arguments provided.")

            case "plus" | "+":
                # Filip, nie, NECHCE sa mi robit to cez if elif
                if not are_integers(args): print("++ Expected integers."); continue

                numbers = [int(i) for i in args]
                print(sum(numbers))

            case "minus" | "-":
                # Filip, nie, NECHCE sa mi robit to cez if elif
                if len(args) < 2: print("++ Few arguments provided."); continue
                if not are_integers(args): print("++ Expected integers."); continue

                numbers = [int(i) for i in args]
                print(numbers[0] - sum(numbers[1:]))

            case "nasobenie" | "*":
                if len(args) < 2: print("++ Few arguments provided."); continue
                if not are_integers(args): print("++ Expected integers."); continue

                numbers = [int(i) for i in args]
                cinitel = numbers[0]
                for nasobok in numbers[1:]:
                    cinitel *= nasobok

            case "delenie" | "/":
                if len(args) < 2: print("++ Few arguments provided."); continue
                if not are_integers(args): print("++ Expected integers."); continue

                numbers = [int(i) for i in args]
                delenec = numbers[0]
                for delitel in numbers[1:]:
                    if delitel == 0: print("++ Division by zero is not possible."); break
                    delenec /= delitel
                else: print(round(delenec, 2))

            case "faktorial" | "!":
                if len(args) != 1: print("++ Expected 1 argument."); continue
                if not are_integers(args): print("++ Expected integer."); continue

                cislo = odpoved = int(args[0])
                for i in range(1, cislo-1):
                    odpoved *= cislo-i
                print(odpoved)

            case "stop": return

            case "help" | 'h' | "?":
                print("++ Currently available commands: \n"
                      "print [value(s)] \n"
                      "plus [int], ..., \n"
                      "minus [int], ..., \n"
                      "nasobenie [int], ..., \n"
                      "delenie [int], ... \n"
                      "factorial [int]\n"
                      "stop\n"
                      "help")

            case _: print( f"++ Invalid command. \n Command: {main_arg}" )

druhe_cvicenie()
