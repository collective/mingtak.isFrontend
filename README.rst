.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==================
mingtak.isFrontend
==================

Testing a browserview is(not) a frontend

Examples
--------

In a browserview's python code, you can using below code

    from plone import api

    isFrontendView = api.content.get_view(name='is_frontend', context=context, request=request)

    return isFrontendView(self.view)

    # if self.view is a frontend view, return True, else False


Installation
------------

Install mingtak.isFrontend by adding it to your buildout::

    [buildout]

    ...

    eggs =
        mingtak.isFrontend


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/mingtak.isFrontend/issues
- Source Code: https://github.com/collective/mingtak.isFrontend

License
-------

The project is licensed under the GPLv2.
