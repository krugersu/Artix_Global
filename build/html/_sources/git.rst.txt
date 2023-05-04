
Установка и настройка Gitea
===========================

Git должен уже быть установлен в системе -  :ref:`gitinst`

Ссылка на сайт с полной инструкцией_ 

.. _инструкцией: https://routerus.com/how-to-install-gitea-on-ubuntu-18-04/#Настроить_Gitea


1. Подготовка
"""""""""""""

Gitea поддерживает SQLite, PostgreSQL и MySQL / MariaDB в качестве серверной части базы данных.

Мы будем использовать SQLite в качестве базы данных для Gitea. Если SQLite не установлен в вашей
системе Ubuntu, вы можете установить его, введя следующие команды от имени пользователя sudo :


.. code-block:: bash

    $ sudo apt update
    $ sudo apt install sqlite3

2. Установка Gitea    
""""""""""""""""""

Проверьте установку, отобразив версию Git:

.. code-block:: bash

    $ git --version

.. code-block:: bash

    $ git version 2.34.1

3. Создайте пользователя Git
""""""""""""""""""""""""""""

Создайте нового системного пользователя, который будет запускать приложение Gitea, набрав:

.. code-block:: bash

    $ sudo adduser --system --group --disabled-password --shell /bin/bash --home /home/git --gecos 'Git Version Control' git

Команда создаст нового пользователя и группу с именем git и установит домашний каталог в /home/git . Результат будет выглядеть примерно так:

.. code-block:: bash

    Adding system user `git' (UID 111) ...
    Adding new group `git' (GID 116) ...
    Adding new user `git' (UID 111) with group `git' ...
    Creating home directory `/home/git' ...

4. Скачать бинарный файл Gitea
""""""""""""""""""""""""""""""

Посетите страницу загрузки Gitea и загрузите последнюю версию двоичного файла для вашей архитектуры.
На момент написания последняя версия — 1.19.3. Если доступна новая версия, измените переменную VERSION в приведенной ниже команде.

Загрузите двоичный файл Gitea в каталог /tmp используя следующую команду wget :

.. code-block:: bash

    $ wget sudo wget -O /tmp/gitea https://dl.gitea.com/gitea/1.19.3/gitea-1.19.3-linux-amd64

gitea файл gitea можно запускать из любого места. Мы будем следовать соглашению и переместим двоичный файл в каталог `/usr/local/bin` :    

.. code-block:: bash

    $ sudo mv /tmp/gitea /usr/local/bin

Сделайте двоичный исполняемый файл:

.. code-block:: bash

    $ sudo chmod +x /usr/local/bin/gitea

Выполните следующие команды, чтобы создать каталоги и установить необходимые разрешения и владение :

.. code-block:: bash

    $ sudo mkdir -p /var/lib/gitea/{custom,data,indexers,public,log}
    $ sudo chown git: /var/lib/gitea/{data,indexers,log}
    $ sudo chmod 750 /var/lib/gitea/{data,indexers,log}
    $ sudo mkdir /etc/gitea
    $ sudo chown root:git /etc/gitea
    $ sudo chmod 770 /etc/gitea

Указанная выше структура каталогов рекомендована официальной документацией Gitea.
Разрешения для каталога `/etc/gitea` установлены на 770 чтобы мастер установки мог создать файл конфигурации.

5. Создайте файл модуля Systemd
"""""""""""""""""""""""""""""""

Gitea предоставляет файл модуля Systemd, который уже настроен в соответствии с нашей настройкой.
Загрузите файл в каталог `/etc/systemd/system/` , набрав:

.. code-block:: bash

    $ sudo wget https://raw.githubusercontent.com/go-gitea/gitea/master/contrib/systemd/gitea.service -P /etc/systemd/system/

После этого включите и запустите службу Gitea:

.. code-block:: bash

    $ sudo systemctl daemon-reload
    $ sudo systemctl enable --now gitea

Убедитесь, что служба запущена успешно:

.. code-block:: bash

    $ sudo systemctl status gitea


.. code-block:: bash

        gitea.service - Gitea (Git with a cup of tea)
        Loaded: loaded (/etc/systemd/system/gitea.service; enabled; vendor preset: enabled)
        Active: active (running) since Sat 2020-01-04 21:27:23 UTC; 3s ago
    Main PID: 14804 (gitea)
        Tasks: 9 (limit: 1152)
        CGroup: /system.slice/gitea.service
                └─14804 /usr/local/bin/gitea web --config /etc/gitea/app.ini
    ...

6. Настроить Gitea
""""""""""""""""""

Теперь, когда Gitea загружена и запущена, пора завершить установку через веб-интерфейс.
По умолчанию Gitea прослушивает подключения через порт 3000 на всех сетевых интерфейсах.
Если на вашем сервере работает брандмауэр UFW , вам нужно открыть порт Gitea:

Откройте браузер, введите http://YOUR_DOMAIN_IR_IP:3000

Настройки базы данных:

#. Тип базы данных: SQLite3
#. Путь: используйте абсолютный путь, `/var/lib/gitea/data/gitea.db`


Общие настройки приложения:

#. Заголовок сайта: введите название вашей организации.
#. Корневой путь репозитория: оставьте значение по умолчанию `/home/git/gitea-repositories` .
#. Корневой путь Git LFS: оставьте значение по умолчанию `/var/lib/gitea/data/lfs` .
#. Запуск от имени пользователя: git
#. Домен SSH-сервера: введите IP-адрес вашего домена или сервера.
#. Порт SSH: 22, измените его, если SSH прослушивает другой порт
#. Порт прослушивания HTTP Gitea: 3000
#. Базовый URL Gitea: используйте http и IP-адрес вашего домена или сервера.
#. Путь к `/var/lib/gitea/log` : оставьте значение по умолчанию `/var/lib/gitea/log`

Вы можете изменить настройки в любое время, отредактировав файл конфигурации Gitea.
После этого нажмите кнопку «Установить Gitea». Установка происходит мгновенно.
По завершении вы будете перенаправлены на страницу входа.
Щелкните ссылку «Зарегистрироваться сейчас». Первый зарегистрированный пользователь
автоматически добавляется в группу администратора.

Измените разрешения файла конфигурации Gitea на доступ только для чтения, используя:

.. code-block:: bash

    $ sudo chmod 750 /etc/gitea
    $ sudo chmod 640 /etc/gitea/app.ini


Вот и все. Gitea установлена на вашем компьютере с Ubuntu.


7. Обновление Gitea
"""""""""""""""""""

Чтобы обновить Gitea до последней версии, просто скачайте и замените двоичный файл.

1. Остановите сервис Gitea:

.. code-block:: bash

    $ sudo systemctl stop gitea

2. Загрузите последнюю версию Gitea и переместите ее в каталог /usr/local/bin :

.. code-block:: bash

    $ VERSION=<THE_LATEST_GITEA_VERSION>
    $ wget -O /tmp/gitea https://dl.gitea.io/gitea/${VERSION}/gitea-${VERSION}-linux-amd64
    $ sudo mv /tmp/gitea /usr/local/bin

3. Сделайте двоичный исполняемый файл:

.. code-block:: bash

    $ sudo chmod +x /usr/local/bin/gitea

4. Перезапустите сервис Gitea:

.. code-block:: bash

    $ sudo systemctl restart gitea
