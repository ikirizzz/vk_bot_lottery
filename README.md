# vk_bot_lottery  
Краткое описание
Создавался бот для лотереи: покупатель получает код после покупки и регестрирует его через вк бот, для удобства отслеживания и связи с победителями.

Бот проверяет наличие подписки на соосветствующую группу и имеет следующие кнопки: Общая информация, Правила проведения, Стать участником, Список участников.
Каждый код используется лишь раз (есть проверка)

В качестве базы данных использовался простой json тк реальная бд была бы избыточна.
Любые коды можно генерировать на онлайн сервисах, для их быстрого введения в базу запускается server_manager.py (сравнивает и добавляет новые).
