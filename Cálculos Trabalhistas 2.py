def adicionais(sal, tipo=("p", "i1", "i2", "i3")):
    tipo = tipo
    if tipo == "i1":
        adicional = sal / 100 * 10
    elif tipo == "i2":
        adicional = sal / 100 * 20
    elif tipo == "i3":
        adicional = sal / 100 * 40
    elif tipo == "p":
        adicional = sal / 100 * 30
    return adicional


def hora_extra(quantas, valor_hora, valor_horanoturna, qual=("0", "1", "2", "3", "4")):
    """
    Horas extras normais[0], hora extra noturna[1], hora notura[2],
    hora extra domingo e feriados[3], hora extra domingo e feriados noturno[4]
    """

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

def faltas(horas, salario_bruto, dias_q_faltou, carga_horaria):
    preco_falta = (salario_bruto/220) * horas
    
    if dias_q_faltou != 0:
        for i in range(dias_q_faltou):
            falta_dsr = (salario_bruto/220) * carga_horaria
    else:
        falta_dsr = 0.
    
    total = preco_falta + falta_dsr

    return total


def dsr(dia_uteis, domingos_feriado, quantidade_de_horas_extras=(), horas_extras=()):
    dsrs1 = 0.
    dsrs2 = 0.
    dsrs3 = 0.
    dsrs4 = 0.
    dsrs5 = 0.

    if horas_extra_1 != 0:
        dsrs1 = (quantidade_de_horas_extras[0] / dia_uteis) * \
            (horas_extras[0] / quantidade_de_horas_extras[0]) * domingos_feriado

    if horas_extra_2 != 0:
        dsrs2 = (quantidade_de_horas_extras[1] / dia_uteis) * \
            (horas_extras[1] / quantidade_de_horas_extras[1]) * domingos_feriado

    if horas_extra_3 != 0:
        dsrs3 = (quantidade_de_horas_extras[2] / dia_uteis) * \
            (horas_extras[2] / quantidade_de_horas_extras[2]) * domingos_feriado

    if horas_extra_4 != 0:
        dsrs4 = (quantidade_de_horas_extras[3] / dia_uteis) * \
            (horas_extras[3] / quantidade_de_horas_extras[3]) * domingos_feriado

    if horas_extra_5 != 0:
        dsrs5 = (quantidade_de_horas_extras[4] / dia_uteis) * \
            (horas_extras[4] / quantidade_de_horas_extras[4]) * domingos_feriado

    dsrs = [dsrs1, dsrs2, dsrs3, dsrs4, dsrs5]
    return dsrs


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
    elif salario > 6101.06:
        inss = 713.09
    return inss


def irrf(valor, dependentes, pensao, previdencia):
    
    deducao = 189.59 * dependentes
    
    valor = valor - deducao - pensao - previdencia
    
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


print("Digite o valor do salário: ")
salario = float(input('> '))

print("Digite o valor da carga horária diária, para contar o desconto em faltas: ")
carga = float(input("> "))

print("Qual adicional ele recebe: ")
qual_adicional = input("> ")

adicional_valor = adicionais(salario, qual_adicional)

salario_adicional = salario + adicional_valor

valor_da_hora = salario_adicional / 220
valor_hora_noturna = valor_da_hora * 1.14

print("Trabalhou horas extras normais[0], hora extra noturna[1], hora notura[2],\
      hora extra domingo e feriados[3], hora extra domingo e feriados noturno[4]\
      ? [0/1/2/3/4]")
tipo_1 = input("> ")
print("Trabalhou quantas horas extras? ")
quantidade_de_horas_extras1 = float(input("> "))
horas_extra_1 = hora_extra(quantidade_de_horas_extras1, valor_da_hora, 
                           valor_hora_noturna, tipo_1)

print("Trabalhou horas extras normais[0], hora extra noturna[1], hora notura[2],\
      hora extra domingo e feriados[3], hora extra domingo e feriados noturno[4]\
      ? [0/1/2/3/4]")
tipo_2 = input("> ")
print("Trabalhou quantas horas extras? ")
quantidade_de_horas_extras2 = float(input("> "))
horas_extra_2 = hora_extra(quantidade_de_horas_extras2, valor_da_hora, 
                           valor_hora_noturna, tipo_2)

print("Trabalhou horas extras normais[0], hora extra noturna[1], hora notura[2],\
      hora extra domingo e feriados[3], hora extra domingo e feriados noturno[4]\
      ? [0/1/2/3/4]")
tipo_3 = input("> ")
print("Trabalhou quantas horas extras? ")
quantidade_de_horas_extras3 = float(input("> "))
horas_extra_3 = hora_extra(quantidade_de_horas_extras3, valor_da_hora, 
                           valor_hora_noturna, tipo_3)

print("Trabalhou horas extras normais[0], hora extra noturna[1], hora notura[2],\
      hora extra domingo e feriados[3], hora extra domingo e feriados noturno[4]\
      ? [0/1/2/3/4]")
tipo_4 = input("> ")
print("Trabalhou quantas horas extras? ")
quantidade_de_horas_extras4 = float(input("> "))
horas_extra_4 = hora_extra(quantidade_de_horas_extras4, valor_da_hora, 
                           valor_hora_noturna, tipo_4)

print("Trabalhou horas extras normais[0], hora extra noturna[1], hora notura[2],\
      hora extra domingo e feriados[3], hora extra domingo e feriados noturno[4]\
      ? [0/1/2/3/4]")
tipo_5 = input("> ")
print("Trabalhou quantas horas extras? ")
quantidade_de_horas_extras5 = float(input("> "))
horas_extra_5 = hora_extra(quantidade_de_horas_extras5, valor_da_hora, 
                           valor_hora_noturna,tipo_5)

salario_adicional_mais_hora_extra = salario_adicional + horas_extra_1 + \
    horas_extra_2 + horas_extra_3 + horas_extra_4 + horas_extra_5

print("Quantos dias úteis houve nesse mês: ")
dias_uteis = int(input("> "))
print("Quantos domingos e feriados houve nesse mês: ")
domingos_feriados = int(input("> "))

print("Faltou quantas horas? ")
horas_faltadas = float(input("> "))
print("Faltou quantos dias? ")
dias_faltados = int(input("> "))
print("Possui quantos dependentes? ")
dependets = float(input("> "))
print("Paga quantos reais de pensão? ")
pens = float(input("> "))
print("Paga quantos reais de previdência? ")
previ = float(input("> "))

valor_falta = faltas(horas_faltadas, salario_adicional, dias_faltados, carga)

domingos_feriados = domingos_feriados - dias_faltados

dsr1, dsr2, dsr3, dsr4, dsr5 = dsr(dias_uteis,domingos_feriados,
                                   (quantidade_de_horas_extras1, 
                                    quantidade_de_horas_extras2, 
                                    quantidade_de_horas_extras3,
                                    quantidade_de_horas_extras4,
                                    quantidade_de_horas_extras5),
                                   (horas_extra_1, horas_extra_2,
                                    horas_extra_3, horas_extra_4,
                                    horas_extra_5)
                                   )

total_proventos = salario_adicional_mais_hora_extra + \
    dsr1 + dsr2 + dsr3 + dsr4 + dsr5

total_proventos_menos_faltas = total_proventos - valor_falta

inss = inss(total_proventos_menos_faltas)

total_proventos_menos_faltas_menos_inss = total_proventos_menos_faltas - inss

irrf = irrf(total_proventos_menos_faltas_menos_inss,dependets, pens, previ)

salario_liquido = total_proventos_menos_faltas_menos_inss - irrf

print(f"Salário: R$ {salario:.2f}")
print(f"Adicional: R$ {adicional_valor:.2f}")
print(f"Valor da hora: R$ {valor_da_hora:.2f}")
print(f"Valor da hora noturna: R$ {valor_hora_noturna:.2f}")
print(f"Valor da hora extra 1: R$ {horas_extra_1:.2f}")
print(f"Valor da hora extra 2: R$ {horas_extra_2:.2f}")
print(f"Valor da hora extra 3: R$ {horas_extra_3:.2f}")
print(f"Valor da hora extra 4: R$ {horas_extra_4:.2f}")
print(f"Valor da hora extra 5: R$ {horas_extra_5:.2f}")
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
    f"Total de proventos menos as faltas: R$ {total_proventos_menos_faltas:.2f}")
print(f"Valor do INSS: R$ {inss:.2f}")
print(
    f"Total de proventos menos faltas menos INSS: R$ {total_proventos_menos_faltas_menos_inss:.2f}")
print(f"IRFF: R$ {irrf:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
