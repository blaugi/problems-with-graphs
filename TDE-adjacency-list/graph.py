# %% [markdown]
# ### TDE Lista de Adjancências

# %%
from collections import defaultdict

class Grafo():
  def __init__(self):
    self.adj_list = defaultdict(list)

  def adiciona_vertice(self, vertice):
    if vertice in self.adj_list: # Verificação redudante apenas para existir um retorno da função, a adinção em defaultdict já verifica se existe ou não
      print("Vertice já existente!")
    else:
        self.adj_list[vertice] 
        print(f"Vertice {vertice} inserido com sucesso!")

  def remove_vertice(self, vertice):
    if vertice  in dict(self.adj_list):
        for v in self.adj_list:
          if self.tem_aresta(v, vertice):
            self.remove_aresta(v, vertice)
        self.adj_list.pop(vertice)
        print(f"Vertice {vertice} removido com sucesso!.")
    else:
        print(f"Vertice {vertice} não existe.")
        

  def adiciona_aresta(self, vertice1, vertice2, peso):
    if vertice1 not in self.adj_list: 
      self.adiciona_vertice(vertice1) 
      
    if vertice2 not in self.adj_list: 
      self.adiciona_vertice(vertice2) 

    if not self.tem_aresta(vertice1, vertice2):
        self.adj_list[vertice1].append((vertice2, peso))
        self.adj_list[vertice2].append((vertice1, peso))
        print(f"Aresta entre {vertice1} e {vertice2} Inserida com sucesso!")
    else:
        self.remove_aresta(vertice1, vertice2) #remove antes de atualizar
        self.adj_list[vertice1].append((vertice2, peso))
        self.adj_list[vertice2].append((vertice1, peso))
        print(f"Aresta entre {vertice1} e {vertice2} atualizada com sucesso!") 

  def remove_aresta(self, vertice1, vertice2):
    if self.tem_aresta(vertice1, vertice2):
        #Usa list comprehension pra filtrar o elemento a ser removido
        self.adj_list[vertice1] = [(v, w) for v, w in self.adj_list[vertice1] if v != vertice2]
        self.adj_list[vertice2] = [(v, w) for v, w in self.adj_list[vertice2] if v != vertice1]
        print(f"Aresta entre {vertice1} e {vertice2} removida.")
    else:
        print(f"Aresta entre {vertice1} e {vertice2} não existe.")


  def tem_aresta(self, vertice1, vertice2):
    if vertice2 in dict(self.adj_list[vertice1]) and vertice1 in dict(self.adj_list[vertice2]): 
        return True
    else:
        return False

  def grau_entrada(self, vertice):
    if vertice in self.adj_list:
      grau_entrada = 0
      for v in self.adj_list:
          if any(neighbor == vertice for neighbor, _ in self.adj_list[v]): # percorre a lista de adjacencia do vertice especifico
              grau_entrada +=1
      return grau_entrada
    else:
      print(f'Vertice {vertice} não existe.')

  def grau_saida(self, vertice):
    if vertice in self.adj_list:
      return len(self.adj_list[vertice])
    else:
      print(f'Vertice {vertice} não existe.')

  def grau(self, vertice):
    if vertice in self.adj_list:
      return self.grau_entrada(vertice) + self.grau_saida(vertice) 
    else:
      print(f'Vertice {vertice} não existe.')

  def imprime_lista_adjacencias(self):
    for vertice, vizinhos in self.adj_list.items():
        print(f"{vertice}: {' '.join(f'{v}({w})->' for v, w in vizinhos)}")


# %%
grafo = Grafo()

grafo.adiciona_vertice("A")
grafo.adiciona_vertice("B")
grafo.adiciona_vertice("C")
grafo.adiciona_vertice("A")  # Duplicada

grafo.imprime_lista_adjacencias()

grafo.adiciona_aresta("A", "B", 5)
grafo.adiciona_aresta("A", "C", 3)
grafo.adiciona_aresta("B", "C", 2)
grafo.adiciona_aresta("A", "B", 6)  # Duplicada 

grafo.imprime_lista_adjacencias()

print("Aresta entre A e B:", grafo.tem_aresta("A", "B"))  # True
print("Aresta entre B e A:", grafo.tem_aresta("B", "A"))  # True
print("Aresta entre A e D:", grafo.tem_aresta("A", "D"))  # False

grafo.remove_aresta("A", "B")
grafo.remove_aresta("A", "D")  # Não existe

grafo.imprime_lista_adjacencias()

grafo.remove_vertice("C")
grafo.remove_vertice("D")  # Não existe

grafo.imprime_lista_adjacencias()

grafo.adiciona_aresta("A", "B", 4)
grafo.adiciona_aresta("B", "C", 6)


grafo.imprime_lista_adjacencias()
print("Grau de entrada de B:", grafo.grau_entrada("B"))  # 2
print("Grau de saída de B:", grafo.grau_saida("B"))  # 2
print("Grau total de B:", grafo.grau("B"))  # 4


# %% [markdown]
# #### Esperado:
# ```txt
# Vertice A inserido com sucesso!
# Vertice B inserido com sucesso!
# Vertice C inserido com sucesso!
# Vertice já existente!
# A: 
# B: 
# C: 
# Vertice já existente!
# Aresta entre A e B Inserida com sucesso!
# Vertice já existente!
# Aresta entre A e C Inserida com sucesso!
# Vertice já existente!
# Aresta entre B e C Inserida com sucesso!
# Vertice já existente!
# Aresta entre A e B removida.
# Aresta entre A e B atualizada com sucesso!
# A: C(3)-> B(6)->
# B: C(2)-> A(6)->
# C: A(3)-> B(2)->
# Aresta entre A e B: True
# Aresta entre B e A: True
# Aresta entre A e D: False
# Aresta entre A e B removida.
# Aresta entre A e D não existe.
# A: C(3)->
# B: C(2)->
# C: A(3)-> B(2)->
# Aresta entre A e C removida.
# Aresta entre B e C removida.
# Vertice C removido com sucesso!.
# Vertice D não existe.
# A: 
# B: 
# Vertice já existente!
# Aresta entre A e B Inserida com sucesso!
# Vertice já existente!
# Vertice C inserido com sucesso!
# Aresta entre B e C Inserida com sucesso!
# A: B(4)->
# B: A(4)-> C(6)->
# C: B(6)->
# Grau de entrada de B: 2
# Grau de saída de B: 2
# Grau total de B: 4


