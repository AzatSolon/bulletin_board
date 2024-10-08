# bulletin_board

**Дипломный проект: Доска объявлений.**
*Разработать backend-часть для сайта объявлений. Бэкенд-часть проекта предполагает реализацию следующего функционала:*
- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- Восстановление пароля через электронную почту (не обязательно).
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.

*Краткое техническое задание и рекомендации по порядку выполнения:*

**Этап I. Настройка Django-проекта.**

*На данном этапе нам предстоит подготовить наш Django-проект к работе. Данный этап состоит из трех подзадач:*

- Подключение базы данных Postgres.
- Подключение CORS headers.
- Подключение Swagger.
  **Этап II. Создание модели юзера. Настройка авторизации и аутентификации.**

*Создание модели пользователя.*

- Необходимые поля:
- first_name — имя пользователя (строка).
- last_name — фамилия пользователя (строка).
- phone — телефон для связи (строка).
- email — электронная почта пользователя (email) (используется в качестве логина).
- role — роль пользователя, доступные значения: user, admin.
- image - аватарка пользователя
  *Настройка авторизации и аутентификации.*

- На данном этапе мы будем настраивать авторизацию пользователя с помощью библиотеки simple_jwt. Подробнее об этом можно
  узнать в рекомендациях

*Сброс и восстановление пароля через почту*

- Основная сложность при настройке сброса и восстановления пароля через почту — подключение самого почтового ящика,
  через который будет происходить отправка таких сообщений. Как правило, при такой настройке требуется разрешить доступ
  неавторизованным приложениям к используемому почтовому ящику — эти настройки обычно находятся в разделе «Безопасность»
  на сайтах почтовых сервисов. В целом логика сброса пароля с использованием Djoser достаточно проста.

Юзер отправляет POST-запрос на адрес
/users/reset_password/ с содержанием:

  ```json
  {
  "email": "example@mail.com"
} 
  ```

Сервер высылает на почту ссылку вида:

"/<url>/{uid}/{token}" # предварительно это настраивается в settings
Далее идет работа фронта — из данной ссылки парсится uid и токен, который впоследствии передается в JSON вместе с новым
паролем на адрес users/reset_password_confirm — по умолчанию он выглядит именно так. А содержание POST-запроса,
отправляемого на бэкэнд, выглядит следующим образом:

{
"uid": "uid",
"token": "token"
"new_password": "P4$$W0RD"
}
**Этап III. Описание моделей объявлений и отзывов.**

*Модель объявления должна содержать следующие поля:*

- title — название товара.
- price — цена товара (целое число).
- description — описание товара.
- author — пользователь, который создал объявление.
- created_at — время и дата создания объявления.
- Все записи при выдаче должны быть отсортированы по дате создания (чем новее, тем выше).

*Модель отзыва должна содержать следующие поля:*

- text — текст отзыва.
- author — пользователь, который оставил отзыв.
- ad — объявление, под которым оставлен отзыв.
- created_at - время и дата создания отзыва

**Этап IV. Создание views и эндпоинтов.**

- Также наша работа предусматривает реализацию поиска товаров на главной странице по названию. Для выполнения данного
  задания рекомендуем использовать библиотеку django-filter. С документацией можно ознакомиться
  здесь: https://django-filter.readthedocs.io/en/stable/guide/install.html. В рекомендациях есть краткая инструкция по
  использованию фильтров.

- Также обратите внимание на эндпоинты, которые требуют реализации пагинации. Эндпоинт /ads/ требует не более 4 объектов
  на странице (ограничение фронта)

**Этап V. Определение permissions к views.**

*Анонимный пользователь может:*

- получать список объявлений.

*Пользователь может:*

- получать список объявлений,
- получать одно объявление,
- создавать объявление
- редактировать и удалять свое объявление,
- получать список комментариев,
- создавать комментарии,
- редактировать/удалять свои комментарии.

*Администратор может:*

- дополнительно к правам пользователя редактировать или удалять объявления и комментарии любых других пользователей.

**Этап VI. Упаковка в Docker.**

- Создать `Dockerfile` для сборки образа приложения.
- Создать `docker-compose.yml` для запуска приложения и базы данных PostgreSQL.

**Этап VII. Написание тестов.**

- Написать тесты для всех основных функций платформы.
- Использовать библиотеку `pytest` для тестирования.
