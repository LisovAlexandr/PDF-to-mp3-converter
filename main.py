"""преобразование текста pdf файла в озвученный mp3 файл"""
from gtts import gTTS
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path='test.pdf',language='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # проверка есть ли такой файл    и его расширение равно .pdf
        # принты для пользователя
        print(f'[+] Original file name: {Path(file_path).name}')
        print('[+] Processing...')


        # return 'файл на месте'

        # открываем файл в двоичном режиме mode='rb'
        with pdfplumber.PDF(open(file_path,mode='rb')) as pdf:
            # извлекаем текст из каждой страницы
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        # with open('text1.txt','w') as file:
        #     file.write(text)

        text = text.replace('\n','')
        # with open('text2.txt','w') as file:
        #     file.write(text)

        # преобразуем файл в аудио
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem # получаем имя файлв
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 saved successfully\n---Done!---'
    else:
        return 'файла нет..('

# print(pdf_to_mp3())
# pdf_to_mp3() # тестовый файл на месте, потому что объявлен дефолтным значением параметра
# pdf_to_mp3('test.pdf') # переданный файл на месте
# pdf_to_mp3('test1.pdf') # файла нет..(

def main():
    file_path = input('Введите расположение файла: ')
    language = input('Введите язык: ')
    print(pdf_to_mp3(file_path=file_path,language=language))

if __name__ == '__main__':
    main()
