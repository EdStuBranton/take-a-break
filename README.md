# take-a-break
A small timer that implements the pomodoro technique to help you make sure that you take those important small breaks.

This is a small program that is coupled with a tkinter interface. 
It was one of the first things I built when I really started getting 
into learning python so I didn't have to look at the clock constantly
to see whether or not I was within my 25 minutes of learning and 5 minutes
of getting away from the screen. It has been updated recently with
my newly acquired knowledge so look at bit more up to date. It's
still not quite done yet, since the buttons for restart and stop
don't work yet but I'll get to that at some point since it's currently
in heavy use to give my study sessions some structure.

A few things that I'd still like to implement:

improvement 1
I'd like to couple the counter with a database.
The idea here being that, when the time is up, 
the app will ask you what you did and how you 
felt about it. This will allow you to make the 
journaling process way easier because you won't 
have to sit down in the end and try to remember 
what you did all day, so now you can write down 
what you did in the last 23-25 minutes which should
be doable. 

Critique would be that this would take you time
to do everytime and since you're supposed to do
25 minutes and a break of 5 minutes, this doesn't
really work since writing that down might take extra
so the question would be if you then take away from
those 25 minutes and make it 23 minutes so you'll
have 2 minutes to write down what you were working
on? I think that would be a good compromise since
it's for learning and not for on the job work, so
you should be allowed to spend those 2 minutes on
your journaling.

improvement 2
create a timer that counts the time "after" the
countdown has stopped, it could maybe gray out
the restart button for 5 minutes before you're
allowed to continue but it'll also show you how
much you went over the time limit.

improvement 3
Currently, the app has a little plop sound which
in itself is cute an'all but it's hard to hear 
if you've got music running in the background 
so I'll try to make a few voice recordings in 
order to spice it up a little and have something 
to listen to that you "will" notice. Also I'd like 
to make multiple replies with a random module 
choosing which one to play so it won't get too 
boring and one sided.
