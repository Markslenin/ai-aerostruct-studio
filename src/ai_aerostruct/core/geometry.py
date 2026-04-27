import numpy as np


def naca4_airfoil(code: str = "NACA2412", n: int = 80) -> np.ndarray:
    """Generate normalized NACA 4-digit airfoil points.

    Returns:
        ndarray shape: (2*n, 2), columns are x, z.
    """
    digits = code.upper().replace("NACA", "")
    if len(digits) != 4 or not digits.isdigit():
        raise ValueError(f"Only NACA 4-digit airfoils are supported now: {code}")

    m = int(digits[0]) / 100
    p = int(digits[1]) / 10
    t = int(digits[2:]) / 100

    x = np.linspace(0, 1, n)
    yt = 5 * t * (
        0.2969 * np.sqrt(x)
        - 0.1260 * x
        - 0.3516 * x**2
        + 0.2843 * x**3
        - 0.1015 * x**4
    )

    yc = np.zeros_like(x)
    dyc_dx = np.zeros_like(x)

    if p > 0:
        left = x < p
        right = ~left
        yc[left] = m / p**2 * (2 * p * x[left] - x[left] ** 2)
        yc[right] = m / (1 - p) ** 2 * ((1 - 2 * p) + 2 * p * x[right] - x[right] ** 2)
        dyc_dx[left] = 2 * m / p**2 * (p - x[left])
        dyc_dx[right] = 2 * m / (1 - p) ** 2 * (p - x[right])

    theta = np.arctan(dyc_dx)
    xu = x - yt * np.sin(theta)
    zu = yc + yt * np.cos(theta)
    xl = x + yt * np.sin(theta)
    zl = yc - yt * np.cos(theta)

    upper = np.column_stack([xu, zu])
    lower = np.column_stack([xl[::-1], zl[::-1]])
    return np.vstack([upper, lower])
