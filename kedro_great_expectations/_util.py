from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def doc(docstring: str) -> Callable[[F], F]:
    """
    Return a decorator that takes a function and replaces its docstring.

    Parameters
    ----------
    docstring : str
        The docstring to replace the original function's docstring with.

    Returns
    -------
    decorator : callable
        A decorator that takes a function and replaces its docstring.
    """

    def decorator(decorated: F) -> F:
        decorated.__doc__ = docstring
        return decorated

    return decorator
