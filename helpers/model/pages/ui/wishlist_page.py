from selene import browser, be, have
import allure

from config import config

PATCH_URL='/my-books/liked/'

class WishlistPage:
   def open_wishlist(self):
       with allure.step('Open wishlist page'):
          browser.open(f"{config.base_ui_url}{PATCH_URL}")
          return self

   def remove_book_from_wishlist(self):
       with allure.step('Remove book from wishlist from Wishlist page'):
           browser.element('[data-testid="overlay__trigger"]').should(be.present).should(be.visible).click()
           browser.element('[data-testid="contextMenu__favorites--button"]').should(be.present).should(be.visible).click()
           return self

   def book_should_be_in_wishlist(self, book):
       with allure.step('Check book in wishlist'):
           browser.element('[data-testid="art__title"]').should(be.visible)
           browser.element('[data-testid="art__title"]').should(have.text(book.name))
           browser.element('[data-testid="art__authorName"]').should(have.text(book.author))
           return self

   def book_should_not_be_in_wishlist(self):
       with allure.step('Check empty wishlist'):
           browser.element('.EmptyState_empty__content__bCfgR').should(have.text('Здесь будет все, что вы отложите на потом'))
           return self

wishlist_page = WishlistPage()