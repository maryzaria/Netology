import pytest

from ..main import solution, get_unique_names, course_duration


@pytest.mark.parametrize(
    'a, b, c, expected',
    [(1, 8, 15, (-3.0, -5.0)),
     (1, -13, 12, (12.0, 1.0)),
     (-4, 28, -49, 3.5),
     (1, 1, 1, "no solution")]
)
def test_solution(a, b, c, expected):
    result = solution(a, b, c)
    assert result == expected


def test_get_unique_names():
    result = get_unique_names()
    expected = 'Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим,' \
               ' Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, ' \
               'Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий'
    assert result == expected


@pytest.mark.parametrize(
    'course_name,expected',
    [('Java-разработчик с нуля', 14),
     ('Fullstack-разработчик на Python', 20),
     ('Python-разработчик с нуля', 12),
     ('Frontend-разработчик с нуля', 20)]
)
def test_course_duration(course_name, expected):
    res = course_duration(course_name)
    assert res == expected

