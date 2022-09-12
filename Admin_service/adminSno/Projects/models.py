from django.db import models
from datetime import datetime
from django.urls import reverse


class Projects(models.Model):
    class Meta:
        db_table = 'Projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    OPEN = '0'
    START = '1'
    IN_PROGRESS = '2'
    TEST = '3'
    FINISH = '4'
    DONE = '5'
    CLOSED = '6'
    INFO_NEED = '7'
    END = '8'

    projects_stage = [
        (OPEN, 'Ведутся переговоры'),
        (START, 'Подписание договора'),
        (IN_PROGRESS, 'В разработке'),
        (FINISH, 'Сдача проекта'),
        (CLOSED, 'Отказ'),
        (INFO_NEED, 'В заморозке'),
        (END, 'Проект закрыт')
    ]

    name = models.TextField(verbose_name='Название проекта')
    create_id = models.DateTimeField(verbose_name='Дата создания')
    descriptions = models.TextField(verbose_name='Описание')
    stage = models.CharField(verbose_name='Стадия', choices=projects_stage, max_length=1, default=OPEN)
    persons = models.ManyToManyField('Person', verbose_name='Состав сотрудников', blank=True)
    notes = models.TextField(verbose_name='Заметки')
    price = models.IntegerField('Стоимость проекта', default=0)

    def __str__(self):
        return self.name


class Courses(models.Model):
    class Meta:
        db_table = 'Courses'
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    name = models.TextField(verbose_name='Название курса')
    descriptions = models.TextField(verbose_name='Описание курса')
    create_id = models.DateTimeField(verbose_name='Дата начало курсов')

    def __str__(self):
        return self.name


class Person(models.Model):
    class Meta:
        db_table = 'Person'
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    JUNIOR = 'J'
    MIDDLE = 'M'
    SENIOR = 'S'

    knowLvl = [
        (JUNIOR, 'JUNIOR'),
        (MIDDLE, 'MIDDLE'),
        (SENIOR, 'SENIOR')
    ]

    PROMOTION = 'P'
    SALE = 'S'
    ADMIN = 'A'
    PM = 'P'
    FRONTEND = 'FRONT'
    BACKEND = 'BACK'
    FULLSTACK = 'FULL'
    TEST = 'TEST'
    LAYOUT = 'LAYOUT'
    WEB_DESIGNER = 'W'

    posit = [
        (PROMOTION, 'Копирайтер/наполнение контента/SMM специалист'),
        (SALE, 'Отдел продаж'),
        (ADMIN, 'Системный администратор'),
        (PM, 'PM Менеджер'),
        (FRONTEND, 'Frontend'),
        (BACKEND, 'Backend'),
        (FULLSTACK, 'Fullstack'),
        (TEST, 'Тестировщик'),
        (LAYOUT, 'Верстальщик'),
        (WEB_DESIGNER, 'Web дизайнер')
    ]

    name = models.CharField(verbose_name='ФИО', max_length=100)
    mail = models.CharField(verbose_name='Эл. почта', max_length=100)
    create_id = models.DateTimeField(verbose_name='Дата вступления')
    description = models.TextField(verbose_name='Опыт/стэк технологий')
    project = models.ManyToManyField(Projects, verbose_name='Проекты', blank=True)
    position = models.CharField(verbose_name='Должность', choices=posit, default=PM, max_length=10)
    rate = models.IntegerField(verbose_name='Ставка в час')
    knowledgeLevel = models.CharField(verbose_name='Уровень знаний', choices=knowLvl, default=JUNIOR, max_length=5)
    link = models.TextField('Ссылка на соц сети')
    visit = models.TextField(verbose_name='Посещения')
    courses = models.ForeignKey(Courses, verbose_name='Курсы', on_delete=models.RESTRICT, blank=True)

    def __str__(self):
        return f'{self.name}'


class TasksProjects(models.Model):
    class Meta:
        db_table = 'TasksProjects'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    name = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание')
    create_id = models.DateTimeField(verbose_name='Дата начала задачи')
    deadline = models.DateTimeField(verbose_name='Дедлайн')
    projects = models.ForeignKey(Projects, verbose_name='Проект', on_delete=models.RESTRICT)
    person = models.ForeignKey(Person, verbose_name='Сотрудник', on_delete=models.RESTRICT)


class Estimate(models.Model):
    class Meta:
        db_table = 'Estimate'
        verbose_name = 'Смета'
        verbose_name_plural = 'Сметы'

    project = models.ForeignKey(Projects, verbose_name='Проект', on_delete=models.RESTRICT)
    promotion = models.IntegerField(verbose_name='Копирайтер/наполнение контента/SMM специалист', default=0)
    sale = models.IntegerField(verbose_name='Отдел продаж', default=0)
    admin = models.IntegerField(verbose_name='Системный администратор', default=0)
    project_manage = models.IntegerField(verbose_name='PM Менеджер', default=0)
    backend = models.IntegerField(verbose_name='Backend', default=0)
    frontend = models.IntegerField(verbose_name='Frontend', default=0)
    fullstack = models.IntegerField(verbose_name='Fullstack', default=0)
    test = models.IntegerField(verbose_name='Тестировщик', default=0)
    layout = models.IntegerField(verbose_name='Верстальщик', default=0)
    web_designer = models.IntegerField(verbose_name='Web дизайнер', default=0)
    manager_1 = models.IntegerField(verbose_name='Управленец 1(Максим)', default=0)
    manager_2 = models.IntegerField(verbose_name='Упраленец 2(Дмитрий)', default=0)
    manager_3 = models.IntegerField(verbose_name='Управленец 3(Валерий)', default=0)





