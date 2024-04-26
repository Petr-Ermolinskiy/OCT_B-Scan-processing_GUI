##########################
from function import *
# основное окно приложения
from main_ui import Ui_MainWindow
##########################
# необходимые библиотеки
import glob
import os
import sys
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import Slot
# для вывода диалогового окна
from PySide6.QtWidgets import QMessageBox
# для обработки данных
from cv2 import imdecode, IMREAD_COLOR
import seaborn as sns
from pandas import DataFrame, ExcelWriter
# для визуализации
from matplotlib import gridspec, patches
import matplotlib

matplotlib.use('Qt5Agg')
from matplotlib.pyplot import figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
##########################
# чтобы Лого показывалось - https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
import ctypes

myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


###########################


########################################
# Основной класс, через который вызывается приложение
########################################
class Main_window(QMainWindow):
    def __init__(self):
        super(Main_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # путь к папке с файлами
        self.ui.main_path.textChanged.connect(self.add_files_to_combobox)
        # связка top с ползунком
        self.ui.top_num.textChanged.connect(self.update_field2)
        # связка ползунка c top
        self.ui.verticalScrollBar_top.valueChanged.connect(self.update_field3)
        # связка кнопок и действий, которые совершаются при нажатии
        self.ui.pushButton_save_val.pressed.connect(self.save_val)
        self.ui.pushButton_save_massive.pressed.connect(self.save_massive)
        self.ui.pushButton_clear_massive.pressed.connect(self.clear_massive)

        # обновим n каждый раз, когда выбирается какой-то новый файл
        self.ui.comboBox.currentTextChanged.connect(self.update_n)

        # сигналы объединим
        self.ui.top_num.textChanged.connect(self.plot_amd_all)
        self.ui.center.textChanged.connect(self.plot_amd_all)
        self.ui.width.textChanged.connect(self.plot_amd_all)
        self.ui.height.textChanged.connect(self.plot_amd_all)
        self.ui.smooth_n.textChanged.connect(self.plot_amd_all)
        self.ui.comboBox.currentTextChanged.connect(self.plot_amd_all)

        ###########
        # СТРОИМ ГРАФИК
        ###########
        # Создадим figure and canvas для построения
        self.figure = figure(constrained_layout=True, figsize=(5.5, 5))
        self.canvas = FigureCanvas(self.figure)
        # веса, с которыми будут относиться длины и ширины графиков
        widths = [1, 0.3]
        heights = [2, 2]
        # и добавляем болванки графиков...
        spec2 = gridspec.GridSpec(ncols=2, nrows=2, figure=self.figure, width_ratios=widths, height_ratios=heights)
        # ...для рисунка bmp
        self.ax1 = self.figure.add_subplot(spec2[0, 0])
        # ...для данных аппроксимации
        self.ax2 = self.figure.add_subplot(spec2[1, 0])
        # ...для отображения выделенной области
        self.ax3 = self.figure.add_subplot(spec2[:, 1])

        # Создадим layout и добавим canvas на него
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)

        # Добавим наш график на ffwidget_plot
        self.ui.ffwidget_plot.setLayout(layout)
        ###########
        # построили! обновление происходит при изменении какого-либо значения
        ###########

    # изменим n_of_mesurment=0, когда выбираем другой файл в списке
    def update_n(self):
        global n_of_mesurment
        n_of_mesurment = 0

    # основная функция в классе, через которую всё строится
    def plot_amd_all(self):
        # для начала уберем всё то, что есть на графике
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()

        # добавление расширений к имени файла
        file_bmp = self.ui.comboBox.currentText() + '.bmp'
        file_matrix = self.ui.comboBox.currentText() + '.txt'

        # Открытие сохраненного рисунка bmp.
        # Такой порядок открытия гарантирует то, что файл прочитается
        # (при открытии стандартно через cv2 могут быть ошибки при наличии русских символов)
        try:
            f = open(self.ui.main_path.text() + '//' + file_bmp, "rb")
            bytes_ = f.read()
        except Exception:
            self.ui.comment_for_person.setText('Файл .bmp не открылся')
            bytes_ = None

        chunk_arr = np.frombuffer(bytes_, dtype=np.uint8)
        M_img = imdecode(np.asarray(chunk_arr, np.uint8), IMREAD_COLOR)

        # Запись в матрицу значений из txt файла.
        # Это ровно такая же картинка, как и ранее открытая bmp, однако "не ужатая" 8 битным форматом.
        # Именно её мы будем использовать для обработки.
        M_matrix = np.genfromtxt(self.ui.main_path.text() + '//' + file_matrix, delimiter='\t')
        # транспонирование матрицы, для такого же отображения, как и рисунок bmp
        M_matrix = M_matrix.T

        # получим количество строк и столбцов в матрице (количество пикселей по горизонтали и вертикали)
        N_row, N_col = M_matrix.shape

        # центр маски для выделения
        center = math.floor(N_col / 2) + int(self.ui.center.text())
        # верхняя граница для выделения (в пикселях)
        top = int(self.ui.top_num.text())
        # ширина выбранного выделения (в пикселях)
        width = int(self.ui.width.text())
        # высота выделения (в пикселях)
        height = int(self.ui.height.text())

        # количество точек для сглаживания
        smooth_w = int(self.ui.smooth_n.text())

        # выполнение основной функции, которая строит графики и выводит значения аппроксимации
        approx = fig_and_approx(M_matrix, center, top, width, height, smooth_w)
        # return (std, mean, h, y0, A, m_u, message)
        self.ui.approx_A.setText(str(approx[4]))
        self.ui.approx_y0.setText(str(approx[3]))
        self.ui.approx_mt.setText(str(approx[5]))

        # успешно ли прошла аппроксимация
        self.ui.comment_for_person.setText(approx[6])

        # ____________________________________#

        # добавляем рисунок bmp на график
        self.ax1.imshow(M_img, cmap='gray', interpolation='nearest', aspect='auto')

        # добавляем прямоугольник интерисущей нас области
        rect = patches.Rectangle((center - math.floor(width / 2), top), width, height, linewidth=2, edgecolor='r',
                                 facecolor='none')
        # добавим прямоугольник на график
        self.ax1.add_patch(rect)

        # ____________________________________#
        # функция, которой аппроксимируется кривая для аппроксимации - спадающая экспонента
        def f(x, y0, A, m_u):
            return y0 + A * np.exp(-(x * m_u) / 10000)

        # сглаженные данные
        sns.lineplot(x=approx[2], y=approx[1], ax=self.ax2, label='сглаженные данные')
        # аппроксимированные данные
        sns.lineplot(x=approx[2], y=f(approx[2], approx[3], approx[4], approx[5]), ax=self.ax2,
                     label='аппроксимированные данные')
        # строим разброс: среднее значений +- стандартное отклонение
        self.ax2.fill_between(approx[2], PlUS_or_MINUS(approx[1], approx[0], '+'),
                              PlUS_or_MINUS(approx[1], approx[0], '-'), color='b', alpha=0.2)
        # добавим в виде текста параметр коэффициента ослабления на график - чтобы не изменять вид графика не будем использовать transform
        min_ax2, top_ax2 = self.ax2.get_ylim()
        self.ax2.text(approx[2][-1] * 0.8, min_ax2 + (top_ax2 - min_ax2) * 0.65,
                      " $\mu_t$={}".format(round(approx[5], 2)))

        # выводим легенду
        self.ax2.legend()

        # добавляем подписи к осям
        self.ax2.set_xlabel('Глубина от верхней границы, мкм')
        self.ax2.set_ylabel('Сигнал, отн.ед.')

        # ____________________________________#

        # добавляем рисунок bmp на график
        self.ax3.imshow(M_img[top:top + height, center - math.floor(width / 2):center + math.floor(width / 2)],
                        cmap='gray',
                        interpolation='nearest', aspect='auto')

        # ____________________________________#

        # добавим названия
        self.ax1.set_title('Определение выделенного региона', fontsize=12)
        self.ax2.set_title('Сглаженные данные и данные аппроксимации', fontsize=12)
        self.ax3.set_title('Выделенный \n регион', fontsize=12)
        self.canvas.draw()

    #########
    # функции при нажатии на кнопку
    #########
    # сохраняем значение в массив
    def save_val(self):
        message = save_values(self.ui.main_path.text(), self.ui.comboBox.currentText(), self.ui.approx_mt.text(),
                              self.ui.approx_A.text(), self.ui.approx_y0.text())
        self.ui.comment_for_person.setText(message)

    # сохраняем массив по пути
    def save_massive(self):
        message = SAVE_ALL(self.ui.path_for_save.text())
        self.ui.comment_for_person.setText(message)

    # очищаем массив
    def clear_massive(self):
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle('OCT')
        msgBox.setInformativeText("Очистить массив?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        ret = msgBox.exec()

        if ret == QMessageBox.Yes:
            clear_massive()
            self.ui.comment_for_person.setText('Массивы данных успешно очищены')
        else:
            self.ui.comment_for_person.setText('Массивы данных не были очищены')

    # связка значения 'top' с ползунком
    @Slot(str)
    def update_field2(self, text):
        self.ui.verticalScrollBar_top.setValue(int(text))

    @Slot(int)
    def update_field3(self, text):
        self.ui.top_num.setText(str(text))

    ##############################
    #изменим стиль - светлая или темная тема
    ##############################
    @Slot(int)
    def on_comboBox_theme_currentIndexChanged(self, index):
        # меняем стили
        if index == 1:
            with open("style_dark.qss", "r") as func:
                _style = func.read()
            self.setStyleSheet(_style)
        else:
            self.setStyleSheet("")

    # добавление списка файлов в папке в comboBox
    def add_files_to_combobox(self):
        files = get_name_out_of_path(glob.glob(self.ui.main_path.text() + '//' + '*.txt'))
        global n_of_mesurment
        n_of_mesurment = 0
        self.ui.comboBox.clear()  # удалить все элементы из combobox
        self.ui.comboBox.addItems(files)


#######################
#
# дополнительные функции, через которые происходит сохранение массива
#
#######################

# функция сохранения данных во временный массив
def save_values(path, file_in_folder, mu_for_save, A, y):
    # Переменная для индекса (см. ниже после функций описание)
    global n_of_mesurment
    n_of_mesurment += 1
    # важно объявить DataFrame глобальными
    global all_data_mu
    global all_data_y
    global all_data_A
    # имя папки = имя образца
    name_of_sample = path.split('\\')[-1]
    try:
        # сохраняем полученное значение mu_t в основной массив
        all_data_mu.loc[file_in_folder[:-5] + str(n_of_mesurment), name_of_sample] = float(mu_for_save)
        all_data_y.loc[file_in_folder[:-5] + str(n_of_mesurment), name_of_sample] = float(y)
        all_data_A.loc[file_in_folder[:-5] + str(n_of_mesurment), name_of_sample] = float(A)
        return 'Значения успешно сохранились в массив ' + '(' + str(n_of_mesurment) + ')'
    except:
        return 'Значения в массив не сохранились. Обратитесь в поддержку.'


# очистить массив
def clear_massive():
    # важно объявить DataFrame глобальными
    global all_data_mu
    global all_data_y
    global all_data_A
    all_data_mu = DataFrame()
    all_data_y = DataFrame()
    all_data_A = DataFrame()


# сохранить массив
def SAVE_ALL(path):
    # важно объявить DataFrame глобальными
    global all_data_mu
    global all_data_y
    global all_data_A

    if path == '':
        return 'Введите путь к сохранению'
    # сохранение в excel файл
    try:
        with ExcelWriter(path + '\\' + 'OCT_data' + '.xlsx') as writer:
            all_data_mu.to_excel(writer, sheet_name='mu')
            all_data_y.to_excel(writer, sheet_name='y0')
            all_data_A.to_excel(writer, sheet_name='A')
        return 'Файл exсel успешно сохранен'
    except:
        return 'Файл excel не сохранен. Скорее всего нет такого пути к папке, или файл открыт.'


# выполянем основной код программы
if __name__ == '__main__':
    # Data Frame для суммарных данных аппроксимации для mu
    all_data_mu = DataFrame()
    all_data_y = DataFrame()
    all_data_A = DataFrame()
    # переменная для индекса. При добавлении нескольких данных от одного рисунка в массив индексы могли бы быть одинаковыми. Поэтому надо ввести переменную, чтобы индексы везьде были уникальными
    n_of_mesurment = 0

    # запускаем приложение
    app = QApplication(sys.argv)
    # важно обозначить для того, чтобы лого обозначалось правильно
    basedir = os.path.dirname(__file__)
    app.setWindowIcon(QIcon(os.path.join(basedir, 'ICO.ico')))
    window = Main_window()
    window.show()
    sys.exit(app.exec())
