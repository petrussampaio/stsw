Feature: Classificação de Triângulos

  Scenario Outline: Classificar triângulo com valores válidos
    Given um triângulo com lados <lado_a>, <lado_b>, <lado_c>
    When classifico o triângulo
    Then o tipo de triângulo deve ser "<resultado_esperado>"

    Examples:
      | lado_a | lado_b | lado_c | resultado_esperado  |
      | 100    | 100    | 100    | Equilátero          |
      | 5      | 5      | 3      | Isósceles           |
      | 7      | 10     | 5      | Escaleno            |
      | 199    | 100    | 100    | Isósceles           |
      | 100    | 199    | 100    | Isósceles           |
      | 100    | 100    | 1      | Isósceles           |
      | 1      | 1      | 1      | Equilátero          |
      | 1      | 2      | 2      | Isósceles           |
      | 1      | 100    | 100    | Isósceles           |
      | 2      | 2      | 2      | Equilátero          |
      | 2      | 2      | 1      | Isósceles           |
      | 2      | 100    | 100    | Isósceles           |
      | 2      | 199    | 200    | Escaleno            |
      | 2      | 200    | 200    | Isósceles           |
      | 100    | 100    | 100    | Equilátero          |
      | 100    | 199    | 199    | Isósceles           |
      | 100    | 200    | 200    | Isósceles           |
      | 199    | 199    | 1      | Isósceles           |
      | 199    | 199    | 2      | Isósceles           |
      | 199    | 199    | 100    | Isósceles           |
      | 199    | 100    | 200    | Escaleno            |

  Scenario Outline: Classificar triângulo com valores inválidos
    Given um triângulo com lados <lado_a>, <lado_b>, <lado_c>
    When classifico o triângulo
    Then o tipo de triângulo deve ser "<resultado_esperado>"

    Examples:
      | lado_a | lado_b | lado_c | resultado_esperado |
      | 0      | 100    | 100    | Não é um triângulo | 
      | 200    | 100    | 100    | Não é um triângulo |           
      | 100    | 0      | 100    | Não é um triângulo |           
      | 100    | 100    | 0      | Não é um triângulo |           
      | -5     | 100    | 100    | Não é um triângulo |           
      | 100    | -5     | 100    | Não é um triângulo |           
      | 100    | 100    | -5     | Não é um triângulo |          
      | 1      | 1      | 100    | Não é um triângulo |
      | 1      | 2      | 100    | Não é um triângulo |
      | 1      | 200    | 100    | Não é um triângulo |
      | 100    | 1      | 200    | Não é um triângulo |
      | 100    | 1      | 1      | Não é um triângulo |
      | 100    | 2      | 2      | Não é um triângulo |
      | 200    | 1      | 1      | Não é um triângulo |
      | 200    | 2      | 1      | Não é um triângulo |
      | 1      | 1      | 199    | Não é um triângulo |
      | 1      | 2      | 199    | Não é um triângulo |
      | 1      | 100    | 199    | Não é um triângulo |
      | 100    | 199    | 1      | Não é um triângulo |
      | 2      | 100    | 199    | Não é um triângulo |
      | 2      | 200    | 1      | Não é um triângulo |
      | 2      | 200    | 2      | Não é um triângulo |
      | 2      | 200    | 100    | Não é um triângulo |