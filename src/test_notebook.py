import marimo

__generated_with = "0.13.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import attoworld as aw
    import matplotlib.pyplot as plt
    return aw, mo, np, plt


@app.cell
def _(mo):
    mo.md(r"""## Check convergence of numerical derivatives""")
    return


@app.cell
def _(aw, np, plt):
    def convergence_check(order, N_pts):
        x = np.linspace(0.0, 2*np.pi, N_pts+1)[0:-1]
        dx = x[1]-x[0]
        y = np.cos(x)
        y_derivative_analytic = -np.sin(x)
        y_derivative = aw.numeric.uniform_derivative(y,1,order,boundary='periodic')/dx
        return np.max(np.abs(y_derivative - y_derivative_analytic))

    N_pts_range = [16, 32, 64, 128, 256, 512]
    order_range = range(1,6)

    convergence_data = np.array([[convergence_check(_order, _n) for _n in N_pts_range] for _order in order_range])

    lines = plt.loglog(N_pts_range,convergence_data.T)
    for order, line in zip(order_range, lines):
        line.set_label(f"{order}")
    plt.xlabel("Number of grid points")
    plt.ylabel("Mean error")
    plt.ylim(1e-15, 0.1)
    plt.legend()
    aw.plot.showmo()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
