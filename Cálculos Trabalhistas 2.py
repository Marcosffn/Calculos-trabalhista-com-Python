print("Digite o valor do salário: ")
salario = float(input('> '))


def adicionais(sal, tipo=("p", "i1", "i2", "i3")):
    tip = tipo
    if tipo == "i1":
        adicional = salario / 100 * 10
    elif tipo == "i2":
        adicional = salario / 100 * 20
    elif tipo == "i3":
        adicional = salario / 100 * 40
    elif tipo == "p":
        adicional = salario / 100 * 30
    return adicional


print("Qual adicional ele recebe: ")
qual_adicional = input("> ")

adicional_valor = adicionais(salario, qual_adicional)

######
salario_adicional = salario + adicional_valor

valor_da_hora = salario_adicional / 220
valor_hora_noturna = valor_da_hora * 1.14


def hora_extra(quantas, qual=("0", "1", "2", "3", "4")):
    """
    Horas extras normais[0], hora extra noturna[1], hora notura[2],
    hora extra domingo e feriados[3], hora extra domingo e feriados noturno[4]
    """

    global valor_da_hora, valor_hora_noturna

    valor_hora = 0

    if qual == "0":
        valor_hora = valor_da_hora * 1.5 * quantas
    elif qual == "1":
        valor_hora = (valor_hora_noturna * 1.5) * 1.2 * quantas
    elif qual == "2":
        valor_hora = valor_hora_noturna * 1.2 * quantas
    elif qual == "3":
        valor_hora = valor_da_hora * 2 * quantas
    elif qual == "4":
        valor_hora = (valor_hora_noturna * 2) * 1.2 * quantas
    return valor_hora


print("Trabalhou quantas horas extras? ")
quantidade_de_horas_extras1 = float(input("> "))
print("Trabalhou horas extras normais[0], hora extra noturna[1], hora notura[2],\
      hora extra domingo e feriados[3], hora extra domingo e feriados noturno[4]\
      ? [0/1/2/3/4]")
tipo_1 = input("> ")
horas_extra_1 = hora_extra(quantidade_de_horas_extras1, tipo_1)

print("Trabalhou quantas horas extras? ")
quantidade_de_horas_extras2 = float(input("> "))
print("Trabalhou horas extras normais[0], hora extra noturna[1], hora notura[2],\
      hora extra domingo e feriados[3], hora extra domingo e feriados noturno[4]\
      ? [0/1/2/3/4]")
tipo_2 = input("> ")
horas_extra_2 = hora_extra(quantidade_de_horas_extras2, tipo_2)

print("Trabalhou quantas horas extras? ")
quantidade_de_horas_extras3 = float(input("> "))
print("Trabalhou horas extras normais[0], hora extra noturna[1], hora notura[2],\
      hora extra domingo e feriados[3], hora extra domingo e feriados noturno[4]\
      ? [0/1/2/3/4]")
tipo_3 = input("> ")
horas_extra_3 = hora_extra(quantidade_de_horas_extras3, tipo_3)

print("Trabalhou quantas horas extras? ")
quantidade_de_horas_extras4 = float(input("> "))
print("Trabalhou horas extras normais[0], hora extra noturna[1], hora notura[2],\
      hora extra domingo e feriados[3], hora extra domingo e feriados noturno[4]\
      ? [0/1/2/3/4]")
tipo_4 = input("> ")
horas_extra_4 = hora_extra(quantidade_de_horas_extras4, tipo_4)

print("Trabalhou quantas horas extras? ")
quantidade_de_horas_extras5 = float(input("> "))
print("Trabalhou horas extras normais[0], hora extra noturna[1], hora notura[2],\
      hora extra domingo e feriados[3], hora extra domingo e feriados noturno[4]\
      ? [0/1/2/3/4]")
tipo_5 = input("> ")
horas_extra_5 = hora_extra(quantidade_de_horas_extras5, tipo_5)


salario_adicional_mais_hora_extra = salario_adicional + horas_extra_1 + \
    horas_extra_2 + horas_extra_3 + horas_extra_4 + horas_extra_5

print("Quantos dias úteis houve nesse mês: ")
dias_uteis = int(input("> "))
print("Quantos domingos e feriados houve nesse mês: ")
domingos_feriados = int(input("> "))


def faltas(horas, dias):

    global domingos_feriados, valor_da_hora

    preco_falta = (salario/220) * horas

    domingos_feriados -= dias
    return preco_falta


print("Faltou quantas horas? ")
horas_faltadas = float(input("> "))
print("Faltou quantos dias? ")
dias_faltados = int(input("> "))
valor_falta = faltas(horas_faltadas, dias_faltados)


def dsr():
    dsrs1 = 0.
    dsrs2 = 0.
    dsrs3 = 0.
    dsrs4 = 0.
    dsrs5 = 0.

    if horas_extra_1 != 0:
        dsrs1 = (quantidade_de_horas_extras1 / dias_uteis) * \
            (horas_extra_1 / quantidade_de_horas_extras1) * domingos_feriados

    if horas_extra_2 != 0:
        dsrs2 = (quantidade_de_horas_extras2 / dias_uteis) * \
            (horas_extra_2 / quantidade_de_horas_extras2) * domingos_feriados

    if horas_extra_3 != 0:
        dsrs3 = (quantidade_de_horas_extras3 / dias_uteis) * \
            (horas_extra_3 / quantidade_de_horas_extras3) * domingos_feriados

    if horas_extra_4 != 0:
        dsrs4 = (quantidade_de_horas_extras4 / dias_uteis) * \
            (horas_extra_4 / quantidade_de_horas_extras4) * domingos_feriados

    if horas_extra_5 != 0:
        dsrs5 = (quantidade_de_horas_extras5 / dias_uteis) * \
            (horas_extra_5 / quantidade_de_horas_extras5) * domingos_feriados

    dsrs = [dsrs1, dsrs2, dsrs3, dsrs4, dsrs5]
    return dsrs


dsr1, dsr2, dsr3, dsr4, dsr5 = dsr()

total_proventos = salario_adicional_mais_hora_extra + \
    dsr1 + dsr2 + dsr3 + dsr4 + dsr5

total_proventos_menos_faltas = total_proventos - valor_falta


def inss(salario):
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
    return inss


inss = inss(total_proventos_menos_faltas)

total_proventos_menos_faltas_menos_inss = total_proventos - inss


def irrf(valor):
    irff = 0.
    if valor <= 1903.98:
        irrf = 0.
    elif valor <= 2826.65 and valor > 1903.99:
        irrf = valor * 0.075 - 142.8
    elif valor <= 3751.05 and valor > 2826.66:
        irrf = valor * 0.15 - 354.8
    elif valor <= 4664.68 and valor > 3751.06:
        irrf = valor * 0.225 - 636.13
    elif valor > 4664.68:
        irrf = valor * 0.275 - 869.36
    return irrf


irrf = irrf(total_proventos_menos_faltas_menos_inss)

salario_liquido = total_proventos_menos_faltas_menos_inss - irrf


print(f"Salário: R$ {salario:.2f}")
print(f"Adicional: R$ {adicional_valor:.2f}")
print(f"Valor da hora: R$ {valor_da_hora:.2f}")
print(f"Valor da hora noturna: R$ {valor_hora_noturna:.2f}")
print(f"Valor da hora extra 1: {horas_extra_1:.2f}")
print(f"Valor da hora extra 2: {horas_extra_2:.2f}")
print(f"Valor da hora extra 3: {horas_extra_3:.2f}")
print(f"Valor da hora extra 4: {horas_extra_4:.2f}")
print(f"Valor da hora extra 5: {horas_extra_5:.2f}")
print(
    f"Total do valor de horas extras: R$ {horas_extra_1 + horas_extra_2 + horas_extra_3 + horas_extra_4 + horas_extra_5: .2f}")
print(f"DSR 1: R$ {dsr1:.2f}")
print(f"DSR 2: R$ {dsr2:.2f}")
print(f"DSR 3: R$ {dsr3:.2f}")
print(f"DSR 4: R$ {dsr4:.2f}")
print(f"DSR 5: R$ {dsr5:.2f}")
print(f"Total de DSR: R$ {dsr1 + dsr2 + dsr3 + dsr4 + dsr5:.2f}")
print(f"Total de proventos: R$ {total_proventos:.2f}")
print(f"Valor das faltas: R$ {valor_falta:.2f}")
print(
    f"Total de proventos menos as faltas: {total_proventos_menos_faltas:.2f}")
print(f"Valor do INSS: {inss:.2f}")
print(
    f"Total de proventos menos faltas menos INSS: R$ {total_proventos_menos_faltas_menos_inss:.2f}")
print(f"IRFF: R$ {irrf:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
