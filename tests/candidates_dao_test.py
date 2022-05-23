from app.candidates.dao.candidates_dao import CandidateDAO
import pytest


# Нам пригодится экземпляр DAO, так что мы создадим его в фикстуре
# Но пригодится только один раз, поэтому выносить в conftest не будем
@pytest.fixture()
def candidates_dao():
    candidates_dao_instance = CandidateDAO("./data/candidates.json")
    return candidates_dao_instance


# Задаем, какие ключи ожидаем получать у кандидата
keys_should_be = {"pk", "name", "position"}

class TestCandidateDAO:
    def test_get_all(self, candidates_dao):
        """ Проверяем, верный ли список кандидатов возвращается """
        candidates = candidates_dao.get_all()
        assert type(candidates) == list, "возвращается не список"
        assert len(candidates) > 0, "возвращается пустой список"
        assert set(candidates[0].keys()) == keys_should_be, "неверный список ключей"