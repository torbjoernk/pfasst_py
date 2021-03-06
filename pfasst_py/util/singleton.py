# coding=utf-8
"""
.. moduleauthor:: Paul Manta
"""


class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the class that should be a singleton.

    The decorated class can define one `__init__` function that takes only the `self` argument. Other than that, there
    are no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method.
    Trying to use `__call__` will result in a `TypeError` being raised.

    .. note::
        Limitations: The decorated class cannot be inherited from.

    .. seealso:: http://stackoverflow.com/a/7346105/588243

    >>> from pfasst_py.util.singleton import Singleton
    >>>
    >>> @Singleton
    ... class Foo:
    ...    def __init__(self):
    ...        print('Foo created')
    >>>
    >>> # f = Foo()  # Error, this isn't how you get the instance of a singleton
    >>> f = Foo.instance()  # Good. Being explicit is in line with the Python Zen
    Foo created
    >>> g = Foo.instance()  # Returns already created instance
    >>> assert(f is g)
    """

    def __init__(self, decorated):
        self._decorated = decorated

    def instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a new instance of the decorated class and calls
        its `__init__` method.
        On all subsequent calls, the already created instance is returned.
        """
        try:
            return self._instance
        except AttributeError:
            # noinspection PyAttributeOutsideInit
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)
