Проект "Рассылочная"

Проект позволяет пользователям создавать почтовые рассылки,
и отправлять их в нужное время с определенной периодичностью

Пока что функционал временных отправок всех рассылок реализован через комманду 
"python manage.py runsending"

В данном проекте имеется:
-Возможность регистрации и смены пароля по эл. почте, редактирование профиля
-Возможность создавать свой список клиентов, писем и рассылок
-Возможность оставлять свои отзывы в разделе "Блог"
-Возможность разово выполнять рассылку
-Группа менеджеров, права которых позволяют мониторить аккаунты пользователей и их данные, блокировать пользователя,
отключать рассылки пользователей, однако запрещающие что-либо в них редактировать


Cодержимое .env находится в файле dotenv-content.txt

Для теста имеется фикстура db.json