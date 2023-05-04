salario = float(input("Digite seu salario R$: "))
inss = 0
irpf = 0
resultado = 0
calculoInss = 0
calculoIrpf = 0

if salario <= 1200.00:
    inss = 0.08
    irpf = 0.08
   
elif salario <= 1800:
    inss = 0.09
    irpf = 0.09
else:
    inss = 0.12
    irpf = 0.12
impostoInss = round(salario * inss,2)
calculoInss = round(salario - salario * inss,2)
salario2 = calculoInss
calculoIrpf = round(salario2 * irpf,2)
resultado = round(salario2 -(salario * irpf),2)

print("Seu imposto do Inss é de R$:",impostoInss)
print("........................................")
print("Seu salario depois no Inss é de R$:",salario2)
print("........................................")
print("Seu imposto do IRPF é de R$:",calculoIrpf)
print("........................................")
print("Seu salario liquido é de R$:",resultado)