# Numerical Methods in Python [![Actions Status](https://github.com/cfgnunes/numerical-methods-python/workflows/build/badge.svg)](https://github.com/cfgnunes/numerical-methods-python/actions)

Numerical methods implementation in Python.

For the implementation in MATLAB, see [this repository](https://github.com/cfgnunes/numerical-methods-matlab).

## Начало работы

### Предварительные требования

#### Использование Conda (рекомендуется)

```sh
conda env create
conda activate numerical-methods

```sh
conda env create
conda activate numerical-methods
```

#### Использование Pip

```sh
pip install -r requirements.txt
```

#### Using Ubuntu

Этот раздел предполагает использование Ubuntu 18.04 (также протестировано на Ubuntu 22.04), но процедура аналогична для других дистрибутивов Linux.
```sh
sudo apt -y install python3-numpy
```

### Запуск примеров

Для запуска основного примера используйте:

```sh
python3 main.py

```

## Реализации

### Пределы

- Метод эпсилон-дельта

### Методы решений уравнений

* Метод бисекции
* Метод секущих
* Метод Регула Фальси (ложного положения)
* Метод Пегаса
* Метод Мюллера
* Метод Ньютона

### Интерполяция

* Метод Лагранжа
* Метод Ньютона
* Метод Грегори-Ньютона
* Метод Невилля

### Algorithms for polynomials

* Метод Брио-Руффини
* Метод разделенных разностей Ньютона
* Пределы действительных корней

### Numerical differentiation

* Метод конечных разностей назад
* Метод трех точек
* Метод пяти точек

### Numerical integration

* Составной метод трапеций
* Составной метод Симпсона 1/3
* Метод Ромберга

### Initial-value problems for ordinary differential equations

- Euler's method
- Taylor's (Order Two) method
- Taylor's (Order Four) method
- Runge-Kutta (Order Four) method

### Systems of differential equations

- Runge-Kutta (Order Four) method

### Methods for Linear Systems

- Gaussian Elimination
- Backward Substitution
- Forward Substitution

### Iterative Methods for Linear Systems

- Jacobi method
- Gauss-Seidel method
