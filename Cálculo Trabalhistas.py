# -*- coding: UTF-8 -*-
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
valor_hora_extra2 = 0.

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
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
quanto2 = 0.
valor_hora_extra3 = 0.

trabalhou_extra = input(
    "Trabalhou horas extras ou seu turno é noturno? [s/n] ")

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
        quanto2 = float(input("Trabalhou quantas horas noturnas? "))
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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
quanto3 = 0.
valor_hora_extra4 = 0.

trabalhou_extra = input(
    "Trabalhou horas extras ou seu turno é noturno? [s/n] ")

if trabalhou_extra == "s":
    qual3 = input(
        "Trabalhou horas extras normais[0], hora extra noturna[1], hora notura[2], hora extra domingo e feriados[3], hora extra domingo e feriados noturno[4]? [0/1/2/3/4] ")
    if qual3 == "0":
        quanto3 = float(input("Trabalhou quantas horas extras normais? "))
        valor_hora_extra4 = valor_hora * 1.5 * quanto3

    elif qual3 == "1":
        quanto3 = float(input("Trabalhou quantas horas extras noturnas? "))
        valor_hora_extra4 = (valor_hora * 1.5) * 1.2 * quanto3

    elif qual3 == "2":
        quanto3 = float(input("Trabalhou quantas horas noturnas? "))
        valor_hora_extra4 = valor_hora * 1.2 * quanto3

    elif qual3 == "3":
        quanto3 = float(
            input("Trabalhou quantas horas extras nos domingos ou feriados? "))
        valor_hora_extra4 = valor_hora * 2 * quanto3

    elif qual3 == "4":
        quanto3 = float(
            input("Trabalhou quantas horas extras noturnas nos domingos ou feriados? "))
        valor_hora_extra4 = (valor_hora * 2) * 1.2 * quanto3

    else:
        pass
else:
    pass
# ! # # # # # # # # Cálculo do DSR # # # # # # # # # # # # # # # # # # # # # #
dsr = 0.
dsr1 = 0.
dsr2 = 0.
dsr3 = 0.
## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
falta_dias = 0
falta_horas = 0.
falta_valor = 0.
falta_valor_dsr = 0.

faltou = input("Houve alguma falta?[s/n] ")

if faltou == "s":
    falta_dias = int(input("Faltou quantos dias? "))
    falta_horas = float(input("Faltou por quantas horas? "))
    falta_valor = salario / horas * falta_horas
else:
    pass
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
dias_uteis = int(input("Quantos dias úteis tem o mês? "))
domingos_feriados = int(input("Quantos domingos e feriados tem o mês? "))

domingos_feriados -= falta_dias

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
    dsr2 = (quanto2 / dias_uteis) * \
        (valor_hora_extra3 / quanto2) * domingos_feriados
else:
    pass
if valor_hora_extra4 != 0:
    dsr3 = (quanto3 / dias_uteis) * \
        (valor_hora_extra4 / quanto2) * domingos_feriados
else:
    pass

# * # # # # # # # # # # # #Total de proventos # # # # # # # # # # # # # # # # # # # # #

total_proventos = salario + periculosidade + \
    insalubridade + dsr + dsr1 + dsr2 + dsr3 + valor_hora_extra1 + \
    valor_hora_extra2 + valor_hora_extra3

total_proventos_menos_faltas = total_proventos - \
    (falta_valor + falta_valor_dsr)

# # # # # # # # # # # # # # # # # # # # INSS # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
aliquota1 = 0.075
aliquota2 = 0.09
aliquota3 = 0.12
aliquota4 = 0.14

limite1 = 1045.00
limite2 = 2089.60
limite3 = 3134.40
limite4 = 6101.06
inss = 0.

faixa1 = limite1 * aliquota1
faixa2 = (limite2 - (limite1 + 0.01)) * aliquota2
faixa3 = (limite3 - (limite2 + 0.01)) * aliquota3
faixa4 = (limite4 - (limite3 + 0.1)) * aliquota4

valor_residual = 0.

if salario <= limite1:
    valor_residual = 0.
    inss = total_proventos_menos_faltas * aliquota1

elif salario <= limite2 and total_proventos_menos_faltas > limite1:
    valor_residual = 0.
    valor_residual = (total_proventos_menos_faltas - limite1) * aliquota2
    inss = faixa1 + valor_residual

elif salario <= limite3 and total_proventos_menos_faltas > limite2:
    valor_residual = 0.
    valor_residual = (total_proventos_menos_faltas - limite2) * aliquota3
    inss = valor_residual + faixa1 + faixa2

elif salario <= limite4 and total_proventos_menos_faltas > limite3:
    valor_residual = 0.
    valor_residual = (total_proventos_menos_faltas - limite3) * aliquota4
    inss = faixa1 + faixa2 + faixa3 + valor_residual
else:
    pass
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# * # # # # # # # # # # # Interface # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
print("\n")
print(f"Salário: R$ {salario:.2f}")
print(f"Valor da hora: R$ {valor_hora:.2f}")
print(f"Valor da hora noturna: R$ {valor_hora_noturna:.2f}")
print(f"Insalubridade: R$ {insalubridade:.2f}")
print(f"Periculosidade: R$ {periculosidade:.2f}")
print(f"Valor das horas extras 1: R$ {valor_hora_extra1:.2f}")
print(f"Valor das horas extras 2: R$ {valor_hora_extra2:.2f}")
print(f"Valor das horas extras 3: R$ {valor_hora_extra3:.2f}")
print(f"Valor das horas extras 4: R$ {valor_hora_extra4:.2f}")
print(
    f"Valor hora extra 1, 2, 3 e 4: R$ {(valor_hora_extra1 + valor_hora_extra2 + valor_hora_extra3 + valor_hora_extra4): .2f}")
print(f"Descanso semanal remunerado 1: R$ {dsr:.2f}")
print(f"Descanso semanal remunerado 2: R$ {dsr1:.2f}")
print(f"Descanso semanal remunerado 3: R$ {dsr2:.2f}")
print(f"Descanso semanal remunerado 4: R$ {dsr3:.2f}")
print(
    f"Descanso semanal remunerado 1, 2, 3 e 4: R$ {(dsr+dsr1+dsr2+dsr3):.2f}")
print(f"Total de proventos: R$ {total_proventos:.2f}")
print(f"Valor das horas faltadas: R$ {falta_valor:.2f}")
print(f"Valor da DSR das horas faltadas: R$ {falta_valor_dsr:.2f}")
print(
    f"Total de desconto por ter faltado: R$ {falta_valor+falta_valor_dsr:.2f}")
print(f"Salário pré-líquido: R$ {total_proventos_menos_faltas:.2f}")
print(f"Valor do desconto do INSS: R$ {inss:.2f}")
print(f"Salário líquido: R$ {total_proventos_menos_faltas - inss:.2f}")
