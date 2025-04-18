import psycopg2

def connect_db():
    return psycopg2.connect(
        dbname='test',
        user='postgres',
        password='1',
        host='localhost',
        port='5432'
    )


async def add_user_to_db(user_id, username):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT id FROM users WHERE user_id = %s', (user_id,))
        user = cursor.fetchone()

        if user is None:
            cursor.execute(
                'INSERT INTO users (user_id, username) VALUES (%s, %s)',
                (user_id, username)
            )
            conn.commit()

    except Exception as e:
        print(f'Error database: {e}')
    finally:
        cursor.close()
        conn.close()