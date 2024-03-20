# Modelagem e otimização algorítmica

## Feito pelos acadêmicos Matheus Hamada (ra124101@uem.br) & Rafael Alexander Lopes (ra127522@uem.br)

### Códigos de heurística para os problemas conhecidos, o problema da mochila e o problema do caixeiro viajante

### Heurística do problema da mochila:

#### O problema da mochila se resume a por itens dentro de uma mochila com um peso máximo, porém fora dela temos itens com pesos e utilidades, qual seria a melhor organização da mochila, visando a maior utilidade possível?

#### A heurística aqui é a seguinte: fazemos uma média entre utilidade e peso, e pegamos das melhores médias até as piores

#### Por exemplo, um item com utilidade 5 e peso 2 tem média 2,5, enquanto o outro item tem utilidade 3 e peso 8, o que resulta em uma média de 0,375. Logo a priorirdade é pegar o primeiro item, mas sempre respeitando o peso máximo da mochila

### Heurística do caixeiro viajante:

#### Um caixeiro viajante deve percorrer todas as cidades em seu mapa, de forma de percorra a menor distância possível. Como ele pode fazer isso?

#### A heurística aqui é bem simples, pegamos sempre os caminhos menores cada vez que fomos percorrendo as cidades.

#### Em um exemplo bem banal, se eu tenho distâncias 2, 3 e 8, escolho 2.
