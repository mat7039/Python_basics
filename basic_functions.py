'''School project to solve a few exercise from statistics.
Project uses simple python tools like creating functions (like creating my own function for factorial, using if/else statement and creating easy to read prints for complex calculations)
'''

import scipy.stats as st

def statystyka(n,e,c):

    def Parametry(e):
        print('1. Niech ξ oznacza 3. cyfrę numeru albumu')
        print('Xi\t-3\t1\t3\t5\nPi\t0.2\t0.1ξ\tq\t0.3')
        print('ξ = ',e)
        print('Oblicz wariancję zmiennej losowej X, znajdując wcześniej nieznane prawdopodobieństwo q.')
        print()
        print('Rozwiązanie: ')
        x = 0.1 + e / 100
        q = 1 - 0.2 - x - 0.3
        print('q = 1 - 0.2 -',round(x,3),'- 0.3 = ',round(q,3))
        EX = -3 * 0.2 + 1 * x + 3 * q + 5 * 0.3
        print('EX = -3 * 0.2 + 1 *',round(x,3),'+ 3 *',round(q,3),'+ 5 * 0.3 =',round(EX,3))
        EX2 = 9 * 0.2 + 1 * x + 9 * q + 25 * 0.3
        print('EX^2 = 9 * 0.2 + 1 *',round(x,3),' + 9 *',round(q,3),' + 25 * 0.3 =',round(EX2,3))
        D2X = EX2 - EX ** 2
        print('D\u00b2X =',round(EX2,3),'-',round(EX,3),'\u00b2 =',round(D2X,3))

    Parametry(e)

    print('\n\n')

    def koty(n):
        def factorial(f):
            fact = 1
            if f < 0:
                print('Factorial can\'t be negative')
            elif f == 0:
                x = 1
                return fact
            else:
                for i in range(1,f + 1):
                    fact *= i
                return fact

        p = n * 2 / 100
        q = 1 - p
        p = round(p,4)
        q = round(q,4)
        
        print(f'''2. Niech η oznacza 2. cyfrę numeru albumu 
η = {n}
W pewnej populacji kotów jest 2η"%" czarno-białych. W kamienicy mieszka 5 kotów. Jakie jest prawdopodobieństwo, że więcej niż 2 są  czarno-białe? ''')
        print()
        print('Rozwiązanie: ')
        print()
        print('Więcej niż 2 to 3, 4 lub 5.\nS - ilość czarno-białych kotów.\np =',p,';q = 1 - p =',q)
        P3 = (factorial(5) / (factorial(3) * factorial(2))) * p ** 3 * q ** 2
        print(f'P(S=3) = (5! / (3! * (5-3)!)) * {p}\u00b3 * {q}\u00b2 = {round(P3,4)}')
        P4 = (factorial(5) / (factorial(4) * factorial(1))) * p ** 4 * q
        print(f'P(S=4) = (5! / (4! * (5-4)!)) * {p}\u2074 * {q} = {round(P4,4)}')
        P5 = (factorial(5) / (factorial (5) * factorial(0)) * p ** 5)
        print(f'P(S=5) = (5! / (5! * (5-5)!)) * {p}\u2075 * {q}\u2070 = {round(P5,4)}')
        print()
        print('P(S>2) = P(S=3) + P(S=4) + P(S=5)')
        print()
        print('Więc nasze prawdopodobieństwo:')
        Pr = P3 + P4 + P5
        print(f'P = {round(P3,4)} + {round(P4,4)} + {round(P5,4)} = {round(Pr,4)}')
        Pw = Pr * 100
        print('Nasze prawdopodobieństwo wynosi', round(Pw,4),'%')

    koty(n)

    print('\n\n\n')


    
    def stdev(n, e, c):

        print(f'''3. Niech η oznacza 2., ξ oznacza 3. i ζ oznacza 4. cyfrę numeru albumu 
η = {n}; ξ = {e}; ζ = {c}
Zmienna losowa X   ̴ N(0; 1). Oblicz prawdopodobieństwa:

a)P (-2 < X < 0,η) 



b)P (|X|< 1,ξ) 



c)P (X > -0,ζ)''') 

        print()
        print('Rozwiązanie:')
        print()

        x = st.norm.cdf(n/10) - (1 - st.norm.cdf(2))
        print('a)P (-2 < x <',n/10,') = Φ(',n/10,') - (1 - Φ(2)) =',st.norm.cdf(n/10),'- (1 -',st.norm.cdf(2),') =',x)
        print()
        y = st.norm.cdf(1 + e/10) - (1 - st.norm.cdf(1 + e/10))
        print(f'b)P (|x| < {1 + e/10}) = P({-(1 + e/10)} < x < {1 + e/10} ) = Φ({1 + e/10}) - (1 - Φ({1 + e/10})) = {st.norm.cdf(1 + e/10)} - (1 - {st.norm.cdf(1 + e/10)}) = {y}')
        print()
        z = -(c/10)
        print(f'c)P(x > {z}) = 1 - Φ({z}) = 1 - (1 - Φ({c/10})) = Φ({c/10}) = {st.norm.cdf(c/10)}')
    stdev(n,e,c)


    print('\n\n')



    def standard(c):

        print(f'''4. Niech ζ oznacza 4. cyfrę numeru albumu 
ζ = {c}
4a. Zmienna losowa Y   ̴ N(3; 0,5). Oblicz prawdopodobieństwo:

P(2 < Y < 2,ζ) 



4b. Zmienna losowa T   ̴ N(10+ζ; 8). Oblicz prawdopodobieństwo:

P (T > 12) ''')



        print()
        print('Rozwiązanie:')
        print()
        print('4a. Y~N(3;0,5)\nU = (Y - 3) / 0,5 = 2(Y - 3) ~ N(0,1)')

        k = round(2 * ((2+(c/10)) - 3),2)

        l = (-1) * k

        f = st.norm.cdf(2) - st.norm.cdf(l)

        print(f'P1 = P(2 < Y < {2+c/10} = P(2(2 - 3) < U < 2({2+c/10} - 3)) = P(-2 < U < {k}) = Φ({k} - Φ(-2) = 1 - Φ({l}) - (1 - Φ(2)) = -{st.norm.cdf(2)} + {st.norm.cdf(l)} = {round(f,10)}')
        print()
        print(f'4b. T~N({10+c};8)\nU = (T - {10+c}) / 8 ~ N(0,1)')

        s = st.norm.cdf((12+10+c)/8)

        if c > 5:
            s = round(s)
        
        print(f'P2 = P(T > 12) = 1 - P(T < 12) = P(U < (12 + {10+c}) / 8) = 1 - P(U < {(12 + 10 + c) / 8}) = 1 - Φ({(12 + 10 + c) / 8}) = 1 - {st.norm.cdf((12+10+c)/8)} = {1 - s}')

    standard(c)


    print('\n\n\n')



    def cent(e):

        print(f'''5. Niech ξ oznacza 3. cyfrę numeru albumu 

ξ = {e}



Jeżeli podchorąży na 20 oddanych strzałów trafia średnio 1ξ razy to jakie jest prawdopodobieństwo, że ilość „pudeł”  na 400 strzałów wyniesie między 10 a 20?.''')

        print()

        print('Rozwiązanie (tw. de Moivre\'a - Laplace\'a):')

        print('\n\n')

        print('P\u2084\u2080\u2080 = ilość "pudeł" na 400 strzałów')

        print(f'n = 400; p = 1 - ({10+e}/20) = {round((1 - ((10+e)/20)),4)};(prawdpodobieństwo "pudła"); q = {(10+e)}/20 = {(10+e)/20};(prawdopodobieństwo celnego strzału)')

        np = 400 * ((20-(10+e))/20)

        print(f'np = {np}')

        nq = round(((10+e)/20) * 400,4)

        if np > 5 or nq > 5:

            print(f'(np = {np}, nq = {nq}, oba większe niż 5, więc spełniliśmy warunki założenia)')

            print()

        else:

            print('(np lub nq jest mniejsze niż 5, nie spełniliśmy warunków założenia.)')

        σ = (400 * ((10+e)/20) * ((20-(10+e))/20)) ** 0.5

        print(f'σ = \u221A(npq) = \u221A(400 * {(10+e)/20} * {(20-(10+e))/20}) = \u221A({σ ** 2}) = {σ}')

        print()

        σ = round(σ,4)

        print(f'P(10 < P\u2084\u2080\u2080 < 20) = P(((10 - {np}) / {σ}) < ((P\u2084\u2080\u2080 - {np}) / {σ}) < ((20 - {np}) / {σ})) =')

        O = (10 - np) / σ 

        U = (20 - np) / σ

        

        if O < 0:
            x = 1 - st.norm.cdf((-1)*O)

        else:
            x = st.norm.cdf(O)
            
        if U < 0:
            y = 1 - st.norm.cdf((-1)*U)

        else:
            y = st.norm.cdf(U)

        

            

        print(f'= P({O} < U\u2084\u2080\u2080 < {U}) = Φ({U}) - Φ({O}) = {y - x}')

        print()

    

        if y - x == 0:

            print('Oczywiście wynik nigdy nie będzie równy 0, ale jest tak bliski 0, że przedstawienie go bez zaawansowanych kalkulatorów jest problematyczne.')

    cent(e)

    

statystyka(9,4,0)  
