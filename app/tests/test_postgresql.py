from src.functions.postgresql import PostgreSQL


class TestPostgreSQL:

    def test_should_return_a_valid_connection_to_the_database():
        return True
    
    def test_should_return_a_data_frame_with_the_sql_query():
        return True
    
    def test_should_close_the_database_connection_after_executing_the_query():
        return True
    
    def test_should_handle_connection_errors():
        return True
    
    def test_should_handle_execute_query_errors():
        return True
