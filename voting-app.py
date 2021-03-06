from pywebio.input import *
from pywebio.output import *
from pymongo import MongoClient

client = MongoClient('localhost',port=27017)
db= client.voting_app
coll = db.user_vote

def voting():
    name = input("Enter your name", type="text")
    age = input("Enter your age", type=NUMBER)
    if age>=18:
        put_text("Check your details")
        put_table([['NAME','AGE'],[name,age]])

        check = checkbox(options=['All details are correct.'])
        if check:
            selection = radio('Select Your party',['BJP','NPP','Congress','AAP'])

            records= {
                'name':name,
                'age':age,
                'vote_for':selection
            }
            coll.insert_one(records)
            put_text('Your Response has been recorded')

            keep_voting= radio('Keep Voting',['Yes','No'])
            if keep_voting == 'Yes':
                voting()
            else:
                return style(put_text('Voting has been ended'),'color:green')

    else:
        style(put_text("Your are not eligible for voting"),'color:red')
        keep_voting= radio('Keep Voting',['Yes','No'])

        if keep_voting == 'Yes':
            voting()
        else:
            return style(put_text('Voting has been ended'),'color:green')


voting()    
