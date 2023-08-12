import openai
from Phraends_Flask.Backend.Crawler import Crawler

def summarize_article(article_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Please summarize the articles."
            },
            {
                "role": "user",
                "content": article_text
            }
        ],
        temperature=0.5,
        max_tokens=130,
        top_p=1.0,
        frequency_penalty=0.3,
        presence_penalty=0.3
    )

    return response['choices'][0]['message']['content']

def main(article_texts):
    
    openai.api_key = 'KEY PLACEHOLDER'

    #example_articles:
    article_texts = [
    """
    Apple Inc. prides itself on selling devices rather than relying on ads.
    Now the iPhone maker is looking to expand its digital-advertising business, people familiar with the matter said, as it shifts its growth strategy beyond selling devices toward pushing services on them.
    Over the past year, Apple has met with Snap Inc., Pinterest Inc. and other companies about participating in an Apple network that would distribute ads across their collective apps, the people said. Apple would share revenue with the apps displaying the ads, with the split varying from app to app, they said.
    The move would expand on Apple’s current small-but-growing business selling promotional ads for search terms in its App Store, which delivered nearly $1 billion in revenue last year, they said.
    Under the concept discussed internally and raised with potential partners, users searching in Pinterest’s app for “drapes” might turn up an ad distributed by Apple for an interior-design app, or Snap users searching for “NFL” might see an ad for a ticket-reseller app, one of the people said.
    It’s unclear where Apple’s planning for the possible ad network stands. Representatives for Apple, Snap and Pinterest declined to comment.
    The digital ad effort, If it proceeds, would push Apple into territory dominated by Alphabet Inc.’s Google, which claims 35% of the mobile ad market, and Facebook Inc., which has 25%, according to research firm eMarketer.
    Tech giants increasingly are elbowing into each other’s turf seeking new sources of growth. Google launched its high-end Pixel smartphone in 2016 to compete with the iPhone. And Facebook is pushing into hardware with plans for a smart speaker that would compete with Apple’s HomePod, Google Home and Amazon.com Inc.’s suite of Alexa-powered Echo speakers, according to a person familiar with the project.
    Google tools such as AdMob, AdWords and DoubleClick Ad Exchange let marketers promote their products or services across a network of mobile apps, as well as online. Google typically takes about 30% of ad sales and the rest goes to the publisher, the company says.
    With smartphone sales broadly stagnating and iPhone growth slowing, Apple has begun looking to its services business — which includes App Store sales, music-streaming subscriptions and mobile payments — to drive growth. Its App Store ad business was a small fraction of its total services revenue of $29.98 billion, or about 13% of Apple’s total sales, in the fiscal year ended September 2017. Apple aims to grow services revenue to about $50 billion by 2020.
    Competing with Google and Facebook wouldn’t be easy, in part because they build detailed user profiles that marketers can use to more effectively target ads. Apple has criticized that extensive use of data for advertising, saying it effectively turns the customer into the product.
    “The truth is we could make a ton of money if we monetized our customer, ” Chief Executive Tim Cook said in a television interview on MSNBC in March. “We’ve elected not to do that.”
    For its App Store advertising, Apple says it collects information such as name, address, age, gender, device use, app activity and music, video or book downloads. It uses that data to create groups of people for targeted ads, such as 18- to 34-year-old men using an iPhone. It doesn’t collect personal data from tools like Maps and Siri to use for advertising.
    Apple is “the most constrained when it comes to collecting and using user data,” said Karsten Weide, a digital-advertising analyst with researcher International Data Corp. “If they got back in the ad business for good, they would be super-handicapped compared with Google and Facebook.”
    Apple failed in its last advertising push. Its iAd service, launched in 2010, sold ads within mobile apps on iPhones and iPads but failed to catch on because it charged higher prices than competitors and restricted the types of ads marketers ran.
    Apple shut iAd in 2016. Todd Teresi, who oversees the ad business, refocused on the App Store ad business. While the business is small, its wide profit margins and strong performance have drawn attention from Mr. Cook and Senior Vice President Eddy Cue, a person close to Mr. Teresi said.
    """,
    """
    Apple, Goldman Sachs Plan New Joint Credit Card
    By Tripp Mickle and Liz Hoffman
    Apple Inc. and Goldman Sachs Group Inc. are preparing to launch a new joint credit card, a move that would deepen the technology giant’s push into its customers’ wallets and mark the Wall Street firm’s first foray into plastic.
    The planned card would carry the Apple Pay brand and could launch early next year, people familiar with the matter said. Apple will replace its longstanding rewards-card partnership with Barclays PLC, the people said.
    The Apple-Goldman card could help the companies combat weaknesses in their core businesses. As new iPhone sales growth slows, Apple is focusing on services such as mobile payments, streaming-music subscriptions, and App Store sales. Apple Pay, which generates revenue on each transaction, is a key contributor, but adoption has been slower than executives hoped.
    Goldman, meanwhile, is pushing into consumer banking to compensate for a slump in securities-trading, where revenue has fallen by two-thirds since the financial crisis. It launched a retail banking business called Marcus in 2016 for online savings accounts and personal loans, and executives have been exploring adding credit cards and wealth-management tools.
    The partnership will extend into other services including Goldman offering in-store loans to Apple customers buying iPhones and other gadgets, an effort The Wall Street Journal reported on in February.
    Apple and Goldman are still hashing out the terms and benefits of the planned card including the perks for customers, these people said. The current Apple credit card with Barclays offers interest-free financing on Apple devices and points toward Apple gift cards.
    Apple, Goldman and Barclays declined to comment.
    Write to Tripp Mickle at Tripp.Mickle@wsj.com and Liz Hoffman at liz.hoffman@wsj.com
    """,
    """
    As Apple Inc.’s investment bank, Goldman Sachs Group Inc. has raised tens of billions of dollars for the technology company. Now, Goldman wants to bank Apple’s customers, too — with a ticket size of a few hundred dollars at a time.
    The Wall Street firm is in talks to offer financing to shoppers buying phones, watches and other gadgets from Apple, people familiar with the matter said. Customers purchasing a $1,000 iPhone X could take out a loan from Goldman instead of charging it to credit cards that often carry high interest rates.
    Talks between the tech giant and the investment bank are continuing and could still fall apart. A spokesman for Goldman declined to comment. Apple didn’t respond to requests for comment.
    The partnership would be a coup for Goldman as it tries to grow its new consumer bank. Better known as an elite adviser to corporations and governments, Goldman is embracing retail banking and plain-vanilla lending in pursuit of growth as some traditional areas of strengths, namely trading, slump.
    In 2016 Goldman launched Marcus, an online lender that helps people refinance credit-card debt. The firm is now building a “point-of-sale” financing business that will offer loans to shoppers at checkout, according to people familiar with the firm — effectively finding those customers one step earlier.
    Shoppers in 2017 borrowed more than $200 billion for purchases using credit cards affiliated with retailers or point-of-sale loans, consulting firm First Annapolis estimates. Some $80 billion went toward big-ticket items like furniture and electronics that can take months to pay off, racking up extra interest as borrowers roll over balances from month to month.
    By offering a lower-cost loan, Goldman hopes to siphon off some of that business. Goldman charges 12% interest on its average Marcus loans. Credit cards can charge upward of 20% and carry late fees and other charges.
    Partnerships with big retailers like Apple are key. They can deliver millions of customers that Goldman would struggle to find on its own.
    The bank in October hired Scott Young from Citigroup Inc., where he ran retail credit-card partnerships and helped snag the Costco Wholesale Corp. relationship away from American Express Co. He is tasked with striking similar deals for Goldman, which aims to finance purchases ranging from vacations to home furnishings to orthodontics.
    The bank will start by offering loans similar to its existing Marcus product, but is exploring adding traditional store-brand credit cards down the road, the people familiar with the matter said.
    Apple introduced a program in 2015 with Citizens Financial Group Inc., in which the regional bank offered zero-interest loans for iPhone upgrades and higher-interest options for other device purchases. Part of Goldman’s talks with Apple involves taking over some form of the upgrade program. It is unclear whether anything will change with the handling of the outstanding Citizens loans. The Providence, R.I.-based bank didn’t have an immediate comment.
    The program started as wireless providers were scaling back subsidies for iPhones. It allows customers to pay for a new iPhone with a 24-month financing plan and upgrade to a new device after making 12 payments, a strategy that helps keep customers coming back for the newest models.
    For Apple, the upgrade program is taking on increasing importance as its high-priced devices create sticker shock for some. Facing questions about the affordability of the new $1,000 iPhone, Chief Executive Tim Cook said it works out to $33 a month. “That’s a few coffees a week,” he told analysts during an earnings call in November.
    Goldman’s entry into point-of-sale lending will pit it against financial-technology startups including Affirm Inc., which extends loans to online shoppers, and GreenSky LLC, which finances home-improvement projects and elective medical procedures. Each firm raised about $200 million in recent weeks to expand into new sectors.
    """,
    """
    Months before its hotly anticipated public stock offering, Spotify AB’s lead in music streaming is shrinking, at least in the U.S.
    Apple Inc.’s Apple Music is adding subscriber accounts in the U.S. at a higher rate than Spotify, and is on track to pass the No. 1 streaming service this summer, according to people in the record business familiar with figures reported by the two services.
    Spotify is widely considered the dominant force in the streaming world, with Apple at a distant second. To be sure, Spotify is larger globally and continues to grow slightly faster. But that the No. 2 streaming service is quietly gaining ground in the largest music-subscription market in the world signals Spotify now has significant competition.
    The introduction of streaming services has fueled a recovery for the record industry following years of declines amid plummeting sales of CDs and, more recently, downloads. Streaming customers pay a flat monthly fee or listen to ads in exchange for unlimited access to vast music catalogs; with downloads, consumers pay for individual songs or albums once and own them permanently. Paid subscriptions, up 61%, were the largest source of record-company revenue in the U.S. in the first half of 2017, according to the Recording Industry Association of America.
    But music streaming has yet to prove itself as a viable business as the tech companies operating these services struggle to make them profitable. Active users and paid subscribers are the most closely watched metrics as these services grow.
    Apple’s subscriber-account base in the U.S. has been growing about 5% monthly, versus Spotify’s 2% clip, according to the people familiar with the numbers. Assuming those growth rates continue, Apple will overtake Spotify in accounts this summer.
    Apple’s popular devices have helped add subscribers to its music service, which is preloaded on all iPhones, Apple Watches and other hardware the company sells.
    One question lingering in the industry is what metrics Spotify will have to disclose once it becomes a publicly traded company. The service has periodically released global subscriber totals and just last month touted a new high of 70 million.
    Apple Music told The Wall Street Journal it now has 36 million, up from the 30 million it last reported in September.
    But both companies’ numbers are increased by counting individual users who are part of family plans and people with discounted subscriptions bundled with other services. In some countries, mobile-phone plans can include an Apple Music subscription; Spotify offers students in the U.S. a subscription plan that includes video-service Hulu. Neither company publicly breaks out figures for the U.S. or any other single market.
    In their licensing deals, labels let streaming services pay lower royalty rates for music when they meet certain subscription-growth targets. As part of those deals, the services are required to report how many accounts they have — a number not inflated by multiple users on a family subscription. They also have to report the number of monthly active subscribers they have, stripping out people who were signed up in bundle deals but don’t use the service and are likely to churn.
    By one standard, Apple Music has already passed Spotify. Including people who are still in free or deeply discounted trial periods leading up to paid subscription, Apple Music has a slight edge on Spotify in the U.S., according to one of the people familiar with the figures.
    Apple Music has three to four times the number of such trial users as Spotify, according to this person, in part because it doesn’t offer a free tier. Also, all Apple Music subscribers are entered automatically into a free initial three-month period. Excluding those trial users, Spotify is ahead, but by a small amount — and that gap is closing.
    Apple’s services segment, which includes Apple Music as well as the App Store and its payment services, was a bright spot in the company’s earnings posted last week, with an 18% jump in revenue. It is unclear how much Apple Music contributed to that increase as the company doesn’t break out the streaming service’s results.
    Launched in 2008, Spotify lets users listen to a library of more than 30 million songs on demand. It started offering its service in the U.S. in 2011. Subscribers who shell out $9.99 a month can listen without hearing ads; users of the free version need to sit through ads and have more limited ability to pick the order in which they hear the songs they select. As of June, Spotify said it has 140 million active users world-wide. Spotify has never reported a profit, but has said it believes it can become profitable once it has amassed sufficient users, without specifying what that scale would be.
    """,
    """
    Apple is Designing iPhones and iPads That Would Drop Qualcomm Components
    Apple Inc., locked in an intensifying legal fight with Qualcomm Inc., is designing iPhones and iPads for next year that would jettison the chipmaker’s components, according to people familiar with the matter.
    Apple is considering building the devices only with modem chips from Intel Corp. and possibly MediaTek Inc. because San Diego, Calif.-based Qualcomm has withheld software critical to testing its chips in iPhone and iPad prototypes, according to one of the people.
    Qualcomm, which has worked with Apple for a decade, stopped sharing the software after Apple filed a federal lawsuit in January accusing Qualcomm of using its market dominance unfairly to block competitors and to charge exorbitant patent royalties, this person said. Qualcomm has said Apple is mischaracterizing its practices.
    Apple’s planned move for next year involve the modem chips that handle communications between wireless devices and cellular networks. Qualcomm is by far the biggest supplier of such chips for the current wireless standard.
    Qualcomm said its “modem that could be used in the next generation iPhone has already been fully tested and released to Apple.” The chip company said it is “committed to supporting Apple’s new devices” as it does for others in the industry.
    Apple in the past used only Qualcomm modem chips for iPhones, but started also procuring the chips from Intel for its iPhone 7 and 7 Plus models last year. It again used a mix of the two in the iPhone 8 and 8 Plus that started selling in September.
    Apple’s plans to exclude Qualcomm chips from next year’s model could still change. People familiar with Apple’s manufacturing process said the company could change modem-chip suppliers as late as June, three months before the next iPhone is expected to ship. Still, some of the people said Apple hasn’t previously designed iPhones and iPads to exclude Qualcomm chips at a similar stage of the process.
    """
    ]

    all_summaries = []

    for i, article_text in enumerate(article_texts, start=1):
        
        # Set this to True if you want to test the function
        test_function = False  
        if test_function:
            
            # Generate summarized text for each article
            summary = summarize_article(article_text)
            all_summaries.append(f"{i}. {summary}")
        else:
            # Just print something instead of running the function
            print(f"Article {i} summary: This is a placeholder summary.")

    if test_function:
        return all_summaries

if __name__ == "__main__":
    main()

