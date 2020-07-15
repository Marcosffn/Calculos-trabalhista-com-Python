salario = float(input("Valor do salário: R$ ").replace(",", "."))

horas = 220

# # Cálculo do adicional 1 # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
adicional = input(
    "Recebe insalubridade, periculosidade ou não recebe?[i/p/n] ")

insalubridade = 0.
periculosidade = 0.

if adicional == "i":
    grau = input("Qual o grau de insalubridade?[1/2/3] ")
    if grau == "1":
        insalubridade = salario / 100 * 10
    elif grau == "2":
        insalubridade = salario / 100 * 20
    elif grau == "3":
        insalubridade = salario / 100 * 40
elif adicional == "p":
    periculosidade = salario / 100 * 30
else:
    pass

#  # # # # # # # # # Valor da hora # # # # # # # # # # # # # # # # # # # # # # # # # #

valor_hora = (salario + periculosidade + insalubridade) / horas
valor_hora_noturna = valor_hora * 1.14

# ! # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
valor_hora_extra1 = 0.
valor_hora_extra2 = 0.
quanto = 0.

trabalhou_extra = input(
    "Trabalhou horas extras ou seu turno é noturno? [s/n] ")

if trabalhou_extra == "s":
    qual = input(
        "Trabalhou horas extras normais[0], hora extra noturna[1], hora notura[2], hora extra domingo e feriados[3], hora extra domingo e feriados noturno[4]? [0/1/2/3/4] ")
    if qual == "0":
        quanto = float(input("Trabalhou quantas horas extras normais? "))
        valor_hora_extra1 = valor_hora * 1.5 * quanto

    elif qual == "1":
        quanto = float(input("Trabalhou quantas horas extras noturnas? "))
        valor_hora_extra1 = (valor_hora_noturna * 1.5) * 1.2 * quanto

    elif qual == "2":
        quanto = float(input("Trabalhou quantas horas noturnas? "))
        valor_hora_extra1 = valor_hora_noturna * 1.2 * quanto

    elif qual == "3":
        quanto = float(
            input("Trabalhou quantas horas extras nos domingos ou feriados? "))
        valor_hora_extra1 = valor_hora * 2 * quanto

    elif qual == "4":
        quanto = float(
            input("Trabalhou quantas horas extras noturnas nos domingos ou feriados? "))
        valor_hora_extra1 = (valor_hora_noturna * 2) * 1.2 * quanto

    else:
        pass
else:
    pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
quanto1 = 0.

trabalhou_extra = input(
    "Trabalhou horas extras ou seu turno é noturno? [s/n] ")

if trabalhou_extra == "s":
    qual1 = input(
        "Trabalhou horas extras normais[0], hora extra noturna[1], hora notura[2], hora extra domingo e feriados[3], hora extra domingo e feriados noturno[4]? [0/1/2/3/4] ")
    if qual1 == "0":
        quanto1 = float(input("Trabalhou quantas horas extras normais? "))
        valor_hora_extra2 = valor_hora * 1.5 * quanto1

    elif qual1 == "1":
        quanto1 = float(input("Trabalhou quantas horas extras noturnas? "))
        valor_hora_extra2 = (valor_hora * 1.5) * 1.2 * quanto1

    elif qual1 == "2":
        quanto1 = float(input("Trabalhou quantas horas noturnas? "))
        valor_hora_extra2 = valor_hora * 1.2 * quanto1

    elif qual1 == "3":
        quanto1 = float(
            input("Trabalhou quantas horas extras nos domingos ou feriados? "))
        valor_hora_extra2 = valor_hora * 2 * quanto1

    elif qual1 == "4":
        quanto1 = float(
            input("Trabalhou quantas horas extras noturnas nos domingos ou feriados? "))
        valor_hora_extra2 = (valor_hora * 2) * 1.2 * quanto1

    else:
        pass
else:
    pass

quanto2 = 0.

trabalhou_extra = input(
    "Trabalhou horas extras ou seu turno é noturno? [s/n] ")

valor_hora_extra3 = 0.

if trabalhou_extra == "s":
    qual2 = input(
        "Trabalhou horas extras normais[0], hora extra noturna[1], hora notura[2], hora extra domingo e feriados[3], hora extra domingo e feriados noturno[4]? [0/1/2/3/4] ")
    if qual2 == "0":
        quanto2 = float(input("Trabalhou quantas horas extras normais? "))
        valor_hora_extra3 = valor_hora * 1.5 * quanto2

    elif qual2 == "1":
        quanto2 = float(input("Trabalhou quantas horas extras noturnas? "))
        valor_hora_extra3 = (valor_hora * 1.5) * 1.2 * quanto2

    elif qual2 == "2":
        quanto1 = float(input("Trabalhou quantas horas noturnas? "))
        valor_hora_extra3 = valor_hora * 1.2 * quanto2

    elif qual2 == "3":
        quanto2 = float(
            input("Trabalhou quantas horas extras nos domingos ou feriados? "))
        valor_hora_extra3 = valor_hora * 2 * quanto2

    elif qual2 == "4":
        quanto2 = float(
            input("Trabalhou quantas horas extras noturnas nos domingos ou feriados? "))
        valor_hora_extra3 = (valor_hora * 2) * 1.2 * quanto2

    else:
        pass
else:
    pass
# ! # # # # # # # # Cálculo do DSR # # # # # # # # # # # # # # # # # # # # # # # # # # #
dsr = 0.
dsr1 = 0.
dsr2 = 0.
dias_uteis = int(input("Quantos dias úteis tem o mês? "))

domingos_feriados = int(input("Quantos domingos e feriados tem o mês? "))

if valor_hora_extra1 != 0:
    dsr = (quanto / dias_uteis) * domingos_feriados * \
        (valor_hora_extra1 / quanto)
else:
    pass

if valor_hora_extra2 != 0:
    dsr1 = (quanto1 / dias_uteis) * \
        (valor_hora_extra2 / quanto1) * domingos_feriados
else:
    pass
if valor_hora_extra3 != 0:
    dsr2 = (quanto2/dias_uteis) * \
        (valor_hora_extra3/quanto2) * domingos_feriados
else:
    pass

# * # # # # # # # # # # # #Total de proventos # # # # # # # # # # # # # # # # # # # # #

total_proventos = salario + periculosidade + \
    insalubridade + dsr + dsr1 + dsr2 + valor_hora_extra1 + \
    valor_hora_extra2 + valor_hora_extra3

# * # # # # # # # # # # # Interface # # # # # # # # # # # # # # # # # # # # # # # # # #
print("\n")
print(f"Salário: R$ {salario:.2f}")
print(f"Valor da hora: R$ {valor_hora:.2f}")
print(f"Valor da hora noturna: R$ {valor_hora_noturna:.2f}")
print(f"Insalubridade: R$ {insalubridade:.2f}")
print(f"Periculosidade: R$ {periculosidade:.2f}")
print(f"Valor das horas extras 1: R$ {valor_hora_extra1:.2f}")
print(f"Valor das horas extras 2: R$ {valor_hora_extra2:.2f}")
print(f"Valor das horas extras 3: R$ {valor_hora_extra3:.2f}")
print(
    f"Valor hora extra 1, 2 e 3: R$ {(valor_hora_extra1+valor_hora_extra2+valor_hora_extra3):.2f}")
print(f"Descanso semanal remunerado 1: R$ {dsr:.2f}")
print(f"Descanso semanal remunerado 2: R$ {dsr1:.2f}")
print(f"Descanso semanal remunerado 3: R$ {dsr2:.2f}")
print(f"Descanso semanal remunerado 1, 2 e 3: R$ {(dsr+dsr1+dsr2):.2f}")
print(f"Total de proventos: R$ {total_proventos:.2f}")
