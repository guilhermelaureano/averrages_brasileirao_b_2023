import matplotlib.pyplot as plt
import numpy as np

import team

# mostrar dados de média de pontos por 5 rodadas
rounds = 5
teams = []
teams.append(team("black", "ABC", [1]))
teams.append(team("red", "ATLÉTICO-GO", [1]))
teams.append(team("blue", "AVAí", [1]))
teams.append(team("red", "BOTAFOGO-SP", [1]))
teams.append(team("dimgrey", "CEARÁ", [1]))
teams.append(team("green", "CHAPECOENSE", [1]))
teams.append(team("r", "CRB", [1]))
teams.append(team("gold", "CRICIÚMA", [1]))
teams.append(team("g", "GUARANI", [1]))
teams.append(team("darkred", "ITUANO", [1]))
teams.append(team("lime", "JUVENTUDE", [1]))
teams.append(team("deepskyblue", "LONDRINA", [1]))
teams.append(team("yellow", "MIRASSOL", [1]))
teams.append(team("yellow", "NOVORIZONTINO", [1]))
teams.append(team("black", "PONTE PRETA", [1]))
teams.append(team("orange", "SAMPAIO CORRÊA", [1]))
teams.append(team("r", "SPORT", [1]))
teams.append(team("tomato", "TOMBENSE", [1]))
teams.append(team("indianred", "VILA NOVA", [1]))
teams.append(team("maroon", "VITÓRIA", [1]))

# criar figura e eixos
fig, ax = plt.subplots()

# plotar dados
for team in teams: ax.plot(rounds, team.points, c=team.color, label=team.name)

# Mostrar os rótulos dos eixos e a legenda do gráfico
ax.set_xlabel('Rodadas')
ax.set_xticks(list(range(5,24)))
ax.set_ylabel('Total de pontos')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 8})

# Exibir o gráfico pronto
plt.show()
