import time
from typing import List, Optional, Any
from numbers import Number
import numpy as np
from pprint import pprint

_BASIC_TEST = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

_SMALL = list(np.random.randint(0, int(1e10), 10, 'int64'))
_NORMAL = list(np.random.randint(0, int(1e10), int(1e3), 'int64'))
_BIG = list(np.random.randint(0, int(1e10), int(1e4), 'int64'))
_LARGE = list(np.random.randint(0, int(1e10), int(1e5), 'int64'))


def _measure_sub(func, test: List) -> float:
    timing = time.time()
    func(test)
    return time.time() - timing


def measure(func, test: Optional[List[Number]] = None, verbose: bool = True) -> Any:
    """
        Measure time to sort test array

        Parameters
        ----------
        - func : function to test
        - test : test array, time_test.TEST by default
                 'small' : array with size 10
                 'normal' : array with size 1000
                 'big' : array with size 10000
                 'large' : array with size 100000
        - verbose : if True prints timing, if False only returns it

        Returns
        -------
        timing : time to sort test array
    """
    _test = None
    if test:
        if isinstance(test, str):
            test = test.lower()
            if test == 'small':
                _test = _SMALL.copy()
            if test == 'normal':
                _test = _NORMAL.copy()
            if test == 'big':
                _test = _BIG.copy()
            if test == 'large':
                _test = _LARGE.copy()
        else:
            if isinstance(test, list):
                _test = test.copy()
            else:
                raise ValueError(
                    "'test' parameter must be list to sort or string ('SMALL', 'NORMAL', 'BIG')")
    else:
        _test = _NORMAL.copy()

    if isinstance(func, list):
        result = {}
        for f in func:
            result[f.__name__] = _measure_sub(f, _test)
        result = dict(sorted(result.items(), key=lambda item: item[1]))
    else:
        result = _measure_sub(func, _test)

    if verbose:
        pprint(result, sort_dicts=False)

    return result
