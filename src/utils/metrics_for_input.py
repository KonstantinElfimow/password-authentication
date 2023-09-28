import scipy
from scipy import stats as st
import numpy as np


def calculate_confidence_interval(sample: list, alpha: float | None = None, std: float | None = None) -> tuple:
    """
    Функция рассчитывает доверительный интервал для выборки из генеральной совокупности.
    :param sample: выборка из ГС.
    :param alpha: уровень значимости; \
        пример: если нужно рассчитать 95% доверительный интервал, то alpha = 0.05; \
        по умолчанию: alpha = 0.32.
    :param std: стандартное отклонение предыдущих исследований \
        (для ГС большей, чем 30 наблюдений - известно, для выборки из ГС - нет).
    :return: возвращается нижняя и верхняя границы доверительного интервала.
    """
    arr = np.array(sample)
    if arr.ndim != 1 or arr.shape[0] < 2:
        raise ValueError('Передан неверный массив!')

    n = len(arr)
    mean = arr.mean()
    if alpha is None:
        alpha = 0.32

    if n <= 30:
        std_err = arr.std(ddof=n - 1) / np.sqrt(n)
        t_val = st.t.ppf(1 - alpha / 2, n - 1)
        return np.round((mean - std_err * t_val, mean + std_err * t_val), 6)
    else:
        if std is None:
            std = arr.std(ddof=n - 1)
        std_err = std / np.sqrt(n)
        z_val = st.norm(loc=0, scale=1).ppf(1 - alpha / 2)
        return np.round((mean - std_err * z_val, mean + std_err * z_val), 6)