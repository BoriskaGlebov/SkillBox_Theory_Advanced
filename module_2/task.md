Немного программирования.
Вызовите команду $ ls -la для папки /etc . Скопируйте output в файл. Обратите внимание: мы опустили флаг -h, который сделал бы формат размера человекачитаемым. Напишите программу, которая бы переработала результат так, будто он был выведен с использованием флага -h
С помощью python выясните количество файлов и папок в output. У папок права доступа обычно начинаются с d , например drwxr-xr-x. По этому признаку папки можно отличить от файлов.
Подсчитайте суммарный размер всех файлов в папке /etc в байтах
Переведите его в человекочитаемый формат (1024 байта = 1 кБ, 1024 кБ = 1 МБ и тд). Напишите функцию, которая по output из ls -la выводит суммарный размер файлов в человекочитаемом формате.
