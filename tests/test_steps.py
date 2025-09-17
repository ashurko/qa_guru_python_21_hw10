import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_with_steps():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Tasks on repo")
    allure.dynamic.story("Example using dynamic labels")
    allure.dynamic.link("https://github.com", name="Testing")
    with allure.step('Открываем Git'):
        browser.open("https://github.com")

    with allure.step('Ищем репозиторий'):
        s('.search-input').click()
        s('#query-builder-test').send_keys("eroshenkoam/allure-example")
        s('#query-builder-test').submit()

    with allure.step('Переходим в репозиторий'):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('Переходим на вкладку Actions'):
        s("#actions-tab").click()

    with allure.step('Проверяем наличие Actions #280'):
        s(by.partial_text("#280")).should(be.visible)