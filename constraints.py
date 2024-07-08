import sqlite3
from datetime import datetime

conn = sqlite3.connect('events.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS events (
               id INTEGER PRIMARY KEY,
               name TEXT,
               date DATE,
               time TIME,
               items TEXT
               )''')
conn.commit()

def add_event(event_name, event_date, event_time, items):
    try:
        
        cur.execute("INSERT INTO events (name, date, time, items) VALUES (?, ?, ?, ?)",
                    (event_name, event_date, event_time, str(items)))
        conn.commit()
        print("Event added successfully")
    except sqlite3.Error as e:
        print(f"Error adding event: {e}")

def edit_event(event_id, event_name, event_date, event_time, items):
    try:
       
        cur.execute("UPDATE events SET name=?, date=?, time=?, items=? WHERE id=?",
                    (event_name, event_date, event_time, str(items), event_id))
        conn.commit()
        print("Event updated successfully")
    except sqlite3.Error as e:
        print(f"Error updating event: {e}")

def delete_event(event_id):
    try:
        
        cur.execute("DELETE FROM events WHERE id=?", (event_id,))
        conn.commit()
        print("Event deleted successfully")
    except sqlite3.Error as e:
        print(f"Error deleting event: {e}")

def display_events():
    try:
        
        cur.execute("SELECT * FROM events")
        rows = cur.fetchall()

        if not rows:
            print("No events found")
        else:
            print("Events:")
            for row in rows:
                print(f"Event ID: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Date: {row[2]}")
                print(f"Time: {row[3]}")
                print("Items:")
                items = eval(row[4]) 
                for item in items:
                    print(f"{item['item']} - {item['price']}")
                print()
    except sqlite3.Error as e:
        print(f"Error displaying events: {e}")

def search_events_by_date(search_date):
    try:
        # Search events by date
        cur.execute("SELECT * FROM events WHERE date=?", (search_date,))
        rows = cur.fetchall()

        if not rows:
            print(f"No events found on {search_date}")
        else:
            print(f"Events on {search_date}:")
            for row in rows:
                print(f"Event ID: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Time: {row[3]}")
                print("Items:")
                items = eval(row[4])  
                for item in items:
                    print(f"{item['item']} - {item['price']}")
                print()
    except sqlite3.Error as e:
        print(f"Error searching events by date: {e}")

def search_events_by_time(search_time):
    try:
        
        cur.execute("SELECT * FROM events WHERE time=?", (search_time,))
        rows = cur.fetchall()

        if not rows:
            print(f"No events found at {search_time}")
        else:
            print(f"Events at {search_time}:")
            for row in rows:
                print(f"Event ID: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Date: {row[2]}")
                print("Items:")
                items = eval(row[4])  
                for item in items:
                    print(f"{item['item']} - {item['price']}")
                print()
    except sqlite3.Error as e:
        print(f"Error searching events by time: {e}")

def main():
    while True:
        print("\n1. Add event\n2. Edit event\n3. Delete event\n4. Display events\n5. Search events by date\n6. Search events by time\n7. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            event_name = input("Event name: ")
            event_date = input("Event date (YYYY-MM-DD): ")
            event_time = input("Event time (HH:MM): ")

            try:
                datetime.strptime(event_date, "%Y-%m-%d")
                datetime.strptime(event_time, "%H:%M")
            except ValueError:
                print("Invalid date or time format. Please enter dates in Year-Month-Day format and time in Hours:Minutes format.")
                continue

            items = []
            while True:
                item = input("Item name (or press enter to finish): ")
                if not item:
                    break
                try:
                    price = float(input("Price: "))
                except ValueError:
                    print("Invalid price. Please enter a valid number.")
                    continue
                items.append({"item": item, "price": price})

            add_event(event_name, event_date, event_time, items)

        elif choice == "2":
            event_id = input("Enter event ID to edit: ")
            event_name = input("New event name: ")
            event_date = input("New event date (YYYY-MM-DD): ")
            event_time = input("New event time (HH:MM): ")

            try:
                datetime.strptime(event_date, "%Y-%m-%d")
                datetime.strptime(event_time, "%H:%M")
            except ValueError:
                print("Invalid date or time format. Please enter dates in Year-Month-Day format and time in Hours:Minutes format.")
                continue

            items = []
            while True:
                item = input("New item name (or press enter to finish): ")
                if not item:
                    break
                try:
                    price = float(input("Price: "))
                except ValueError:
                    print("Invalid price. Please enter a valid number.")
                    continue
                items.append({"item": item, "price": price})

            edit_event(event_id, event_name, event_date, event_time, items)

        elif choice == "3":
            event_id = input("Enter event ID to delete: ")
            delete_event(event_id)

        elif choice == "4":
            display_events()

        elif choice == "5":
            search_date = input("Enter date to search for (YYYY-MM-DD): ")
            search_events_by_date(search_date)

        elif choice == "6":
            search_time = input("Enter time to search for (HH:MM): ")
            search_events_by_time(search_time)

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()


cur.close()
conn.close()



