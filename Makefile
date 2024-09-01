# Устанавливает зависимости проекта через Poetry
install:
	poetry install

# Запускает команду brain-games
brain-games:
	poetry run brain-games

# Собирает пакет
build:
	poetry build

# Публикует пакет (отладочная публикация)
publish:
	poetry publish --dry-run

# Устанавливает собранный пакет
package-install:
	python3 -m pip install --user dist/*.whl