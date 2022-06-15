from people import Aleksi as me
from people import Employer as you
from people import discuss
from time import sleep

def look_for_job():
    if (me.contacting(you) or you.contacting(me)) and (you.has_open_position and you.interested(me)):
        me.happy = True
        discuss(me, you)
        if you.ideas == me.ideas:
            you.hiring(me)
            while me.happy and you.happy:
                me.working(you)
                sleep(16)

if __name__ == '__main__':
    look_for_job()

