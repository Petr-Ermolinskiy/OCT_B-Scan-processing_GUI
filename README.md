# Графическое приложение для обработки B-сканов, полученных с помощью ОКТ-системы OCP930SR

В этом репозитории представлен код графического интерфейса Python для обработки B-сканов от ОКТ-системы OCP930SR.

## Авторы

Разработчики программного кода на Mathcad: Башкатов Алексей Николаевич и Генина Элина Алексеевна. 

Разработчик графического интерфейса на Python: Ермолинский Петр Борисович.


## Использование
Последнюю версию программы можно скачать в разделе `Releases`.

После запуска приложения вам необходимо перейти в ту папку, в которой сохранены файлы В-сканов (это файлы .bmp и .txt). Расчет осуществляется автоматически для выборанной области. Чтобы сохранить значение, необходимо нажать на кнопку `сохранить измерение`. Значения хранятся во внетренней памяти. Чтобы сохранить измеренные значения в Excel файл, то необходимо выбрать путь до папки для сохранения, и нажать на кнопку `Сохранить массив`.


# Python GUI to process B-Scan of OCT imaging system OCP930SR

In this repository, the sorce code of Python GUI to process B-Scan of OCT imaging system OCP930SR is presented.

__Note__: all comments in the code as well as in the GUI are written in Russian.

## Authors

Developers of program code in Mathcad: Bashkatov A.N. and Genina E.A. 

Developer of Python GUI: Ermolinskiy P.B.

## Usage
You can download the last version of the programm trought `Releases`.

After launching the application, you need to go to the folder in which the B-scan files are saved (i.e., .bmp and .txt files). The calculation is carried out automatically for the selected area. To save the value, you must click on the `сохранить измерение` button. The values are stored in external memory. To save the measured values to an Excel file, you need to select the path to the folder to save and click on the `Сохранить массив` button.

## Manual Installation

If you are using git, you can clone the project and set up a virtual environment using Python 3.11.6 (only this version was tested) in PyCharm or any other workspace:
```bash
git clone https://github.com/Petr-Ermolinskiy/OCT_B-Scan-processing_GUI.git
```
Otherwise you can download the files manually. Then you can open a terminal or command prompt and navigate to the directory where you want to create the virtual environment, i.e., the directory where you have placed the files from this repository. You can use `cd your/path/to/the/directory`.

Run the following command to create a new virtual environment named `venv` (make sure that you have the Python 3.11.5 installed):
```bash
python3.11 -m venv venv
```

Activate the virtual environment. On Windows, you can do this by running:
```bash
venv\Scripts\activate
```
On macOS and Linux, you can do this by running:
```bash
source venv/bin/activate
```

Finally, you can install all the necessary packages:

```bash
pip install -r requirements.txt
```
Run the script:
```bash
python main.py
```

## Creating an exe file

To create an exe file in Windows, you need to execute the following command in the terminal or command prompt:

```bash
pyinstaller --onefile --windowed --add-data "style_dark.qss;." --name='OCT' --add-data "ICO.ico;." --icon=logo.ICO main.py
```
I strongly recommend that you use [UPX](https://upx.github.io/) to reduce the size of the executable. In this case you can run the following command:
```bash
pyinstaller --onefile --windowed --add-data "ICO.ico;." --add-data "style_dark.qss;." --name='OCT' --icon=ICO.ico --upx-dir=Path\to\the\upx-4.2.2-win64 main.py
```
The final size of the exe file will be about 115 MB.
