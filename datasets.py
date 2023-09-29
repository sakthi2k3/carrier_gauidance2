domain_questions = [
    "Which of the following areas interests you the most?\na. Technology and gadgets\nb. Finance and investments\nc. Online shopping and e-commerce\nd. Health and wellness",
    "When you have free time, what do you enjoy doing?\na. Exploring new tech devices and apps\nb. Reading about financial markets and strategies\nc. Online shopping for various products\nd. Focusing on health and fitness activities",
    "Have you ever dabbled in any of the following?\na. Coding or programming\nb. Stock trading or investing\nc. Selling products online\nd. Pursuing a healthy lifestyle",
    "Which of the following topics would you like to learn more about?\na. Emerging technology trends\nb. Financial planning and budgeting\nc. Optimizing e-commerce businesses\nd. Health and medical advancements",
    "When it comes to your personal interests, which area are you most likely to discuss with friends?\na. The latest tech gadgets and innovations\nb. Investment opportunities and financial tips\nc. Online shopping finds and deals\nd. Health and wellness practices",
    "Which of these online communities or forums do you participate in or follow most often?\na. Tech forums and subreddits\nb. Financial planning and investing communities\nc. E-commerce seller groups and platforms\nd. Health and wellness forums and support groups",
    "What kind of content do you enjoy consuming on the internet or social media?\na. Tech reviews and tutorials\nb. Financial news and market analysis\nc. Online shopping hauls and product reviews\nd. Health and fitness tips and advice",
    "Which of the following career paths sounds most appealing to you?\na. Software developer or IT professional\nb. Financial analyst or advisor\nc. E-commerce entrepreneur or marketer\nd. Healthcare practitioner or wellness coach",
    "If you were to start a blog or YouTube channel, what would it primarily focus on?\na. Tech and innovation updates\nb. Financial advice and investment strategies\nc. Product reviews and e-commerce tips\nd. Health and wellness tips and experiences",
    "What kind of books or magazines do you like to read in your spare time?\na. Science fiction and tech-related books\nb. Finance and business magazines\nc. Lifestyle and shopping catalogs\nd. Health and fitness publications",
    "If you had to attend a conference, which of the following would you be most excited about?\na. Tech and innovation conference\nb. Financial summit or investment seminar\nc. E-commerce and online retail expo\nd. Health and wellness convention",
    "When you watch documentaries or TV shows, what topics intrigue you the most?\na. Technological advancements and discoveries\nb. Financial scandals and success stories\nc. Behind-the-scenes of e-commerce giants\nd. Health transformations and medical breakthroughs",
    "Which of these hobbies or activities are you most likely to engage in?\na. Building or tinkering with gadgets\nb. Studying financial markets and investments\nc. Online shopping and finding great deals\nd. Exercising and practicing a healthy lifestyle",
    "If you were to invest time and effort in learning a new skill, which one would it be?\na. Coding and software development\nb. Financial analysis and investment strategies\nc. E-commerce business management\nd. Health and wellness coaching",
    "Which of the following YouTube channels would you subscribe to without hesitation?\na. Tech review and tutorial channels\nb. Financial education and investment channels\nc. Shopping haul and product review channels\nd. Health and fitness advice channels"
]

domain_question_options = {
    domain_questions[0]: {
        "a": "Technology and gadgets",
        "b": "Finance and investments",
        "c": "Online shopping and e-commerce",
        "d": "Health and wellness"
    },
    domain_questions[1]: {
        "a": "Exploring new tech devices and apps",
        "b": "Reading about financial markets and strategies",
        "c": "Online shopping for various products",
        "d": "Focusing on health and fitness activities"
    },
    domain_questions[2]: {
        "a": "Coding or programming",
        "b": "Stock trading or investing",
        "c": "Selling products online",
        "d": "Pursuing a healthy lifestyle"
    },
    domain_questions[3]: {
        "a": "Emerging technology trends",
        "b": "Financial planning and budgeting",
        "c": "Optimizing e-commerce businesses",
        "d": "Health and medical advancements"
    },
    domain_questions[4]: {
        "a": "The latest tech gadgets and innovations",
        "b": "Investment opportunities and financial tips",
        "c": "Online shopping finds and deals",
        "d": "Health and wellness practices"
    },
    domain_questions[5]: {
        "a": "Tech forums and subreddits",
        "b": "Financial planning and investing communities",
        "c": "E-commerce seller groups and platforms",
        "d": "Health and wellness forums and support groups"
    },
    domain_questions[6]: {
        "a": "Tech reviews and tutorials",
        "b": "Financial news and market analysis",
        "c": "Online shopping hauls and product reviews",
        "d": "Health and fitness tips and advice"
    },
    domain_questions[7]: {
        "a": "Software developer or IT professional",
        "b": "Financial analyst or advisor",
        "c": "E-commerce entrepreneur or marketer",
        "d": "Healthcare practitioner or wellness coach"
    },
    domain_questions[8]: {
        "a": "Tech and innovation updates",
        "b": "Financial advice and investment strategies",
        "c": "Product reviews and e-commerce tips",
        "d": "Health and wellness tips and experiences"
    },
    domain_questions[9]: {
        "a": "Science fiction and tech-related books",
        "b": "Finance and business magazines",
        "c": "Lifestyle and shopping catalogs",
        "d": "Health and fitness publications"
    },
    domain_questions[10]: {
        "a": "Tech and innovation conference",
        "b": "Financial summit or investment seminar",
        "c": "E-commerce and online retail expo",
        "d": "Health and wellness convention"
    },
    domain_questions[11]: {
        "a": "Technological advancements and discoveries",
        "b": "Financial scandals and success stories",
        "c": "Behind-the-scenes of e-commerce giants",
        "d": "Health transformations and medical breakthroughs"
    },
    domain_questions[12]: {
        "a": "Building or tinkering with gadgets",
        "b": "Studying financial markets and investments",
        "c": "Online shopping and finding great deals",
        "d": "Exercising and practicing a healthy lifestyle"
    },
    domain_questions[13]: {
        "a": "Coding and software development",
        "b": "Financial analysis and investment strategies",
        "c": "E-commerce business management",
        "d": "Health and wellness coaching"
    },
    domain_questions[14]: {
        "a": "Tech review and tutorial channels",
        "b": "Financial education and investment channels",
        "c": "Shopping haul and product review channels",
        "d": "Health and fitness advice channels"
    }
}


domain_all_datasets =[
    {"interest": "Technology and gadgets", "helping_others": "Exploring new tech devices and apps", "enjoy_learning": "Exploring new tech devices and apps", 
    "dabbled": "Coding or programming", "learn_more": "Emerging technology trends", "discuss_with_friends": "The latest tech gadgets and innovations",
    "online_communities": "Tech forums and subreddits", "content_preference": "Tech reviews and tutorials", "career_path": "Software developer or IT professional",
    "blog_or_channel": "Tech and innovation updates", "reading_preference": "Science fiction and tech-related books", "conference_preference": "Tech and innovation conference",
    "documentary_preference": "Technological advancements and discoveries", "hobby": "Building or tinkering with gadgets", "new_skill": "Coding and software development",
    "youtube_channel": "Tech review and tutorial channels", "startup_field": "Technology"},
     {"interest": "Technology and gadgets", "helping_others": "Exploring new tech devices and apps", "enjoy_learning": "Exploring new tech devices and apps", 
    "dabbled": "Coding or programming", "learn_more": "Emerging technology trends", "discuss_with_friends": "The latest tech gadgets and innovations",
    "online_communities": "Tech forums and subreddits", "content_preference": "Tech reviews and tutorials", "career_path": "Software developer or IT professional",
    "blog_or_channel": "Tech and innovation updates", "reading_preference": "Science fiction and tech-related books", "conference_preference": "Tech and innovation conference",
    "documentary_preference": "Technological advancements and discoveries", "hobby": "Building or tinkering with gadgets", "new_skill": "Coding and software development",
    "youtube_channel": "Tech review and tutorial channels", "startup_field": "Technology"},   
    {"interest": "Technology and gadgets", "helping_others": "Exploring new tech devices and apps", "enjoy_learning": "Exploring new tech devices and apps", 
    "dabbled": "Coding or programming", "learn_more": "Emerging technology trends", "discuss_with_friends": "The latest tech gadgets and innovations",
    "online_communities": "Tech forums and subreddits", "content_preference": "Tech reviews and tutorials", "career_path": "Software developer or IT professional",
    "blog_or_channel": "Tech and innovation updates", "reading_preference": "Science fiction and tech-related books", "conference_preference": "Tech and innovation conference",
    "documentary_preference": "Technological advancements and discoveries", "hobby": "Building or tinkering with gadgets", "new_skill": "Coding and software development",
    "youtube_channel": "Tech review and tutorial channels", "startup_field": "Technology"},   
    {"interest": "Technology and gadgets", "helping_others": "Exploring new tech devices and apps", "enjoy_learning": "Exploring new tech devices and apps", 
    "dabbled": "Coding or programming", "learn_more": "Emerging technology trends", "discuss_with_friends": "The latest tech gadgets and innovations",
    "online_communities": "Tech forums and subreddits", "content_preference": "Tech reviews and tutorials", "career_path": "Software developer or IT professional",
    "blog_or_channel": "Tech and innovation updates", "reading_preference": "Science fiction and tech-related books", "conference_preference": "Tech and innovation conference",
    "documentary_preference": "Technological advancements and discoveries", "hobby": "Building or tinkering with gadgets", "new_skill": "Coding and software development",
    "youtube_channel": "Tech review and tutorial channels", "startup_field": "Technology"},   
    {"interest": "Technology and gadgets", "helping_others": "Exploring new tech devices and apps", "enjoy_learning": "Exploring new tech devices and apps", 
    "dabbled": "Coding or programming", "learn_more": "Emerging technology trends", "discuss_with_friends": "The latest tech gadgets and innovations",
    "online_communities": "Tech forums and subreddits", "content_preference": "Tech reviews and tutorials", "career_path": "Software developer or IT professional",
    "blog_or_channel": "Tech and innovation updates", "reading_preference": "Science fiction and tech-related books", "conference_preference": "Tech and innovation conference",
    "documentary_preference": "Technological advancements and discoveries", "hobby": "Building or tinkering with gadgets", "new_skill": "Coding and software development",
    "youtube_channel": "Tech review and tutorial channels", "startup_field": "Technology"},   
    {"interest": "Technology and gadgets", "helping_others": "Exploring new tech devices and apps", "enjoy_learning": "Exploring new tech devices and apps", 
    "dabbled": "Coding or programming", "learn_more": "Emerging technology trends", "discuss_with_friends": "The latest tech gadgets and innovations",
    "online_communities": "Tech forums and subreddits", "content_preference": "Tech reviews and tutorials", "career_path": "Software developer or IT professional",
    "blog_or_channel": "Tech and innovation updates", "reading_preference": "Science fiction and tech-related books", "conference_preference": "Tech and innovation conference",
    "documentary_preference": "Technological advancements and discoveries", "hobby": "Building or tinkering with gadgets", "new_skill": "Coding and software development",
    "youtube_channel": "Tech review and tutorial channels", "startup_field": "Technology"},

    {"interest": "Finance and investments", "helping_others": "Reading about financial markets and strategies", "enjoy_learning": "Reading about financial markets and strategies",
    "dabbled": "Stock trading or investing", "learn_more": "Financial planning and budgeting", "discuss_with_friends": "Investment opportunities and financial tips",
    "online_communities": "Financial planning and investing communities", "content_preference": "Financial news and market analysis", "career_path": "Financial analyst or advisor",
    "blog_or_channel": "Financial advice and investment strategies", "reading_preference": "Finance and business magazines", "conference_preference": "Financial summit or investment seminar",
    "documentary_preference": "Financial scandals and success stories", "hobby": "Studying financial markets and investments", "new_skill": "Financial analysis and investment strategies",
    "youtube_channel": "Financial education and investment channels", "startup_field": "Finance"},
    {"interest": "Finance and investments", "helping_others": "Discussing stock market trends and investment strategies", "enjoy_learning": "Studying financial analysis and economic indicators", 
    "dabbled": "Day trading and investing in cryptocurrencies", "learn_more": "Advanced financial modeling and algorithmic trading", "discuss_with_friends": "Sharing investment success stories and market tips",
    "online_communities": "Stock trading forums and cryptocurrency investor groups", "content_preference": "Financial podcasts and in-depth market analysis articles", "career_path": "Hedge fund manager or investment consultant",
    "blog_or_channel": "Stock market analysis blog and YouTube channel", "reading_preference": "Economics journals and finance research papers", "conference_preference": "Global financial summits and cryptocurrency conferences",
    "documentary_preference": "Inside look into major financial institutions and their impact on the global economy", "hobby": "Collecting rare and valuable financial artifacts", "new_skill": "Financial risk management and portfolio optimization",
    "youtube_channel": "Cryptocurrency trading and investment channels", "startup_field": "Finance"},    
    {"interest": "Finance and investments", "helping_others": "Discussing stock market trends and investment strategies", "enjoy_learning": "Studying financial analysis and economic indicators", 
    "dabbled": "Day trading and investing in cryptocurrencies", "learn_more": "Advanced financial modeling and algorithmic trading", "discuss_with_friends": "Sharing investment success stories and market tips",
    "online_communities": "Stock trading forums and cryptocurrency investor groups", "content_preference": "Financial podcasts and in-depth market analysis articles", "career_path": "Hedge fund manager or investment consultant",
    "blog_or_channel": "Stock market analysis blog and YouTube channel", "reading_preference": "Economics journals and finance research papers", "conference_preference": "Global financial summits and cryptocurrency conferences",
    "documentary_preference": "Inside look into major financial institutions and their impact on the global economy", "hobby": "Collecting rare and valuable financial artifacts", "new_skill": "Financial risk management and portfolio optimization",
    "youtube_channel": "Cryptocurrency trading and investment channels", "startup_field": "Finance"},   
    {"interest": "Finance and investments", "helping_others": "Discussing stock market trends and investment strategies", "enjoy_learning": "Studying financial analysis and economic indicators", 
    "dabbled": "Day trading and investing in cryptocurrencies", "learn_more": "Advanced financial modeling and algorithmic trading", "discuss_with_friends": "Sharing investment success stories and market tips",
    "online_communities": "Stock trading forums and cryptocurrency investor groups", "content_preference": "Financial podcasts and in-depth market analysis articles", "career_path": "Hedge fund manager or investment consultant",
    "blog_or_channel": "Stock market analysis blog and YouTube channel", "reading_preference": "Economics journals and finance research papers", "conference_preference": "Global financial summits and cryptocurrency conferences",
    "documentary_preference": "Inside look into major financial institutions and their impact on the global economy", "hobby": "Collecting rare and valuable financial artifacts", "new_skill": "Financial risk management and portfolio optimization",
    "youtube_channel": "Cryptocurrency trading and investment channels", "startup_field": "Finance"},  
    {"interest": "Finance and investments", "helping_others": "Discussing stock market trends and investment strategies", "enjoy_learning": "Studying financial analysis and economic indicators", 
    "dabbled": "Day trading and investing in cryptocurrencies", "learn_more": "Advanced financial modeling and algorithmic trading", "discuss_with_friends": "Sharing investment success stories and market tips",
    "online_communities": "Stock trading forums and cryptocurrency investor groups", "content_preference": "Financial podcasts and in-depth market analysis articles", "career_path": "Hedge fund manager or investment consultant",
    "blog_or_channel": "Stock market analysis blog and YouTube channel", "reading_preference": "Economics journals and finance research papers", "conference_preference": "Global financial summits and cryptocurrency conferences",
    "documentary_preference": "Inside look into major financial institutions and their impact on the global economy", "hobby": "Collecting rare and valuable financial artifacts", "new_skill": "Financial risk management and portfolio optimization",
    "youtube_channel": "Cryptocurrency trading and investment channels", "startup_field": "Finance"},  
    {"interest": "Finance and investments", "helping_others": "Discussing stock market trends and investment strategies", "enjoy_learning": "Studying financial analysis and economic indicators", 
    "dabbled": "Day trading and investing in cryptocurrencies", "learn_more": "Advanced financial modeling and algorithmic trading", "discuss_with_friends": "Sharing investment success stories and market tips",
    "online_communities": "Stock trading forums and cryptocurrency investor groups", "content_preference": "Financial podcasts and in-depth market analysis articles", "career_path": "Hedge fund manager or investment consultant",
    "blog_or_channel": "Stock market analysis blog and YouTube channel", "reading_preference": "Economics journals and finance research papers", "conference_preference": "Global financial summits and cryptocurrency conferences",
    "documentary_preference": "Inside look into major financial institutions and their impact on the global economy", "hobby": "Collecting rare and valuable financial artifacts", "new_skill": "Financial risk management and portfolio optimization",
    "youtube_channel": "Cryptocurrency trading and investment channels", "startup_field": "Finance"},


    
    {"interest": "Online shopping and e-commerce", "helping_others": "Online shopping for various products", "enjoy_learning": "Optimizing e-commerce businesses",
    "dabbled": "Selling products online", "learn_more": "Optimizing e-commerce businesses", "discuss_with_friends": "Online shopping finds and deals",
    "online_communities": "E-commerce seller groups and platforms", "content_preference": "Online shopping hauls and product reviews", "career_path": "E-commerce entrepreneur or marketer",
    "blog_or_channel": "Product reviews and e-commerce tips", "reading_preference": "Lifestyle and shopping catalogs", "conference_preference": "E-commerce and online retail expo",
    "documentary_preference": "Behind-the-scenes of e-commerce giants", "hobby": "Online shopping and finding great deals", "new_skill": "E-commerce business management",
    "youtube_channel": "Shopping haul and product review channels", "startup_field": "E-commerce"},
     {"interest": "Online shopping and e-commerce", "helping_others": "Providing e-commerce business consultation and tips", "enjoy_learning": "Studying customer behavior and market trends in online retail", 
    "dabbled": "Managing an online store selling handmade products", "learn_more": "Implementing advanced SEO strategies for e-commerce websites", "discuss_with_friends": "Sharing online shopping hacks and best deals",
    "online_communities": "E-commerce business owner forums and digital marketing groups", "content_preference": "E-commerce case studies and successful online store stories", "career_path": "E-commerce strategist or digital marketing expert",
    "blog_or_channel": "E-commerce success blog and YouTube channel", "reading_preference": "Books on online consumer psychology and digital marketing", "conference_preference": "E-commerce expos and digital marketing summits",
    "documentary_preference": "Behind-the-scenes of major e-commerce platforms and their impact on global trade", "hobby": "Collecting vintage online shopping advertisements", "new_skill": "E-commerce analytics and conversion rate optimization",
    "youtube_channel": "E-commerce growth hacks and online retail strategies channels", "startup_field": "E-commerce and digital marketing"},   
    {"interest": "Online shopping and e-commerce", "helping_others": "Providing e-commerce business consultation and tips", "enjoy_learning": "Studying customer behavior and market trends in online retail", 
    "dabbled": "Managing an online store selling handmade products", "learn_more": "Implementing advanced SEO strategies for e-commerce websites", "discuss_with_friends": "Sharing online shopping hacks and best deals",
    "online_communities": "E-commerce business owner forums and digital marketing groups", "content_preference": "E-commerce case studies and successful online store stories", "career_path": "E-commerce strategist or digital marketing expert",
    "blog_or_channel": "E-commerce success blog and YouTube channel", "reading_preference": "Books on online consumer psychology and digital marketing", "conference_preference": "E-commerce expos and digital marketing summits",
    "documentary_preference": "Behind-the-scenes of major e-commerce platforms and their impact on global trade", "hobby": "Collecting vintage online shopping advertisements", "new_skill": "E-commerce analytics and conversion rate optimization",
    "youtube_channel": "E-commerce growth hacks and online retail strategies channels", "startup_field": "E-commerce and digital marketing"},   
    {"interest": "Online shopping and e-commerce", "helping_others": "Providing e-commerce business consultation and tips", "enjoy_learning": "Studying customer behavior and market trends in online retail", 
    "dabbled": "Managing an online store selling handmade products", "learn_more": "Implementing advanced SEO strategies for e-commerce websites", "discuss_with_friends": "Sharing online shopping hacks and best deals",
    "online_communities": "E-commerce business owner forums and digital marketing groups", "content_preference": "E-commerce case studies and successful online store stories", "career_path": "E-commerce strategist or digital marketing expert",
    "blog_or_channel": "E-commerce success blog and YouTube channel", "reading_preference": "Books on online consumer psychology and digital marketing", "conference_preference": "E-commerce expos and digital marketing summits",
    "documentary_preference": "Behind-the-scenes of major e-commerce platforms and their impact on global trade", "hobby": "Collecting vintage online shopping advertisements", "new_skill": "E-commerce analytics and conversion rate optimization",
    "youtube_channel": "E-commerce growth hacks and online retail strategies channels", "startup_field": "E-commerce and digital marketing"},    
    {"interest": "Online shopping and e-commerce", "helping_others": "Providing e-commerce business consultation and tips", "enjoy_learning": "Studying customer behavior and market trends in online retail", 
    "dabbled": "Managing an online store selling handmade products", "learn_more": "Implementing advanced SEO strategies for e-commerce websites", "discuss_with_friends": "Sharing online shopping hacks and best deals",
    "online_communities": "E-commerce business owner forums and digital marketing groups", "content_preference": "E-commerce case studies and successful online store stories", "career_path": "E-commerce strategist or digital marketing expert",
    "blog_or_channel": "E-commerce success blog and YouTube channel", "reading_preference": "Books on online consumer psychology and digital marketing", "conference_preference": "E-commerce expos and digital marketing summits",
    "documentary_preference": "Behind-the-scenes of major e-commerce platforms and their impact on global trade", "hobby": "Collecting vintage online shopping advertisements", "new_skill": "E-commerce analytics and conversion rate optimization",
    "youtube_channel": "E-commerce growth hacks and online retail strategies channels", "startup_field": "E-commerce and digital marketing"},   
    {"interest": "Online shopping and e-commerce", "helping_others": "Providing e-commerce business consultation and tips", "enjoy_learning": "Studying customer behavior and market trends in online retail", 
    "dabbled": "Managing an online store selling handmade products", "learn_more": "Implementing advanced SEO strategies for e-commerce websites", "discuss_with_friends": "Sharing online shopping hacks and best deals",
    "online_communities": "E-commerce business owner forums and digital marketing groups", "content_preference": "E-commerce case studies and successful online store stories", "career_path": "E-commerce strategist or digital marketing expert",
    "blog_or_channel": "E-commerce success blog and YouTube channel", "reading_preference": "Books on online consumer psychology and digital marketing", "conference_preference": "E-commerce expos and digital marketing summits",
    "documentary_preference": "Behind-the-scenes of major e-commerce platforms and their impact on global trade", "hobby": "Collecting vintage online shopping advertisements", "new_skill": "E-commerce analytics and conversion rate optimization",
    "youtube_channel": "E-commerce growth hacks and online retail strategies channels", "startup_field": "E-commerce and digital marketing"},

    {"interest": "Health and wellness", "helping_others": "Focusing on health and fitness activities", "enjoy_learning": "Pursuing a healthy lifestyle",
    "dabbled": "Pursuing a healthy lifestyle", "learn_more": "Health and medical advancements", "discuss_with_friends": "Health and wellness practices",
    "online_communities": "Health and wellness forums and support groups", "content_preference": "Health and fitness tips and advice", "career_path": "Healthcare practitioner or wellness coach",
    "blog_or_channel": "Health and wellness tips and experiences", "reading_preference": "Health and fitness publications", "conference_preference": "Health and wellness convention",
    "documentary_preference": "Health transformations and medical breakthroughs", "hobby": "Exercising and practicing a healthy lifestyle", "new_skill": "Health and wellness coaching",
    "youtube_channel": "Health and fitness advice channels", "startup_field": "Healthcare"},
    {"interest": "Health and wellness", "helping_others": "Volunteering at local healthcare clinics and wellness centers", "enjoy_learning": "Studying holistic medicine and alternative therapies", 
    "dabbled": "Participating in medical research studies", "learn_more": "Exploring cutting-edge medical technologies and treatments", "discuss_with_friends": "Sharing fitness routines and healthy recipes",
    "online_communities": "Healthcare professionals networks and medical research forums", "content_preference": "Medical journals and research publications", "career_path": "Medical researcher or holistic healthcare practitioner",
    "blog_or_channel": "Holistic health and wellness blog and YouTube channel", "reading_preference": "Books on integrative medicine and natural healing", "conference_preference": "Healthcare conferences on holistic wellness and preventive medicine",
    "documentary_preference": "Documentaries on medical breakthroughs and alternative healing practices", "hobby": "Gardening and cultivating medicinal plants", "new_skill": "Holistic healthcare practices and natural remedies",
    "youtube_channel": "Holistic health and wellness channels focusing on mind-body-spirit healing", "startup_field": "Holistic healthcare and wellness industry"},  
    {"interest": "Health and wellness", "helping_others": "Volunteering at local healthcare clinics and wellness centers", "enjoy_learning": "Studying holistic medicine and alternative therapies", 
    "dabbled": "Participating in medical research studies", "learn_more": "Exploring cutting-edge medical technologies and treatments", "discuss_with_friends": "Sharing fitness routines and healthy recipes",
    "online_communities": "Healthcare professionals networks and medical research forums", "content_preference": "Medical journals and research publications", "career_path": "Medical researcher or holistic healthcare practitioner",
    "blog_or_channel": "Holistic health and wellness blog and YouTube channel", "reading_preference": "Books on integrative medicine and natural healing", "conference_preference": "Healthcare conferences on holistic wellness and preventive medicine",
    "documentary_preference": "Documentaries on medical breakthroughs and alternative healing practices", "hobby": "Gardening and cultivating medicinal plants", "new_skill": "Holistic healthcare practices and natural remedies",
    "youtube_channel": "Holistic health and wellness channels focusing on mind-body-spirit healing", "startup_field": "Holistic healthcare and wellness industry"},   
    {"interest": "Health and wellness", "helping_others": "Volunteering at local healthcare clinics and wellness centers", "enjoy_learning": "Studying holistic medicine and alternative therapies", 
    "dabbled": "Participating in medical research studies", "learn_more": "Exploring cutting-edge medical technologies and treatments", "discuss_with_friends": "Sharing fitness routines and healthy recipes",
    "online_communities": "Healthcare professionals networks and medical research forums", "content_preference": "Medical journals and research publications", "career_path": "Medical researcher or holistic healthcare practitioner",
    "blog_or_channel": "Holistic health and wellness blog and YouTube channel", "reading_preference": "Books on integrative medicine and natural healing", "conference_preference": "Healthcare conferences on holistic wellness and preventive medicine",
    "documentary_preference": "Documentaries on medical breakthroughs and alternative healing practices", "hobby": "Gardening and cultivating medicinal plants", "new_skill": "Holistic healthcare practices and natural remedies",
    "youtube_channel": "Holistic health and wellness channels focusing on mind-body-spirit healing", "startup_field": "Holistic healthcare and wellness industry"},  
    {"interest": "Health and wellness", "helping_others": "Volunteering at local healthcare clinics and wellness centers", "enjoy_learning": "Studying holistic medicine and alternative therapies", 
    "dabbled": "Participating in medical research studies", "learn_more": "Exploring cutting-edge medical technologies and treatments", "discuss_with_friends": "Sharing fitness routines and healthy recipes",
    "online_communities": "Healthcare professionals networks and medical research forums", "content_preference": "Medical journals and research publications", "career_path": "Medical researcher or holistic healthcare practitioner",
    "blog_or_channel": "Holistic health and wellness blog and YouTube channel", "reading_preference": "Books on integrative medicine and natural healing", "conference_preference": "Healthcare conferences on holistic wellness and preventive medicine",
    "documentary_preference": "Documentaries on medical breakthroughs and alternative healing practices", "hobby": "Gardening and cultivating medicinal plants", "new_skill": "Holistic healthcare practices and natural remedies",
    "youtube_channel": "Holistic health and wellness channels focusing on mind-body-spirit healing", "startup_field": "Holistic healthcare and wellness industry"},   
    {"interest": "Health and wellness", "helping_others": "Volunteering at local healthcare clinics and wellness centers", "enjoy_learning": "Studying holistic medicine and alternative therapies", 
    "dabbled": "Participating in medical research studies", "learn_more": "Exploring cutting-edge medical technologies and treatments", "discuss_with_friends": "Sharing fitness routines and healthy recipes",
    "online_communities": "Healthcare professionals networks and medical research forums", "content_preference": "Medical journals and research publications", "career_path": "Medical researcher or holistic healthcare practitioner",
    "blog_or_channel": "Holistic health and wellness blog and YouTube channel", "reading_preference": "Books on integrative medicine and natural healing", "conference_preference": "Healthcare conferences on holistic wellness and preventive medicine",
    "documentary_preference": "Documentaries on medical breakthroughs and alternative healing practices", "hobby": "Gardening and cultivating medicinal plants", "new_skill": "Holistic healthcare practices and natural remedies",
    "youtube_channel": "Holistic health and wellness channels focusing on mind-body-spirit healing", "startup_field": "Holistic healthcare and wellness industry"}

]



e_comerce_questions = [
    "What type of products or services are you most interested in selling?\na) Physical products\nb) Digital products (e.g., e-books, software)\nc) Both physical and digital products\nd) B2B services",
    
    "Are you more interested in selling to individual consumers or other businesses?\na) Individual consumers (B2C)\nb) Other businesses (B2B)\nc) Both B2C and B2B\nd) Not sure",
    
    "Do you have a unique and innovative product that sets you apart from competitors?\na) Yes, it's unique\nb) No, it's similar to existing products\nc) I'm not sure",
    
    "Are you comfortable managing a physical inventory and shipping logistics?\na) Yes\nb) No, I prefer digital products\nc) I'm open to both",
    
    "Are you interested in building a marketplace that connects multiple sellers and buyers?\na) Yes, I want to create a marketplace\nb) No, I prefer to sell my own products or services\nc) I'm not sure",
    
    "Are you willing to invest time and resources in content creation, such as blogging or video production?\na) Yes, I enjoy creating content\nb) No, I prefer not to focus on content creation\nc) I'm open to it",
    
    "Do you have existing business relationships with other companies that could be leveraged for B2B transactions?\na) Yes\nb) No\nc) I'm not sure",
    
    "Are you interested in selling subscription-based products or services?\na) Yes, I want to offer subscriptions\nb) No, I prefer one-time sales\nc) I'm open to both",
    
    "Are you technologically savvy and comfortable with online marketing and e-commerce platforms?\na) Yes, I have technical skills\nb) No, I may need assistance with technology\nc) I'm moderately tech-savvy",
    
    "What is your long-term vision for your e-commerce venture?\na) Building a large online retail store\nb) Creating a digital product or content empire\nc) Establishing a thriving online marketplace\nd) Providing specialized B2B services"
]


e_comerce_question_options = {
    e_comerce_questions[0]: {
        "a": "Physical products",
        "b": "Digital products (e.g., e-books, software)",
        "c": "Both physical and digital products",
        "d": "B2B services"
    },
    e_comerce_questions[1]: {
        "a": "Individual consumers (B2C)",
        "b": "Other businesses (B2B)",
        "c": "Both B2C and B2B",
        "d": "Not sure"
    },
    e_comerce_questions[2]: {
        "a": "Yes, it's unique",
        "b": "No, it's similar to existing products",
        "c": "I'm not sure"
    },
   e_comerce_questions[3]: {
        "a": "Yes",
        "b": "No, I prefer digital products",
        "c": "I'm open to both"
    },
    e_comerce_questions[4]: {
        "a": "Yes, I want to create a marketplace",
        "b": "No, I prefer to sell my own products or services",
        "c": "I'm not sure"
    },
    e_comerce_questions[5]: {
        "a": "Yes, I enjoy creating content",
        "b": "No, I prefer not to focus on content creation",
        "c": "I'm open to it"
    },
    e_comerce_questions[6]: {
        "a": "Yes",
        "b": "No",
        "c": "I'm not sure"
    },
    e_comerce_questions[7]: {
        "a": "Yes, I want to offer subscriptions",
        "b": "No, I prefer one-time sales",
        "c": "I'm open to both"
    },
    e_comerce_questions[8]: {
        "a": "Yes, I have technical skills",
        "b": "No, I may need assistance with technology",
        "c": "I'm moderately tech-savvy"
    },
    e_comerce_questions[9]: {
        "a": "Building a large online retail store",
        "b": "Creating a digital product or content empire",
        "c": "Establishing a thriving online marketplace",
        "d": "Providing specialized B2B services"
    }
}


e_comerce_data_set = [
    {
        "question_1": "Physical products",
        "question_2": "Individual consumers (B2C)",
        "question_3": "Yes, it's unique",
        "question_4": "Yes",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I enjoy creating content",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Building a large online retail store",
        "startup_domain": "Online Retail"
    },{
        "question_1": "Physical products",
        "question_2": "Individual consumers (B2C)",
        "question_3": "Yes, it's unique",
        "question_4": "Yes",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I enjoy creating content",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Building a large online retail store",
        "startup_domain": "Online Retail"
    },
    {
        "question_1": "Physical products",
        "question_2": "Individual consumers (B2C)",
        "question_3": "Yes, it's unique",
        "question_4": "Yes",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I enjoy creating content",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Building a large online retail store",
        "startup_domain": "Online Retail"
    },
    {
        "question_1": "Physical products",
        "question_2": "Individual consumers (B2C)",
        "question_3": "Yes, it's unique",
        "question_4": "Yes",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I enjoy creating content",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Building a large online retail store",
        "startup_domain": "Online Retail"
    },
    {
        "question_1": "Physical products",
        "question_2": "Individual consumers (B2C)",
        "question_3": "Yes, it's unique",
        "question_4": "Yes",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I enjoy creating content",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Building a large online retail store",
        "startup_domain": "Online Retail"
    },
    {
        "question_1": "Physical products",
        "question_2": "Individual consumers (B2C)",
        "question_3": "Yes, it's unique",
        "question_4": "Yes",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I enjoy creating content",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Building a large online retail store",
        "startup_domain": "Online Retail"
    },


    {
        "question_1": "Digital products",
        "question_2": "Individual consumers (B2C)",
        "question_3": "Yes, it's unique",
        "question_4": "No, I prefer digital products",
        "question_5": "Yes, I enjoy creating content",
        "question_6": "No",
        "question_7": "No",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Creating a digital product or content empire",
        "startup_domain": "Digital Products"
    },
    {
        "question_1": "Digital products (e.g., e-books, software)",
        "question_2": "Individual consumers (B2C)",
        "question_3": "Yes, it's unique",
        "question_4": "No, I prefer digital products",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I enjoy creating digital content",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Creating a digital product or content empire",
        "startup_domain": "Digital Products"
    },
    {
        "question_1": "Digital products (e.g., e-books, software)",
        "question_2": "Individual consumers (B2C)",
        "question_3": "Yes, it's unique",
        "question_4": "No, I prefer digital products",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I enjoy creating digital content",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Creating a digital product or content empire",
        "startup_domain": "Digital Products"
    },
    {
        "question_1": "Digital products (e.g., e-books, software)",
        "question_2": "Individual consumers (B2C)",
        "question_3": "Yes, it's unique",
        "question_4": "No, I prefer digital products",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I enjoy creating digital content",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Creating a digital product or content empire",
        "startup_domain": "Digital Products"
    },
    {
        "question_1": "Digital products (e.g., e-books, software)",
        "question_2": "Individual consumers (B2C)",
        "question_3": "Yes, it's unique",
        "question_4": "No, I prefer digital products",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I enjoy creating digital content",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Creating a digital product or content empire",
        "startup_domain": "Digital Products"
    },
    {
        "question_1": "Digital products (e.g., e-books, software)",
        "question_2": "Individual consumers (B2C)",
        "question_3": "Yes, it's unique",
        "question_4": "No, I prefer digital products",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I enjoy creating digital content",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Creating a digital product or content empire",
        "startup_domain": "Digital Products"
    },

    {
        "question_1": "Both physical and digital products",
        "question_2": "Both B2C and B2B",
        "question_3": "Yes, it's unique",
        "question_4": "Yes, I'm open to both",
        "question_5": "Yes, I'm open to it",
        "question_6": "No",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "I'm moderately tech-savvy",
        "question_10": "Establishing a thriving online marketplace",
        "startup_domain": "Marketplace and Platform"
    },{
        "question_1": "Both physical and digital products",
        "question_2": "Both B2C and B2B",
        "question_3": "Yes, it's unique",
        "question_4": "I'm open to both",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I enjoy creating content",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Establishing a thriving online marketplace",
        "startup_domain": "Marketplace and Platform"
    },
    {
        "question_1": "Both physical and digital products",
        "question_2": "Both B2C and B2B",
        "question_3": "Yes, it's unique",
        "question_4": "I'm open to both",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I enjoy creating content",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Establishing a thriving online marketplace",
        "startup_domain": "Marketplace and Platform"
    },
    {
        "question_1": "Both physical and digital products",
        "question_2": "Both B2C and B2B",
        "question_3": "Yes, it's unique",
        "question_4": "I'm open to both",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I enjoy creating content",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Establishing a thriving online marketplace",
        "startup_domain": "Marketplace and Platform"
    },
    {
        "question_1": "Both physical and digital products",
        "question_2": "Both B2C and B2B",
        "question_3": "Yes, it's unique",
        "question_4": "I'm open to both",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I enjoy creating content",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Establishing a thriving online marketplace",
        "startup_domain": "Marketplace and Platform"
    },
    {
        "question_1": "Both physical and digital products",
        "question_2": "Both B2C and B2B",
        "question_3": "Yes, it's unique",
        "question_4": "I'm open to both",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I enjoy creating content",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Establishing a thriving online marketplace",
        "startup_domain": "Marketplace and Platform"
    },

    {
        "question_1": "B2B services",
        "question_2": "Other businesses (B2B)",
        "question_3": "Yes, it's unique",
        "question_4": "No, I prefer digital products",
        "question_5": "I'm open to it",
        "question_6": "No",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Providing specialized B2B services",
        "startup_domain": "Business-to-Business (B2B) E-commerce"
    },
        {
        "question_1": "B2B services",
        "question_2": "Other businesses (B2B)",
        "question_3": "Yes, it's unique",
        "question_4": "Yes",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I'm open to it",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Providing specialized B2B services",
        "startup_domain": "Business-to-Business (B2B) E-commerce"
    },
    {
        "question_1": "B2B services",
        "question_2": "Other businesses (B2B)",
        "question_3": "Yes, it's unique",
        "question_4": "Yes",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I'm open to it",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Providing specialized B2B services",
        "startup_domain": "Business-to-Business (B2B) E-commerce"
    },
    {
        "question_1": "B2B services",
        "question_2": "Other businesses (B2B)",
        "question_3": "Yes, it's unique",
        "question_4": "Yes",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I'm open to it",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Providing specialized B2B services",
        "startup_domain": "Business-to-Business (B2B) E-commerce"
    },
    {
        "question_1": "B2B services",
        "question_2": "Other businesses (B2B)",
        "question_3": "Yes, it's unique",
        "question_4": "Yes",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I'm open to it",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Providing specialized B2B services",
        "startup_domain": "Business-to-Business (B2B) E-commerce"
    },
    {
        "question_1": "B2B services",
        "question_2": "Other businesses (B2B)",
        "question_3": "Yes, it's unique",
        "question_4": "Yes",
        "question_5": "Yes, I want to create a marketplace",
        "question_6": "Yes, I'm open to it",
        "question_7": "Yes",
        "question_8": "Yes, I want to offer subscriptions",
        "question_9": "Yes, I have technical skills",
        "question_10": "Providing specialized B2B services",
        "startup_domain": "Business-to-Business (B2B) E-commerce"
    }
]


finance_questions = [
    "What aspect of finance interests you the most?\na) Managing corporate finances\nb) Helping individuals with their financial goals\nc) Working in financial markets and trading\nd) Assisting companies in raising capital",
    "Which of the following appeals to you as a career goal?\na) Maximizing shareholder value for a corporation\nb) Helping individuals plan for retirement and investments\nc) Becoming a trader in financial markets\nd) Advising companies on mergers and acquisitions",
    "Do you enjoy analyzing financial data and market trends?\na) Yes, I find it fascinating\nb) Not particularly\nc) I'm unsure",
    "Are you interested in providing financial advice to individuals or businesses?\na) Yes, I enjoy helping others make financial decisions\nb) No, I prefer working with numbers and data\nc) I'm open to both",
    "How comfortable are you with risk and uncertainty in financial matters?\na) I'm comfortable with risk\nb) I prefer more stable and predictable situations\nc) It depends on the context",
    "Which financial instrument or concept interests you the most?\na) Stocks and bonds\nb) Retirement planning and savings\nc) Derivatives and options\nd) Capital budgeting and investment analysis",
    "Are you more interested in working with individuals or institutions?\na) I prefer working with individuals\nb) I prefer working with institutions and businesses\nc) I'm open to both",
    "What appeals to you about finance: the opportunity to make strategic financial decisions or the ability to analyze financial markets in real-time?\na) Making strategic financial decisions\nb) Analyzing financial markets in real-time\nc) Both options interest me",
    "Are you interested in a career that involves mergers, acquisitions, and corporate finance transactions?\na) Yes, I find it intriguing\nb) No, I prefer other aspects of finance\nc) I'm undecided",
    "How would you describe your long-term career aspirations in finance?\na) Climbing the corporate ladder in a finance department\nb) Becoming a certified financial planner or advisor\nc) Becoming a professional trader or analyst\nd) Working in investment banking or corporate finance"
]

finance_question_options = {
    finance_questions[0]: {
        "a": "Managing corporate finances",
        "b": "Helping individuals with their financial goals",
        "c": "Working in financial markets and trading",
        "d": "Assisting companies in raising capital"
    },
    finance_questions[1]: {
        "a": "Maximizing shareholder value for a corporation",
        "b": "Helping individuals plan for retirement and investments",
        "c": "Becoming a trader in financial markets",
        "d": "Advising companies on mergers and acquisitions"
    },
    finance_questions[2]: {
        "a": "Yes, I find it fascinating",
        "b": "Not particularly",
        "c": "I'm unsure"
    },
    finance_questions[3]: {
        "a": "Yes, I enjoy helping others make financial decisions",
        "b": "No, I prefer working with numbers and data",
        "c": "I'm open to both"
    },
    finance_questions[4]: {
        "a": "I'm comfortable with risk",
        "b": "I prefer more stable and predictable situations",
        "c": "It depends on the context"
    },
    finance_questions[5]: {
        "a": "Stocks and bonds",
        "b": "Retirement planning and savings",
        "c": "Derivatives and options",
        "d": "Capital budgeting and investment analysis"
    },
    finance_questions[6]: {
        "a": "I prefer working with individuals",
        "b": "I prefer working with institutions and businesses",
        "c": "I'm open to both"
    },
    finance_questions[7]: {
        "a": "Making strategic financial decisions",
        "b": "Analyzing financial markets in real-time",
        "c": "Both options interest me"
    },
    finance_questions[8]: {
        "a": "Yes, I find it intriguing",
        "b": "No, I prefer other aspects of finance",
        "c": "I'm undecided"
    },
    finance_questions[9]: {
        "a": "Climbing the corporate ladder in a finance department",
        "b": "Becoming a certified financial planner or advisor",
        "c": "Becoming a professional trader or analyst",
        "d": "Working in investment banking or corporate finance"
    }
}



finance_data_set = [
    {
        "question_1": "Managing corporate finances",
        "question_2": "Maximizing shareholder value for a corporation",
        "question_3": "Yes, I find it fascinating",
        "question_4": "No, I prefer working with numbers and data",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Stocks and bonds",
        "question_7": "I prefer working with institutions and businesses",
        "question_8": "Making strategic financial decisions",
        "question_9": "No, I prefer other aspects of finance",
        "question_10": "Climbing the corporate ladder in a finance department",
        "startup_domain": "Corporate Finance and Financial Management"
    },{
        "question_1": "Managing corporate finances",
        "question_2": "Maximizing shareholder value for a corporation",
        "question_3": "Yes, I find it fascinating",
        "question_4": "No, I prefer working with numbers and data",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Stocks and bonds",
        "question_7": "I prefer working with institutions and businesses",
        "question_8": "Making strategic financial decisions",
        "question_9": "No, I prefer other aspects of finance",
        "question_10": "Climbing the corporate ladder in a finance department",
        "startup_domain": "Corporate Finance and Financial Management"
    },
    {
        "question_1": "Managing corporate finances",
        "question_2": "Maximizing shareholder value for a corporation",
        "question_3": "Yes, I find it fascinating",
        "question_4": "No, I prefer working with numbers and data",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Stocks and bonds",
        "question_7": "I prefer working with institutions and businesses",
        "question_8": "Making strategic financial decisions",
        "question_9": "No, I prefer other aspects of finance",
        "question_10": "Becoming a financial analyst in a corporation",
        "startup_domain": "Corporate Finance and Financial Management"
    },
    {
        "question_1": "Managing corporate finances",
        "question_2": "Maximizing shareholder value for a corporation",
        "question_3": "Yes, I find it fascinating",
        "question_4": "No, I prefer working with numbers and data",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Stocks and bonds",
        "question_7": "I prefer working with institutions and businesses",
        "question_8": "Making strategic financial decisions",
        "question_9": "No, I prefer other aspects of finance",
        "question_10": "Leading financial planning and analysis in a corporation",
        "startup_domain": "Corporate Finance and Financial Management"
    },
    {
        "question_1": "Managing corporate finances",
        "question_2": "Maximizing shareholder value for a corporation",
        "question_3": "Yes, I find it fascinating",
        "question_4": "No, I prefer working with numbers and data",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Stocks and bonds",
        "question_7": "I prefer working with institutions and businesses",
        "question_8": "Making strategic financial decisions",
        "question_9": "No, I prefer other aspects of finance",
        "question_10": "Becoming a finance manager in a corporation",
        "startup_domain": "Corporate Finance and Financial Management"
    },
    {
        "question_1": "Managing corporate finances",
        "question_2": "Maximizing shareholder value for a corporation",
        "question_3": "Yes, I find it fascinating",
        "question_4": "No, I prefer working with numbers and data",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Stocks and bonds",
        "question_7": "I prefer working with institutions and businesses",
        "question_8": "Making strategic financial decisions",
        "question_9": "No, I prefer other aspects of finance",
        "question_10": "Becoming a CFO in a corporation",
        "startup_domain": "Corporate Finance and Financial Management"
    },

    {
        "question_1": "Helping individuals with their financial goals",
        "question_2": "Helping individuals plan for retirement and investments",
        "question_3": "Yes, I find it fascinating",
        "question_4": "Yes, I enjoy helping others make financial decisions",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Retirement planning and savings",
        "question_7": "I prefer working with individuals",
        "question_8": "Making strategic financial decisions",
        "question_9": "Yes, I find it intriguing",
        "question_10": "Becoming a certified financial planner or advisor",
        "startup_domain": "Wealthtech"
    },    {
        "question_1": "Helping individuals plan for retirement and investments",
        "question_2": "Becoming a certified financial planner or advisor",
        "question_3": "Yes, I find it fascinating",
        "question_4": "Yes, I enjoy helping others make financial decisions",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Retirement planning and savings",
        "question_7": "I prefer working with individuals",
        "question_8": "Both options interest me",
        "question_9": "No, I prefer other aspects of finance",
        "question_10": "Becoming a certified financial planner or advisor",
        "startup_domain": "Wealthtech"
    },
    {
        "question_1": "Helping individuals plan for retirement and investments",
        "question_2": "Becoming a certified financial planner or advisor",
        "question_3": "Yes, I find it fascinating",
        "question_4": "Yes, I enjoy helping others make financial decisions",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Retirement planning and savings",
        "question_7": "I prefer working with individuals",
        "question_8": "Both options interest me",
        "question_9": "No, I prefer other aspects of finance",
        "question_10": "Becoming a wealth management advisor",
        "startup_domain": "Wealthtech"
    },
    {
        "question_1": "Helping individuals plan for retirement and investments",
        "question_2": "Becoming a certified financial planner or advisor",
        "question_3": "Yes, I find it fascinating",
        "question_4": "Yes, I enjoy helping others make financial decisions",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Retirement planning and savings",
        "question_7": "I prefer working with individuals",
        "question_8": "Both options interest me",
        "question_9": "No, I prefer other aspects of finance",
        "question_10": "Becoming a financial consultant for individuals",
        "startup_domain": "Wealthtech"
    },
    {
        "question_1": "Helping individuals plan for retirement and investments",
        "question_2": "Becoming a certified financial planner or advisor",
        "question_3": "Yes, I find it fascinating",
        "question_4": "Yes, I enjoy helping others make financial decisions",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Retirement planning and savings",
        "question_7": "I prefer working with individuals",
        "question_8": "Both options interest me",
        "question_9": "No, I prefer other aspects of finance",
        "question_10": "Becoming a financial advisor for high-net-worth individuals",
        "startup_domain": "Wealthtech"
    },
    {
        "question_1": "Helping individuals plan for retirement and investments",
        "question_2": "Becoming a certified financial planner or advisor",
        "question_3": "Yes, I find it fascinating",
        "question_4": "Yes, I enjoy helping others make financial decisions",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Retirement planning and savings",
        "question_7": "I prefer working with individuals",
        "question_8": "Both options interest me",
        "question_9": "No, I prefer other aspects of finance",
        "question_10": "Becoming a financial coach for individuals",
        "startup_domain": "Wealthtech"
    },

    {
        "question_1": "Working in financial markets and trading",
        "question_2": "Becoming a trader in financial markets",
        "question_3": "Yes, I find it fascinating",
        "question_4": "No, I prefer working with numbers and data",
        "question_5": "I'm comfortable with risk",
        "question_6": "Derivatives and options",
        "question_7": "I prefer working with institutions and businesses",
        "question_8": "Analyzing financial markets in real-time",
        "question_9": "Yes, I find it intriguing",
        "question_10": "Becoming a professional trader or analyst",
        "startup_domain": "Fintech (Financial Technology)"
    },{
        "question_1": "Assisting companies in raising capital",
        "question_2": "Advising companies on mergers and acquisitions",
        "question_3": "Yes, I find it fascinating",
        "question_4": "Yes, I enjoy helping others make financial decisions",
        "question_5": "It depends on the context",
        "question_6": "Capital budgeting and investment analysis",
        "question_7": "I prefer working with institutions and businesses",
        "question_8": "Both options interest me",
        "question_9": "Yes, I find it intriguing",
        "question_10": "Working in investment banking or corporate finance",
        "startup_domain": "Fintech (Financial Technology)"
    },
    {
        "question_1": "Managing corporate finances",
        "question_2": "Maximizing shareholder value for a corporation",
        "question_3": "Yes, I find it fascinating",
        "question_4": "Yes, I enjoy helping others make financial decisions",
        "question_5": "It depends on the context",
        "question_6": "Stocks and bonds",
        "question_7": "I prefer working with individuals",
        "question_8": "Both options interest me",
        "question_9": "Yes, I find it intriguing",
        "question_10": "Climbing the corporate ladder in a finance department",
        "startup_domain": "Fintech (Financial Technology)"
    },
    {
        "question_1": "Managing corporate finances",
        "question_2": "Maximizing shareholder value for a corporation",
        "question_3": "Yes, I find it fascinating",
        "question_4": "Yes, I enjoy helping others make financial decisions",
        "question_5": "It depends on the context",
        "question_6": "Stocks and bonds",
        "question_7": "I prefer working with individuals",
        "question_8": "Both options interest me",
        "question_9": "Yes, I find it intriguing",
        "question_10": "Becoming a certified financial planner or advisor",
        "startup_domain": "Fintech (Financial Technology)"
    },
    {
        "question_1": "Assisting companies in raising capital",
        "question_2": "Advising companies on mergers and acquisitions",
        "question_3": "Yes, I find it fascinating",
        "question_4": "Yes, I enjoy helping others make financial decisions",
        "question_5": "It depends on the context",
        "question_6": "Capital budgeting and investment analysis",
        "question_7": "I prefer working with institutions and businesses",
        "question_8": "Both options interest me",
        "question_9": "Yes, I find it intriguing",
        "question_10": "Becoming a financial advisor for high-net-worth individuals",
        "startup_domain": "Fintech (Financial Technology)"
    },
    {
        "question_1": "Managing corporate finances",
        "question_2": "Maximizing shareholder value for a corporation",
        "question_3": "Yes, I find it fascinating",
        "question_4": "Yes, I enjoy helping others make financial decisions",
        "question_5": "It depends on the context",
        "question_6": "Stocks and bonds",
        "question_7": "I prefer working with individuals",
        "question_8": "Both options interest me",
        "question_9": "Yes, I find it intriguing",
        "question_10": "Working in investment banking or corporate finance",
        "startup_domain": "Fintech (Financial Technology)"
    },

    {
        "question_1": "Assisting companies in raising capital",
        "question_2": "Advising companies on mergers and acquisitions",
        "question_3": "Yes, I find it fascinating",
        "question_4": "No, I prefer working with numbers and data",
        "question_5": "I'm comfortable with risk",
        "question_6": "Capital budgeting and investment analysis",
        "question_7": "I prefer working with institutions and businesses",
        "question_8": "Making strategic financial decisions",
        "question_9": "Yes, I find it intriguing",
        "question_10": "Working in investment banking or corporate finance",
        "startup_domain": "Corporate Finance and Investment Banking"
    },  {
        "question_1": "Helping individuals with their financial goals",
        "question_2": "Helping individuals plan for retirement and investments",
        "question_3": "Yes, I find it fascinating",
        "question_4": "Yes, I enjoy helping others make financial decisions",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Retirement planning and savings",
        "question_7": "I prefer working with individuals",
        "question_8": "Making strategic financial decisions",
        "question_9": "No, I prefer other aspects of finance",
        "question_10": "Becoming a certified financial planner or advisor",
        "startup_domain": "Wealthtech"
    },
    {
        "question_1": "Helping individuals with their financial goals",
        "question_2": "Helping individuals plan for retirement and investments",
        "question_3": "Yes, I find it fascinating",
        "question_4": "Yes, I enjoy helping others make financial decisions",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Retirement planning and savings",
        "question_7": "I prefer working with individuals",
        "question_8": "Making strategic financial decisions",
        "question_9": "No, I prefer other aspects of finance",
        "question_10": "Becoming a certified financial planner or advisor",
        "startup_domain": "Wealthtech"
    },
    {
        "question_1": "Helping individuals with their financial goals",
        "question_2": "Helping individuals plan for retirement and investments",
        "question_3": "Yes, I find it fascinating",
        "question_4": "Yes, I enjoy helping others make financial decisions",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Retirement planning and savings",
        "question_7": "I prefer working with individuals",
        "question_8": "Making strategic financial decisions",
        "question_9": "No, I prefer other aspects of finance",
        "question_10": "Becoming a certified financial planner or advisor",
        "startup_domain": "Wealthtech"
    },
    {
        "question_1": "Helping individuals with their financial goals",
        "question_2": "Helping individuals plan for retirement and investments",
        "question_3": "Yes, I find it fascinating",
        "question_4": "Yes, I enjoy helping others make financial decisions",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Retirement planning and savings",
        "question_7": "I prefer working with individuals",
        "question_8": "Making strategic financial decisions",
        "question_9": "No, I prefer other aspects of finance",
        "question_10": "Becoming a certified financial planner or advisor",
        "startup_domain": "Wealthtech"
    },
    {
        "question_1": "Helping individuals with their financial goals",
        "question_2": "Helping individuals plan for retirement and investments",
        "question_3": "Yes, I find it fascinating",
        "question_4": "Yes, I enjoy helping others make financial decisions",
        "question_5": "I prefer more stable and predictable situations",
        "question_6": "Retirement planning and savings",
        "question_7": "I prefer working with individuals",
        "question_8": "Making strategic financial decisions",
        "question_9": "No, I prefer other aspects of finance",
        "question_10": "Becoming a certified financial planner or advisor",
        "startup_domain": "Wealthtech"
    }
]

healthcare_questions = [
    "What aspect of healthcare interests you the most?\na) Direct patient care and medical treatment\nb) Healthcare administration and management\nc) Promoting community health and disease prevention\nd) Working with healthcare technology and data",
    "Do you enjoy working closely with patients and providing hands-on care?\na) Yes, I have a passion for patient care\nb) No, I prefer working on the administrative side\nc) I'm open to both",
    "Are you interested in the business and organizational aspects of healthcare?\na) Yes, I enjoy managing healthcare facilities and resources\nb) No, I prefer clinical work with patients\nc) I'm open to both",
    "Do you have a strong interest in public health and community wellness?\na) Yes, I'm passionate about improving public health\nb) No, I prefer working with individual patients\nc) I'm open to both",
    "Are you technologically inclined and interested in healthcare technology systems?\na) Yes, I'm interested in health IT and data analytics\nb) No, I prefer non-technical aspects of healthcare\nc) I have a moderate interest in technology",
    "Which area of healthcare would you find most rewarding?\na) Diagnosing and treating medical conditions\nb) Managing healthcare facilities and budgets\nc) Educating the public about health and wellness\nd) Implementing and maintaining healthcare technology systems",
    "Are you comfortable with making critical decisions in high-pressure healthcare environments?\na) Yes, I thrive in high-pressure clinical situations\nb) No, I prefer more structured and managerial roles\nc) It depends on the situation",
    "Which of the following areas aligns with your long-term career aspirations?\na) Becoming a healthcare provider (e.g., doctor, nurse)\nb) Pursuing a career in healthcare management or administration\nc) Focusing on public health and community health initiatives\nd) Specializing in health information technology",
    "Do you have a strong interest in research and data analysis related to healthcare?\na) Yes, I'm interested in healthcare research and data analysis\nb) No, I prefer practical application in patient care or administration\nc) I have a moderate interest in research",
    "Are you drawn to healthcare's potential for helping individuals or improving the health of entire communities?\na) I want to make a difference in individual lives\nb) I want to contribute to the betterment of communities and populations\nc) I want a role that allows me to do both to some extent"
]

healthcare_question_options = {
    healthcare_questions[0]: {
        "a": "Direct patient care and medical treatment",
        "b": "Healthcare administration and management",
        "c": "Promoting community health and disease prevention",
        "d": "Working with healthcare technology and data"
    },
    healthcare_questions[1]: {
        "a": "Yes, I have a passion for patient care",
        "b": "No, I prefer working on the administrative side",
        "c": "I'm open to both"
    },
    healthcare_questions[2]: {
        "a": "Yes, I enjoy managing healthcare facilities and resources",
        "b": "No, I prefer clinical work with patients",
        "c": "I'm open to both"
    },
    healthcare_questions[3]: {
        "a": "Yes, I'm passionate about improving public health",
        "b": "No, I prefer working with individual patients",
        "c": "I'm open to both"
    },
    healthcare_questions[4]: {
        "a": "Yes, I'm interested in health IT and data analytics",
        "b": "No, I prefer non-technical aspects of healthcare",
        "c": "I have a moderate interest in technology"
    },
    healthcare_questions[5]: {
        "a": "Diagnosing and treating medical conditions",
        "b": "Managing healthcare facilities and budgets",
        "c": "Educating the public about health and wellness",
        "d": "Implementing and maintaining healthcare technology systems"
    },
    healthcare_questions[6]: {
        "a": "Yes, I thrive in high-pressure clinical situations",
        "b": "No, I prefer more structured and managerial roles",
        "c": "It depends on the situation"
    },
    healthcare_questions[7]: {
        "a": "Becoming a healthcare provider (e.g., doctor, nurse)",
        "b": "Pursuing a career in healthcare management or administration",
        "c": "Focusing on public health and community health initiatives",
        "d": "Specializing in health information technology"
    },
    healthcare_questions[8]: {
        "a": "Yes, I'm interested in healthcare research and data analysis",
        "b": "No, I prefer practical application in patient care or administration",
        "c": "I have a moderate interest in research"
    },
    healthcare_questions[9]: {
        "a": "I want to make a difference in individual lives",
        "b": "I want to contribute to the betterment of communities and populations",
        "c": "I want a role that allows me to do both to some extent"
    }
}

healthcare_data_set = [
    {
        "question_1": "Healthcare administration and management",
        "question_2": "Yes, I have a passion for patient care",
        "question_3": "Yes, I enjoy managing healthcare facilities and resources",
        "question_4": "Yes, I'm passionate about improving public health",
        "question_5": "Yes, I'm interested in health IT and data analytics",
        "question_6": "Diagnosing and treating medical conditions",
        "question_7": "Yes, I thrive in high-pressure clinical situations",
        "question_8": "Becoming a healthcare provider (e.g., doctor, nurse)",
        "question_9": "Yes, I'm interested in healthcare research and data analysis",
        "question_10": "I want to make a difference in individual lives",
        "startup_domain": "Telemedicine and Telehealth"
    },
    {
        "question_1": "Healthcare administration and management",
        "question_2": "Yes, I have a passion for patient care",
        "question_3": "Yes, I enjoy managing healthcare facilities and resources",
        "question_4": "Yes, I'm passionate about improving public health",
        "question_5": "Yes, I'm interested in health IT and data analytics",
        "question_6": "Diagnosing and treating medical conditions",
        "question_7": "Yes, I thrive in high-pressure clinical situations",
        "question_8": "Becoming a healthcare provider (e.g., doctor, nurse)",
        "question_9": "Yes, I'm interested in healthcare research and data analysis",
        "question_10": "I want to make a difference in individual lives",
        "startup_domain": "Telemedicine and Telehealth"
    },
    {
        "question_1": "Healthcare administration and management",
        "question_2": "Yes, I have a passion for patient care",
        "question_3": "Yes, I enjoy managing healthcare facilities and resources",
        "question_4": "Yes, I'm passionate about improving public health",
        "question_5": "Yes, I'm interested in health IT and data analytics",
        "question_6": "Diagnosing and treating medical conditions",
        "question_7": "Yes, I thrive in high-pressure clinical situations",
        "question_8": "Becoming a healthcare provider (e.g., doctor, nurse)",
        "question_9": "Yes, I'm interested in healthcare research and data analysis",
        "question_10": "I want to make a difference in individual lives",
        "startup_domain": "Telemedicine and Telehealth"
    },
    {
        "question_1": "Healthcare administration and management",
        "question_2": "Yes, I have a passion for patient care",
        "question_3": "Yes, I enjoy managing healthcare facilities and resources",
        "question_4": "Yes, I'm passionate about improving public health",
        "question_5": "Yes, I'm interested in health IT and data analytics",
        "question_6": "Diagnosing and treating medical conditions",
        "question_7": "Yes, I thrive in high-pressure clinical situations",
        "question_8": "Becoming a healthcare provider (e.g., doctor, nurse)",
        "question_9": "Yes, I'm interested in healthcare research and data analysis",
        "question_10": "I want to make a difference in individual lives",
        "startup_domain": "Telemedicine and Telehealth"
    },

    {
        "question_1": "Healthcare administration and management",
        "question_2": "Yes, I have a passion for patient care",
        "question_3": "Yes, I enjoy managing healthcare facilities and resources",
        "question_4": "Yes, I'm passionate about improving public health",
        "question_5": "Yes, I'm interested in health IT and data analytics",
        "question_6": "Diagnosing and treating medical conditions",
        "question_7": "Yes, I thrive in high-pressure clinical situations",
        "question_8": "Becoming a healthcare provider (e.g., doctor, nurse)",
        "question_9": "Yes, I'm interested in healthcare research and data analysis",
        "question_10": "I want to make a difference in individual lives",
        "startup_domain": "Telemedicine and Telehealth"
    },

     {
        "question_1": "Working with healthcare technology and data",
        "question_2": "I'm open to both",
        "question_3": "I'm open to both",
        "question_4": "I'm open to both",
        "question_5": "I'm interested in health IT and data analytics",
        "question_6": "Implementing and maintaining healthcare technology systems",
        "question_7": "It depends on the situation",
        "question_8": "Specializing in health information technology",
        "question_9": "I'm interested in healthcare research and data analysis",
        "question_10": "I want a role that allows me to do both to some extent",
        "startup_domain": "Healthcare Data and Analytics"
    },
    {
        "question_1": "Working with healthcare technology and data",
        "question_2": "I'm open to both",
        "question_3": "I'm open to both",
        "question_4": "I'm open to both",
        "question_5": "I'm interested in health IT and data analytics",
        "question_6": "Implementing and maintaining healthcare technology systems",
        "question_7": "It depends on the situation",
        "question_8": "Specializing in health information technology",
        "question_9": "I'm interested in healthcare research and data analysis",
        "question_10": "I want a role that allows me to do both to some extent",
        "startup_domain": "Healthcare Data and Analytics"
    },
    {
        "question_1": "Working with healthcare technology and data",
        "question_2": "I'm open to both",
        "question_3": "I'm open to both",
        "question_4": "I'm open to both",
        "question_5": "I'm interested in health IT and data analytics",
        "question_6": "Implementing and maintaining healthcare technology systems",
        "question_7": "It depends on the situation",
        "question_8": "Specializing in health information technology",
        "question_9": "I'm interested in healthcare research and data analysis",
        "question_10": "I want a role that allows me to do both to some extent",
        "startup_domain": "Healthcare Data and Analytics"
    },
    {
        "question_1": "Working with healthcare technology and data",
        "question_2": "I'm open to both",
        "question_3": "I'm open to both",
        "question_4": "I'm open to both",
        "question_5": "I'm interested in health IT and data analytics",
        "question_6": "Implementing and maintaining healthcare technology systems",
        "question_7": "It depends on the situation",
        "question_8": "Specializing in health information technology",
        "question_9": "I'm interested in healthcare research and data analysis",
        "question_10": "I want a role that allows me to do both to some extent",
        "startup_domain": "Healthcare Data and Analytics"
    },
    {
        "question_1": "Working with healthcare technology and data",
        "question_2": "I'm open to both",
        "question_3": "I'm open to both",
        "question_4": "I'm open to both",
        "question_5": "I'm interested in health IT and data analytics",
        "question_6": "Implementing and maintaining healthcare technology systems",
        "question_7": "It depends on the situation",
        "question_8": "Specializing in health information technology",
        "question_9": "I'm interested in healthcare research and data analysis",
        "question_10": "I want a role that allows me to do both to some extent",
        "startup_domain": "Healthcare Data and Analytics"
    },

    {
        "question_1": "Working with healthcare technology and data",
        "question_2": "I'm open to both",
        "question_3": "I'm open to both",
        "question_4": "I'm open to both",
        "question_5": "I'm interested in health IT and data analytics",
        "question_6": "Implementing and maintaining healthcare technology systems",
        "question_7": "It depends on the situation",
        "question_8": "Specializing in health information technology",
        "question_9": "I'm interested in healthcare research and data analysis",
        "question_10": "I want a role that allows me to do both to some extent",
        "startup_domain": "Digital health"
    },
    {
        "question_1": "Working with healthcare technology and data",
        "question_2": "I'm open to both",
        "question_3": "I'm open to both",
        "question_4": "I'm open to both",
        "question_5": "I'm interested in health IT and data analytics",
        "question_6": "Implementing and maintaining healthcare technology systems",
        "question_7": "It depends on the situation",
        "question_8": "Specializing in health information technology",
        "question_9": "I'm interested in healthcare research and data analysis",
        "question_10": "I want a role that allows me to do both to some extent",
        "startup_domain": "Digital health"
    },
    {
        "question_1": "Working with healthcare technology and data",
        "question_2": "I'm open to both",
        "question_3": "I'm open to both",
        "question_4": "I'm open to both",
        "question_5": "I'm interested in health IT and data analytics",
        "question_6": "Implementing and maintaining healthcare technology systems",
        "question_7": "It depends on the situation",
        "question_8": "Specializing in health information technology",
        "question_9": "I'm interested in healthcare research and data analysis",
        "question_10": "I want a role that allows me to do both to some extent",
        "startup_domain": "Digital health"
    },
    {
        "question_1": "Working with healthcare technology and data",
        "question_2": "I'm open to both",
        "question_3": "I'm open to both",
        "question_4": "I'm open to both",
        "question_5": "I'm interested in health IT and data analytics",
        "question_6": "Implementing and maintaining healthcare technology systems",
        "question_7": "It depends on the situation",
        "question_8": "Specializing in health information technology",
        "question_9": "I'm interested in healthcare research and data analysis",
        "question_10": "I want a role that allows me to do both to some extent",
        "startup_domain": "Digital health"
    },
    {
        "question_1": "Working with healthcare technology and data",
        "question_2": "I'm open to both",
        "question_3": "I'm open to both",
        "question_4": "I'm open to both",
        "question_5": "I'm interested in health IT and data analytics",
        "question_6": "Implementing and maintaining healthcare technology systems",
        "question_7": "It depends on the situation",
        "question_8": "Specializing in health information technology",
        "question_9": "I'm interested in healthcare research and data analysis",
        "question_10": "I want a role that allows me to do both to some extent",
        "startup_domain": "Digital health"
    },

     {
        "question_1": "Diagnosing and treating medical conditions",
        "question_2": "No, I prefer working on the administrative side",
        "question_3": "No, I prefer clinical work with patients",
        "question_4": "No, I prefer working with individual patients",
        "question_5": "No, I prefer non-technical aspects of healthcare",
        "question_6": "Managing healthcare facilities and budgets",
        "question_7": "No, I prefer more structured and managerial roles",
        "question_8": "Pursuing a career in healthcare management or administration",
        "question_9": "No, I prefer practical application in patient care or administration",
        "question_10": "I want to contribute to the betterment of communities and populations",
        "startup_domain": "Biotechnology and medical devices"
    },
    {
        "question_1": "Diagnosing and treating medical conditions",
        "question_2": "No, I prefer working on the administrative side",
        "question_3": "No, I prefer clinical work with patients",
        "question_4": "No, I prefer working with individual patients",
        "question_5": "No, I prefer non-technical aspects of healthcare",
        "question_6": "Managing healthcare facilities and budgets",
        "question_7": "No, I prefer more structured and managerial roles",
        "question_8": "Pursuing a career in healthcare management or administration",
        "question_9": "No, I prefer practical application in patient care or administration",
        "question_10": "I want to contribute to the betterment of communities and populations",
        "startup_domain": "Biotechnology and medical devices"
    },
    {
        "question_1": "Diagnosing and treating medical conditions",
        "question_2": "No, I prefer working on the administrative side",
        "question_3": "No, I prefer clinical work with patients",
        "question_4": "No, I prefer working with individual patients",
        "question_5": "No, I prefer non-technical aspects of healthcare",
        "question_6": "Managing healthcare facilities and budgets",
        "question_7": "No, I prefer more structured and managerial roles",
        "question_8": "Pursuing a career in healthcare management or administration",
        "question_9": "No, I prefer practical application in patient care or administration",
        "question_10": "I want to contribute to the betterment of communities and populations",
        "startup_domain": "Biotechnology and medical devices"
    },
    {
        "question_1": "Diagnosing and treating medical conditions",
        "question_2": "No, I prefer working on the administrative side",
        "question_3": "No, I prefer clinical work with patients",
        "question_4": "No, I prefer working with individual patients",
        "question_5": "No, I prefer non-technical aspects of healthcare",
        "question_6": "Managing healthcare facilities and budgets",
        "question_7": "No, I prefer more structured and managerial roles",
        "question_8": "Pursuing a career in healthcare management or administration",
        "question_9": "No, I prefer practical application in patient care or administration",
        "question_10": "I want to contribute to the betterment of communities and populations",
        "startup_domain": "Biotechnology and medical devices"
    },
    {
        "question_1": "Diagnosing and treating medical conditions",
        "question_2": "No, I prefer working on the administrative side",
        "question_3": "No, I prefer clinical work with patients",
        "question_4": "No, I prefer working with individual patients",
        "question_5": "No, I prefer non-technical aspects of healthcare",
        "question_6": "Managing healthcare facilities and budgets",
        "question_7": "No, I prefer more structured and managerial roles",
        "question_8": "Pursuing a career in healthcare management or administration",
        "question_9": "No, I prefer practical application in patient care or administration",
        "question_10": "I want to contribute to the betterment of communities and populations",
        "startup_domain": "Biotechnology and medical devices"
    }
]


technology_questions = [
    "What type of technology projects have you been most passionate about?\na. Developing software applications and websites\nb. Building hardware prototypes and devices\nc. Leveraging data and AI for insights and automation\nd. Exploring IoT and connected devices",
    "Which area of tech innovation excites you the most?\na. Creating user-friendly apps and interfaces\nb. Working on physical products and electronics\nc. Harnessing the power of data and machine learning\nd. Building interconnected smart systems",
    "What is your preferred focus when it comes to technology startups?\na. Software development and digital solutions\nb. Hardware manufacturing and physical products\nc. Data analytics and AI-driven applications\nd. IoT and smart device ecosystems",
    "Which aspect of tech startups aligns with your expertise and interests?\na. Software design and coding\nb. Hardware prototyping and engineering\nc. Data analysis and machine learning algorithms\nd. Sensor technology and IoT architecture",
    "In which domain do you have prior experience or technical skills?\na. Web and mobile app development\nb. Electronics and hardware design\nc. Data science and analytics\nd. Internet of Things (IoT) and connected devices",
    "What type of technology products or services do you envision building?\na. User-friendly applications and software tools\nb. Innovative hardware devices and gadgets\nc. AI-powered solutions for complex problems\nd. Smart and interconnected IoT systems",
    "Are you more inclined toward creating virtual or physical tech solutions?\na. Virtual solutions (software and apps)\nb. Physical solutions (hardware and devices)\nc. A combination of both\nd. It depends on the specific project",
    "Which industry or market do you see your tech startup serving?\na. Digital and online services\nb. Consumer electronics and hardware\nc. Finance, healthcare, or other data-driven sectors\nd. IoT applications in various industries",
    "How do you feel about the long development cycles often associated with hardware startups?\na. Comfortable; I enjoy the challenges of hardware development.\nb. Not my preference; I prefer faster-paced software development.\nc. I'm adaptable and can handle varying project timelines.\nd. I have no strong preference.",
    "Which area of technology do you believe will have the most significant impact on society in the next decade?\na. Software and digital experiences\nb. Hardware and physical innovations\nc. Data-driven insights and AI advancements\nd. The interconnected world of IoT"
]
technology_question_options = {
    technology_questions[0]: {
        "a": "Developing software applications and websites",
        "b": "Building hardware prototypes and devices",
        "c": "Leveraging data and AI for insights and automation",
        "d": "Exploring IoT and connected devices"
    },
    technology_questions[1]: {
        "a": "Creating user-friendly apps and interfaces",
        "b": "Working on physical products and electronics",
        "c": "Harnessing the power of data and machine learning",
        "d": "Building interconnected smart systems"
    },
    technology_questions[2]: {
        "a": "Software development and digital solutions",
        "b": "Hardware manufacturing and physical products",
        "c": "Data analytics and AI-driven applications",
        "d": "IoT and smart device ecosystems"
    },
    technology_questions[3]: {
        "a": "Software design and coding",
        "b": "Hardware prototyping and engineering",
        "c": "Data analysis and machine learning algorithms",
        "d": "Sensor technology and IoT architecture"
    },
    technology_questions[4]: {
        "a": "Web and mobile app development",
        "b": "Electronics and hardware design",
        "c": "Data science and analytics",
        "d": "Internet of Things (IoT) and connected devices"
    },
    technology_questions[5]: {
        "a": "User-friendly applications and software tools",
        "b": "Innovative hardware devices and gadgets",
        "c": "AI-powered solutions for complex problems",
        "d": "Smart and interconnected IoT systems"
    },
    technology_questions[6]: {
        "a": "Virtual solutions (software and apps)",
        "b": "Physical solutions (hardware and devices)",
        "c": "A combination of both",
        "d": "It depends on the specific project"
    },
    technology_questions[7]: {
        "a": "Digital and online services",
        "b": "Consumer electronics and hardware",
        "c": "Finance, healthcare, or other data-driven sectors",
        "d": "IoT applications in various industries"
    },
    technology_questions[8]: {
        "a": "Comfortable; I enjoy the challenges of hardware development.",
        "b": "Not my preference; I prefer faster-paced software development.",
        "c": "I'm adaptable and can handle varying project timelines.",
        "d": "I have no strong preference."
    },
    technology_questions[9]: {
        "a": "Software and digital experiences",
        "b": "Hardware and physical innovations",
        "c": "Data-driven insights and AI advancements",
        "d": "The interconnected world of IoT"
    }
}

technology_data_set = [
    {
        "passionate_about": "Developing software applications and websites",
        "excited_about_innovation": "Creating user-friendly apps and interfaces",
        "preferred_startup_focus": "Software development and digital solutions",
        "aligned_expertise_interest": "Software design and coding",
        "prior_experience_domain": "Web and mobile app development",
        "envisioned_tech_products": "User-friendly applications and software tools",
        "tech_solution_preference": "Virtual solutions (software and apps)",
        "targeted_industry_or_market": "Digital and online services",
        "comfort_with_hardware_dev_cycles": "Not my preference; I prefer faster-paced software development.",
        "impactful_tech_area": "Software and digital experiences",
        "startup_field": "Software Development and Applications"
    },
    {
        "passionate_about": "Developing software applications and websites",
        "excited_about_innovation": "Creating user-friendly apps and interfaces",
        "preferred_startup_focus": "Software development and digital solutions",
        "aligned_expertise_interest": "Software design and coding",
        "prior_experience_domain": "Web and mobile app development",
        "envisioned_tech_products": "User-friendly applications and software tools",
        "tech_solution_preference": "Virtual solutions (software and apps)",
        "targeted_industry_or_market": "Digital and online services",
        "comfort_with_hardware_dev_cycles": "Not my preference; I prefer faster-paced software development.",
        "impactful_tech_area": "Software and digital experiences",
        "startup_field": "Software Development and Applications"
    },
    {
        "passionate_about": "Developing software applications and websites",
        "excited_about_innovation": "Creating user-friendly apps and interfaces",
        "preferred_startup_focus": "Software development and digital solutions",
        "aligned_expertise_interest": "Software design and coding",
        "prior_experience_domain": "Web and mobile app development",
        "envisioned_tech_products": "Innovative mobile applications",
        "tech_solution_preference": "Virtual solutions (software and apps)",
        "targeted_industry_or_market": "Entertainment and gaming",
        "comfort_with_hardware_dev_cycles": "Not my preference; I prefer faster-paced software development.",
        "impactful_tech_area": "Software and digital experiences",
        "startup_field": "Software Development and Applications"
    },
    {
        "passionate_about": "Developing software applications and websites",
        "excited_about_innovation": "Creating user-friendly apps and interfaces",
        "preferred_startup_focus": "Software development and digital solutions",
        "aligned_expertise_interest": "Software design and coding",
        "prior_experience_domain": "Web and mobile app development",
        "envisioned_tech_products": "Educational software for interactive learning",
        "tech_solution_preference": "Virtual solutions (software and apps)",
        "targeted_industry_or_market": "Education and e-learning",
        "comfort_with_hardware_dev_cycles": "Not my preference; I prefer faster-paced software development.",
        "impactful_tech_area": "Software and digital experiences",
        "startup_field": "Software Development and Applications"
    },
    {
        "passionate_about": "Developing software applications and websites",
        "excited_about_innovation": "Creating user-friendly apps and interfaces",
        "preferred_startup_focus": "Software development and digital solutions",
        "aligned_expertise_interest": "Software design and coding",
        "prior_experience_domain": "Web and mobile app development",
        "envisioned_tech_products": "Social networking platform with innovative features",
        "tech_solution_preference": "Virtual solutions (software and apps)",
        "targeted_industry_or_market": "Social media and networking",
        "comfort_with_hardware_dev_cycles": "Not my preference; I prefer faster-paced software development.",
        "impactful_tech_area": "Software and digital experiences",
        "startup_field": "Software Development and Applications"
    },
    {
        "passionate_about": "Developing software applications and websites",
        "excited_about_innovation": "Creating user-friendly apps and interfaces",
        "preferred_startup_focus": "Software development and digital solutions",
        "aligned_expertise_interest": "Software design and coding",
        "prior_experience_domain": "Web and mobile app development",
        "envisioned_tech_products": "E-commerce platform with seamless user experience",
        "tech_solution_preference": "Virtual solutions (software and apps)",
        "targeted_industry_or_market": "E-commerce and online retail",
        "comfort_with_hardware_dev_cycles": "Not my preference; I prefer faster-paced software development.",
        "impactful_tech_area": "Software and digital experiences",
        "startup_field": "Software Development and Applications"
    },


    {
        "passionate_about": "Building hardware prototypes and devices",
        "excited_about_innovation": "Working on physical products and electronics",
        "preferred_startup_focus": "Hardware manufacturing and physical products",
        "aligned_expertise_interest": "Hardware prototyping and engineering",
        "prior_experience_domain": "Electronics and hardware design",
        "envisioned_tech_products": "Innovative hardware devices and gadgets",
        "tech_solution_preference": "Physical solutions (hardware and devices)",
        "targeted_industry_or_market": "Consumer electronics and hardware",
        "comfort_with_hardware_dev_cycles": "Comfortable; I enjoy the challenges of hardware development.",
        "impactful_tech_area": "Hardware and physical innovations",
        "startup_field": "Hardware and Electronics"
    },
    {
        "passionate_about": "Building hardware prototypes and devices",
        "excited_about_innovation": "Working on physical products and electronics",
        "preferred_startup_focus": "Hardware manufacturing and physical products",
        "aligned_expertise_interest": "Electronics and hardware design",
        "prior_experience_domain": "Consumer electronics and hardware",
        "envisioned_tech_products": "Innovative wearable devices for health monitoring",
        "tech_solution_preference": "Physical solutions (hardware and devices)",
        "targeted_industry_or_market": "Health and wellness technology",
        "comfort_with_hardware_dev_cycles": "Comfortable; I enjoy the challenges of hardware development.",
        "impactful_tech_area": "Hardware and physical innovations",
        "startup_field": "Hardware and Electronics"
    },
    {
        "passionate_about": "Building hardware prototypes and devices",
        "excited_about_innovation": "Working on physical products and electronics",
        "preferred_startup_focus": "Hardware manufacturing and physical products",
        "aligned_expertise_interest": "Electronics and hardware design",
        "prior_experience_domain": "Consumer electronics and hardware",
        "envisioned_tech_products": "Smart home automation devices for energy efficiency",
        "tech_solution_preference": "Physical solutions (hardware and devices)",
        "targeted_industry_or_market": "Smart home technology",
        "comfort_with_hardware_dev_cycles": "Comfortable; I enjoy the challenges of hardware development.",
        "impactful_tech_area": "Hardware and physical innovations",
        "startup_field": "Hardware and Electronics"
    },
    {
        "passionate_about": "Building hardware prototypes and devices",
        "excited_about_innovation": "Working on physical products and electronics",
        "preferred_startup_focus": "Hardware manufacturing and physical products",
        "aligned_expertise_interest": "Electronics and hardware design",
        "prior_experience_domain": "Consumer electronics and hardware",
        "envisioned_tech_products": "Next-generation virtual reality headsets",
        "tech_solution_preference": "Physical solutions (hardware and devices)",
        "targeted_industry_or_market": "Virtual reality and gaming",
        "comfort_with_hardware_dev_cycles": "Comfortable; I enjoy the challenges of hardware development.",
        "impactful_tech_area": "Hardware and physical innovations",
        "startup_field": "Hardware and Electronics"
    },
    {
        "passionate_about": "Building hardware prototypes and devices",
        "excited_about_innovation": "Working on physical products and electronics",
        "preferred_startup_focus": "Hardware manufacturing and physical products",
        "aligned_expertise_interest": "Electronics and hardware design",
        "prior_experience_domain": "Consumer electronics and hardware",
        "envisioned_tech_products": "Drones with advanced aerial imaging capabilities",
        "tech_solution_preference": "Physical solutions (hardware and devices)",
        "targeted_industry_or_market": "Aerospace and aerial technology",
        "comfort_with_hardware_dev_cycles": "Comfortable; I enjoy the challenges of hardware development.",
        "impactful_tech_area": "Hardware and physical innovations",
        "startup_field": "Hardware and Electronics"
    },
    {
        "passionate_about": "Building hardware prototypes and devices",
        "excited_about_innovation": "Working on physical products and electronics",
        "preferred_startup_focus": "Hardware manufacturing and physical products",
        "aligned_expertise_interest": "Electronics and hardware design",
        "prior_experience_domain": "Consumer electronics and hardware",
        "envisioned_tech_products": "Advanced robotics for industrial automation",
        "tech_solution_preference": "Physical solutions (hardware and devices)",
        "targeted_industry_or_market": "Industrial automation and robotics",
        "comfort_with_hardware_dev_cycles": "Comfortable; I enjoy the challenges of hardware development.",
        "impactful_tech_area": "Hardware and physical innovations",
        "startup_field": "Hardware and Electronics"
    },

    {
        "passionate_about": "Leveraging data and AI for insights and automation",
        "excited_about_innovation": "Harnessing the power of data and machine learning",
        "preferred_startup_focus": "Data analytics and AI-driven applications",
        "aligned_expertise_interest": "Data analysis and machine learning algorithms",
        "prior_experience_domain": "Data science and analytics",
        "envisioned_tech_products": "AI-powered solutions for complex problems",
        "tech_solution_preference": "A combination of both (virtual and physical solutions)",
        "targeted_industry_or_market": "Finance, healthcare, or other data-driven sectors",
        "comfort_with_hardware_dev_cycles": "I'm adaptable and can handle varying project timelines.",
        "impactful_tech_area": "Data-driven insights and AI advancements",
        "startup_field": "Data Science and Artificial Intelligence"
    },{
        "passionate_about": "Leveraging data and AI for insights and automation",
        "excited_about_innovation": "Harnessing the power of data and machine learning",
        "preferred_startup_focus": "Data analytics and AI-driven applications",
        "aligned_expertise_interest": "Data analysis and machine learning algorithms",
        "prior_experience_domain": "Data science and analytics",
        "envisioned_tech_products": "Predictive analytics software for business intelligence",
        "tech_solution_preference": "Data-driven solutions (AI and machine learning)",
        "targeted_industry_or_market": "Enterprise and corporate sector",
        "comfort_with_hardware_dev_cycles": "Not my preference; I prefer faster-paced software development.",
        "impactful_tech_area": "Data-driven insights and AI advancements",
        "startup_field": "Data Science and Artificial Intelligence"
    },
    {
        "passionate_about": "Leveraging data and AI for insights and automation",
        "excited_about_innovation": "Harnessing the power of data and machine learning",
        "preferred_startup_focus": "Data analytics and AI-driven applications",
        "aligned_expertise_interest": "Data analysis and machine learning algorithms",
        "prior_experience_domain": "Data science and analytics",
        "envisioned_tech_products": "Healthcare AI for personalized patient care",
        "tech_solution_preference": "Data-driven solutions (AI and machine learning)",
        "targeted_industry_or_market": "Healthcare and medical sector",
        "comfort_with_hardware_dev_cycles": "Not my preference; I prefer faster-paced software development.",
        "impactful_tech_area": "Data-driven insights and AI advancements",
        "startup_field": "Data Science and Artificial Intelligence"
    },
    {
        "passionate_about": "Leveraging data and AI for insights and automation",
        "excited_about_innovation": "Harnessing the power of data and machine learning",
        "preferred_startup_focus": "Data analytics and AI-driven applications",
        "aligned_expertise_interest": "Data analysis and machine learning algorithms",
        "prior_experience_domain": "Data science and analytics",
        "envisioned_tech_products": "AI-powered chatbots for customer service",
        "tech_solution_preference": "Data-driven solutions (AI and machine learning)",
        "targeted_industry_or_market": "Customer service and support",
        "comfort_with_hardware_dev_cycles": "Not my preference; I prefer faster-paced software development.",
        "impactful_tech_area": "Data-driven insights and AI advancements",
        "startup_field": "Data Science and Artificial Intelligence"
    },
    {
        "passionate_about": "Leveraging data and AI for insights and automation",
        "excited_about_innovation": "Harnessing the power of data and machine learning",
        "preferred_startup_focus": "Data analytics and AI-driven applications",
        "aligned_expertise_interest": "Data analysis and machine learning algorithms",
        "prior_experience_domain": "Data science and analytics",
        "envisioned_tech_products": "AI-driven marketing automation platform",
        "tech_solution_preference": "Data-driven solutions (AI and machine learning)",
        "targeted_industry_or_market": "Marketing and advertising",
        "comfort_with_hardware_dev_cycles": "Not my preference; I prefer faster-paced software development.",
        "impactful_tech_area": "Data-driven insights and AI advancements",
        "startup_field": "Data Science and Artificial Intelligence"
    },
    {
        "passionate_about": "Leveraging data and AI for insights and automation",
        "excited_about_innovation": "Harnessing the power of data and machine learning",
        "preferred_startup_focus": "Data analytics and AI-driven applications",
        "aligned_expertise_interest": "Data analysis and machine learning algorithms",
        "prior_experience_domain": "Data science and analytics",
        "envisioned_tech_products": "AI-driven recommendation engine for e-commerce",
        "tech_solution_preference": "Data-driven solutions (AI and machine learning)",
        "targeted_industry_or_market": "E-commerce and online retail",
        "comfort_with_hardware_dev_cycles": "Not my preference; I prefer faster-paced software development.",
        "impactful_tech_area": "Data-driven insights and AI advancements",
        "startup_field": "Data Science and Artificial Intelligence"
    },

    {
        "passionate_about": "Exploring IoT and connected devices",
        "excited_about_innovation": "Building interconnected smart systems",
        "preferred_startup_focus": "Internet of Things (IoT) and smart device ecosystems",
        "aligned_expertise_interest": "Sensor technology and IoT architecture",
        "prior_experience_domain": "Internet of Things (IoT) and connected devices",
        "envisioned_tech_products": "Smart and interconnected IoT systems",
        "tech_solution_preference": "A combination of both (virtual and physical solutions)",
        "targeted_industry_or_market": "IoT applications in various industries",
        "comfort_with_hardware_dev_cycles": "I have no strong preference.",
        "impactful_tech_area": "The interconnected world of IoT",
        "startup_field": "Internet of Things (IoT) and Connectivity"
    },  {
        "passionate_about": "Exploring IoT and connected devices",
        "excited_about_innovation": "Building interconnected smart systems",
        "preferred_startup_focus": "IoT and smart device ecosystems",
        "aligned_expertise_interest": "Sensor technology and IoT architecture",
        "prior_experience_domain": "Internet of Things (IoT) and connected devices",
        "envisioned_tech_products": "Smart home automation system",
        "tech_solution_preference": "Physical solutions (hardware and devices)",
        "targeted_industry_or_market": "Home automation and consumer IoT",
        "comfort_with_hardware_dev_cycles": "Comfortable; I enjoy the challenges of hardware development.",
        "impactful_tech_area": "The interconnected world of IoT",
        "startup_field": "Internet of Things (IoT) and Connectivity"
    },
    {
        "passionate_about": "Exploring IoT and connected devices",
        "excited_about_innovation": "Building interconnected smart systems",
        "preferred_startup_focus": "IoT and smart device ecosystems",
        "aligned_expertise_interest": "Sensor technology and IoT architecture",
        "prior_experience_domain": "Internet of Things (IoT) and connected devices",
        "envisioned_tech_products": "Industrial IoT solutions for manufacturing",
        "tech_solution_preference": "Physical solutions (hardware and devices)",
        "targeted_industry_or_market": "Manufacturing and industrial automation",
        "comfort_with_hardware_dev_cycles": "Comfortable; I enjoy the challenges of hardware development.",
        "impactful_tech_area": "The interconnected world of IoT",
        "startup_field": "Internet of Things (IoT) and Connectivity"
    },
    {
        "passionate_about": "Exploring IoT and connected devices",
        "excited_about_innovation": "Building interconnected smart systems",
        "preferred_startup_focus": "IoT and smart device ecosystems",
        "aligned_expertise_interest": "Sensor technology and IoT architecture",
        "prior_experience_domain": "Internet of Things (IoT) and connected devices",
        "envisioned_tech_products": "Smart city infrastructure for urban planning",
        "tech_solution_preference": "Physical solutions (hardware and devices)",
        "targeted_industry_or_market": "Urban planning and smart cities",
        "comfort_with_hardware_dev_cycles": "Comfortable; I enjoy the challenges of hardware development.",
        "impactful_tech_area": "The interconnected world of IoT",
        "startup_field": "Internet of Things (IoT) and Connectivity"
    },
    {
        "passionate_about": "Exploring IoT and connected devices",
        "excited_about_innovation": "Building interconnected smart systems",
        "preferred_startup_focus": "IoT and smart device ecosystems",
        "aligned_expertise_interest": "Sensor technology and IoT architecture",
        "prior_experience_domain": "Internet of Things (IoT) and connected devices",
        "envisioned_tech_products": "IoT-based environmental monitoring devices",
        "tech_solution_preference": "Physical solutions (hardware and devices)",
        "targeted_industry_or_market": "Environmental monitoring and conservation",
        "comfort_with_hardware_dev_cycles": "Comfortable; I enjoy the challenges of hardware development.",
        "impactful_tech_area": "The interconnected world of IoT",
        "startup_field": "Internet of Things (IoT) and Connectivity"
    },
    {
        "passionate_about": "Exploring IoT and connected devices",
        "excited_about_innovation": "Building interconnected smart systems",
        "preferred_startup_focus": "IoT and smart device ecosystems",
        "aligned_expertise_interest": "Sensor technology and IoT architecture",
        "prior_experience_domain": "Internet of Things (IoT) and connected devices",
        "envisioned_tech_products": "IoT-based agricultural monitoring system",
        "tech_solution_preference": "Physical solutions (hardware and devices)",
        "targeted_industry_or_market": "Agriculture and precision farming",
        "comfort_with_hardware_dev_cycles": "Comfortable; I enjoy the challenges of hardware development.",
        "impactful_tech_area": "The interconnected world of IoT",
        "startup_field": "Internet of Things (IoT) and Connectivity"
    }
]
