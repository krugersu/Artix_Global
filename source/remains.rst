:orphan:


3. Работа с остатками
---------------------

Работа с остатками товара начинается с http-запроса :ref:`GetChangeShop` к :term:`УНФ` с именем метода **"GetShop"**

.. code-block:: Python

    c_shop = rec_con.getQueryShop()

Запрос возвращает список с номерами магазинов, по которым со времени последнего запроса было изменение остатков.    

.. code-block:: Python

    def getQueryShop(self):
        try:
            r = requests.get('http://' + self.mConfig._sections.one_C.server_ip + ':' 
                    + self.mConfig._sections.one_C.port 
                    + self.mConfig._sections.one_C.shopquery,  auth=('Adm', ''))  #  ,auth=('Adm', ''))
            r.encoding = 'utf-8' 
            c_count = r.json()
            listShop = self._getDirM(c_count)
            return listShop
        except Exception as e:
            logger.exception(e, exc_info=False)
        return None     

После получения списка магазинов, если этот список не пустой, начинается обработка данных по каждому магазину.

.. code-block:: Python
    :linenos:
    
    for curShop in c_shop:
        c_count = rec_con.shopForNumber(curShop)
        if not c_count == None:  
            tData = db.workDb(rc)
            tData.uploadData(c_count, curShop)

Отправляется (**2**) http-запрос :ref:`GetProductRemains` к :term:`УНФ` для получения списка номенклатуры с отстатками
по магазину с номером указанном в параметре **"number"**.


.. code-block:: Python
    :linenos:

    def shopForNumber(self,c_shop):
        mPar = {"number":str(c_shop)}
        print(mPar) 
        try:
            n_shop = tortilla.wrap('http://' + self.mConfig._sections.one_C.server_ip + ':' 
                                + self.mConfig._sections.one_C.port 
                                + self.mConfig._sections.one_C.lquery,  auth=('Adm', '')) #,  auth=('Adm', '')
            c_count = n_shop.test_s.get('V1/GetProductRemains?number=' +str(c_shop))
            return c_count
        except Exception as e:
            logger.exception(e, exc_info=False)
        return None


Если в результате выполнения http-запроса :ref:`GetChangeShop` к :term:`УНФ` получены не нулевые остатки, то
создается объект БД SQLite и вызывается функция по заполнению БД SQLite товарами и остатками.

.. code-block:: Python

    tData.uploadData(c_count, curShop)

.. _uploadData:

.. code-block:: Python
    :linenos:

    def uploadData(self,c_count, shop_Number):
        self.createDB()
        logger.debug('Function call - recursive_items(c_count)' )
        self.recursive_items(c_count)
        logger.debug('Function call - calculating_the_amount()' )
        self.calculating_the_amount()
        logger.debug('Function call - delete_analog()' )
        self.delete_analog()
        logger.debug('Function call - delete_null_parent()' )
        self.delete_null_parent()
        logger.debug('Function call - querySales()' )
        self.querySales()
        logger.debug('Function call - calculateSales()' )
        self.calculateSales()
        logger.debug('Function call - ctest_db(shop_Number)' )
        self.test_db(shop_Number)     

В функции :ref:`uploadData <uploadData>` в строке (**2**) пересоздается БД SQLite. Структура БД максимально соответствует структуре 
файла **".aif"** для выгрузки на кассовый сервер.

.. code-block:: Python
   
    def createDB(self):
        with open(self.pathScript, 'r') as sql_file:
            sql_script = sql_file.read()
        self.cursor.executescript(sql_script)
        self._all_db.commit()

В функции :ref:`uploadData <uploadData>` в строке (**4**) данные полученные из :term:`УНФ` записываются в соответствующие таблицы БД SQLite для последующей 
обработки.       

.. code-block:: Python

    def recursive_items(self,dictionary):
        logger.info('Start add DB from 1C')
        count = 0
        self._cursor.executemany(diff_data.qrAddinvent, dictionary.invent,)
        count = count + len(dictionary.invent)
        self._cursor.executemany(diff_data.qrAddadditionalprices, dictionary.additionalprices,)    
        count = count + len(dictionary.additionalprices)
        self._cursor.executemany(diff_data.qrAddBarcodes, dictionary.barcodes,)
        count = count + len(dictionary.barcodes)
        self._cursor.executemany(diff_data.qrAddinventitemoptions, dictionary.inventitemoptions,)        
        count = count + len(dictionary.inventitemoptions)
        self._cursor.executemany(diff_data.qrAddPriceoptions, dictionary.priceoptions,)                    
        count = count + len(dictionary.priceoptions)
        self._cursor.executemany(diff_data.qrAddquantityoptions, dictionary.quantityoptions,)                    
        count = count + len(dictionary.quantityoptions)
        self._cursor.executemany(diff_data.qrAddSellrestrictperiods, dictionary.sellrestrictperiods,) 
        count = count + len(dictionary.sellrestrictperiods)
        self._cursor.execute(diff_data.qrAddOptions)
        self._all_db.commit()                                
        
        # Текущие закрытые кассовые смены по данному обрабатываемому магазину 
        self.sale_dict = dictionary.wsunf
        logger.info('workshift from UNF - ' + str(dictionary.wsunf))    
        logger.info('End add DB from UNF')    
        logger.info('added - ' + str(count) + ' records')    

В функции :ref:`uploadData <uploadData>` в строке (**6**)   Запускается скрипт **"upd.sql"**, который переносит количество товара с аналогов на 
головную номенклатуру.

.. code-block:: SQL
   
    UPDATE invent 
    set remain  = sumItog.summItog 
    FROM (
        SELECT invent.inventcode, (SummIsParent.remain + invent.remain) as summItog FROM SummIsParent 
        INNER JOIN
        invent ON SummIsParent.isParent = invent.inventcode
        ) as sumItog
    WHERE  invent.inventcode  = sumItog.inventcode


В функции :ref:`uploadData <uploadData>` в строке (**8**)  Запускается скрипт **"del_a.sql"**, который удаляет из БД SQLite аналоги
номенклатуры, после перенесения остаков на головную номенклатуру. 

.. code-block:: SQL

    DELETE   FROM invent WHERE  isParent <> ''


В функции :ref:`uploadData <uploadData>` в строке (**10**) Запускается скрипт **"del_a.sql"**, который удаляет из БД SQLite
головную наменклатуру, с нулевым количеством.

.. code-block:: SQL

    DELETE   FROM invent WHERE parent = 1 and remain = 0.0

В функции :ref:`uploadData <uploadData>` в строке (**12**)  Осуществляется запрос в БД MySQL кассового сервера для получения текущих 
продаж, которые еще не были отражены в :term:`УНФ`. (т.е. смена не была закрыта)  


.. code-block:: Python

    def querySales(self):
        for  value in self.sale_dict:    # 
                logger.info('cashcode - ' + str(value['cashcode']))    
                logger.info('shiftnum - ' + str(value['shiftnum']))    
                self._mycursor.execute(diff_data.qrSimpleSelectSale,(value['cashcode'],(value['shiftnum'])),)
                x = []
                rows = self._mycursor.fetchall()
                logger.info('rows - ' + str(rows))    
                for row in rows:
                    x.append(row)
                self._cursor.executemany('INSERT INTO goodsitem VALUES(?,?,?)',x)    
                self._all_db.commit() 


В функции :ref:`uploadData <uploadData>` в строке (**14**) Запускается скрипт **"updateprod.sql"**, который минусует
текущие продажи от полученных остатков.            

.. code-block:: SQL

        UPDATE
	    INVENT
    SET
	    REMAIN = SUMITOG.ITOG
    FROM
	    (
	    SELECT
		    * ,
            CASE WHEN opcode = '50'
            THEN (REMAIN - "SUM(CQUANT)" )
            ELSE (REMAIN + "SUM(CQUANT)" )
            END AS ITOG
	    FROM
		    SUMMPROD
        ) AS SUMITOG
    WHERE
	    INVENT.INVENTCODE = SUMITOG.CODE


        