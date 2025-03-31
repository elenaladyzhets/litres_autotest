# Фреймворк для автоматизации тестирования сайта "ЛитРес"
> <a target="_blank" href="https://www.litres.ru/">litres.ru</a>

![main page screenshot](/attachments/icons/litres.png)

----

### Особенности проекта

* Оповещения о тестовых прогонах в Telegram
* Отчеты с видео, скриншотом, логами, исходной моделью разметки страницы
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Автоматизация отчетности о тестовых прогонах и тест-кейсах в Jira
* Запуск web/UI автотестов в Selenoid

### Список проверок, реализованных в web/UI автотестах

- [x] Поиск книги (через кнопку/нажатие Enter, а также поиск валидного/невалидного наименования книги)
- [x] Добавление книги в корзину
- [x] Удаление книги из корзины
- [x] Добавление книги в избранное (через страницу книги/корзину)
- [x] Удаление книги из избранного (через корзину/страницу Отложенного)

### Используемый стэк

<img title="Python" src="attachments/icons/python-original.svg" height="40" width="40"/> <img title="Jira" src="attachments/icons/jira.png" height="40" width="40"/> <img title="Allure Report" src="attachments/icons/Allure_Report.png" height="40" width="40"/> <img title="Allure TestOps" src="attachments/icons/AllureTestOps.png" height="40" width="40"/> <img title="GitHub" src="attachments/icons/github-original.svg" height="40" width="40"/> <img title="Selenoid" src="attachments/icons/selenoid.png" height="40" width="40"/> <img title="Selene" src="attachments/icons/selene.png" height="40" width="40"/> <img title="Pycharm" src="attachments/icons/pycharm.png" height="40" width="40"/> <img title="Telegram" src="attachments/icons/tg.png" height="40" width="40"/> <img title="Jenkins" src="attachments/icons/jenkins-original.svg" height="40" width="40"/> 

----

### Локальный запуск
> Перед запуском в корне проекта создать файл .env с содержимым:
```
SELENOID_LOGIN='user1'
SELENOID_PASS='1234'
SELENOID_URL='selenoid.autotests.cloud'
```
> Для запуска web/UI автотестов выполнить:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -s . --browser_version=${BROWSER_VERSION}
```

#### Получение отчёта:
```bash
allure serve build/allure-results
```

----

### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/litres_autotest/">Ссылка</a>

#### Параметры сборки
> [!NOTE]
> Параметры сборки не обязательны
```python
BROWSER_VERSION = ['128.0', '127.0'] # Версия браузера
ENVIRONMENT = ['STAGE', 'PREPROD', 'PROD'] # Окружение
COMMENT = ['litres autotest']
```
#### Запуск автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/litres_autotest/">проект</a>

![jenkins project main page](attachments/pictures/jenkins_project_main_page.png)

2. Нажать "Build with Parameters"
3. Из списка "ENVIRONMENT" выбрать любое окружение
4. Нажать "Build"

![jenkins_build](attachments/pictures/jenkins_build.png)

----

### Allure отчет
#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/">Общие результаты</a>
![allure_report_overview](attachments/pictures/allure_report_overview.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/#suites">Результаты прохождения теста</a>

![allure_reports_behaviors](attachments/pictures/allure_reports_suites.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/#graph">Графики</a>


![allure_reports_graphs](attachments/pictures/alluere_reports_graphs_1.png)
![allure_reports_graphs](attachments/pictures/alluere_reports_graphs_2.png)

----

### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/4692/dashboards">Ссылка на проект</a>

#### <a target="_blank" href="https://allure.autotests.cloud/project/4692/dashboards">Дашборд с общими показателями тестовых прогонов</a>

![allure_test_ops_dashboards](attachments/pictures/allure_testops_dashboards.png)

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/launches">История запуска тестовых наборов</a>

![allure_testops_launches](attachments/pictures/allure_testops_launches.png)

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/test-cases/28510?treeId=0">Тест кейсы</a>

![allure_testops_suites](attachments/pictures/allure_testops_suites.png)

----

### Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1429">Ссылка на проект</a>

![jira_project](attachments/pictures/jira_project.png)

----

### Оповещения в Telegram
![telegram_allert](attachments/pictures/telegram_allert.png)



