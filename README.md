


<p align="center">
    <img src="cubo.jpeg" width="200">
</p>


## Descrição

Este projeto implementa um simulador de um Cubo de Rubik 2×2 em Python. O estado do cubo é representado por seis matrizes 2×2, uma para cada face.

Cada movimento (`UP`, `DOWN`, `LEFT`, `RIGHT`, `FRONT` e `BACK`) é realizado girando a face correspondente e atualizando as oito posições das faces adjacentes por meio de um deslocamento cíclico de um vetor.

O programa também possui uma interface gráfica desenvolvida com Tkinter, que exibe uma representação aberta e colorida do cubo, facilitando a visualização e a validação dos movimentos.

##

Exemplo de uso

Movimento da face superior no sentido horário:

E = movimento(E, "UP", 1)

1 → rotação no sentido horário.
0 → rotação no sentido anti-horário.

O sentido de rotação é sempre definido observando diretamente a face que está sendo movimentada.

##

Saída: 





<p align="center">
    <img src="output.png" width="300">
</p>
