import operator

gQuestions = [
    {
        'id': 1,
        'title': 'How to edit videos for YouTube',
        'text': 'Hi! I shot my first video for YouTube, but I don\'t know how to edit it. Can you please tell me what programs to use and how to crop, glue, and add effects correctly?',
        'likes': 15,
        'tags': [
            'video editing', 'YouTube'
        ],
        'date': '10/23/2024 4:55 PM',
        'user': {
            'name': 'Vlogger',
            'img': '/img/cat-avatar.jpeg'
        },
        'answers': [
            {
                'text': 'For beginners, I recommend using the free program DaVinci Resolve. It has all the necessary tools for video editing including cropping, gluing, and adding effects.',
                'likes': 10,
                'is_right_answer': True,
                'date': '10/23/2024 6:01 PM',
                'user': {
                    'name': 'Editor',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Adobe Premiere Pro is also a great choice, though it’s not free. It’s powerful and widely used in the industry.',
                'likes': 5,
                'is_right_answer': False,
                'date': '10/23/2024 6:15 PM',
                'user': {
                    'name': 'ProUser',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Try Shotcut or OpenShot for a free and user-friendly editing experience, perfect for basic editing needs.',
                'likes': 3,
                'is_right_answer': False,
                'date': '10/23/2024 6:20 PM',
                'user': {
                    'name': 'NewEditor',
                    'img': '/img/cat-avatar.jpeg'
                }
            }
        ]
    },
    {
        'id': 2,
        'title': 'How to promote your YouTube channel',
        'text': 'I started my YouTube channel, but I\'m getting very few subscribers. What am I doing wrong and how to promote my channel effectively?',
        'likes': 7,
        'tags': [
            'promotion', 'YouTube'
        ],
        'date': '10/24/2024 11:03 AM',
        'user': {
            'name': 'Newbie',
            'img': '/img/cat-avatar.jpeg'
        },
        'answers': [
            {
                'text': 'Regularity of posting new videos is important. Post videos on a specific schedule so that subscribers know when to expect new content.',
                'likes': 9,
                'is_right_answer': True,
                'date': '10/24/2024 12:10 PM',
                'user': {
                    'name': 'Expert',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Collaborate with other YouTubers in your niche to increase visibility.',
                'likes': 4,
                'is_right_answer': False,
                'date': '10/24/2024 12:20 PM',
                'user': {
                    'name': 'CollabFan',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Engage with your audience in the comments and on social media to create a loyal community.',
                'likes': 5,
                'is_right_answer': False,
                'date': '10/24/2024 12:30 PM',
                'user': {
                    'name': 'CommunityBuilder',
                    'img': '/img/cat-avatar.jpeg'
                }
            }
        ]
    },
    {
        'id': 3,
        'title': 'How to make money on your YouTube videos',
        'text': 'I want to start making money on my YouTube channel. How do I do it and what conditions do I need to meet?',
        'likes': 12,
        'tags': [
            'earning', 'YouTube'
        ],
        'date': '10/25/2024 09:21 AM',
        'user': {
            'name': 'Money',
            'img': '/img/cat-avatar.jpeg'
        },
        'answers': [
            {
                'text': 'To enable monetization on your channel, you need to gain 1000 subscribers and 4000 watch hours in the last year.',
                'likes': 10,
                'is_right_answer': True,
                'date': '10/25/2024 10:05 AM',
                'user': {
                    'name': 'Requirements',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Aside from YouTube ads, you can also make money through sponsorships and affiliate marketing.',
                'likes': 7,
                'is_right_answer': False,
                'date': '10/25/2024 10:15 AM',
                'user': {
                    'name': 'MarketingGuru',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Consider setting up a Patreon account for dedicated fans who want to support your content.',
                'likes': 4,
                'is_right_answer': False,
                'date': '10/25/2024 10:30 AM',
                'user': {
                    'name': 'Support',
                    'img': '/img/cat-avatar.jpeg'
                }
            }
        ]
    },
    {
        'id': 4,
        'title': 'How to create an eye-catching thumbnail for YouTube videos',
        'text': 'My video is getting few views. How to create a thumbnail that will hook viewers and make them click on the video?',
        'likes': 8,
        'tags': [
            'thumbnail', 'YouTube'
        ],
        'date': '10/26/2024 02:33 PM',
        'user': {
            'name': 'Attractiveness',
            'img': '/img/cat-avatar.jpeg'
        },
        'answers': [
            {
                'text': 'Use bright and contrasting colors to make your thumbnail stand out from other videos.',
                'likes': 10,
                'is_right_answer': True,
                'date': '10/26/2024 03:10 PM',
                'user': {
                    'name': 'Colors',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Include a close-up of a face with an expressive emotion, as it can attract more clicks.',
                'likes': 6,
                'is_right_answer': False,
                'date': '10/26/2024 03:20 PM',
                'user': {
                    'name': 'Expressions',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Add a short, bold text overlay to convey the main idea of the video quickly.',
                'likes': 5,
                'is_right_answer': False,
                'date': '10/26/2024 03:30 PM',
                'user': {
                    'name': 'BoldText',
                    'img': '/img/cat-avatar.jpeg'
                }
            }
        ]
    },
    {
        'id': 5,
        'title': 'How to fix sound problems in videos for YouTube',
        'text': 'My videos have terrible sound. How to fix this problem and make the sound clear and high-quality?',
        'likes': 6,
        'tags': [
            'sound', 'YouTube'
        ],
        'date': '10/27/2024 10:07 AM',
        'user': {
            'name': 'Quality',
            'img': '/img/cat-avatar.jpeg'
        },
        'answers': [
            {
                'text': 'Make sure your microphone or external audio equipment is properly connected and configured.',
                'likes': 8,
                'is_right_answer': True,
                'date': '10/27/2024 11:01 AM',
                'user': {
                    'name': 'Settings',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Use a noise reduction tool in editing software to remove background noise.',
                'likes': 4,
                'is_right_answer': False,
                'date': '10/27/2024 11:10 AM',
                'user': {
                    'name': 'NoiseReduction',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Record in a quiet, controlled environment to minimize ambient noise during filming.',
                'likes': 3,
                'is_right_answer': False,
                'date': '10/27/2024 11:20 AM',
                'user': {
                    'name': 'SilentRoom',
                    'img': '/img/cat-avatar.jpeg'
                }
            }
        ]
    },
    {
        'id': 6,
        'title': 'How to choose a topic for your YouTube channel',
        'text': 'I want to start a YouTube channel, but I don\'t know what to talk about. How to choose a topic that will be interesting to viewers?',
        'likes': 9,
        'tags': [
            'topic', 'YouTube'
        ],
        'date': '10/28/2024 12:09 PM',
        'user': {
            'name': 'Topic',
            'img': '/img/cat-avatar.jpeg'
        },
        'answers': [
            {
                'text': 'Think about your hobbies, interests, and skills. What are you passionate about and what do you know a lot about?',
                'likes': 8,
                'is_right_answer': True,
                'date': '10/28/2024 12:50 PM',
                'user': {
                    'name': 'Passion',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Research trending topics on YouTube to see what viewers are currently interested in.',
                'likes': 5,
                'is_right_answer': False,
                'date': '10/28/2024 1:00 PM',
                'user': {
                    'name': 'TrendHunter',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Experiment with different content until you find what resonates with your audience.',
                'likes': 4,
                'is_right_answer': False,
                'date': '10/28/2024 1:15 PM',
                'user': {
                    'name': 'TrialAndError',
                    'img': '/img/cat-avatar.jpeg'
                }
            }
        ]
    },
    {
        'id': 7,
        'title': 'How to record high-quality videos for YouTube',
        'text': 'My videos are blurry and the sound is bad. How to record high-quality videos that will look and sound good on YouTube?',
        'likes': 11,
        'tags': [
            'recording', 'YouTube'
        ],
        'date': '10/29/2024 09:13 AM',
        'user': {
            'name': 'Recording',
            'img': '/img/cat-avatar.jpeg'
        },
        'answers': [
            {
                'text': 'Use a good camera or smartphone with a high-resolution camera. Make sure the lighting is good and the sound is recorded in a quiet environment.',
                'likes': 9,
                'is_right_answer': True,
                'date': '10/29/2024 10:03 AM',
                'user': {
                    'name': 'Equipment',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Invest in a tripod to keep your camera steady and avoid shaky footage.',
                'likes': 6,
                'is_right_answer': False,
                'date': '10/29/2024 10:10 AM',
                'user': {
                    'name': 'SteadyShot',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Experiment with different lighting setups to see what works best for your location and equipment.',
                'likes': 5,
                'is_right_answer': False,
                'date': '10/29/2024 10:20 AM',
                'user': {
                    'name': 'LightExpert',
                    'img': '/img/cat-avatar.jpeg'
                }
            }
        ]
    },
    {
        'id': 8,
        'title': 'How to write catchy titles and descriptions for YouTube videos',
        'text': 'My videos have few views. How to write catchy titles and descriptions that will make people want to watch my videos?',
        'likes': 10,
        'tags': [
            'titles', 'descriptions', 'YouTube'
        ],
        'date': '10/30/2024 01:05 PM',
        'user': {
            'name': 'Titles',
            'img': '/img/cat-avatar.jpeg'
        },
        'answers': [
            {
                'text': 'Use keywords in your titles and descriptions so that your videos appear in search results. Keep your titles short and to the point, and write descriptions that give viewers a clear idea of what your video is about.',
                'likes': 8,
                'is_right_answer': True,
                'date': '10/30/224 02:03 PM',
                'user': {
                    'name': 'Optimization',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Make your titles intriguing by using questions or statements that create curiosity.',
                'likes': 5,
                'is_right_answer': False,
                'date': '10/30/2024 02:15 PM',
                'user': {
                    'name': 'Intrigue',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Consider using numbers or lists in titles (e.g., "Top 5 Tips") to make them more appealing.',
                'likes': 4,
                'is_right_answer': False,
                'date': '10/30/2024 02:25 PM',
                'user': {
                    'name': 'NumberedList',
                    'img': '/img/cat-avatar.jpeg'
                }
            }
        ]
    },
    {
        'id': 9,
        'title': 'How to promote your YouTube videos on social media',
        'text': 'I posted my video on YouTube, but it\'s not getting any views. How to promote my video on social media and get more people to watch it?',
        'likes': 7,
        'tags': [
            'promotion', 'YouTube', 'social media'
        ],
        'date': '10/31/2024 10:46 AM',
        'user': {
            'name': 'Social',
            'img': '/img/cat-avatar.jpeg'
        },
        'answers': [
            {
                'text': 'Share your video on different social media platforms, like Instagram, Twitter, and Facebook, and tailor your posts for each platform.',
                'likes': 9,
                'is_right_answer': True,
                'date': '10/31/2024 11:30 AM',
                'user': {
                    'name': 'Sharing',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Engage with followers by replying to comments and sharing your video link in relevant groups or forums.',
                'likes': 6,
                'is_right_answer': False,
                'date': '10/31/2024 11:45 AM',
                'user': {
                    'name': 'Engagement',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Create short teasers for your videos and share them as Stories or Reels to attract more viewers.',
                'likes': 4,
                'is_right_answer': False,
                'date': '10/31/2024 12:00 PM',
                'user': {
                    'name': 'Teasers',
                    'img': '/img/cat-avatar.jpeg'
                }
            }
        ]
    },
    {
        'id': 10,
        'title': 'How to increase engagement on YouTube videos',
        'text': 'My videos are getting views, but few likes or comments. How to increase engagement with my audience on YouTube?',
        'likes': 12,
        'tags': [
            'engagement', 'YouTube'
        ],
        'date': '11/01/2024 02:25 PM',
        'user': {
            'name': 'EngagementBoost',
            'img': '/img/cat-avatar.jpeg'
        },
        'answers': [
            {
                'text': 'Ask questions at the end of your video to encourage viewers to comment.',
                'likes': 10,
                'is_right_answer': True,
                'date': '11/01/2024 03:05 PM',
                'user': {
                    'name': 'QuestionPrompt',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Remind viewers to like and subscribe in the video or description to boost engagement.',
                'likes': 7,
                'is_right_answer': False,
                'date': '11/01/2024 03:15 PM',
                'user': {
                    'name': 'CallToAction',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Engage with your audience by responding to comments regularly.',
                'likes': 5,
                'is_right_answer': False,
                'date': '11/01/2024 03:25 PM',
                'user': {
                    'name': 'ReplyBuddy',
                    'img': '/img/cat-avatar.jpeg'
                }
            }
        ]
    },
    {
        'id': 11,
        'title': 'How to monetize a YouTube channel',
        'text': 'I have a growing YouTube channel. How can I start earning money from it?',
        'likes': 15,
        'tags': [
            'monetization', 'YouTube'
        ],
        'date': '11/02/2024 10:11 AM',
        'user': {
            'name': 'MoneyMaker',
            'img': '/img/cat-avatar.jpeg'
        },
        'answers': [
            {
                'text': 'Once you reach 1,000 subscribers and 4,000 watch hours, you can apply for the YouTube Partner Program to earn from ads.',
                'likes': 12,
                'is_right_answer': True,
                'date': '11/02/2024 10:45 AM',
                'user': {
                    'name': 'PartnerProgram',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Consider affiliate marketing by promoting products related to your content.',
                'likes': 8,
                'is_right_answer': False,
                'date': '11/02/2024 10:55 AM',
                'user': {
                    'name': 'AffiliateMarketer',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Create exclusive content for members and use platforms like Patreon for additional revenue.',
                'likes': 6,
                'is_right_answer': False,
                'date': '11/02/2024 11:05 AM',
                'user': {
                    'name': 'MembershipContent',
                    'img': '/img/cat-avatar.jpeg'
                }
            }
        ]
    },
    {
        'id': 12,
        'title': 'How to improve video editing for YouTube',
        'text': 'I want my videos to look more professional. What are some tips for editing YouTube videos?',
        'likes': 13,
        'tags': [
            'editing', 'YouTube'
        ],
        'date': '11/03/2024 08:30 AM',
        'user': {
            'name': 'EditorPro',
            'img': '/img/cat-avatar.jpeg'
        },
        'answers': [
            {
                'text': 'Use a consistent style for transitions, colors, and text to create a cohesive look across your videos.',
                'likes': 10,
                'is_right_answer': True,
                'date': '11/03/2024 09:05 AM',
                'user': {
                    'name': 'StyleMaster',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Keep your videos engaging by cutting out unnecessary pauses and adding background music.',
                'likes': 7,
                'is_right_answer': False,
                'date': '11/03/2024 09:15 AM',
                'user': {
                    'name': 'EngageMaster',
                    'img': '/img/cat-avatar.jpeg'
                }
            },
            {
                'text': 'Experiment with effects like zoom-ins and slow motion to emphasize important parts.',
                'likes': 5,
                'is_right_answer': False,
                'date': '11/03/2024 09:25 AM',
                'user': {
                    'name': 'EffectsGuru',
                    'img': '/img/cat-avatar.jpeg'
                }
            }
        ]
    }


]


def getMostPopularUsers():
    users = {}
    for question in gQuestions:
        if not question['user']['name'] in users:
            users[question['user']['name']] = 0
        users[question['user']['name']] += 1
        for answer in question['answers']:
            if not answer['user']['name'] in users:
                users[answer['user']['name']] = 0
            users[answer['user']['name']] += 1
    
    return list(dict(sorted(users.items(), key=operator.itemgetter(1), reverse=True)[:5]).keys())

def getAllQuestions():
    return gQuestions

def findQuestionById(id):
    for question in gQuestions:
        if question['id'] == id:
            return question
    return None

def getHotQuestions(minLikes=10):
    questions = []
    for question in gQuestions:
        if question['likes'] >= minLikes:
            questions.append(question)
    sorted(questions, key=lambda question: question['likes'], reverse=True)
    return questions

def getQuestionsContainingTag(tag):
    questions = []
    for question in gQuestions:
        for questionTag in question['tags']:
            if questionTag.lower() == tag.lower():
                questions.append(question)
                break
    return questions

def getTagListFromQuestions():
    tags = []
    for question in gQuestions:
        for questionTag in question['tags']:
            if questionTag.lower() not in tags:
                tags.append(questionTag.lower())
    return tags