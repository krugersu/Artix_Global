:orphan:



2. Кассовые смены
-----------------


При первом запуске программы происходит инициализация счетчиков кассовых смен.

.. todo:: 

    Проверить насколько это актуально в связи с переходом учета кассовых смен в БД

.. code-block:: Python

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

В момент инициализации создается    