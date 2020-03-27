
===================
Statistical Sauce
===================
A curated list of definitions and concepts from Statistics.

*Rahul Bhadani*


Design Matrix
=============
In statistics, a design matrix, also known as model matrix or regressor matrix and often denoted by :math:`X`, is a matrix of values of explanatory variables of a set of objects. Each row represents an individual object, with the successive columns corresponding to the variables and their specific values for that object. The design matrix is used in certain statistical models, e.g., the general linear model. It can contain indicator variables (ones and zeros) that indicate group membership in an ANOVA, or it can contain values of continuous variables.

As an example, consider the following Equation:

.. math::
    y_i = \beta_0 = \beta_1 x_i + \epsilon_i


where  :math:`\beta_0` is the y-intercept :math:`\beta_1` is the slope of the regression line. In matrix form, this model can be written as:

.. math::
    \begin {equation}
    \begin{pmatrix}
    y_1\\
    y_2\\
    \vdots\\
    y_n
    \end{pmatrix}
    =
    \begin{pmatrix}
    1 & x_1\\
    1 & x_2\\
    \vdots & \vdots\\
    1 & x_n
    \end{pmatrix}\begin{pmatrix} \beta_0 \\ \beta_1 \end{pmatrix} + \begin{pmatrix}
    \epsilon_1\\
    \epsilon_2\\
    \vdots\\
    \epsilon_n
    \end{pmatrix}
    \end{equation}
