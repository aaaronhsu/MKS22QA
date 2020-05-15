# COVID-19 Data Analysis Project

## Description
A program that graphs some of the effects of COVID-19 including:

* Change in price of certain items
* Change in pollution change estimates
* Confirmed/active/dead/recovered patients

Data is retrieved manually for items and pollution change while the data on patients is retrieved using an [API](https://covid19api.com/#details) who's data is sourced from Johns Hopkins CSSE.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages

```bash
pip install tkinter
pip install matplotlib
pip install requests
pip install pandas
```

## Usage
Edit line 8 to match the path of the root folder
```python
# example path
path = 'D://Python/Data Analysis Project/'
```

## Known Issues

Program crashes if given bad input

Program crashes if start date preceeds 1/22 or end date succeeds yesterday (Deaths button)

## Contributors
* Aaron Hsu
* Ella Krechmer
* Israel Pina
* Logan Byers
* Sasha Motielall
* Maret Rudin-Aulenbach