# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default easy_questions = {
    "f(x) = 3x^2 + 1": ["6x", "3x", "6", "12", "6x"],
    "f(x) = 1.5x^2 + 1": ["6x", "3x", "6", "12", "3x"],
    "f(x) = 6x + 1": ["6x", "3x", "6", "12", "6"],
    "f(x) = 6x^2 + 1": ["6x", "3x", "6", "12x", "12x"],
    "f(x) = 2x^3 + 1": ["6x^2", "3x", "6", "12", "6x^2"]
}

default medium_questions = {
    "f''''(x) of f(x) = x^3 - x^2 + x - 1":             ["0", "1", "x", "6x", "0"],
    "d/dx(0.5x^2)":                                     ["1", "x", "0", "x^2", "x"],
    "f''''(x) of f(x) = 3t^7 - 6t^4 + 8t^3 - 12t + 18": ["0", "1", "2520t^3 - 144", "2408t^3 - 124", "2520t^3 - 144"],
    "d/dx(8 - 2x/5)":                                   ["0", "1", "(2/5)x", "-2/5", "-2/5"],
    "f''(x) of f(x) = cos^2(7t)":                       ["0", "sin^2(7t) - cos^2(t)", "sin^2(7t) - 98cos^2", "-98cos^2(7t)", "-98cos^2(7t)"],
}

define Akari = Character("Akari")
define Harumi  = Character("Harumi")
define Narrate = Character("")
define Friend1 = Character("Mio")
define Friend2 = Character("Friend2")
define Friend3 = Character("Friend3")
define School = Character("Intercom")
define Sensei = Character("Sensei")
define Sister = Character("Little Sister")

screen show_question_menu(question_index):
            hbox:
                xalign 0.5
                yalign 0.1
                text "[list(easy_questions.keys())[question_index]]":
                    xalign 0.5
                    yalign 0.5
            
            vbox:
                xalign 0.5
                yalign 0.4
                spacing 40
                hbox:
                    spacing 80
                    textbutton easy_questions[list(easy_questions.keys())[question_index]][0]:
                        if easy_questions[list(easy_questions.keys())[question_index]][0] == easy_questions[list(easy_questions.keys())[question_index]][4]:
                            action Return(True)
                        else:
                            action Return(False)
                    textbutton easy_questions[list(easy_questions.keys())[question_index]][1]:
                        if easy_questions[list(easy_questions.keys())[question_index]][1] == easy_questions[list(easy_questions.keys())[question_index]][4]:
                            action Return(True)
                        else:
                            action Return(False)
                hbox:
                    spacing 80
                    textbutton easy_questions[list(easy_questions.keys())[question_index]][2]:
                        if easy_questions[list(easy_questions.keys())[question_index]][2] == easy_questions[list(easy_questions.keys())[question_index]][4]:
                            action Return(True)
                        else:
                            action Return(False)
                    textbutton easy_questions[list(easy_questions.keys())[question_index]][3]:
                        if easy_questions[list(easy_questions.keys())[question_index]][3] == easy_questions[list(easy_questions.keys())[question_index]][4]:
                            action Return(True)
                        else:
                            action Return(False)

screen show_question_menu_medium_scam(question_index):
            hbox:
                xalign 0.5
                yalign 0.1
                text "[list(medium_questions.keys())[question_index]]":
                    xalign 0.5
                    yalign 0.5
            
            vbox:
                xalign 0.5
                yalign 0.4
                spacing 40
                hbox:
                    spacing 80
                    textbutton "Erm....":
                        action Return(False)

                    textbutton "I dont know!":
                        action Return(False)
                
screen show_question_menu_medium(question_index):
            hbox:
                xalign 0.5
                yalign 0.1
                text "[list(medium_questions.keys())[question_index]]":
                    xalign 0.5
                    yalign 0.5
            
            vbox:
                xalign 0.5
                yalign 0.4
                spacing 40
                hbox:
                    spacing 80
                    textbutton medium_questions[list(medium_questions.keys())[question_index]][0]:
                        if medium_questions[list(medium_questions.keys())[question_index]][0] == medium_questions[list(medium_questions.keys())[question_index]][4]:
                            action Return(True)
                        else:
                            action Return(False)
                    textbutton medium_questions[list(medium_questions.keys())[question_index]][1]:
                        if medium_questions[list(medium_questions.keys())[question_index]][1] == medium_questions[list(medium_questions.keys())[question_index]][4]:
                            action Return(True)
                        else:
                            action Return(False)
                hbox:
                    spacing 80
                    textbutton medium_questions[list(medium_questions.keys())[question_index]][2]:
                        if medium_questions[list(medium_questions.keys())[question_index]][2] == medium_questions[list(medium_questions.keys())[question_index]][4]:
                            action Return(True)
                        else:
                            action Return(False)
                    textbutton medium_questions[list(medium_questions.keys())[question_index]][3]:
                        if medium_questions[list(medium_questions.keys())[question_index]][3] == medium_questions[list(medium_questions.keys())[question_index]][4]:
                            action Return(True)
                        else:
                            action Return(False)

# The game starts here.

label start:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg sky
    play music "main.mp3" loop
    Narrate "It was supposed to be a day like no other."
    Narrate "I walked towards the school while looking at the blue sky… not that there’s much to see, I just think it’s relaxing so you know?"
    Narrate "After all, with all the chaos at home, the thing I desire most is peace…"
    Narrate "Ahh, how lovely it would be, just sleeping away, without a care about the world"

    scene school hallway

    Narrate "Well anyway, I’m getting a bit off track now right? Where were we at again?  Right, school."
    Narrate "Without noticing it, I was eventually greeted by the classroom door. My everyday routine remains unchanged since graduating from middle school."
    Narrate "How many more years of this again? {w} …I don’t wanna… {w} I don’t even know what to do in my life yet. Life is tough eh?"
    Narrate "No matter what happens it just keeps pushing on. God, please slow down a bit eh? I'm trying so hard to keep up, you know?"
    Narrate "Finally, I open the door to our classroom- And I was greeted with… {p} —Silence."
    scene school classroom
    show akari headscatch_1 at center
    Akari "{i}Wha?!{/i}"
    Narrate "I naturally made my way towards my friends who were uncharacteristically studying their notes."
    show akari boust at center
    Narrate "Good morning everyone! So, what's up? Why are you guys studying your notes? Did hell freeze over or something?"
    show akari eyebrow_raise at center
    Friend1 "Ah- Akarin! Did you not know?"
    Akari "Hmm? Know what?"
    Friend1 "We have an exam today you know!"
    show akari shocked
    stop music
    Narrate "..."
    play sound "boom.mp3"
    Akari "It's over..."
    with fade

label tutorial_question_1:
    play music "huh.mp3" loop
    scene bg desk
    define question_index = renpy.random.randint(0, 4)
    call screen show_question_menu(question_index)
    $ a = _return
    if a == True:
        Akari "Yes!"
    else:
        Akari "Nooooo!"
    $ print (list(easy_questions.keys())[question_index][4])
    $ easy_questions.pop(list(easy_questions.keys())[question_index])
    

    $ question_index = renpy.random.randint(0, 3)
    call screen show_question_menu(question_index)
    $ a = _return
    if a:
        Akari "Yes!"
    else:
        Akari "Nooooo!"
    $ easy_questions.pop(list(easy_questions.keys())[question_index])


    $ question_index = renpy.random.randint(0, 2)
    call screen show_question_menu(question_index)
    $ a = _return
    if a:
        Akari "Yes!"
    else:
        Akari "Nooooo!"
    $ easy_questions.pop(list(easy_questions.keys())[question_index])

label end_of_exam:
    scene school classroom
    Narrate "After multiple hours of suffering, the loud bell outside rang."
    stop music fadeout 1.0
    play sound "bell.mp3" fadein 1.0 volume 0.5
    show akari sigh at center
    Akari "It's over..."
    stop sound fadeout 0.5
    play music "comedy.mp3"
    Friend1 "Akarin… you really gotta pay more attention in school. Did you not check the class group chat?"
    show akari crying_1 at center
    Akari "I didn't have the time to check yesterday…"
    Friend1 "Sigh* Let me guess, your siblings again?"
    show akari crying at center
    Akari "Yeah, Dad’s on a business trip and mom got home late, I had to take care of them…"
    Narrate "It was a hopeless situation, but I understood our struggles so I didn't complain."
    hide akari
    Friend1 "I wonder how bad your grades are at this point?  We don’t study much but we try to keep up you know?"
    Friend2 "Yeah, I’m kinda worried about you now, Akari…"
    Friend3 "Me too…"
    Narrate "Suddenly the school intercom rang"
    School "Akari from Class 1-B, please come to the staff room"
    Friend1 "...Maybe it really is over for you this time"
    Akari "AAHHHHHHHHHH"

label meeting_at_ofice:
    scene school hallway
    play music "main.mp3" loop
    Narrate "The door to the staff room stood in front of me, menacingly. {w} I took a quick gulp before knocking on the door. A reply came back after a few seconds."
    Sensei "Yes? Who is it?" 
    Akari "Um! I’m Akari from Class 1-B!"
    Sensei "Oh, Akari-san, please come in."
    Akari "Yes!"
    
    scene school office
    Narrate "I replied like a soldier to the person on the other side of the door before entering. I took a look around the room and found 2 people waiting inside."
    Narrate "Our classroom advisor, sensei, sat in the rightmost cubicle, the nearest one to the door, and right beside her, a certain girl stood."
    Sensei "Akari, can you come closer to me please, we need to talk about our grades."
    show akari nervous at left
    Akari "{i}Awawawawawa, as I thought, it was about that huh{/i}"
    Akari "Yes ma’am."
    Narrate "As instructed, I got closer to the teacher and the girl. The teacher got into the matter at hand immediately."
    Sensei "Akari-san, as of right now, you’re failing the class."
    show akari surprised at left
    Akari "Eck!"
    Sensei "I’ve heard of your current circumstances. You’ve always been tired during our classes, and there’s been reports and complaints from other teachers about you sleeping in their class, how do you plead?"
    show akari at left
    Akari "Guilty ma’am, I apologise"
    Sensei "I see… I wasn’t expecting such a straightforward answer from you Akari-san."
    Akari "There is simply no excuse for my actions, so I don't really have a choice…"
    Sensei "Well, considering how kind you are, I’m willing to give you another chance."
    Akari "Really?"
    Sensei "Yes, let me explain. The biggest contributor to you failing the class were the exams you just took now. If you had passed, there wouldn't have been any problems, but that didn’t happen, did it now?" 
    Sensei "That’s why, I’m willing to let you retake the exams. However, as of now, if you retake the exams, do you think you have the ability to pass?"
    Akari "I don’t think so…"
    Sensei "Yes, that’s why, this girl right here will teach you some stuff before you retake the exams. Introduce yourself"  
    show harumi at right
    Narrate "I stared at the girl in question. The girl who can be called a true \"Yamato nadeshiko\". Her long, straight black hair, which glimmered due to the bright sunlight, swayed as breeze flowed through the room. "
    Narrate "A face so white and smooth that it can be compared to the best of pearls in the world and a head that is believed to be as wide as the great library of alexandria. That’s the type of girl Harumi is."
    Narrate "One of the most Popular girls in our school, Miyahira Harumi, also known as the gentle princess. Known because of her beauty and attitude, she also boasts the highest exam scores within the prefecture. Truly a perfect girl."
    Narrate "And now, our homeroom teacher is proposing that such a perfect girl teach me… Eh? Is this really fine? Did sensei get some blackmail material on her to persuade her to do this? Why me???"
    Harumi "Good afternoon, Akari-san. My name is Miyahira Harumi. It is a pleasure to meet you."
    Narrate "Harumi greeted, followed by a bow."
    Akari "A-Ah. Likewise, my name is Akari… wait you already know! E-erm, I thank you in advance for your help, let’s get along" 
    Narrate "Fumbling, I followed up with a bow too, but it doesn’t really fit me, does it now."
    Narrate "I looked towards Harumi again. Her refined movements truly makes her worthy of her title. Finally, the teacher interrupts our awkward situation-"
    Sensei "Akari-san, with this you should be able to catch up, right?"
    Akari "Of course ma’am!"
    Sensei "Good, then, please prepare for your exam in 2 weeks. Harumi-san, please take care of Akari for me."
    Akari "Understood."
    Sensei "Well then kids, you can go now. See you in monday~" 
    Akari "Yes, thank you ma’am.."
    show harumi calm at right
    Harumi "Farewell…"
    Narrate "And with that, we left the room. I slowly turned my head towards Harumi."
    show akari happy at left
    Akari "Please look after me for the upcoming two weeks together."
    Harumi "Of course Akari-san. I look forward to our upcoming times together. Let us do our best together."
    Akari "{i}Ahhh as expected, the almighty Harumi-sama is as gentle as ever. But huh… I thought I saw her cheeks twitch for a bit… {/i}"
    show harumi annoyed at right
    Harumi "{i}Tsk…{/i}"
    Akari "{i}E? Ehhhhhh???{/i}"



label ActII:
    scene akarin house outside
    Narrate "Finally, I am back home"
    Akari "{i}Man... I wonder if Mom is back yet...{/i}"
    Narrate "Reluctantly, I opened the door-"
    
label inside_house:
    scene akarin house inside
    show akari at center
    Akari "I’m home~"
    Sister "Ah onee-chan! Welcome back~!"
    Narrate "After a long day of unexpected events happening, like the test, getting called by the teacher, and having the opportunity for the one and only Harumi to tutor me in preparation for my retaking of exams, I finally got back home after my part time job."
    Akari "Is mom home yet?"
    Sister "Nope! She called us and said she'll be late for today too!"
    Akari "Ahhh... I see. So yyou guys haven't eaten yet?"
    Sister "She shakes her head"
    Akari "We're hungry!"
    Akari "I see..."
    Narrate "Well, it's not like im not used to it at this point. This has been my daily routine for weeks now. {i}sigh{/i}"

    scene akarin house bedroom
    Narrate "Afterwards, I cooked for my siblings and went to bed early"
    Narrate "It's been a tough day okay! Let me enough sleep for once. Thinking about it, today's been crazy. Failing was meh but having the encounter with Harumi... That's something."
    Narrate "But she seemed irritated at the end... maybe I'm just overthiking it. Oh well, have to make sure I have enough energy for tomorrow. Time for sleep!"
   
    scene empty
    Narrate "And with that, the night skipped forward, and before I know it, Class was about to end."
    Narrate"{i}*Ding Dong Ding Dong{/i}"

    scene school classroom
    show mio at left
    Friend1 "Yo, Akarin"
    show akari at right
    Akari "What's up?"
    Friend1 "Wanna hang out and stuff?"
    Akari "Well..."
    Narrate "I looked towards her back and noticed Harumi waiting outside our class. A commotion has already started as people wondered who Harumi could be waiting for in the class"
    Narrate "Noticing my shift of attention, Mio also looked outside the class, then back to me. Smirking."
    Friend1 "Hee~ Is that how it is? This is quite unexpected. You didn't tell us about this development yesterday you know?"
    Akari "It's not like that... Sensei just asked her to help me study up for my make up exams"
    Friend1 "Heh. So, where are you guys going to study at?"
    Akari "I wonder."
    Narrate "Perhaps losing her patience (Impossible), Harumi entered our class."
    show harumi calm at center
    Harumi "May I borrow Akari-san? We have to study today."
    Friend1 "Sure!"
    Akari "{i}Ehhhh{/i}"
    Narrate "It seems like my school life is about to bevome become nosier."


label restaurant_test_exam:
    scene restaurant
    show harumi calm at center
    Harumi "Before we start studying, do you mind taking a short test, Akari-san?"
    show akari at center
    Akari "No, not at all!"
    Narrate "Thus, hell began."

    scene paper
    play music "comedy.mp3" loop
    $ question_index = renpy.random.randint(0, 4)
    call screen show_question_menu_medium_scam(question_index)
    Akari "This is too hard!"
    $ medium_questions.pop(list(medium_questions.keys())[question_index])

    $ question_index = renpy.random.randint(0, 3)
    call screen show_question_menu_medium_scam(question_index)
    Akari "TAAARGHHHH"
    $ medium_questions.pop(list(medium_questions.keys())[question_index])
    $ question_index = renpy.random.randint(0, 2)

    call screen show_question_menu_medium_scam(question_index)
    Akari "I dont know anymore!"
    $ medium_questions.pop(list(medium_questions.keys())[question_index])

    $ medium_questions = {
    "f''''(x) of f(x) = x^3 - x^2 + x - 1":             ["0", "1", "x", "6x", "0"],
    "d/dx(0.5x^2)":                                     ["1", "x", "0", "x^2", "x"],
    "f''''(x) of f(x) = 3t^7 - 6t^4 + 8t^3 - 12t + 18": ["0", "1", "2520t^3 - 144", "2408t^3 - 124", "2520t^3 - 144"],
    "d/dx(8 - 2x/5)":                                   ["0", "1", "(2/5)x", "-2/5", "-2/5"],
    "f''(x) of f(x) = cos^2(7t)":                       ["0", "sin^2(7t) - cos^2(t)", "sin^2(7t) - 98cos^2", "-98cos^2(7t)", "-98cos^2(7t)"],
    }

    $ easy_questions = {
        "f(x) = 3x^2 + 1": ["6x", "3x", "6", "12", "6x"],
        "f(x) = 1.5x^2 + 1": ["6x", "3x", "6", "12", "3x"],
        "f(x) = 6x + 1": ["6x", "3x", "6", "12", "6"],
        "f(x) = 6x^2 + 1": ["6x", "3x", "6", "12x", "12x"],
        "f(x) = 2x^3 + 1": ["6x^2", "3x", "6", "12", "6x^2"]
    }

    scene restaurant

    Narrate "I nervously handed the paper to Harumi who was currently studying on the other side of the table. I had taken so long to complete the example answer sheet she gave me that she eventually went on to do something else instead.. I feel so bad... "
    Akari "Here's my paper madaam!" 
    show harumi surprised at center
    Harumi "Oh... thanks for the hard work Akari-san. Please let me check your paper for a moment."
    show harumi at center
    Akari "Of course!" 
    Narrate "Slowly, Harumi checked the contents of my paper line by line. As she continued, the motion of her pen gradually slowed down, as her perfect straight lines became jagged as she progressed down the paper. By the end of it, it seemed like she was struggling to check as her pen was starting to shake..."
    show harumi surprised at center
    Akari "Harumi-san, are you alright?"
    Harumi "Um... cough cough, of course. I apologize for the wait. Here is your paper. My I go to the restroom for a bit?" 
    Akari "Sure!"
    Narrate "Harumi made her way to the bathroom, and I was left alone with my paper at hand. I checked my score and was surprised by it's contents. "
    Narrate"5. I had scored a measly five points out of the thirty total. To put it frankly, it was a disaster, no, a tragedy. A tragedy so drastic that it was able to put Harumi into panic. Perhaps the reason she went to the bathroom was because she doesn't know how to handle someone like me..."
    Narrate "Deciding on giving her some alone time, I waited patiently, simply checking the contents of my paper, seeing what I did wrong and what I should've done. "
    Narrate "Time passed quickly, and before I knew it, it has been 15 minutes since she went to the restroom. Worried, I finally stood up from my chair and approached the restroom stall. "
    Narrate"There I could here someone familiar talking. I slowly opened the door and was faced with a surprising situation. Something nobody would ever expect of the gentle, kind and saint-like harumi-"

    scene bathroom
    play music "unwelcome_school.mp3" loop
    show harumi raging at center
    Harumi "What even was that! How can someone be so dull witted! It doesn't make sense! I thought humans are all supposed to have some kind of intelligence, but to think that she couldn't even answer the common sense questions?!" 
    Narrate "A shocking scene was presented to me on the other side of the door. Harumi, throwing out harsh words as if they were nothing. "
    Harumi "How does one not know what's heavier, a kilogram of steel or a kilogram of feathers? It's right there in the question! They're the same! How can someone be so worthless!" 
    Akari "{i}*Goufh!{/i}"
    Akari "{i}Harsh!{/i}" 
    Harumi "This is an impossible task... I thought it would be beneficial for me since it was sensei asking, but... Maybe this is punishment for being too popular?" 
    Akari "{i}what's with her ego!?{/i}"
    Harumi "No... I've never failed before... you can do this Harumi. Smile like you always do. No matter what happens, I--- ...eh?" 
    Narrate "It seems like she finally noticed that I was watching her whole rant, stopping dead on her tracks, the room became silent."
    show harumi angry at center
    Harumi "You... did you see?" 
    show akari scared at left
    Akari "Errr... yes?" 
    Harumi "Did you hear everything?" 
    Akari "Affirmative." 
    Harumi "Then, do I need to tell more?"
    Akari "Tell me what?" 
    Harumi "Do not speak of this event to anyone. The moment you do, I'll make sure you will regret it."
    Akari "...I shall do what you ask" 
    Harumi "Good, sigh*. I apologise for what you've witnessed, Akarin-san. I believe it is the best interest of both parties that we finish up for the day here. We will meet again after class in this restaurant to continue your studying, understood?" 
    Narrate "Harumi continued as if the whole ordeal that happened just a few seconds ago did not happen."

    scene restaurant
    play music "main.mp3" loop
    show akari at center
    Akari "You... you're still willing to teach me?" 
    show harumi at right
    Harumi "Of course, it was the request of sensei after all. And I never back down on the things I accepted."
    Narrate "Finally, she started towards the exit of the restaurant with me following closely. "
    Narrate "Of course we made sure to pick up our bags before leaving. But before Harumi left for good, she suddenly stops- "
    Harumi "Here's my LINE ID, it'd be easier to organize if we can talk online afterall, I'll keep my guard down on you since you already know anyway." 
    Narrate "Harumi then hands me a small piece of paper containing her contact information. "
    Akari "Thank you..." 
    Harumi "Well, let me reintroduce myself, my name is Harumi, and although you've discovered the real me, make no mistake, I will make you pass your exam. Please don't be late for tomorrow."  
    Narrate "She continues- now with her seiso voice- "
    Harumi "Well then, thank you for the pleasant afternoon and for keeping me company. We shall start our proper lessons tomorrow. I look forward to meeting you again Akari-san, Farewell."


label end_exam:
    scene school classroom
    Narrate "Finally the day of my redemption has come!"
    Sensei "Alright class. You may start answering you papers... now!"

    scene paper

    define correct_answers = 0

    define question_index = renpy.random.randint(0, 4)
    call screen show_question_menu(question_index)
    $ a = _return
    if a == True:
        $ correct_answers += 1
    $ easy_questions.pop(list(easy_questions.keys())[question_index])

    define question_index = renpy.random.randint(0, 3)
    call screen show_question_menu(question_index)
    $ a = _return
    if a == True:
        $ correct_answers += 1
    $ easy_questions.pop(list(easy_questions.keys())[question_index])

    $ question_index = renpy.random.randint(0, 4)
    call screen show_question_menu_medium(question_index)
    $ a = _return
    if a == True:
        $ correct_answers += 1
    $ medium_questions.pop(list(medium_questions.keys())[question_index])

    $ question_index = renpy.random.randint(0, 3)
    call screen show_question_menu_medium(question_index)
    $ a = _return
    if a == True:
        $ correct_answers += 1
    $ medium_questions.pop(list(medium_questions.keys())[question_index])

    $ question_index = renpy.random.randint(0, 2)
    call screen show_question_menu_medium(question_index)
    $ a = _return
    if a == True:
        $ correct_answers += 1
    $ medium_questions.pop(list(medium_questions.keys())[question_index])

    $ print(correct_answers)
    Narrate "you got [correct_answers]!"
    if correct_answers >= 3:
        jump Good_End
    else:
        jump Bad_End


label Good_End:
    scene bg sky
    play music "happi.mp3" loop
    Narrate "In the end, I was able to pass and found my passion in studying"
    Narrate "I still stayed friends with Mio and the others, of course, but despite having finished her task, Harumi kept spending her time with me."
    Narrate "Eventually, this lead us to living together during college and beyond."
    Narrate "Now we enjoy a satisfying life while living together."
    Narrate "I can say that I am glad. Glad that I was \"Learning With You\""
    jump End

label Bad_End:
    play music "REIN.mp3" loop
    scene bg sky
    Narrate "In the end, I wasn't able to pass the exam"
    Narrate "Disappointed with me, Harumi never approached me after the exam."
    Narrate "Our surroundings also began to look down upon me, as if I was some worthless trash"
    Narrate "Thankfully, Mio was there to support me... the same could not be said about my other friends"
    Narrate "Perhaps it would have been better if I had never met you, Harumi."
    jump End

label End:

    return
