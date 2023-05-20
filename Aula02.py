#iniciando comandos condicionais(if/else) condições 
#x=float(input('Digite um numero: '));
#o=input("Digite aqui uma operação: ")
#y=float(input('Digite outro numero: '));
#if (y == 0):
#    print('não é possivel dividir por zero')
#else:
 # print(x/y);




nota=float(input('Nota '));
faltas=float(input('Percentual de presença '));

if (nota>=7 and faltas>=75):
  print('Aluno Aprovado');

elif(nota<7 and faltas>=75):
  print('Aluno reporvado por nota e aprovado por presença');
elif (nota>=7 and faltas <75):
  print('Aluno aprovado por nota e reprovado por faltas')
else:
  print('Aluno Reprovado');


x=(input("Olá usuario,onde você está, escolha as opções, a= casa, b=faculdade, c=biblioteca, d=pagode, e=nenhuma dessas "));
if x==("a"):
  print("legal então você está descansando");

elif x==("b") or x==("c"):
  print("Então você está estudando");

elif x==("d"):
  print("você é bailarino");

elif x==("e"):
   print('me diga onde andas, que direi quem és');

else:
  print("reponda corretamente as alternativas");
  
  
  
  





 
  