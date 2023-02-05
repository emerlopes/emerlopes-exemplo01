from src.functions.postgresql import PostgreSQL
import psycopg2
import pytest
import pandas as pd
from pytest import mark
from unittest.mock import MagicMock, patch


def test_get_connection_success():
    db = Database(host='localhost', database='mydb', user='user', password='password')
    connection = db.get_connection()
    assert connection is not None

def test_get_connection_failure():
    # Criação de um objeto fictício de conexão com dados inválidos
    postgresql = PostgreSQL(host='invalid', database='mydb', user='myuser', password='mypassword')

    # Chama a função e verifica se o erro é lançado corretamente
    with pytest.raises(psycopg2.OperationalError):
        postgresql.get_connection()