:orphan:



2. Кассовые смены
-----------------

.. rubric:: 
    Старт программы

При первом запуске программы происходит инициализация счетчиков кассовых смен.


.. code-block:: Python
    :linenos:

    """ Main program entry. """
    # Если это первый запуск системы
    if not os.path.exists(fileinit):
        logger.info("First start programs")
        with open(fileinit, 'w', encoding='utf-8') as outfile:
            outfile.write('')    
            init_pr()    

.. rubric:: 
    Подготовительные процедуры


Далее происходит непосредственно работа  с касоовыми сменами. 
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


Создается объект "запрос" для работы с http-запросами.

.. code-block:: Python

    rec_con = request.req1C(rc)

.. rubric:: 
    Открытые кассовые смены

Возвращается список открытых смен с последнего зафиксированого ID смены.

.. code-block:: Python

    l_workshift_open = tData.get_last_workshift_open(rc)

Запросом ка БД кассового сервера возвращается таблица содержащая данные открытых кассовых смен,
у которых ID больше зафиксированного.




Для получения последних открытых смен,
используется функция ``bMysql.get_last_workshift_open(self,rc)``:

.. py:function:: dbMysql.get_last_workshift_open(self,rc)

    Возвращает таблицу с данными последних открытых кассовых смен.

    :param rc: Объект с данными настроек программы.
    :type kind: Объект configparser.
    :return: Результат запроса (список строк данных).
    :rtype: Список



.. code-block:: Python
    :linenos:

    def get_last_workshift_open(self,rc):
        l_date = self.load_last_date_open()
        self._mycursor.execute(diff_data.qrSelect_workshift_open, [l_date])
        l_workshift = self._mycursor.fetchall()
        
        self.tData.get_workshiftid(l_workshift)
        with open('data_open.json', 'w', encoding='utf-8') as f:
            json.dump(l_workshift, f, ensure_ascii=False,
                    indent=4,  default=str)

        return l_workshift

ID открытых кассовых смен из таблицы с данными добавляются в БД SQlite для дальнейшего анализа.


.. code-block:: Python
    :linenos:
    :caption: module: db.py

    def get_workshiftid(self,l_workshift):
        # Формируем список номеров открытых кассовых смен для добавление в БД
        l_wsh = []
        for row in l_workshift:
            l_wsh.append(row[4])
        print(l_wsh)
        self.add_open_workshift(l_wsh)


Если количество новых открытых кассовых смен больше ноля, то отправляем post запрос в :term:`УНФ` с данными по открытым сменам.
в 1С создаются документы "Кассовая смена", со статусом "открыта" и заполняются переданными данными.

.. rubric:: 
    Закрытые кассовые смены

Для получения последних закрытых смен,
используется функция ``bMysql.get_last_workshift(self)``:

.. py:function:: dbMysql.get_last_workshift_open(self)

    Возвращает таблицу с данными последних закрытых кассовых смен.


    :return: Результат запроса (список строк данных).
    :rtype: Список

.. code-block:: Python
    :linenos:



    def get_last_workshift(self):

        l_date = self.load_last_date()
        logger.info('Date of the last closed cash shift - ' + str(l_date))

        # Номера открытых смен в БД        
        l_close_workshift = self.tData.get_close_workshift()
        try:

        if len(l_close_workshift) > 0:                
            self._mycursor.execute(diff_data.qrSelect_workshiftnew.format(",".join([str(i) for i in l_close_workshift])))
                #self._mycursor.execute(diff_data.qrSelect_workshiftnew, [wh],)
        except Exception as e:
            logger.info('Get date from DB - ' + str(l_date))
            logger.exception(e, exc_info=True)

        l_workshift = self._mycursor.fetchall()
        with open('data.json', 'w', encoding='utf-8') as f:
            logging.info('Writing a new date for closed shifts to a file')
            json.dump(l_workshift, f, ensure_ascii=False,
                    indent=4,  default=str)

        self.tData.del_close_workshift(l_workshift)
        return l_workshift


Данные по открытым сменам берутся из БД SQLite, и запрос к кассовому серверу возвращает
данные по сменам из списока открытых смен,  у которых появилась дата закрытия.

Если количество закрытых кассовых смен больше ноля, то отправляем post запрос в :term:`УНФ` с данными по закрытым сменам.
в 1С  документы "Кассовая смена" по списку изменяют  статус на "закрыта" и заполняются переданными данными.
После чего курсор БД закрывается.



