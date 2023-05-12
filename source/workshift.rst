:orphan:



2. Кассовые смены
-----------------


При первом запуске программы происходит инициализация счетчиков кассовых смен.

.. todo:: 

    Проверить насколько это актуально в связи с переходом учета кассовых смен в БД

.. code-block:: Python
    :linenos:

    """ Main program entry. """
    # Если это первый запуск системы
    if not os.path.exists(fileinit):
        logger.info("First start programs")
        with open(fileinit, 'w', encoding='utf-8') as outfile:
            outfile.write('')    
            init_pr()    

Инициализируется объект для работы с БД MySQL.

.. code-block:: Python

    tData = dbMysql.workDb(rc)

В момент инициализации открывается соединение с базой данных (1)  MySQL кассового сервера и создается
курсор (5), так же инициализируется соединение со служебной базой данных SQlite (6).



.. code-block:: Python
    :linenos:
    :caption: module: dbMysql.py

    self.mydb = pymysql.connect(host=rc._sections.artix.server_ip,
                                    database=rc._sections.artix.database,
                                    user=rc._sections.artix.user,
                                    passwd=rc._sections.artix.passwd)
        self._mycursor = self.mydb.cursor()  # cursor created
        self.tData = db.workDb(rc)

