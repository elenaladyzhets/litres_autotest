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

<h3> Список проверок, реализованных в автотестах:</h3>

### UI-тесты

* ✅ Поиск книги (через кнопку/нажатие Enter, а также поиск валидного/невалидного наименования книги)
* ✅ Добавление книги в корзину
* ✅ Удаление книги из корзины
* ✅ Добавление книги в избранное (через страницу книги/корзину)
* ✅ Удаление книги из избранного (через корзину/страницу Отложенного)

### API-тесты

* ✅ Добавление книги в корзину
* ✅ Добавление книги в избранное
* ✅ Удаление книги из избранного
* ✅ Поиск книги (поиск валидного/невалидного наименования книги)

### Mobile-тесты

* ✅ Поиск книги (поиск валидного/невалидного наименования книги)
* ✅ Добавление книги в избранное
* ✅ Удаление книги из избранного

----

### Используемый стэк

<img title="Python" src="attachments/icons/python-original.svg" height="40" width="40"/> <img title="Jira" src="attachments/icons/jira.png" height="40" width="40"/> <img title="Allure Report" src="attachments/icons/Allure_Report.png" height="40" width="40"/> <img title="Allure TestOps" src="attachments/icons/AllureTestOps.png" height="40" width="40"/> <img title="GitHub" src="attachments/icons/github-original.svg" height="40" width="40"/> <img title="Selenoid" src="attachments/icons/selenoid.png" height="40" width="40"/> <img title="Selene" src="attachments/icons/selene.png" height="40" width="40"/> <img title="Pycharm" src="attachments/icons/pycharm.png" height="40" width="40"/> <img title="Telegram" src="attachments/icons/tg.png" height="40" width="40"/> <img title="Jenkins" src="attachments/icons/jenkins-original.svg" height="40" width="40"/> <img title="Android Studio" src="attachments/icons/android_studio.png" height="40" width="40"/> <img title="Appium" src="attachments/icons/appium.png" height="40" width="40"/> <img title="Browserstack" src="attachments/icons/browserstack.png" height="40" width="40"/> 

----

### Локальный запуск
> Перед запуском в корне проекта создать файлы .env и env.credentials с содержимым:
```
SELENOID_LOGIN='user1'
SELENOID_PASS='1234'
SELENOID_URL='selenoid.autotests.cloud'
```
> и 
```
bstack_userName={your browserstack username}
bstack_accessKey={your browserstack password}
```
> соответственно

> Для локального запуска с дефолтными значениями необходимо выполнить команду:

```bash
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest tests
```

#### Получение отчёта:
```bash
allure serve build/allure-results
```

----

### <img width="3%" title="Jenkins" src="attachments/icons/jenkins-original.svg"> Запуск проекта в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/litres_autotest/">Ссылка на проект в Jenkins</a>

#### Параметры сборки
> [!NOTE]
> Параметры сборки не обязательны
```python
TYPE_TEST = ['all', 'api', 'mobile', 'ui'] # Тип автотестов
BROWSER = ['128.0' '127.0'] # Версия браузера
COMMENT = ['litres autotest']
```
#### Запуск автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/litres_autotest/">проект</a>

![jenkins project main page](attachments/pictures/jenkins_project_main_page.png)

2. Нажать "Build with Parameters"
3. Из списка "TYPE_TEST" выбрать тип, который необходимо протестировать
4. Из списка "BROWSER" выбрать версию браузера
4. Нажать "Build"

![jenkins_build](attachments/pictures/jenkins_build.png)

----

### <img width="3%" title="Allure" src="attachments/icons/Allure_Report.png"> Allure отчет
#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/">Общие результаты</a>
![allure_report_overview](attachments/pictures/allure_report_overview.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/#suites">Результаты прохождения теста</a>

![allure_reports_behaviors](attachments/pictures/allure_reports_suites.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/#graph">Графики</a>


![allure_reports_graphs](attachments/pictures/alluere_reports_graphs_1.png)
![allure_reports_graphs](attachments/pictures/alluere_reports_graphs_2.png)

----

### <img width="3%" title="Allure Test Ops" src="attachments/icons/AllureTestOps.png"> Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/4692/dashboards">Ссылка на проект</a>

#### <a target="_blank" href="https://allure.autotests.cloud/project/4692/dashboards">Дашборд с общими показателями тестовых прогонов</a>

![allure_test_ops_dashboards](attachments/pictures/allure_testops_dashboards.png)

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/launches">История запуска тестовых наборов</a>

![allure_testops_launches](attachments/pictures/allure_testops_launches.png)

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/test-cases/28510?treeId=0">Тест кейсы</a>

![allure_testops_suites](attachments/pictures/allure_testops_suites.png)

----

### <img width="3%" title="Jira" src="attachments/icons/jira.png"> Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1429">Ссылка на проект</a>

![jira_project](attachments/pictures/jira_project.png)

----

### <img width="3%" title="Telegram" src="attachments/icons/tg.png"> Оповещения в Telegram
![telegram_allert](attachments/pictures/telegram_allert.png)


----
### <img width="3%" title="UI" src="attachments/icons/monitor.png"> Пример видео прохождения ui-автотеста
![autotest_gif](attachments/video/ui_test.gif)

----

### <img width="3%" title="Mobile" src="attachments/icons/mobile.png"> Пример видео прохождения mobile-автотеста
![autotest_gif](attachments/video/mobile_test.mp4)
