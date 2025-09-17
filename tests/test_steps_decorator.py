import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_with_steps_decorator():
    open_page()
    search_repo('eroshenkoam/allure-example')
    go_to_repo('eroshenkoam/allure-example')
    go_to_actions_tab()
    should_be_action_by_number('#280')

@allure.step ('Открываем Git')
def open_page():
    browser.open("https://github.com")

@allure.step ('Ищем репозиторий {repo}')
def search_repo(repo):
    s('.search-input').click()
    s('#query-builder-test').send_keys(repo)
    s('#query-builder-test').submit()

@allure.step ('Переходим в репозиторий {repo}')
def go_to_repo(repo):
    s(by.link_text(repo)).click()

@allure.step ('Переходим на вкладку Actions')
def go_to_actions_tab():
    s("#actions-tab").click()

@allure.step ('Проверяем наличие Actions {number}')
def should_be_action_by_number(number):
    s(by.partial_text(number)).should(be.visible)