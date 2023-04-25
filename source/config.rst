:orphan:


**Структура файла**



    Файл настроек, это простой "ini" файл с двумя секциями

.. code-block:: ini
    :linenos:


    [one_C]
    queryNumberX = /unf_vz_const/hs/test_s/V1/GetProductRemains 
    lquery = /unf_vz_const/hs/

    shopquery = /unf_vz_const/hs/GetChangeShop/V1/GetShop
    workshift = /unf_vz_const/hs/Workshift/V1/post_workshop
    workshift_open = /unf_vz_const/hs/Workshift/V1/post_workshop_open

    cat_skl = \\192.168.252.250\unf_teleport
    server_ip = 192.168.252.250
    port = 80

    [artix]
    path = world
    tPriceQR = 1 
    server_ip = 10.0.0.239 
    exchange_cat = //10.0.0.239/obmen/dict/  
    enablepricemanual = 1  
    database = documentsAll
    user= netroot 
    passwd= netroot 



.. csv-table:: **Значение параметров**
   :header: "Параметр", "Значение"
   :widths: 15,30

   "queryNumberX", "Запрос для получения остатков по магазину"
   "barcodes", "массив объектов", "Массив дополнительных штрих-кодов"
   "inventitemoptions", "объект", "Опции товара"
   "priceoptions", "объект", "Опции цены"
   "quantityoptions", "объект", "Опции количества"
   "sellrestrictperiods", "массив объектов", "Массив ограничений продаж по времени"