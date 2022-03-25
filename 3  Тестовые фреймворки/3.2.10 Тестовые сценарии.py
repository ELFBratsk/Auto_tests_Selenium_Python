# Тестовые сценарии
# Созданные тесты нужно сохранить в файле, 
# чтобы его было удобно запускать и хранить в системе контроля версий. 
# Давайте создадим файл test_abs_project.py и напишем в нём следующий код:
def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number" 

if __name__ == "__main__":
    test_abs1()
    print("All tests passed!")
# Мы поместили тестовый сценарий в функцию для разделения тест-кейсов 
# и возможности их независимого запуска.
# Не вдаваясь в подробности, 
# скажем только, что конструкция if __name__ == "__main__" служит для подтверждения того, 
# что данный скрипт был запущен напрямую, а не вызван внутри другого файла в качестве модуля. 
# Весь код написанный в теле этого условия будет выполнен только если 
# пользователь запустил файл самостоятельно. 
# Подробнее можно ознакомиться в видео Олега Молчанова. https://www.youtube.com/watch?v=cW_-zGG4ef4
# В этой конструкции мы вызвали функцию test_abs1(), которая выполняет тестовый сценарий.
# С помощью print("All tests passed!") мы вывели сообщение, если все тесты прошли успешно.
# Чтобы запустить тест, выполните в консоли команду:
# python test_abs_project.py
# Вы должны увидеть в консоли сообщение "All tests passed!".
# Если нам нужно добавить еще один тест, мы можем написать его как функцию в этом же файле. 
# В приведенном примере мы уже не увидим сообщение "Everything passed", 
# так как падение любого теста вызывает выход из программы:
def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")

'''Запустите файл снова. Вы должны увидеть сообщение об упавшем втором тесте:
$ python test_abs_project.py

Traceback (most recent call last):
  File "test_abs_project.py", line 9, in <module>
    test_abs2()
  File "test_abs_project.py", line 5, in test_abs2
    assert abs(-42) == -42, "Should be absolute value of a number"
AssertionError: Should be absolute value of a number'''