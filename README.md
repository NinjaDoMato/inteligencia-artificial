# Inteligência Artificial

Trabalhos desenvolvidos para a disciplina de Inteligência Artificial do curso
de Bacharelado em Ciência da Computação da Universidade Tuiuti do Paraná.

## Autor

- Aluno: Daniel Deda

## Descrição

Trabalhos referentes aos algoritmos de busca.

Trabalho 1
  - Implementada a Busca em Largura e Em Profundadade para solução do problema da torre de Hanói
  
Trabalho 2 
  - Implementada Busca Gulosa para resolução de labirintos
  
Estudo dirigido
  - Implementada o Tabu Search
  
Considerações:
    - Os arquvivos dos labirintos foram alterados para que cada corredor ficasse com apenas 1 caracter de largura
    - Para escolher qual labirinto irá ser feita a busca, basta alterar o atributo "arquivo" no arquivo labirinto.py
    - A função "solução" estava retornando None quando a lista de estados era invertida, então as funções de busca retornam 
      apenas o estado final e na função main é exibida a lista de estados até a solução final
    - Prints para testes foram comentados no cógigo
