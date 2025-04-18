from aiogram import Router

from Bot.database.connect_db import connect_db
from Bot.referral_program.referral_program import generate_referral_code

router = Router()

async def add_user_to_db(user_id, username, referred_by):
    connect = connect_db()
    cursor = connect.cursor()

    try:
        cursor.execute(
            'select user_id from users where user_id = %s',
            (user_id,)
        )
        user = cursor.fetchone()

        if user is None:
            referral_code = generate_referral_code()
            cursor.execute(
                'insert into users (user_id, username, referred_by, referral_code) values (%s, %s, %s, %s)',
                (user_id, username, referred_by, referral_code)
            )
            connect.commit()
    
    except Exception as e:
        print(f'error database is {e}') #should add logging 
    finally:
        connect.close()
        cursor.close()

async def add_user_to_db_no_ref(user_id, username):
    connect = connect_db()
    cursor = connect.cursor()

    try:
        cursor.execute(
            'select user_id from users where user_id = %s',
            (user_id,)
        )
        user = cursor.fetchone()

        if user is None:
            referral_code = generate_referral_code()
            cursor.execute(
                'insert into users (user_id, username, referral_code) values (%s, %s, %s)',
                (user_id, username, referral_code)
            )
            connect.commit()
    
    except Exception as e:
        print(f'error database is {e}') #should add logging 
    finally:
        connect.close()
        cursor.close()
