# необходимые библиотеки
import math
import numpy as np
import scipy.optimize as opt
from scipy import signal


################################################
# дополнительные функции для выполнения программы
################################################

# функция, чтобы разделить путь до файла на название файла без расширений
def get_name_out_of_path(files):
    out=[0]*(len(files)-1)
    for i in range(len(files)-1):
        out[i]=files[i].split('\\')[-1][:-4]
    return out

# Функция для поочередного складывания элементов массива.
# Возвращает массив, в котором каждый i элемент является суммой или разностью i-ых элементов 2-х массивов
def PlUS_or_MINUS(mas_1, mas_2, op='+'):
    if len(mas_1) != len(mas_2):
        print('Размеры массивов не совпадают.')
        return 0
    result = []
    if op == '+':
        for i, j in zip(mas_1, mas_2):
            result.append(i + j)
    if op == '-':
        for i, j in zip(mas_1, mas_2):
            result.append(i - j)
    if op == '/':
        for i, j in zip(mas_1, mas_2):
            result.append(i / j)
    return result


# данная функция принимает срез матрицы (slice_) и возвращает 3 массива:
# 1) массив по глубине проникновения,
# 2) среднее по строчкам
# 3) стандартное отклонение по строчкам
# также в данной функции происходит сглаживание -- параметр smooth_w отвечает за количество усреднений
def _data_from_slice(slice_, smooth_w=1):
    # создаем пустой массив для средних значений интенсивности по строкам,
    # а также для стандартного отклонения интенсивности по строкам
    massive = []
    __error = []

    # для каждой строки рассчитываем среднее и стандартное отклонение, и записываем данные значения в массив
    for i in slice_:
        massive.append(i.mean())
        __error.append(i.std())

    # сглаживание кривых путем медианного фильтра
    massive = signal.medfilt(massive, smooth_w)
    __error = signal.medfilt(__error, smooth_w)

    # создадим массив по глубине проникновения в микронах - 1 пиксель : 3 микрона
    z_axis_in_micron = np.arange(0, len(massive)) * 3

    return z_axis_in_micron, massive, __error

################################################
# функция, выполняющая визуализацию и аппроксимацию данных
################################################
def fig_and_approx(M_matrix, center, top, width, height, smooth_w):
    message = 'Аппроксимация данных прошла успешно'
    if center - width / 2 < 0 or top + height > 512 or center + width / 2 > 500:
        message = 'Вы вышли за границу рисунка'
        return (0, 0, 0, 0, 0, 0, message)

    # выделим интерисующий нас участок на графике
    slice_of_M = M_matrix[top:top + height, center - math.floor(width / 2):center + math.floor(width / 2)]

    # получаем 3 массива через функцию _data_from_slice:
    # 1) массив по глубине проникновения,
    # 2) среднее по строчкам,
    # 3) стандартное отклонение по строчкам.
    h, mean, std = _data_from_slice(slice_of_M, smooth_w)

    # определенным образом нормируем, чтобы данные соответствовали действительности
    std = 10 ** (mean / 20) * PlUS_or_MINUS(std, mean, '/')
    mean = 10 ** (mean / 20)

    # Обрезаем массивы по такому условию.
    # Это одна из важных частей:
    # если не обрезать массив, то параметры аппроксимации будут не такими, как в изначальной программе
    mean = mean[math.floor(top / 3):math.floor((top + height) / 3)]
    h = h[math.floor(top / 3):math.floor((top + height) / 3)]
    std = std[math.floor(top / 3):math.floor((top + height) / 3)]

    # функция, которой аппроксимируется кривая для аппроксимации - спадающая экспонента
    def f(x, y0, A, m_u):
        return y0 + A * np.exp(-(x * m_u) / 10000)

    # аппроксимация данных (функция opt.curve_fit)
    try:
        # функцию пишем через try, чтобы избежать ошибки при неправильно аппроксимации
        (y0, A, m_u), _ = opt.curve_fit(f, h, mean, p0=[0, 200, 50], bounds=((0, 0, 0), (50000, 50000, 3000)))
    except:
        (y0, A, m_u) = (1, 1, 1)
        message = 'Не получилось достоверно найти параметры аппроксимации. Попробуйте изменить параметры.'

    # print('Параметры аппроксимации: y0 =', round(y0, 2), '; А0 =', round(A, 2), '; mu_t =', round(m_u, 2))

    # возвращаем данные аппроксимации
    return std, mean, h, y0, A, m_u, message



