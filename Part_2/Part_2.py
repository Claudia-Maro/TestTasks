from playwright.sync_api import sync_playwright

def test_example_com():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://example.com")
        print("1. Страница example.com успешно открыта")
        
        title = page.title()
        assert "Example" in title, f"Заголовок не содержит 'Example'. Фактический заголовок: {title}"
        print("2. Заголовок страницы содержит 'Example'")
        
        more_info_link = page.locator("css=a:has-text('More information')")
        assert more_info_link.is_visible(), "Ссылка 'More information' не найдена на странице"
        
        with page.expect_navigation():
            more_info_link.click()
        print("3. Успешно кликнули на 'More information'")
        
        current_url = page.url
        expected_url = "https://www.iana.org/help/example-domains"
        assert current_url == expected_url, (
            f"URL не соответствует ожидаемому. Ожидалось: {expected_url}, Фактический: {current_url}"
        )
        print(f"4. Успешный переход на страницу: {current_url}")
        
        browser.close()

test_example_com()