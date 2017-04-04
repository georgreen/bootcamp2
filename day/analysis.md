### Asymptotic Analysis for Prime function

|                                    code                                        |   Time      | Ex times |
|_ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ |:_ _ _ _ _ _:| _ _ _ _ :|
|    '''                                                                         |             |          |
|    input: n integer                                                            |             |          |
|    output: a list, containing prime numbers in range(0,n)                      |             |          |
|    '''                                                                         |             |          |
|    if type(n) != type(1):                                                      |    c1       |     1    |
|        return "Invalid Data Type"                                              |    c2       |     1    |
|                                                                                |    c3       |     1    |
|    solution = []                                                               |    c4       |     1    |
|    for i in range(0, n + 1):                                                   |    c5       |     n    |
|        if prime_test(i, solution):                                             |    c6       |     c    |
|            solution.append(i)                                                  |    c7       |     n    |
|    return solution                                                             |    c8       |     1    |
|                                                                                |             |          |


<br /> * T(n) = c1 * 1 + c2 * 1 + c3 * 1 + c4 * 1 + c5 * n + c6 * c + c7 * n + c8 * 1 <br />
       * T(n) = c1 + c2 + c3 + c4 + c5n + c6c + c7n + c8 <br />
       *  *Drop constants* <br />
       *  T(n) = c7n + c5n   <br />
       * *Take dominat factor as n scales* <br />
       * T(n) = O(f(n))
