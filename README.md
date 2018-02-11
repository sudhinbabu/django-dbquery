dbquery: easy sql queries in django
===================================

Example
-------

.. code-block:: python

    >>> from django_dbquery import dbquery
    >>> dbquery("select * from django_migrations limit 4").as_dicts()
    >>> [{'app': 'contenttypes',
		  'applied': datetime.datetime(2018, 1, 20, 16, 54, 41, 836572, tzinfo=<UTC>),
		  'id': 1,
		  'name': '0001_initial'},
		 {'app': 'auth',
		  'applied': datetime.datetime(2018, 1, 20, 16, 54, 42, 905238, tzinfo=<UTC>),
		  'id': 2,
		  'name': '0001_initial'}]

	>>> pk = 2
    >>> dbquery("select * from django_migrations where id= %s limit 4", pk).as_dict()
    >>> {'app': 'auth',
		 'applied': datetime.datetime(2018, 1, 20, 16, 54, 42, 905238, tzinfo=<UTC>),
		 'id': 2,
		 'name': '0001_initial'}


Installation
============

.. code-block:: bash

    $ pip install django-dbquery


Documentation
=============

dbquery is a python class which makes easy sql queries, where the connection part is
expected to be handled by django framework. There are some convenient methods
to strcuture data fetched. Parameters can be passed as positional arguments.


as_dicts()
-----------
When the result contains more than 1 row and column. 
.. code-block:: python
 	>>> dbquery("select * from django_migrations limit 4").as_dicts()
    >>> [{'app': 'contenttypes',
		  'applied': datetime.datetime(2018, 1, 20, 16, 54, 41, 836572, tzinfo=<UTC>),
		  'id': 1,
		  'name': '0001_initial'},
		 {'app': 'auth',
		  'applied': datetime.datetime(2018, 1, 20, 16, 54, 42, 905238, tzinfo=<UTC>),
		  'id': 2,
		  'name': '0001_initial'}]

as_dict()
-----
When the result contains only one 1 row.
.. code-block:: python
 	>>> dbquery("select * from django_migrations where id= %s limit 4", pk).as_dict()
    >>> [{'app': 'contenttypes',
		  'applied': datetime.datetime(2018, 1, 20, 16, 54, 41, 836572, tzinfo=<UTC>),
		  'id': 1,
		  'name': '0001_initial'},
		 {'app': 'auth',
		  'applied': datetime.datetime(2018, 1, 20, 16, 54, 42, 905238, tzinfo=<UTC>),
		  'id': 2,
		  'name': '0001_initial'}]

as_list()
-----
When the result contains values in a single column.
.. code-block:: python
 	>>> dbquery("select * from django_migrations limit 4").as_list()
    >>> [1, 2, 3, 4]

as_value()
-----
When the result contains values in a single column.
.. code-block:: python
 	>>> dbquery("select count(*) from django_migrations limit 4", app).as_value()
    >>> 12


insert, update or delete queries
-----------
for these queries this version will return a dbquery instance but if we try to fetch 
using above methods will give errors. i am planning to add new fetures about meta data in 
next release.
eg:
	>>> dbquery("update  django_content_type set app_label = %s where id = %s", "admin", 1)
	>>> <django_dbquery.dbquery.DBquery at 0x7fccc82a9ac8>



