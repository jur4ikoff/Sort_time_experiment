# Замерный эксперимент по ПТП

## Типы сортировок
`1` - использование операции индексации a[i];
`2` - формальная замена операции индексации на выражение *(a + i);
`3` - использование указателей для работы с массивом.

## Директория Scripts
В этой папке хранятся скрипты, к которым обращаются скрипты из родительского каталога  
`clean.sh` - Очищает директорию `apps` от всех исполняемых и объектных файлов
`build_app.sh` - Компиляция программы с аргументами    


## Главные скрипты
`build_apps.sh` - Скрипт запускает `build_app.sh` для компиляции файлов эксперементов  
