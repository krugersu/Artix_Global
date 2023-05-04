:orphan:


1. Установка и настройка
------------------------

Установка Webmin (панель управления сервером)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ссылка на сайт с полной инструкцией по установке_ (англ.)

.. _установке: https://www.digitalocean.com/community/tutorials/how-to-install-webmin-on-ubuntu-22-04


Webmin - это современная веб-панель управления, которая позволяет вам администрировать ваш Linux-сервер через интерфейс на основе браузера.
С помощью Webmin вы можете управлять учетными записями пользователей, настраивать параметры DNS и изменять параметры для обычных пакетов "на лету".
В этом руководстве вы установите и настроите Webmin на своем сервере и обеспечите доступ к интерфейсу с помощью действительного сертификата от Let's Encrypt.
Затем вы будете использовать Webmin для добавления новых учетных записей пользователей и обновления всех пакетов на вашем сервере с панели мониторинга.

Требования:

#. One Ubuntu 22.04 server
#. Apache 

Инсталяция

.. code-block:: bash
    :linenos:

    $ sudo apt update
    $ curl -fsSL https://download.webmin.com/jcameron-key.asc | sudo gpg --dearmor -o /usr/share/keyrings/webmin.gpg
    $ sudo nano /etc/apt/sources.list
    $ deb [signed-by=/usr/share/keyrings/webmin.gpg] http://download.webmin.com/download/repository sarge contrib
    $ sudo apt update
    $ sudo apt install webmin

Webmin доступен по адресу  - https://your_server:10000

Установка Neofetch
~~~~~~~~~~~~~~~~~~

Neofetch - это очень простая в использовании и кроссплатформенная утилита которая позволяет отображать информацию о системе в терминале

.. code-block:: bash
    :linenos:

    $ sudo apt-get update
    $ sudo apt-get install neofetch



Установка Python
~~~~~~~~~~~~~~~~

.. code-block:: bash
    :linenos:

    $ sudo apt update
    $ sudo apt install python3.10
    $ sudo apt install -y python3-venv


.. _gitinst:

Установка Git
~~~~~~~~~~~~~~~~

Для подключения к GitHub

.. code-block:: bash
    :linenos:

    $ sudo apt update
    $ sudo apt install git
    $ git --version

    $ git config --global user.name "Your Name"
    $ git config --global user.email "youremail@domain.com"
    $ git config --list


Установка программы
~~~~~~~~~~~~~~~~~~~

Клонируем исходники из репозитория GitHub    

.. code-block:: bash

    $ git clone https://github.com/krugersu/Global


Переходим в папку проекта

.. code-block:: bash

    $ cd Global/


Устанавливаем и активируем виртуальное окружение

.. code-block:: bash

    $ python3 -m venv .venv
    $ source .venv/bin/activate


Установка pysqlite3

.. code-block:: bash

    $ pip install pysqlite3-binary


Установка остальных пакетов

.. code-block:: bash

    $ pip install -r requirements.txt


Переходим в рабочую папку проекта и делаем основной файл скрипта исполняемым

.. code-block:: bash

    $ cd src/
    $ chmod +x main.py




Настройка crontab
~~~~~~~~~~~~~~~~~    

.. code-block:: bash
    :linenos:

    $ cd ~
    $ mkdir log


Команда для редактирования планировщика

.. code-block:: bash
    :linenos:

    $ crontab -e

В открывшемся редакторе в конец файла добавить строку:

.. code-block:: bash
    :linenos:

    * * * * * /home/administrator/Global/.venv/bin/python3  /home/administrator/Global/src/main.py /home/administrator/log/command.log  2>&1

Здесь мы указываем периодичность запуска, полный путь к исполняемому скрипту, путь до файла в
который будут выводиться сообщения планировщика. Сохранить файл. Теперь при таких настрой-
ках скрипт будет запускаться каждую минуту. Для работы нужно выставить нужный интервал
запуска. Он выставляется в первой секции строки:


.. figure:: images/crontab-2.png


Синтаксис: *(Minute)*(Hour)*(Day of the Month)*(Month of the Year) *(Day of the Week) username
<path to command/script to execute>


.. csv-table:: **Параметры**
    :header: "Интервал",  "Описание"
    :widths: 15,  30

    "Минуты", "Это значение может быть в пределах 0 — 59"
    "Часы", "Это значение может быть в пределах 0 — 23"
    "День месяца", "Это значение может быть в пределах 1 — 31"
    "Месяц в году", "Это значение поля находится в диапазоне от 1 до 12. Так же можно использовать три первые буквы названия месяца, например: jan, feb, mar"
    "День недели", "Это значение поля находится в диапазоне от 0 до 7.
    Где 0 и 7-воскресенье. 1-понедельник, 2-вторник и так далее"
    
.. csv-table:: **Пример**
    :header: "Следующее выражение для выполнения задачи каждые 5 минут"
    :widths:  30

    "*/5 * * * * /home/administrator/Workshift_load/src/wsh_load.py"


После этого программа должна начать запускаться согласно составленному расписанию.






