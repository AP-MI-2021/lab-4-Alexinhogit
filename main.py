def list_input() -> [int]:
    """
    Functia care permite citirea unei liste de numere intregi.
    :return: Numerele introduse sub forma de lista.
    """
    lst = [int(x) for x in input("Introduceti numerele listei separate cu un spatiu: ").split(" ")]

    return lst


def return_negative_numbers_from_lst(lst: [int]) -> [int]:
    """
    Functia care citeste numerele dintr-o lista si le afiseaza doar pe cele negative nenule.
    :param lst: Lista verificata.
    :return: Lista numerelor negative nenule din lista initiala.
    """
    lista_numere_negative = []
    for n in lst:
        if n < 0:
            lista_numere_negative.append(n)
    return lista_numere_negative


def test_return_negative_numbers_from_lst():
    """
    Functia care testeaza return_negative_numbers_from_lst
    """
    assert return_negative_numbers_from_lst([-1, 0, 1, -23, 4]) == [-1, -23]
    assert return_negative_numbers_from_lst([0]) == []
    assert return_negative_numbers_from_lst([2, 3, 17]) == []
    assert return_negative_numbers_from_lst([-2, -3, -17]) == [-2, -3, -17]


def smallest_number_with_last_digit_equal_to_an_input_digit(lst: [int], n) -> int:
    """
    Functia va verifica lista data si va afisa doar cel mai mic numar din ea care are ultima cifra egala cu o cifra data
    de la user.
    :param lst: Lista verificata.
    :param n: Cifra data de user.
    :return: Cel mai mic numar din lista cu ultima cifra egala cu cifra data de user.
    """
    lowest = None
    for x in lst:
        last_digit = abs(x) % 10
        if last_digit == n and (lowest is None or x < lowest):
            lowest = x
    return lowest


def test_smallest_number_with_last_digit_equal_to_an_input_digit():
    """
    Functia care testeaza smallest_number_with_last_digit_equal_to_an_input_digit
    """
    assert smallest_number_with_last_digit_equal_to_an_input_digit([1, 6, 34, 68, 40, 48, 20], 8) == 48
    assert smallest_number_with_last_digit_equal_to_an_input_digit([1, 2, 3], 3) == 3
    assert smallest_number_with_last_digit_equal_to_an_input_digit([101, 1001, 100001], 1) == 101


def is_prime(x: int) -> bool:
    """
    Verifica un numar daca este prim sau nu.
    :param x: Numarul intreg ce urmeaza a fi verificat.
    :return: True daca e prim, False daca nu e prim.
    """
    if x < 2:
        return False
    if x != 2 and x % 2 == 0:
        return False
    for i in range(3, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def test_is_prime():
    """
    Verifica functia is_prime
    """
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(2) == True
    assert is_prime(37) == True


def is_superprime(x: int) -> bool:
    """
    Verifica daca un numar este superprim sau nu.
    :param x: Numarul intreg verificat.
    :return: True daca e superprim, False daca nu.
    """
    if x <= 0:
        return False

    while x:
        if is_prime(x) == False:
            return False
        x //= 10
    return True


def test_is_superprime():
    """
    Verifica functia is_superprime
    """
    assert is_superprime(239) == True
    assert is_superprime(-23) == False
    assert is_superprime(0) == False
    assert is_superprime(173) == False
    assert is_superprime(23) == True


def list_superprime_numbers(lst: [int]) -> [int]:
    """
    Verifica numerele din lista daca sunt superprime sau nu si la final returneaza o lista cu numere superprime din
    lista data.
    :param lst: Lista data.
    :return: Lista doar cu numere superprime din lista data.
    """
    return [x for x in lst if is_superprime(x)]


def test_list_superprime_numbers():
    """
    Verifica functia list_superprime_numbers
    """
    assert list_superprime_numbers([173, 239]) == [239]
    assert list_superprime_numbers([2, 17]) == [2]
    assert list_superprime_numbers([0, 173]) == []
    assert list_superprime_numbers([-23, 23, 37]) == [23, 37]


def greatest_common_divisor(x: int, y: int) -> int:
    """
    Functie ajutatoare pentru CMMDC.
    """
    while y != 0:
        (x, y) = (y, x % y)
    return x


def operation_5(lst: [int]) -> [int]:
    """
    Functia va afisa o lista obtinuta din lista initiala in care numerele pozitive si nenule sunt inlocuite cu CMMDC-ul
    lor, iar cele negative au cifrele in ordine inversa.
    :param lst: Lista initiala.
    :return: Lista modificata in urma inlocuirilor.
    """
    current_gcd = max(lst)
    for x in lst:
        if x > 0:
            current_gcd = greatest_common_divisor(current_gcd, x)

    new_list = []
    for x in lst:
        if x < 0:
            new_list.append(-int(str(abs(x))[::-1]))
        elif x == 0:
            new_list.append(0)
        elif x > 0:
            new_list.append(current_gcd)

    return new_list


def test_operation_5():
    """
    Verifica functia operation_5
    """
    assert operation_5([-76, 12, 24, -13, 144]) == [-67, 12, 12, -31, 12]
    assert operation_5([0]) == [0]
    assert operation_5([-11, -12, 36, 72]) == [-11, -21, 36, 36]
    assert operation_5([-11, -12, -13]) == [-11, -21, -31]


def main():
    lst = []
    while True:
        print("""
        1. Citirea unei liste de numere intregi.
        2. Afisarea tuturor numerelor negative nenule din lista.
        3. Afisarea celui mai mic numar care are ultima cifra egala cu o cifra citita de la tastatura.
        4. Afisarea tuturor numerelor din lista care sunt superprime.
        5. Afisarea listei obtinute din lista initiala in care numerele pozitive si nenule au fost inlocuite cu CMMDC-ul
        lor si numerele negative au cifrele in ordine inversa.
        6. Oprire.""")

        cmd = input("Comanda: ")
        if cmd == '1':
            lst = list_input()
        elif cmd == '2':
            print(return_negative_numbers_from_lst(lst))
        elif cmd == '3':
            n = int(input("Alegeti cifra: "))
            print(smallest_number_with_last_digit_equal_to_an_input_digit(lst, n))
        elif cmd == '4':
            print(list_superprime_numbers(lst))
        elif cmd == '5':
            print(operation_5(lst))
        elif cmd == '6':
            break
        else:
            print("Comanda invalida.")


test_return_negative_numbers_from_lst()
test_smallest_number_with_last_digit_equal_to_an_input_digit()
test_is_prime()
test_is_superprime()
test_list_superprime_numbers()
test_operation_5()

if __name__ == "__main__":
    main()
