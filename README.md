**Цель работы:**
Научиться методам решения СЛАУ на ЭВМ

**Описание метода, расчетные формулы:**
Метод Гаусса с выбором главного элемента по строкам (вар 2)

Схема с выбором главного элемента является одной из модификаций метода
Гаусса.
Среди ведущих элементов могут оказаться очень маленькие по абсолютной
величине. При делении на такие ведущие элементы получается большая
погрешность округления (вычислительная погрешность).
Идеей метода Гаусса с выбором главного элемента является такая
перестановка уравнений, чтобы на k-ом шаге исключения ведущим
элементом 𝑎𝑖𝑖 оказывался наибольший по модулю элемент k-го столбца.
Т.е. на очередном шаге k в уравнениях, начиная от k до последнего
( i=k,k+1,…,n ) в столбце k выбирают максимальный по модулю элемент и
строки i и k меняются местами. Это выбор главного элемента «по столбцу».
Выбор главного элемента «по строке» - на очередном шаге k в
строке k, начиная со столбца k ( j=k,k+1,…,n ) справа выбирается
максимальный по модулю элемент. Столбцы j и k меняются местами.

**Листинг программы (по крайне мере, где реализован сам метод):**
```python
    for k in range(len(b) - 1):
        max_abs, max_idx = -1, -1
        for i in range(k, len(b)):
            if max_abs < abs(mat[k][i]):
                max_abs = abs(mat[k][i])
                max_idx = i
        for i in range(len(mat)):
            mat[i][k], mat[i][max_idx] = mat[i][max_idx], mat[i][k]

        indexes[k], indexes[max_idx] = indexes[max_idx], indexes[k]
        forward_step(mat, b, k)

    find_answer(mat, b, ans)
```

**Блок-схема численного метода:**
https://app.code2flow.com/O32EU6Lms4XV

**Примеры и результаты работы программы:**
```Считываем из файла или с терминала [Y/*]: 
Введите размерность:3
(через пробел)>>1 3 2
(через пробел)>>3 2 1
(через пробел)>>1 1 1
B (через пробел):1 1 1
Матрица: [[3.0, 1.0, 2.0], [0, 2.3333333333333335, -0.33333333333333326], [0, 0, 0.4285714285714286]]
Найденные коэфф.: [0.3333333333333333, -0.6666666666666666, 1.3333333333333335]
Вектор неувязок: [2.220446049250313e-16, 2.220446049250313e-16, 2.220446049250313e-16]
```

**Выводы:**
Я научился использовать метод Гаусса в программировании и его варианты для сокращения погрешностей