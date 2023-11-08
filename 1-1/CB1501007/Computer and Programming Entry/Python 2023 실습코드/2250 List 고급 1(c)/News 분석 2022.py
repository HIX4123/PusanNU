News=""" \
Wang Jixian didn't set out to become the Chinese voice of resistance in Ukraine. $ \
The 36-year-old resident of Odesa, a key target in Russia's invasion of the country, \
simply wanted to show his parents he was fine. $ \
I'm coming back from buying groceries. $ \
He said in a video posted to Douyin, China's version of TikTok, on February 24,
the first day of the invasion. $ \
Wang, a programmer originally from Beijing, described buying meat and fruit in the
video, remarking that some food stores were still open. $ \
But his mood darkened as the days passed and the Russian assault escalated. $ \
When he logged onto Douyin, he said he would see Chinese videos praising Russian
troops or supporting the invasion. $ \
I was very angry, then I thought I would record videos for them,
and I'll tell them what the real battlefield is, he told CNN. $\
His daily videos, posted across various platforms including \
YouTube and the Chinese messaging app WeChat, quickly gained traction \
as a rare voice offering Chinese audiences a glimpse into war-torn Ukraine $\
A stark contrast from Chinese state media, \
which has promoted Russian disinformation such \
as unfounded claims Ukrainian soldiers are using Nazi tactics."""

St= News.split("$")
Book=[]
print(f"문장의 수는 {len(St)}")

for w in St :
    astate= w.split()
    print(astate)
    Book.append( astate)
