from Bot.database.connect_db import connect_db

async def give_key_to_user(user_id, duration):
    connect = connect_db()
    cursor = connect.cursor()

    cursor.execute(
        'select key, location_country from keys_primary where owner = %s',
        ('None',)
    )
    key, location_country = cursor.fetchone()

    month_or_s = ('months') if duration > 1 else ('month') 

    cursor.execute(
        "insert into user_subscriptions (user_id, key, duration, end_date, location_country) values (%s, %s, %s, current_date + interval %s, %s)",
        (user_id, key, duration, f'{duration} {month_or_s}', location_country)
    )

    cursor.execute(
        'update users set current_subscribe = true where user_id = %s',
        (user_id,)
    )

    cursor.execute(
        'update keys_primary set owner = %s where key = %s',
        (user_id, key)
    )

    connect.commit()
    connect.close()
    cursor.close()
    return key, location_country