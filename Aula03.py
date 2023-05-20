
renda=float(input("Qual e a sua renda? R$"))
duvida=input("Teria mais algum desconto? sim ou nao ")

if duvida.lower() == "sim":
  desconto2 = float(input("Qual seria o valor do desconto? R$ "))

elif (duvida.lower() =="nao"):
  desconto2=0
else:
  desconto2= float(input("Digite um valor valido"))


rendafinal=renda-desconto2

if rendafinal >= 0 and rendafinal <= 2000.00:
  print("Você está isento do imposto de renda, e seu salário é" ,rendafinal);

elif (rendafinal >=2000.01 and rendafinal <=3000.00):
  print("A porcentagem referente ao seu salario é de 8%")
  desconto=rendafinal *0.08
  print("O valor de imposto descontado é", desconto);
  print("Salario com o desconto é ", rendafinal-desconto)

elif (rendafinal >=3000.01 and rendafinal <=4500.00):
  print("A porcentagem referente ao seu salário é de 18% ")
  desconto=rendafinal*0.18
  print("O valor de imposto descontado é",desconto)
  print("Salario com o desconto é ", rendafinal-desconto)

elif(renda >=4500):
  print("A porcentagem referente ao seu salário é de 28%")
  desconto=rendafinal*0.28
  print("O valor de imposto descontado é", desconto);
  print("Salario com o desconto é ", renda-desconto);
  
else:
  rendafinal<0
  print("Sinto muito você ficou é devendo ", rendafinal)


'''
rec=input("Gostaria de tentar novamente? sim ou não" )

if rec.lower()=="nao" "não":
  print("Ok até mais...")
elif rec.lower()=="sim":
  n=1
  while 1:
    renda=float(input("Qual e a sua renda? R$"))
'''    






  
  







  
  
  
  

  
  


  
  
  