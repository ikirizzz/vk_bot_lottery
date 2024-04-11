import vk
import datetime, time
import vk_api
import server_manager
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard,VkKeyboardButton,VkKeyboardColor

VodKoda = 0
def send_message(user_id, message, keyboard = None):
    MSGparametr = {"user_id": user_id,  "message": message,  "random_id": 0}
    if keyboard != None: MSGparametr["keyboard"] = keyboard.get_keyboard()
    session.method("messages.send", MSGparametr)

print("запущено")
while True:
    try:
        session = vk_api.VkApi(token=server_manager.Tosen)
        for event in VkLongPoll(session).listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if VodKoda == 0:
                    text = event.text.lower()
                else:
                    text = event.text
                user_id = event.user_id
                Mans = session.method("groups.getMembers", {"group_id": server_manager.ID_MD})
                if user_id in Mans['items']:
                    if text == "я подписан(а)" or text == "начать":
                        keyboard = VkKeyboard()
                        keyboard.add_button("Общая информация", VkKeyboardColor.PRIMARY)
                        keyboard.add_button("Правила проведения", VkKeyboardColor.PRIMARY)
                        keyboard.add_line()
                        keyboard.add_button("Стать участником", VkKeyboardColor.PRIMARY)
                        keyboard.add_button("Список участников", VkKeyboardColor.PRIMARY)
                        send_message(user_id,
                                     "Хорошо, вот немного о том что может чат-бот в рамках проведения конкурса:",
                                     keyboard)
                    elif text == "Отменить ввод кода" or text == "отменить ввод кода":
                        VodKoda = 0
                        keyboard = VkKeyboard()
                        keyboard.add_button("Общая информация", VkKeyboardColor.PRIMARY)
                        keyboard.add_button("Правила проведения", VkKeyboardColor.PRIMARY)
                        keyboard.add_line()
                        keyboard.add_button("Стать участником", VkKeyboardColor.PRIMARY)
                        keyboard.add_button("Список участников", VkKeyboardColor.PRIMARY)
                        send_message(user_id, "Хорошо, ввод отменен", keyboard)
                    elif text == "общая информация":
                        send_message(user_id, "Выведение информации")
                    elif text == "правила проведения":
                        send_message(user_id, "Выведение правил")
                    elif text == "список участников":
                        mas = server_manager.PPLS_Vivod.split("\n")
                        bilet = ''
                        for i in range(len(mas)):
                            if str(user_id) in mas[i]:
                                bilet += mas[i][:mas[i].find('.')] + ", "
                        if bilet == '':
                            send_message(user_id, server_manager.PPLS_Vivod)
                        else:
                            bilet = "Ваши номера для участия: " + bilet[:len(bilet) - 2] + "\n" + "Ваш id" + str(user_id) + "\n"
                            send_message(user_id, bilet + server_manager.PPLS_Vivod)
                    elif text == "стать участником":
                        VodKoda = 1
                        keyboard = VkKeyboard()
                        keyboard.add_button("Отменить ввод кода", VkKeyboardColor.PRIMARY)
                        send_message(user_id,
                                     "Отлично, согласно условиям, вы должны были получить свой уникальный код. Пожалйста введите(Скопируйте) его.",
                                     keyboard)
                    elif VodKoda == 1 and len(text) == 15:
                        for i in range(len(server_manager.Code0)):
                            if text == server_manager.Code0[i] and server_manager.CodeM[i] != 0:
                                send_message(user_id, "Данный код уже использован, вы можете нажать назад и просмотреть список участников или ввести другой код.")
                            if text == server_manager.Code0[i] and server_manager.CodeM[i] == 0:
                                server_manager.SonJ["Codes"][i+1]["Meth"] = user_id
                                user = session.method("users.get", {"user_ids": user_id})
                                fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
                                server_manager.SonJ["PPLS"].append({"FIO": fullname, "ManID": user_id, "Cod": text})
                                server_manager.re_and_wr(server_manager.SonJ, server_manager.fail)
                                VodKoda = 0
                                keyboard = VkKeyboard()
                                keyboard.add_button("Общая информация", VkKeyboardColor.PRIMARY)
                                keyboard.add_button("Правила проведения", VkKeyboardColor.PRIMARY)
                                keyboard.add_line()
                                keyboard.add_button("Стать участником", VkKeyboardColor.PRIMARY)
                                keyboard.add_button("Список участников", VkKeyboardColor.PRIMARY)
                                send_message(user_id,
                                             "Код настоящий, данные записаны, теперь вы можете увидеть себя в списке участников.",
                                             keyboard)
                                break
                    elif VodKoda == 1 and len(text) != 15:
                        keyboard = VkKeyboard()
                        keyboard.add_button("Отменить ввод кода", VkKeyboardColor.PRIMARY)
                        send_message(user_id,
                                     "Такого кода нет или он был неверно введен. Введите и проверьте код еще раз или нажмите кнопку назад для выхода.",
                                     keyboard)
                else:
                    keyboard = VkKeyboard()
                    keyboard.add_button("Я подписан(а)", VkKeyboardColor.PRIMARY)
                    keyboard.add_openlink_button('Открыть группу', "url_vk gruop")
                    send_message(user_id,"Кажется, вы еще не подписаны на нашу группу.\nДля продолжения подпишитесь на наше сообщество.", keyboard)
    except Exception as e:
        print(str(datetime.datetime.now()) + str(e))
        time.sleep(5)
