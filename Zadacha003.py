
my_text = "Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. \
Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. \
В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче.\
Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. \
Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил"

removal_list = ["Ну","короче","в общем","Ясен пень","Ээээ..."]

edit_string_as_list = my_text.split()

final_list = [word for word in edit_string_as_list if word not in removal_list]

final_string = ' '.join(final_list)
