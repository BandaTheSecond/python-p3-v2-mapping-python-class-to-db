from __init__ import CURSOR, CONN


class Department:
    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"

    @classmethod
    def create_table(cls):
        """Create the departments table if it does not exist."""
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the departments table if it exists."""
        sql = "DROP TABLE IF EXISTS departments"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Save this Department instance to the database and assign its id."""
        sql = "INSERT INTO departments (name, location) VALUES (?, ?)"
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, location):
        """Create a new Department, save it, and return the instance."""
        department = cls(name, location)
        department.save()
        return department

    def update(self):
        """Update this Department's row in the database."""
        sql = "UPDATE departments SET name = ?, location = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
       """Delete this Department's row from the database."""
       sql = "DELETE FROM departments WHERE id = ?"
       CURSOR.execute(sql, (self.id,))
       CONN.commit()
       self.id = None
