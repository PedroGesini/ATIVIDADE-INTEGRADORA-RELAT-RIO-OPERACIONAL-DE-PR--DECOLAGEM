
#definindo as variaveis iniciais para valores a serem atribuidos

temperatura_interna = 0
temperatura_externa = 0
integridade_estrutural = 0
energia = 0
pressao_tanque = 0
modulos_criticos = 0


#-----------------------------------------------------------------------------------------------------------------------
#importando uma biblioteca (random) que basicamente traz numeros aleatorios
import random

#-----------------------------------------------------------------------------------------------------------------------
#colocando a biblioteca random com o codigo 'randint' para deixar uma randomizaçao de numeros inteiros

temperatura_interna = random.randint(10,30)
temperatura_externa = random.randint(-20,35)
energia = random.randint(50, 100)
pressao_tanque = random.randint(20,60)
integridade_estrutural = random.randint(0,1)
modulos_criticos = random.randint(0,1)

#-----------------------------------------------------------------------------------------------------------------------
#declarando os compontes da aurora como Margem = 0 (para um futuro calculo)

temperatura_interm = 0
temperatura_externam = 0
energiam = 0
pressao_tanquem = 0
integridade_estruturalm = 0
modulos_criticosm = 0


#-----------------------------------------------------------------------------------------------------------------------
#calculando a margem de diferença de quanto falta pro minimo ou quanto passou do minimo/ maximo
temperatura_interm = temperatura_interna - 10
temperatura_externam = temperatura_externa - (-10)
energiam = energia - 60
pressao_tanquem = pressao_tanque - 40
integridade_estruturalm = integridade_estrutural - 1
modulos_criticosm = modulos_criticos - 1


#-----------------------------------------------------------------------------------------------------------------------
#minimo necessario para os requisitos da aurora
temperatura_intermin = 10
temperatura_externamin = -10
energiamin = 60
pressao_tanquemin = 40
integridade_estruturalmin = 1
modulos_criticosmin =  1
#-----------------------------------------------------------------------------------------------------------------------
#maximo que os requisitos podem chegar na aurora
temperatura_intermax = 30
temperatura_externamax = 35
energiamax = 100
pressao_tanquemax = 60
integridade_estruturalmax = 1
modulos_criticosmax =  1

#-----------------------------------------------------------------------------------------------------------------------
#esta parte do codigo mostra os parametros que a nave tem no momento de forma aleatoria!
print("verificando statos da nave...\n")

print("\n------------------ TELEMETRIA E ANÁLISE DO AURORA ------------------\n")

print("| Parâmetro                         | Status Atual | Status Mínimo | Margem |")
print("|-----------------------------------|--------------|---------------|--------|")

print(f"| Temperatura interna da nave       | {temperatura_interna:^12} | {'10°C':^13} | {temperatura_interm:^6} |")
print(f"| Temperatura externa da nave       | {temperatura_externa:^12} | {'-10°C':^13} | {temperatura_externam:^6} |")
print(f"| Energia total da nave             | {energia:^12} | {'60%':^13} | {energiam:^6} |")
print(f"| Pressão do tanque da nave         | {pressao_tanque:^12} | {'40':^13} | {pressao_tanquem:^6} |")
print(f"| Integridade estrutural da nave    | {integridade_estrutural:^12} | {'1':^13} | {integridade_estruturalm:^6} |")
print(f"| Módulos críticos da nave          | {modulos_criticos:^12} | {'1':^13} | {modulos_criticosm:^6} |")

print("\n---------------------------------------------------------------------\n")

#-----------------------------------------------------------------------------------------------------------------------

#definindo os status como OK ou N/G com if e else

status_temp_int = "OK" if temperatura_interna >= temperatura_intermin and temperatura_intermax else "N/G"
status_temp_ext = "OK" if temperatura_externa >= temperatura_externamin and temperatura_externamax else "N/G"
status_energia = "OK" if energia >= energiamin and energiamax else "N/G"
status_pressao = "OK" if pressao_tanque >= pressao_tanquemin and pressao_tanquemax else "N/G"
status_integridade = "OK" if integridade_estrutural >= integridade_estruturalmin and integridade_estruturalmax else "N/G"
status_modulos = "OK" if modulos_criticos >= modulos_criticosmin and modulos_criticosmax else "N/G"
#-----------------------------------------------------------------------------------------------------------------------
#exibir se os status da Aurora esta OK ou N/G
print(f"""
Integridade estrutural da Aurora = {status_integridade}
Modulo Critico do foguete = {status_modulos}
Temperatura interna = {status_temp_int}
Temperatura externa = {status_temp_ext}
Pressão do tanque = {status_pressao}
Energia = {status_energia}
""")
#-----------------------------------------------------------------------------------------------------------------------
#definindo se A Aurora pode decolar a partir dos Status OK e N/G
if "N/G" in [status_integridade,status_modulos,status_temp_int,status_temp_ext,status_pressao,status_energia]:
    print("""               -------------------------------------------
               | A AURORA NÃO ESTA PRONTA PARA DECOLAGEM |
               -------------------------------------------""")

else:
    print("""               ---------------------------------------------------------
               |A AURORA ESTA PRONTA PARA DECOLAR LETS ROCK THE FUTURE!|
               ---------------------------------------------------------""")






