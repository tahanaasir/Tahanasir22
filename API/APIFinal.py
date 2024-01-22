import sqlite3

def create_connection():
    try:
        conn = sqlite3.connect('meals.db')
        return conn
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS meals (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            ingredients TEXT,
            recipe TEXT
        )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def add_meal(conn, meal):
    try:
        sql = ''' INSERT INTO meals(name, ingredients, recipe)
                  VALUES(?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, meal)
        conn.commit()
        print("Meal added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding meal: {e}")

def get_meals(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM meals")
        rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Error fetching meals: {e}")
        return []

def update_meal(conn, meal):
    try:
        sql = ''' UPDATE meals
                  SET name = ?, ingredients = ?, recipe = ?
                  WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, meal)
        conn.commit()
        print("Meal updated successfully!")
    except sqlite3.Error as e:
        print(f"Error updating meal: {e}")

def delete_meal(conn, id):
    try:
        sql = 'DELETE FROM meals WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, (id,))
        conn.commit()
        print("Meal deleted successfully!")
    except sqlite3.Error as e:
        print(f"Error deleting meal: {e}")

def is_valid_choice(choice):
    return choice.isdigit() and 1 <= int(choice) <= 5

def main():
    conn = create_connection()
    if conn is not None:
        create_table(conn)
    else:
        print("Error! Cannot create the database connection.")
        return

    while True:
        print("\nOptions:")
        print("1. Add new meal")
        print("2. Show all meals")
        print("3. Update a meal")
        print("4. Delete a meal")
        print("5. Exit")
        choice = input("Enter choice: ")

        if not is_valid_choice(choice):
            print("Invalid Choice")
            continue

        if choice == '1':
            name = input("Enter meal name: ").strip()
            ingredients = input("Enter ingredients: ").strip()
            recipe = input("Enter recipe: ").strip()
            if name and ingredients and recipe:
                add_meal(conn, (name, ingredients, recipe))
            else:
                print("Invalid input. All fields are required.")

        elif choice == '2':
            meals = get_meals(conn)
            for meal in meals:
                print(meal)

        elif choice == '3':
            meal_id = input("Enter meal id to update: ").strip()
            if meal_id.isdigit():
                name = input("Enter new name: ").strip()
                ingredients = input("Enter new ingredients: ").strip()
                recipe = input("Enter new recipe: ").strip()
                if name and ingredients and recipe:
                    update_meal(conn, (name, ingredients, recipe, meal_id))
                else:
                    print("Invalid input. All fields are required.")
            else:
                print("Invalid meal ID.")

        elif choice == '4':
            meal_id = input("Enter meal id to delete: ").strip()
            if meal_id.isdigit():
                delete_meal(conn, meal_id)
            else:
                print("Invalid meal ID.")

        elif choice == '5':
            conn.close()
            break

if __name__ == '__main__':
    main()