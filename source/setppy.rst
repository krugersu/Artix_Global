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


Установка Git
~~~~~~~~~~~~~~~~

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

.. code-block:: bash
    :linenos:

    $ git clone https://github.com/krugersu/Global
    $ cd Global/
    $ python3 -m venv .venv
    $ source .venv/bin/activate
    $ pip install pysqlite3-binary
    $ pip install -r requirements.txt
    $ cd src/
    $ chmod +x main.py

    





