# dataset.py

ALL_REVIEWS = [
    # 5-STAR REVIEWS (Positive)
    ("An absolute masterpiece! The cinematography was breathtaking and the acting was top-notch.", 5),
    ("I loved every second of this film. It is a true work of art that stays with you long after.", 5),
    ("Incredible performance by the lead actor. This is easily the best movie of the year.", 5),
    ("A stunning achievement in filmmaking. The visual effects were beyond anything I've seen.", 5),
    ("Pure joy from start to finish. A heartwarming story that everyone needs to see right now.", 5),
    ("Brilliant direction and a gripping plot. This movie is a perfect example of modern cinema.", 5),
    ("Exhilarating and deeply emotional. I found myself moved to tears by the final scene.", 5),
    ("A cinematic triumph. It balances action and character development with expert precision.", 5),
    ("Simply amazing. The soundtrack alone is worth the price of admission. Don't miss it.", 5),
    ("Five stars is not enough. This film redefined the genre for me in the best possible way.", 5),

    # 1-STAR REVIEWS (Negative)
    ("Complete garbage. The plot was nonexistent and I hated every single character in it.", 1),
    ("A total waste of time and money. I almost walked out of the theater after twenty minutes.", 1),
    ("Terrible acting and even worse writing. It felt like it was written by an untrained AI.", 1),
    ("Boring, overlong, and incredibly loud without any actual substance. A loud mess.", 1),
    ("Easily the worst movie I have seen in years. Avoid this disaster at all costs.", 1),
    ("Nonsensical plot twists and wooden dialogue. I cannot recommend this to anyone.", 1),
    ("Exhausting to watch. The editing was so jumpy that it gave me a genuine headache.", 1),
    ("A masterclass in how to fail. It fails on every technical and emotional level imaginable.", 1),
    ("I am struggling to find even one positive thing to say. It was a miserable experience.", 1),
    ("Cringeworthy from beginning to end. I felt embarrassed for the actors involved.", 1),

    # 3-STAR REVIEWS (Neutral)
    ("It was okay, nothing special but not terrible either. Fine for a rainy Sunday afternoon.", 3),
    ("The movie had some decent moments, but the pacing felt very slow in the second act.", 3),
    ("An average experience. The lead was good, but the supporting cast was forgettable.", 3),
    ("I didn't hate it, but I wouldn't watch it again. It lacked the spark of the original.", 3),
    ("Technically proficient but emotionally hollow. It looked great but didn't feel like much.", 3),
    ("Some parts were funny, while others fell flat. A very middle-of-the-road comedy.", 3),
    ("The premise was interesting, but the execution was only mediocre. Worth a rental maybe.", 3),
    ("I have mixed feelings. The ending was strong, but getting there was a real chore.", 3),
    ("A standard action flick. It hits all the tropes without adding anything new to the mix.", 3),
    ("Not bad, but certainly not great. It exists in that space of total mediocrity.", 3),

    # 4-STAR REVIEWS (Leaning Positive)
    ("A solid movie with a lot of heart. Not perfect, but definitely worth a watch.", 4),
    ("I was pleasantly surprised by this. The chemistry between the leads was charming.", 4),
    ("Very enjoyable! The humor was sharp and the story kept me engaged until the end.", 4),
    ("Strong performances and a great score make this a very high-quality production.", 4),
    ("I really liked it, even if some of the plot points were a bit predictable.", 4),
    ("A great choice for a weekend watch. It's fun, fast-paced, and well-produced.", 4),
    ("This is a good film that narrowly misses being a great one due to a rushed ending.", 4),
    ("Impressive visuals and a clever script. It stands out from the usual blockbusters.", 4),
    ("A very satisfying experience overall. I'd recommend this to most of my friends.", 4),
    ("Thought-provoking and well-acted. It almost reached 5 stars for me, but not quite.", 4),

    # 2-STAR REVIEWS (Leaning Negative)
    ("A visually beautiful film that is unfortunately hollow inside. Pretty but forgettable.", 2),
    ("It started off strong with a great premise, but it lost its way entirely halfway through.", 2),
    ("Disappointing. I expected much more given the talented cast and director involved.", 2),
    ("The directors spent more time on the lighting than on the actual script or plot.", 2),
    ("Too many plot holes to ignore. It had potential but ultimately fell quite short.", 2),
    ("I wanted to like this, but the protagonist was so annoying I couldn't get into it.", 2),
    ("The action scenes were well-shot, but everything in between was incredibly dull.", 2),
    ("A weak attempt at a psychological thriller. It was more confusing than thrilling.", 2),
    ("The pacing was glacial. I understand slow-burn, but this was just slow-nothing.", 2),
    ("It felt like a long commercial for a better movie. Very little actual content here.", 2)
]

ADDITIONAL_REVIEWS = [
    # 5-STAR (Positive)
    ("A triumph of imagination and heart. The world-building was so immersive I forgot I was in a theater. 10/10.", 5),
    ("Every frame of this film belongs in a museum. A breathtaking visual and auditory experience.", 5),
    ("Finally, a sequel that surpasses the original! It handles the legacy with grace and adds something new.", 5),
    ("I've never seen anything like it. The narrative structure was daring, complex, and ultimately rewarding.", 5),
    ("An absolute powerhouse of a movie. The performances are raw, honest, and incredibly moving.", 5),
    ("A masterfully crafted thriller that kept me guessing until the very last frame. Spectacular work.", 5),
    ("The perfect blockbuster. It has humor, stakes, and special effects that actually serve the story.", 5),
    ("A landmark achievement. This will be talked about as a classic for decades to come.", 5),
    ("Rarely does a film connect so deeply on an emotional level. I was sobbing by the end. Beautiful.", 5),
    ("Cinematic gold. The pacing was relentless and the payoffs were incredibly satisfying.", 5),

    # 1-STAR (Negative)
    ("A loud, confusing, and utterly pointless mess. I want my two hours back immediately.", 1),
    ("Insulting to the audience's intelligence. The logic gaps were wide enough to drive a truck through.", 1),
    ("A cynical, soulless cash grab that fails to capture any of the magic of the source material.", 1),
    ("The worst pacing I have ever experienced. I checked my watch at least fifteen times.", 1),
    ("The dialogue was so unnatural it felt like it was translated back and forth through ten languages.", 1),
    ("Zero chemistry between the leads and a plot that goes absolutely nowhere. A total failure.", 1),
    ("I’m actually angry that this was made. It’s an expensive eyesore with no redeeming qualities.", 1),
    ("Repetitive, boring, and filled with the most tired tropes in the history of cinema.", 1),
    ("Utterly forgettable. I forgot the names of the characters before I even left the parking lot.", 1),
    ("A textbook example of how to ruin a franchise. It’s lazy, boring, and profoundly ugly.", 1),

    # 3-STAR (Neutral)
    ("A perfectly fine movie that doesn't take many risks. It’s exactly what you expect it to be.", 3),
    ("The first half was great, but it really dragged in the second act. A decent enough watch.", 3),
    ("The visuals were 5-star, but the script was 1-star. That averages out to a middle-of-the-road 3.", 3),
    ("I enjoyed the action, but I didn't care about the characters. It's a mixed bag for sure.", 3),
    ("Good enough for a rental, but don't bother seeing it on the big screen. It’s just okay.", 3),
    ("It attempts to be deep but stays on the surface. Still, the acting keeps it afloat.", 3),
    ("A standard romantic comedy. No surprises here, but it’s pleasant enough for a one-time view.", 3),
    ("The movie feels about thirty minutes too long, but the lead actor is quite charismatic.", 3),
    ("Not quite a classic, but not a disaster either. It occupies a comfortable space in the middle.", 3),
    ("It hits all the beats of a typical thriller. Competent, but ultimately uninspired.", 3),

    # 4-STAR (Leaning Positive)
    ("A very strong entry into the genre. It’s smart, stylish, and mostly very satisfying.", 4),
    ("I really appreciated the unique perspective this film took. A few minor flaws, but mostly great.", 4),
    ("A thrill ride from start to finish. It loses a point for a slightly convenient ending, but it’s fun.", 4),
    ("Thoughtful and atmospheric. It’s a slow-burn that actually rewards your patience.", 4),
    ("Wonderfully acted and directed. It’s a bit of a tear-jerker, but in a way that feels earned.", 4),
    ("Sharp writing and great comedic timing. It’s one of the better comedies I've seen lately.", 4),
    ("The world needs more movies like this. It’s ambitious and creative, even if it’s a bit messy.", 4),
    ("Solid entertainment. It doesn't reinvent the wheel, but it polishes the wheel to a high shine.", 4),
    ("Very impressive debut from the director. I'll be keeping an eye out for their future work.", 4),
    ("A really good time at the movies. It’s fast, fun, and surprisingly emotional in spots.", 4),

    # 2-STAR (Leaning Negative)
    ("All style and no substance. It looks like a high-end perfume commercial but has no heart.", 2),
    ("A massive disappointment. It had all the ingredients for success but turned into a bland soup.", 2),
    ("The plot was far too convoluted for its own good. I left feeling more confused than entertained.", 2),
    ("It’s a shame the script was so weak, because the acting was actually quite impressive.", 2),
    ("I fell asleep twice. If you’re looking for a cure for insomnia, this is the movie for you.", 2),
    ("The humor felt forced and the emotional beats felt unearned. A very hollow experience.", 2),
    ("It tries so hard to be 'edgy' that it ends up being a bit of a cringey chore to watch.", 2),
    ("A lot of great ideas that never quite come together. It’s a frustrating watch, to be honest.", 2),
    ("The CGI was distracting and the dialogue was incredibly clunky. Hard to recommend.", 2),
    ("It feels like a TV episode stretched out into a two-hour movie. Far too thin on plot.", 2)
]

# Combine with your existing list
ALL_REVIEWS.extend(ADDITIONAL_REVIEWS)

def get_split_data():
    """Returns (training_data, testing_data) with a 50/50 split"""
    midpoint = len(ALL_REVIEWS) // 2
    return ALL_REVIEWS[:midpoint], ALL_REVIEWS[midpoint:]