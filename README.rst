Plank
=====

Plank is a simple and unopinionated python task runner. Plank doesn't manipulate Python or your environment to run the tasks. Plank doesn't provide any default or template tasks.


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


License
-------

MIT
