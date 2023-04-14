Внешняя программма
==================

Посмотрим на исходный код:
::

	def del_close_workshift(self,l_workshift):
    	    saveworkshift_del = self._all_db.cursor()       
        	for wh in l_workshift:
            	print('delete - ' + str(wh[5]))
            	saveworkshift_del.execute(diff_data.qrDel_workshift_close,[str(wh[5])])
        	self._all_db.commit()


.. code-block:: python
   :emphasize-lines: 1-3,5

   def add_open_workshift(self,l_workshift):
        # Добавляем открытые смены в БД
            #self._mycursor.execute(diff_data.qrAdd_workshift_open, [l_workshift])
            for wh in l_workshift:
                print('open - ' + str(wh))
                self._cursor.execute(diff_data.qrAdd_workshift_open, [str(wh),])
            self._all_db.commit()



.. table:: Простая таблица со сложной шапкой

    =====  =====  ======
       Inputs     Output
    ------------  ------
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    False  True   True
    True   True   True
    =====  =====  ======


.. csv-table:: CSV-таблица
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"


.. sidebar:: Боковая врезка

   Оформление врезки зависит от используемой HTML-темы.


.. function:: pyfunc()

   Описание функции Python.



.. attention::
	
	Блок Внимание, команда: 


   .. Copyright |copy| 2015, |LibreRussia (TM)| |---| все права защищены.

.. .. |copy| unicode:: 0xA9 .. знак копирайта
.. .. |LibreRussia (TM)| unicode:: LibreRussia U+2122 .. символ торговой марки
.. .. |---| unicode:: U+02014 .. длинное тире        	




.. meta::
   :description: The reStructuredText plaintext markup language
   :keywords: plaintext, markup language
