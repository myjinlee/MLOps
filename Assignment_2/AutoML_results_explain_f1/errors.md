## Error for Ensemble

can't multiply sequence by non-int of type 'float'
Traceback (most recent call last):
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\pandas\core\ops\array_ops.py", line 218, in _na_arithmetic_op
    result = func(left, right)
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\pandas\core\computation\expressions.py", line 242, in evaluate
    return _evaluate(op, op_str, a, b)  # type: ignore[misc]
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\pandas\core\computation\expressions.py", line 73, in _evaluate_standard
    return op(a, b)
TypeError: can't multiply sequence by non-int of type 'float'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\supervised\base_automl.py", line 1179, in _fit
    trained = self.ensemble_step(
        is_stacked=params["is_stacked"]
    )
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\supervised\base_automl.py", line 426, in ensemble_step
    self.keep_model(self.ensemble, ensemble_subpath)
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\supervised\base_automl.py", line 304, in keep_model
    self.select_and_save_best()
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\supervised\base_automl.py", line 1368, in select_and_save_best
    ldb = self.get_leaderboard(original_metric_values=True)
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\supervised\base_automl.py", line 281, in get_leaderboard
    ldb["metric_value"] *= -1.0
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\pandas\core\generic.py", line 12729, in __imul__
    return self._inplace_method(other, type(self).__mul__)  # type: ignore[operator]
           ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\pandas\core\generic.py", line 12689, in _inplace_method
    result = op(self, other)
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\pandas\core\ops\common.py", line 76, in new_method
    return method(self, other)
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\pandas\core\arraylike.py", line 202, in __mul__
    return self._arith_method(other, operator.mul)
           ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\pandas\core\series.py", line 6135, in _arith_method
    return base.IndexOpsMixin._arith_method(self, other, op)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\pandas\core\base.py", line 1382, in _arith_method
    result = ops.arithmetic_op(lvalues, rvalues, op)
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\pandas\core\ops\array_ops.py", line 283, in arithmetic_op
    res_values = _na_arithmetic_op(left, right, op)  # type: ignore[arg-type]
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\pandas\core\ops\array_ops.py", line 227, in _na_arithmetic_op
    result = _masked_arith_op(left, right, op)
  File "c:\Users\jin89\MLOps_practice\Assignment_2\env2\Lib\site-packages\pandas\core\ops\array_ops.py", line 182, in _masked_arith_op
    result[mask] = op(xrav[mask], y)
                   ~~^^^^^^^^^^^^^^^
TypeError: can't multiply sequence by non-int of type 'float'


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

