import psycopg2

db_params = {
    'dbname': 'thompsonj2',
    'port': 5432,
    'user': 'thompsonj2',
    'password': 'card262chip',
    'host': 'localhost'
}

create_cities_table = """
CREATE TABLE IF NOT EXISTS topcities (
    city text,
    state text,
    population real,
    latitude real,
    longitude real
);
"""
create_states_table = """
CREATE TABLE IF NOT EXISTS statepop (
    code text,
    state text,
    population real
);
"""

def create_tables():
    try:
        # Connect to the database using the 'with' statement
        with psycopg2.connect(**db_params) as conn:
            with conn.cursor() as cur:
                # Execute the SQL statements to create the tables
                cur.execute(create_cities_table)
                cur.execute(create_states_table)
                # Commit changes are automatic with 'with' statement
                print("Tables created successfully.")
    except psycopg2.DatabaseError as error:
        print(f"Database error: {error}")
    except Exception as error:
        print(f"An error occurred: {error}")

# Main program execution
if __name__ == '__main__':
    create_tables()
