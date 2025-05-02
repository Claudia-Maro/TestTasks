# Тест для example.com
##  Требования
- Python 3.7+
- Playwright 1.40.0+
- Браузер Chromium
- Рекомендуемое расширение для просмотра README:
- **Markdown All in One v3.6.3** (для VS Code)
##  Установка 
```
pip install playwright
playwright install chromium
```
## Как запустить тест с GitHub

###
Откройте командную строку (терминал) и выполните:
```
git clone https://github.com/Claudia-Maro/TestTasks.git
cd TestTasks/Part_2
```
### Установка зависимостей
```
pip install playwright
playwright install chromium
```
### Запуск теста
```
python Part_2.py
```
## Что проверяет тест

### 1. Открытие страницы
- Переход на `https://example.com`
- Проверка успешной загрузки страницы

### 2. Проверка заголовка
- Наличие слова "Example" в теге `<title>`

### 3. Проверка ссылки
- Наличие элемента с текстом "More information"
- Возможность кликнуть по ссылке

### 4. Проверка перенаправления
- Корректность конечного URL (`https://www.iana.org/help/example-domains`)
- Успешность перехода после клика
  
