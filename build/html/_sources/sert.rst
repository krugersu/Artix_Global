Добавление группы сертификатов со сроком действия через REST API.
-----------------------------------------------------------------

**1. Добавление группы сертификатов со сроком действия через REST API.**

	a. Добавить группу сертификатов в БД КС, сформировав запрос типа POST на url: http://<host>:<port>/Csrest/rest/dictionaries/certificates 	
	b. Тело запроса в формате Json должно быть подобного формата:
		
		.. code-block:: json

			{
				"code": "1",
				"rangefrom": 30,
				"rangeto": 40,	
				"name": "Сертификаты",
				"sum": 300,
				"inputmask": 31,
				"discountcampaign": "test campaign"
			} 

	c. Атрибут свойства  discountcampaign должен содержать yaml акции, в которой как раз можно указать сроки действия.
	   Напрример, если смотреть на уже существующую группу сертификатов, созданную вручную через web-интерфейс LM с указанием срока действия (БД КС ArtixAll, таблица certificateTemp), то в поле discountcampaign увидим запись вида:			


		.. code-block:: yaml

			!!python/object:artixds.domain.DiscountCampaign
			active: true
			beginBonusesDateCalculate: null
			beginBonusesIntervalCondition: !!python/unicode 'date'
			beginBonusesIntervalMetric: !!python/unicode 'day'
			beginBonusesIntervalValue: 0
			beginDate: null
			beginDateWithBeginCurrentMetric: !!python/unicode 'day'
			beginDateWithBeginNextMetric: !!python/unicode 'day'
			beginRangeDate: 2022-02-17
			beginTime: null
			checkedTags: null
			daysOfWeek: []
			discounts: []
			endBonusesDateCalculate: null
			endBonusesIntervalCondition: !!python/unicode 'date'
			endBonusesIntervalMetric: !!python/unicode 'day'
			endBonusesIntervalValue: 0
			endDate: null
			endRangeDate: 2022-02-17
			endTime: null
			id: 57026161735168
			interactionType: all
			labels: null
			manualActivate: null
			name: !!python/unicode ''
			parent: null
			parentGroup: null
			priority: null
			qualifiers: !!set {}
			tagsIsAllowed: false
			weight: 300


		То есть в этом случае срок действия для группы сертификатов определен свойствами beginRangeDate и endRangeDate (от 2022-02-17 до 2022-02-17).

		Берем этот Yaml как шаблон и изменияем даты beginRangeDate и endRangeDate на нужные.			


	d. Далее  этот Yaml необходимо переделать в однострочный формат. Для этого после каждой строки добавляем \r\n, и переносим все строки в одну. В итоге должна получиться строка следующего вида:
		
		::

		!python/object:artixds.domain.DiscountCampaign\r\nactive: true\r\nbeginBonusesDateCalculate: null\r\nbeginBonusesIntervalCondition: !!python/unicode 'date'\r\nbeginBonusesIntervalMetric: !!python/unicode 'day'\r\nbeginBonusesIntervalValue: 0\r\nbeginDate: null\r\nbeginDateWithBeginCurrentMetric: !!python/unicode 'day'\r\nbeginDateWithBeginNextMetric: !!python/unicode 'day'\r\nbeginRangeDate: 2022-02-17\r\nbeginTime: null\r\ncheckedTags: null\r\ndaysOfWeek: []\r\ndiscounts: []\r\nendBonusesDateCalculate: null\r\nendBonusesIntervalCondition: !!python/unicode 'date'\r\nendBonusesIntervalMetric: !!python/unicode 'day'\r\nendBonusesIntervalValue: 0\r\nendDate: null\r\nendRangeDate: 2022-02-17\r\nendTime: null\r\nid: 62331387691573\r\ninteractionType: all\r\nlabels: null\r\nmanualActivate: null\r\nname: !!python/unicode ''\r\nparent: null\r\nparentGroup: null\r\npriority: null\r\nqualifiers: !!set {}\r\ntagsIsAllowed: false\r\nweight: 300


      		И в таком виде эту строку можно добавить в тело POST-запроса (пункт 1.1) вместо записи  test campaign.

**2. Отправляем POST-запрос, указав данные для авторизации (как от  WEB  КЦ)**
	
	.. figure:: images/1.png


Далее убеждаемся что запрос прошел без ошибок и проверяем в web-интерфейсе LM, что создалась группа сертификатов. Открываем эту группу на редактирование и убеждаемся, что сроки действия прописаны корректно.	

	.. figure:: images/2.png


**3. Затем добавляем сертификат на сервер POST-запросом http://<хост>:<порт бонусного сервера/сервера сертификатов>/ACC/rest/v1/cards.**

   Тело запроса должно быть вида:	

   		.. code-block:: json

   			{
				"number":"30",
				"accountNumber":"30",
				"status":"EARN_PAY"
			}


Важно, чтобы значения  number и  accountNumber входили в диапозон номеров созданной группы сертификатов.			