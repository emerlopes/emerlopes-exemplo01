import psycopg2
import pandas as pd

class PostgreSQL:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def get_table_as_dataframe(self, query):
        try:
            connection = self.get_connection()

            df = pd.read_sql_query(query, connection)
            return df

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

        finally:
            # Close the connection
            if connection:
                connection.close()
                print("PostgreSQL connection is closed")

    def get_connection(self):
        try:
            connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            return connection

        except psycopg2.OperationalError as error:
            raise error
