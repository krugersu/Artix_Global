Примеры
=======


:what: Field lists map field names to field bodies, like
        database records.  They are often part of an extension
        syntax.

:how: The field marker is a colon, the field name, and a
       colon.

        The field body may contain one or more body elements,
        indented relative to the field marker.

------

-a            command-line option "a"
-b file       options can have arguments
              and long descriptions
--long        options can be long also
--input=file  long options can also have
              arguments
/V            DOS/VMS-style options too        

------


Literal blocks are either indented or line-prefix-quoted blocks,
and indicated with a double-colon ("::") at the end of the
preceding paragraph (right here -->)::

    if literal_block:
        text = 'is left as-is'
        spaces_and_linebreaks = 'are preserved'
        markup_processing = None


-----

Block quotes consist of indented body elements:

    This theory, that is mine, is mine.

    -- Anne Elk (Miss)        


----


>>> print 'Python-specific usage examples; begun with ">>>"'
Python-specific usage examples; begun with ">>>"
>>> print '(cut and pasted from interactive Python sessions)'
(cut and pasted from interactive Python sessions)


------  


+------------------------------+
| paragraph                    |
|                              |
+------------------------------+

+------------------------------+
| paragraph                    |
|                              |
+------------------------------+


------


- This is the first bullet list item.  The blank line above the
  first list item is required; blank lines between list items
  (such as below this paragraph) are optional.

- This is the first paragraph in the second item in the list.

  This is the second paragraph in the second item in the list.
  The blank line above this paragraph is required.  The left edge
  of this paragraph lines up with the paragraph above, both
  indented relative to the bullet.

  - This is a sublist.  The bullet lines up with the left edge of
    the text blocks above.  A sublist is a new list so requires a
    blank line above and below.

- This is the third item of the main list.

This paragraph is not part of the list.

-----



+-------+----------------------+
| "1. " | list item            |
+-------| (body elements)+     |
        +----------------------+



------


term 1
    Definition 1.

term 2
    Definition 2, paragraph 1.

    Definition 2, paragraph 2.

term 3 : classifier
    Definition 3.

term 4 : classifier one : classifier two
    Definition 4.

\-term 5
    Without escaping, this would be an option list item.


-----


+----------------------------+
| term [ " : " classifier ]* |
+--+-------------------------+--+
   | definition                 |
   | (body elements)+           |
   +----------------------------+



------


:Date: 2001-08-16
:Version: 1
:Authors: - Me
          - Myself
          - I
:Indentation: Since the field marker may be quite long, the second
   and subsequent lines of the field body do not have to line up
   with the first line, but they must be indented relative to the
   field name marker, and they must line up with each other.
:Parameter i: integer


-----


+--------------------+----------------------+
| ":" field name ":" | field body           |
+-------+------------+                      |
        | (body elements)+                  |
        +-----------------------------------+


-------



This is a typical paragraph.  An indented literal block follows.

::

    for a in [5,4,3,2,1]:   # this is program code, shown as-is
        print a
    print "it's..."
    # a literal block continues until the indentation ends

This text has returned to the indentation of the first paragraph,
is outside of the literal block, and is therefore treated as an
ordinary paragraph.


------

Paragraph:

::

    Literal block


-----


Paragraph: ::

    Literal block


------


Paragraph::

    Literal block


------



+------------------------------+
| paragraph                    |
| (ends with "::")             |
+------------------------------+
   +---------------------------+
   | indented literal block    |
   +---------------------------+


-----


+------------------------------+
| paragraph                    |
| (ends with "::")             |
+------------------------------+
+------------------------------+
| ">" per-line-quoted          |
| ">" contiguous literal block |
+------------------------------+


-----


Take it away, Eric the Orchestra Leader!

    | A one, two, a one two three four
    |
    | Half a bee, philosophically,
    |     must, *ipso facto*, half not be.
    | But half the bee has got to be,
    |     *vis a vis* its entity.  D'you see?
    |
    | But can a bee be said to be
    |     or not to be an entire bee,
    |         when half the bee is not a bee,
    |             due to some ancient injury?
    |
    | Singing...


-----


* List item.

..

    Block quote 3.


-----


This is an ordinary paragraph.

>>> print 'this is a Doctest block'
this is a Doctest block

The following is a literal block::

    >>> This is not recognized as a doctest block by
    reStructuredText.  It *will* be recognized by the doctest
    module, though!

-----


+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+



-----

.. note:: This is a paragraph

   - Here is a bullet list.

----

|Michael| and |Jon| are our widget-wranglers.

.. |Michael| user:: mjones
.. |Jon|     user:: jhl


-----

.. This is a comment
..
   _so: is this!
..
   [and] this!
..
   this:: too!
..
   |even| this:: !

.. [this] however, is a citation.


-----

*тест*
**тест**
`тест`
``тест``
|тест|

This text is an example of ``inline literals``.

The regular expression ``[+-]?(\d+(\.\d*)?|\.\d+)`` matches
floating-point numbers (without exponents).



------

.. code-block::
   :caption: A cool example
   
        The output of this line starts with four spaces.


.. code-block::

        The output of this line has no spaces at the beginning.


-----


.. function:: foo(x)
            foo(y, z)
    :module: some.module.name

    Return a line of text input from the user.


-----

:fieldname: Field content


-----


def my_function(my_arg, my_other_arg):
    """A function just for me.

    :param my_arg: The first of my arguments.
    :param my_other_arg: The second of my arguments.

    :returns: A message (just for me, of course).
    """

-----


This is a normal text paragraph. The next paragraph is a code sample::

    It is not processed in any way, except
    that the indentation is removed.

    It can span multiple lines.

This is a normal text paragraph again.


-----

.. list-table:: Frozen Delights!
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!


-----

.. contents:: Here's a very long Table of
    Contents title

-----



.. sidebar:: Optional Sidebar Title
   :subtitle: Optional Sidebar Subtitle

   Subsequent indented lines comprise
   the body of the sidebar, and are
   interpreted as body elements.

----


"To Ma Own Beloved Lassie: A Poem on her 17th Birthday", by
Ewan McTeagle (for Lassie O'Shea):

    .. line-block::

        Lend us a couple of bob till Thursday.
        I'm absolutely skint.
        But I'm expecting a postal order and I can pay you back
            as soon as it comes.
        Love, Ewan.

-----


.. parsed-literal::

   ( (title_, subtitle_?)?,
     decoration_?,
     (docinfo_, transition_?)?,
     `%structure.model;`_ )

---------


.. code-block:: Python
    :emphasize-lines: 1-3,5
    :linenos:
    
    """ Main program entry. """
    # Если это первый запуск системы
    if not os.path.exists(fileinit):
        logger.info("First start programs")
        with open(fileinit, 'w', encoding='utf-8') as outfile:
            outfile.write('')    
            init_pr()    

------


.. seealso::

   Module :py:mod:`zipfile`
      Documentation of the :py:mod:`zipfile` standard module.

   `GNU tar manual, Basic Tar Format <http://link>`_
      Documentation for tar archive files, including GNU tar extensions.