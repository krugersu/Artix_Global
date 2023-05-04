Сайт с документацией
====================

Разворачивание сайта:
---------------------

Git должен уже быть установлен в системе -  :ref:`gitinst`

1. Копирование Git репозитория.
"""""""""""""""""""""""""""""""

.. code-block:: bash

    $ mkdir ~/Doc
    $ cd Doc/
    $ git clone https://github.com/krugersu/Artix_Global


2. Установка Apache.
""""""""""""""""""""
Установка без настройки брандмауэра.

Установка:
~~~~~~~~~

.. code-block:: bash

    $ sudo apt update
    $ sudo apt install apache2
    $ sudo systemctl status apache2

Получаем вывод вида:    


.. code-block:: bash

    apache2.service - The Apache HTTP Server
    Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
    Active: active (running) since Thu 2020-04-23 22:36:30 UTC; 20h ago
        Docs: https://httpd.apache.org/docs/2.4/
    Main PID: 29435 (apache2)
        Tasks: 55 (limit: 1137)
    Memory: 8.0M
    CGroup: /system.slice/apache2.service
            ├─29435 /usr/sbin/apache2 -k start
            ├─29437 /usr/sbin/apache2 -k start
            └─29438 /usr/sbin/apache2 -k start

Согласно этому выводу сервис успешно запустился. Но лучше ещё запросить страницу Apache, чтобы убедиться, что веб-сервер работает правильно.


3. Управление процессами Apache.
""""""""""""""""""""""""""""""""

Чтобы остановить веб-сервер, введите:

.. code-block:: bash

    $ sudo systemctl stop apache2

Запустить:

.. code-block:: bash

    $ sudo systemctl start apache2

Перезапуск:

.. code-block:: bash

    $ sudo systemctl restart apache2

По умолчанию Apache добавлен в автозагрузку.


4. Настройка виртуальных хостов.
""""""""""""""""""""""""""""""""

На веб-сервере Apache вы можете использовать виртуальные хосты (в Nginx это блоки server) для изоляции настроек и
размещения нескольких доменов на одном сервере. Здесь используется условный домен example.com, который нужно заменить доменом вашего сайта.

В Ubuntu 22.04 веб-сервер Apache по умолчанию предоставляет один включенный виртуальный хост,
который обслуживает каталог /var/www/html. Этого хватит для работы одного сайта, но если вы хотите
разместить несколько сайтов, вам нужно создать новые виртуальные хосты. Создайте структуру каталогов
в /var/www для сайта example.com, а /var/www/html оставьте как каталог по умолчанию, который будет
обслуживаться, если запрос клиента не соответствует другим сайтам.

Создайте каталог для your_domain:

.. code-block:: bash

    $ sudo mkdir /var/www/krudoc

Затем укажите права на каталог с помощью переменной $USER:

.. code-block:: bash

    $ sudo chown -R $USER:$USER /var/www/krudoc

Права должны быть предоставлены, если вы не меняли значение umask, которое устанавливает права файлов по умолчанию. Чтобы убедиться,
что права предоставлены и пользователь может работать с файлами, нужно ввести команду:    

.. code-block:: bash

    $ sudo chmod -R 755 /var/www/krudoc


Далее копируем содержимое каталога  `~/Doc/Artix_Global/build/html` в  `/var/www/krudoc`

.. code-block:: bash

    $ cp -r ~/Doc/Artix_Global/build/html/.  /var/www/krudoc


Нужно создать файл виртуального хоста с правильными директивами, чтобы Apache мог обслуживать этот контент.
Чтобы напрямую не изменять файл конфигурации по умолчанию, расположенный
в `/etc/apache2/sites-available/000-default.conf`, мы создадим новый в `/etc/apache2/sites-available/your_domain.conf``:    

.. code-block:: bash

    $ sudo nano /etc/apache2/sites-available/krudoc.conf


Вставьте в файл следующий блок настроек. Он похож на конфигурации по умолчанию, но содержит правильный домен и каталог:    


.. code-block:: bash

    <VirtualHost *:80>
        ServerAdmin pk69@kruger.su
        ServerName krudoc
        ServerAlias www.krudoc
        DocumentRoot /var/www/krudoc
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
    </VirtualHost>

Обратите внимание, мы обновили DocumentRoot на наш новый каталог, а ServerAdmin на адрес электронной почты,
к которому может получить доступ администратор сайта your_domain. Также мы добавили две директивы: ServerName,
которая устанавливает базовый домен, который должен соответствовать этому определению виртуального хоста,
и ServerAlias – определяет дополнительные имена, которые должны соответствовать базовому имени.

После того, как закончите, сохраните и закройте файл.

Включим файл с помощью a2ensite:

.. code-block:: bash

    $ sudo a2ensite krudoc.conf

Отключите сайт по умолчанию, определенный в 000-default.conf:

.. code-block:: bash

    $ sudo a2dissite 000-default.conf
