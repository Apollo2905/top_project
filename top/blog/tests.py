from django.test import TestCase

# Create your tests here.

#ORM:
# Post.objects.all()


#SQL
# SELECT  'blog_post'.'id'
#         'blog_post'.'title'
#         'blog_post'.'text'
#         'blog_post'.'slug'
#         'blog_post'.'date'
#         'blog_post'.'author'
#     FROM 'blog_post'


#______________________________________________________________
#Запрос на вывод определенного объекта класса
# Model.objects.get(field=value) - вернет ОДИН подходящий объект с БД

# где field - поле
# а value - значение, которое должно храниться в этом поле

#Person.objects.get(name='Alex') - означает "выведи
# объект, поле name которого равно значению 'Alex'"


#Person.objects.get(pk=1) - означает "выведи
# объект, pk которого равен 1"



# Model.objects.create() - запрос на создание объекта класса
#При построении запроса необходимо заполнить все обязательные поля
#После отправки запроса, информация в БД сохранится сразу

# Model.objects.all() - вывод всех объектов класса

#Model.objects.filter() - метод вывода нескольких объектов, которые подошли по условию
#Например:
# Person.objects.get(last_name='Smith') - вернул ошибку, так как 2 совадения, а get не умеет
# возвращать 2 объекта с одного запроса. В таких случаях, рациональнее будет воспользоваться filter()

#Person.objects.get(name='Alex').delete()  - удаление одного или нескольких объекта(ов) модели

#Person.objects.filter(pk=2).update(age=25)  - запрос на вывод объекта и изменение информации в нем

#Person.objects.get(name='Alex').delete()  - удалить пользователя

#шаблонизатор - templates
