from sklearn import linear_model
import numpy as np
import numpy.testing as nt


def test_line():
    reg = linear_model.LinearRegression()
    reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

    nt.assert_array_almost_equal(reg.coef_, np.array([0.5, 0.5]))
    nt.assert_almost_equal(reg.intercept_, 0)


def test_ridge():
    reg = linear_model.Ridge(alpha=.5)
    reg.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
    nt.assert_array_almost_equal(reg.coef_, np.array([0.34545455, 0.34545455]))
    nt.assert_almost_equal(reg.intercept_, 0.1363636)
