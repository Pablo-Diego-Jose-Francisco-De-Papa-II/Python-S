# Cvicenia z labakov.
# Den - 27.10.2022 ; Skupina - II

# +++> Info:
#
# - V pythone definovanie viacerych variabilit SUCASNE je
#   totalne jednoduche. Pre oddelenie staci na oboch stranach
#   pouzit ',' separator.
#   @ Priklad:
#       a, b = 22667121, "Foo";
#   ( Do variability 'a' sme vlozili integer 22667121 a do 'b' String "Foo". )
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
def prveCvicenie():
    a = 4239
    b = 12
    a, b = b, a

    return print(f"Prehodene hodnoty: \n a = {a} \n b = {b}")


# prveCvicenie()

# ++ Zadanie k druehmu cviceniu:
#    Napis parser s prikazmi: print / plus / minus
#    + print: vypise kazdy argument za prikazom.
#    + plus: scita vsetkych n argumentov.
#    + minus: odcita vsetky argumenty od prveho

# Mozne riesenie:
def druheCvicenie():
    while True:

        cmdArgs = input("> ").split()
        while len(cmdArgs) < 1:
            cmdArgs = input("> ").split()

        mainArg, args = cmdArgs[0], cmdArgs[1:]
        match mainArg:

            case "print":
                if len(args) != 0:
                    print(" ".join(args))
                else:
                    print("++ Few arguments provided.")

            case "plus" | "+":
                # Filip, nie, NECHCE sa mi robit to cez if elif
                try:
                    numbers = [int(i) for i in args]
                    print(sum(numbers))
                except ValueError as error:
                    print(f"++ Expected integers. \n Error: {error}")
                except IndexError as error:
                    print(f"++ Few arguments provided. \n Error: {error}")

            case "minus" | "-":
                # Filip, nie, NECHCE sa mi robit to cez if elif
                try:
                    numbers = [int(i) for i in args]
                    print(numbers[0] - sum(numbers[1:]))
                except ValueError as error:
                    print(f"++ Expected integers. \n Error: {error}")
                except IndexError as error:
                    print(f"++ Few arguments provided. \n Error: {error}")

            case "násobenie" | "*":
                try:
                    numbers = [int(i) for i in args]
                    save = numbers[0]
                    for pozicia in range(len(numbers) - 1):
                        save = save * numbers[pozicia + 1]
                    print(save)
                except ValueError as error:
                    print(f"++ Expected integers. \n Error: {error}")

                except IndexError as error:
                    print(f"++ Few arguments provided. \n Error: {error}")

            case "delenie" | "/":
                try:
                    numbers = [int(i) for i in args]
                    save = numbers[0]
                    for pozicia in numbers[1:]:
                        save /= pozicia
                    print(round(save, 2))
                except ValueError as error:
                    print(f"++ Expected integers. \n Error: {error}")
                except IndexError as error:
                    print(f"++ Few arguments provided. \n Error: {error}")
                except ZeroDivisionError as error:
                    print(f"++ si chuj. \n Error: {error}")

            case "faktorial" | "!":
                try:
                    numbers = [int(i) for i in args]
                    save, unsave = numbers[0], numbers[0]
                    for pozicia in range(unsave - 1):
                        save = save * (unsave - (pozicia + 1))
                    print(save)
                except ValueError as error:
                    print(f"++ Expected integers. \n Error: {error}")



            case "help" | 'h' | "?":
                print("++ Currently available commands: \n"
                      "print [value(s)] \n"
                      "plus [int], ..., \n"
                      "minus [int], ..., \n"
                      "help")

            case _:
                print(f"++ Invalid command. \n Command: {mainArg}")


druheCvicenie()
