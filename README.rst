Plank
=====

Plank is a simple and unopinionated python task runner. Plank doesn't manipulate Python or your environment to run the tasks. Plank doesn't provide any default or template tasks.

.. image:: https://travis-ci.org/atbentley/plank.svg?branch=master
  :target:  https://travis-ci.org/atbentley/plank

.. image:: https://coveralls.io/repos/github/atbentley/plank/badge.svg?branch=master
  :target: https://coveralls.io/github/atbentley/plank?branch=master


Usage
-----

Create a ``planks.py`` file in the project directory containing ``@task`` decorated methods, call them using ``plank task_name``.


Examples
--------

.. code-block:: python

  from plank import task

  @task
  def unit_tests():
      import pytest

      assert pytest.main(['tests/unit']) == 0


Tests
-----

Tests are written using pytest and can be run using plank, ``plank tests``.


License
-------

MIT
