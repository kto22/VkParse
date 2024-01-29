import func

token = input("Введите ваш токен: ")
You = input("Введите ваше имя: ")
user_name = input("Введите имя пользователя, с кем вы вели переписку: ")
user_id = int(input("Введите ID пользователся, с которым вели переписку: "))

func.downloader(token, user_id)
func.repeat_filt()
func.csv_table_maker(You, user_name)
