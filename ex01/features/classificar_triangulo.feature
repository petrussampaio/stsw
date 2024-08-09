Feature: Classificar Triângulo
    O programa deve receber três inteiros representando lados de um triângulo
    e deve retornar seu tipo, qual seja: equilátero, escaleno, isósceles

    Scenario: Classificar um Triânculo Equilátero Válido
    Given os lados do triângulo 1, 1, 1
    When eu classifico o triângulo
    Then o resultado deve ser Equilátero