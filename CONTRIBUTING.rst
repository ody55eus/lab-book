.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every help is valued, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

.. _issues: http://gitlab.com/ody55eus/lab-book/-/issues

Report bugs at issues_.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitLab issues_ for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitLab issues_ for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Implement some new ways to analyze the data and contribute to the  understanding of the data.


Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at issues_.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.

Merge Requests
--------------

To submit a merge request, you must first create a new git branch:

1. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

2. When you're done making changes, check that your changes pass the
   tests (using GitLab CI or local tests).

3. Commit your changes and push your branch to GitLab::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

4. Submit a merge request through the GitLab website.


Merge Request Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~

Before you submit a merge request, check that it meets these guidelines:

1. The merge request should include tests.
2. If the merge request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The merge request should work for Python 3.5, 3.6, 3.7 and 3.8. Check
   http://gitlab.com/ody55eus/lab-book/-/merge_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

    $ python -m unittest discover -s ana/tests/basic
    $ python -m unittest discover -s ana/tests/ana/prepair
    $ python -m unittest discover -s ana/tests/ana/fit
    $ python -m unittest discover -s ana/tests/ana/visualize

Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ git tag add v0.3
$ git push
$ git push --tags

GitLab CI/CD will automatically test your code and the request can be merged
if all tests passes.
