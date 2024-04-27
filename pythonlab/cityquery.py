import psycopg2

db_params = {
    'dbname': 'thompsonj2',
    'port': 5432,
    'user': 'thompsonj2',
    'password': 'card262chip',
    'host': 'localhost'
}

def connect_to_db():
    return psycopg2.connect(**db_params)

def check_northfield():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT latitude, longitude FROM topcities WHERE city = 'Northfield';")
    result = cur.fetchone()
    cur.close()
    conn.close()
    if result:
        print(f"Northfield is located at Latitude: {result[0]} and Longitude: {result[1]}")
    else:
        print("Northfield is not in the database.")

def largest_population_city():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT city FROM topcities ORDER BY population DESC LIMIT 1;")
    result = cur.fetchone()
    cur.close()
    conn.close()
    print(f"The city with the largest population is: {result[0]}")

def smallest_population_city_mn():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT city FROM topcities WHERE state = 'Minnesota' ORDER BY population ASC LIMIT 1;")
    result = cur.fetchone()
    cur.close()
    conn.close()
    print(f"The city in Minnesota with the smallest population is: {result[0]}")

def furthest_cities():
    directions = ['North', 'East', 'South', 'West']
    queries = [
        "SELECT city FROM topcities ORDER BY latitude DESC LIMIT 1;",
        "SELECT city FROM topcities ORDER BY longitude DESC LIMIT 1;",
        "SELECT city FROM topcities ORDER BY latitude ASC LIMIT 1;",
        "SELECT city FROM topcities ORDER BY longitude ASC LIMIT 1;"
    ]
    for direction, query in zip(directions, queries):
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchone()
        cur.close()
        conn.close()
        print(f"The city furthest {direction} is: {result[0]}")

def total_population_by_state():
    state_input = input("Enter a State name or abbreviation: ").strip()
    conn = connect_to_db()
    cur = conn.cursor()
    # This checks if the input is an abbreviation
    cur.execute("SELECT state FROM statepop WHERE code = %s;", (state_input.upper(),))
    state_name = cur.fetchone()
    if state_name:
        state_input = state_name[0]
    cur.execute("SELECT SUM(population) FROM topcities WHERE state = %s;", (state_input,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    if result and result[0]:
        print(f"The total population of all the cities in {state_input} is: {result[0]}")
    else:
        print(f"No data found for the state: {state_input}")

def main():
    check_northfield()
    largest_population_city()
    smallest_population_city_mn()
    furthest_cities()
    total_population_by_state()

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"An error occurred: {error}")
