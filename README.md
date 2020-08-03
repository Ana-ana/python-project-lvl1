#### python-project-lvl1

<a href="https://codeclimate.com/github/Ana-ana/python-project-lvl1/maintainability"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability" /></a>

[![Build Status](https://travis-ci.com/Ana-ana/python-project-lvl1.svg?branch=master)](https://travis-ci.com/Ana-ana/python-project-lvl1)


#### Список команд для скачивания приложения:
- создание окружения 
```bash
python3 -m venv test_even
```
- проверить версию пип 
```bash
python3 -m pip --version
```
- если pip ниже 19 версии, необходимо его обновить 
```bash
python3 -m pip install --upgrade --user pip
```
- Установка пакета из Test Pypiс зависимостями promt(необходимы в поекте и отсутствут в Test Pypi) 
 ```bash
 python3 -m pip install --user --index-url https://test.pypi.org/simple/ ana-ana-brain-games --extra-index-url https://pypi.org/simple/ prompt
 ```
* если не сработала команда выше можно вручную указать последнюю версию приложени(перед установко проверить https://test.pypi.org/project/ana-ana-brain-games/) и ее установить
```bash
pip install -i https://test.pypi.org/simple/ ana-ana-brain-games==0.9.8 
```



#### Создание окружения для разработки.
- Установка зависимостей: 
```bash
poetry install
```
- Тесты:
```bash
make test
```
- Проверка кода линтером Flake8:
```bash
make lint
```
- Установка репозитория:
```bash
poetry config repositories.{login}_brain_games https://test.pypi.org/legacy/
```
- Установка доступа к репозиторию:
```bash
poetry config http-basic.{login}_brain_games {login} {password}
```
- Сборка пакета:
```bash
poetry build
```
- Публикация пакета:
```bash
poetry publish -r {login}_brain_games
```
- Загрузка опубликованного пакета:
```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple {login}_brain_games
```



# Video:
#### Installing package brain-even:

<a href="https://asciinema.org/a/5nmYyPPhCjAl9E6DreSiC9KrD" target="_blank"><img src="https://asciinema.org/a/5nmYyPPhCjAl9E6DreSiC9KrD.svg" /></a>

# Positive brain-even:

<a href="https://asciinema.org/a/D3nmkITRWjYiOXZpckGjTtKl1" target="_blank"><img src="https://asciinema.org/a/D3nmkITRWjYiOXZpckGjTtKl1.svg" /></a>

# Nagativebrain-even:

<a href="https://asciinema.org/a/6M11FGpm2NasUnmuf51inDQaS" target="_blank"><img src="https://asciinema.org/a/6M11FGpm2NasUnmuf51inDQaS.svg" /></a>
_______________________________________________________________


# Installing package brain-calc:

<a href="https://asciinema.org/a/zpyz5WeydosC7XiZ9RCLczykx" target="_blank"><img src="https://asciinema.org/a/zpyz5WeydosC7XiZ9RCLczykx.svg" /></a>

# Positive brain-calc:

<a href="https://asciinema.org/a/KIIX0KANuTEYD8EIKkv0t5dm8" target="_blank"><img src="https://asciinema.org/a/KIIX0KANuTEYD8EIKkv0t5dm8.svg" /></a>

# Negative brain-calc:

<a href="https://asciinema.org/a/DnPAigPySgrWIr8KCSaRfVuzh" target="_blank"><img src="https://asciinema.org/a/DnPAigPySgrWIr8KCSaRfVuzh.svg" /></a>
________________________________________________________________

# Installing brain-progression:

<a href="https://asciinema.org/a/7x2KlZbTlNObbTLGIf3iR3Iuj" target="_blank"><img src="https://asciinema.org/a/7x2KlZbTlNObbTLGIf3iR3Iuj.svg" /></a>

# Positive brain-progression:

<a href="https://asciinema.org/a/VGGEPPY7IOO2Q5y1O3DaGA36h" target="_blank"><img src="https://asciinema.org/a/VGGEPPY7IOO2Q5y1O3DaGA36h.svg" /></a>

# Negative brain-progression:

<a href="https://asciinema.org/a/Y7OVr4BPlfJLB3MdfNFGxuCQ6" target="_blank"><img src="https://asciinema.org/a/Y7OVr4BPlfJLB3MdfNFGxuCQ6.svg" /></a>

_________________________________________________________________

# Installing package brain-prime:

<a href="https://asciinema.org/a/qBshyNABh47BEouhwwGUbm99q" target="_blank"><img src="https://asciinema.org/a/qBshyNABh47BEouhwwGUbm99q.svg" /></a>

# Positive brain-prime:

<a href="https://asciinema.org/a/ItTBp6HdCs1r4PCfzPxqnTomI" target="_blank"><img src="https://asciinema.org/a/ItTBp6HdCs1r4PCfzPxqnTomI.svg" /></a>

# Negative brain-prime:

<a href="https://asciinema.org/a/MgWtv0vx9mZ0Lod84sKa52VDy" target="_blank"><img src="https://asciinema.org/a/MgWtv0vx9mZ0Lod84sKa52VDy.svg" /></a>
