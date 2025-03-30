from selene import browser, be, have, command
import allure


class WishlistPage:
   def open_wishlist(self):
       browser.open("my-books/liked/")
       return self

   def removing_book_from_favorites(self):
       with allure.step('Удаление книги из избранного из Отложенные'):
           browser.element('[data-testid="overlay__trigger"]').should(be.visible).click()
           browser.element('[data-testid="contextMenu__favorites--itemContent"]').should(be.visible).click()
           return self

   def book_must_be_added_to_favorites(self, book):
       with allure.step('Проверка книги в избранном'):
           browser.open("my-books/liked/")
           browser.element('[data-testid="art__title"]').should(have.text(book.name))
           browser.element('[data-testid="art__authorName"]').should(have.text(book.author))
           return self

   def book_must_be_removed_from_favorites(self):
       with allure.step('Проверка, что из избранного книга удалилась'):
           browser.element('.EmptyState_empty__content__bCfgR').should(have.text('Здесь будет все, что вы отложите на потом'))
           return self

wishlist_page = WishlistPage()