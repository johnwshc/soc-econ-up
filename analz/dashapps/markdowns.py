
from dash import dcc,  html


class HTMs:

    @staticmethod
    def SharesText() -> html.Div:
        sharesdiv  = html.Div([
            html.H2('Noted:'),
            html.Ul([
                html.Li([
                    html.P("""Services NOW account for the majority of workers in Administration,
                    healthcare, sales, science and engineering, education and social services,
                     and others. If defined as labor we do directly for each other, services are
                     at least 60 % of the current workforce, as contrasted with production -- 
                     products  we sell to each other as property -- including farm, construction 
                     and extraction, as well as proprietary licensed software.
                      """),

                ]),
                html.Li([
                    html.P("""An 'industrial' data anomaly: In both 1860 and 2015 the services occupations are larger than production.
                    In the intervening eras, as the next chart covering 1910 - 2000 occupational shares will show, production occupations
                    grew to a dominant position absorbing even more from the automation of agriculture
                    than than services. Since about 1960 automation, and then globalization have steadily eroded
                    the manufacturing workforce share while greatly increasing its productivity. The dramatic increase 
                    in services has absorbed most of the reduced production occupation shares. Until AI.""")
                ]),
                html.Li([
                    html.P("""This chart does not distinguish public or non-profit services from commercial ones.""")
                ]),


            ])

        ])

        return sharesdiv

    @staticmethod
    def Shares1910Text():
        shares1910div = html.Div([
            html.H2('Noted:'),
            html.Ul([
                html.Li([
                    html.P("""This chart begins with the Rise of production and services absorbing the collapse
                     of agricultural labor and family farms in occupational shares since 1860. It then
                      illustrates the decline of production. """),

                ]),
                html.Li([
                    html.P("""By 1910, compared with 1860, the rise of scientific, technical 
                    and other skilled trades and occupations  reflected the dramatic rise in mass production.
                    It also reflected the systematic introduction of public education and the spread
                    of literacy beyond re-publications of the Bible. With literacy comes wider 
                    access to science, engineering, history, and art. """)
                ]),


            ])

        ])

        return shares1910div


    @staticmethod
    def AIPerformanceText():
        aiperf = html.Div([
            html.H5("AI Performance Metrics"),
            html.P([
                '''Note the accelerating speed at 
                which AI techniques achieve comparable
                human performance in these tasks '''
            ]),
            html.Ul([
                html.Li('Reading Comprehension'),
                html.Li('image recognition'),
                html.Li('language understanding'),
                html.Li('handwriting recognition'),
                html.Li('predictive reasoning'),
            ],  title='AI Performance Relative to These Tasks'),

        ])
        return aiperf


class Markdowns:

    @staticmethod
    def LearnAI():
        md = dcc.Markdown('''
        Andrew Ng's [Deep Learning AI Courses](https://www.deeplearning.ai/) 
        are a good -- and authoritative -- place to start. Andrew Ng is a 
        leading AI researcher. He is linked to the online
         [Coursera](https://www.coursera.org/specializations/deep-learning)
        educational platform, the Google Brain project, OpenAI, and Stanford University. 
        ''')
        return md

    @staticmethod
    def AlgorithmDefinition():
        md = dcc.Markdown('''
        ## What is an An algorithm?
         
         An algorithm is a mathematically rigorous set of instructions 
         that is designed to accomplish a task. 
         
         Algorithms usually take one or more inputs, 
         run them systematically through a series of steps, 
         and provide one or more outputs. 
         
         Algorithms are typically associated with computing 
         and are an essential element of computer programming.
         
        ''')
        return md



    @staticmethod
    def AIDefinition():
        md = dcc.Markdown('''
        ## What Is Artificial Intelligence?
        [Artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence) 
        (AI), in its broadest sense, 
        is intelligence exhibited by machines, particularly computer systems. 
        It is a field of research in computer science that develops and 
        studies methods and software that enable machines to perceive 
        their environment and use learning and intelligence to take 
        actions that maximize their chances of achieving defined goals.
        Such machines may be called AIs. 
        
        Has the [Turing Test](https://en.wikipedia.org/wiki/Turing_test) 
        of machine intelligence been satisfied?
        
        Some high-profile applications of AI include advanced web search engines, 
        recommendation systems, interacting via human speech, 
        autonomous vehicles (e.g., Waymo); generative and creative tools, 
        and superhuman play and analysis in strategy games (e.g., chess and Go).
        
        ''')
        return md

    @staticmethod
    def SupervisedLearningApps():
        md = dcc.Markdown('''
        ###### Supervised Learning Applications
        real Estate, Authentication, recommendations (including pricing), 
        classification, online advertising, photo tagging, speech recognition,
        machine translation, robotics, autonomous vehicles, including Drones, and
        other weapons.
        ''')
        return md

    @staticmethod
    def SupervisedLearningDefinition():
        md = dcc.Markdown('''
        
            ## Is It A Cat??
           
           In [supervised learning](https://www.geeksforgeeks.org/supervised-unsupervised-learning/), 
           the machine is trained on a set of labeled data, which means that the 
           input data is paired with the desired output. 
            
            Example: A training set consists of one million pictures of cats. One million pictures of "no cats". 
            
           The machine then -- in part --  learns  to self-predict correctly whether  
           the new picture is of a cat. 
           
           This kind of supervised learning algorithm is widely  for tasks such as 
           photo-id verification, classification, regression, and object detection (e.g. medical images).


           ''')
        return md

    @staticmethod
    def UnsupervisedLearningApps():
        md = dcc.Markdown('''
                
        ###### **Unsupervised learning Apps** 
        
        * Two example tasks gauging the current level of AI:
            - Consider a 100 page document. 
            Remove 10 pages from the document. Unsupervised learning algorithms 
            are now getting very good at filling in the missing 10 pages.
            
            - Consider a 5 minute movie clip of a scene at an arbitrary intersection
            in any city. Remove an arbitrary minute of slices the vidio file. Unsupervised
            Learning cannot YET complete the missing minute. But we are working hard on it!
        
        * Natural Language Processing Related Tasks:
            - categorizing articles in news sections, 
            - text translation and classification, 
            - speech recognition in conversational interfaces. 
            
        * Genetic research: Genetic clustering may be a Pandora's 
        Box of Evolutionary secrets. 
        ''')

        return md



    @staticmethod
    def MachineLearningDefinition():
        md = dcc.Markdown('''
        ###### [Machine learning (ML)](https://en.wikipedia.org/wiki/Machine_learning#cite_note-ibm-2) is  concerned with the development and study of statistical algorithms that can:
         - learn from data  for purposes of classification and prediction.
         - generalize learning methods to include **unseen data** and 
         thus perform tasks without explicit instructions. 
         - model human intelligence features.

        ML finds application in many fields, including [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing)
        , [computer vision](https://en.wikipedia.org/wiki/Computer_vision), 
        [speech recognition](https://en.wikipedia.org/wiki/Speech_recognition), 
        [email filtering](https://en.wikipedia.org/wiki/Email_filtering), 
        [agriculture](https://en.wikipedia.org/wiki/Agriculture), and 
        medicine.
        
        ##### Machine Learning algorithms are broadly divided into [symbolic vs statistical](https://www.aibrilliance.com/blog/what-is-the-difference-between-symbolic-systems-and-machine-learning) categories, with the latter making the most rapid progress.
        
        The algorithms have been further classified into unsupervised, and supervised types. 
        
        ''')
        return md

    @staticmethod
    def UnsupervisedLearningDefinition():
        md = dcc.Markdown('''
       
        [Unsupervised learning](https://en.wikipedia.org/wiki/Unsupervised_learning) is a 
        machine learning technique that uses algorithms to analyze unlabeled data 
        without human supervision. The algorithms are able to identify patterns 
        and insights in the data on their own. This type of learning is well 
        suited for complex tasks, such as: 
        [*Clustering*](https://www.geeksforgeeks.org/clustering-in-machine-learning/), 
        [*Association*](https://en.wikipedia.org/wiki/Association_rule_learning), and
         [*Dimensionality reduction*](https://en.wikipedia.org/wiki/Dimensionality_reduction)
         
        ''')
        return md

    @staticmethod
    def DeepLearningDefinition():
        md = dcc.Markdown('''
        
        [Deep learning](https://en.wikipedia.org/wiki/Deep_learning) is the subset 
        of machine learning methods based on neural networks with representation 
        learning. The Representations are "neuron-like". Software "neurons" are constructed
        to accept inputs and generate outputs modeled on the known (and speculated) features 
        of human and other  biological neural networks. The adjective "deep" refers to 
        the use of multiple layers in the network. More hidden layers add to 
        Machine Learning 'intelligence' capacities, given sufficient data,  
        but also the computational costs. 
        
        Methods used can be either supervised, semi-supervised or 
        unsupervised.
        
        ''')
        return md

    @staticmethod
    def DeepLearningApps():
        md = dcc.Markdown('''
        ###### **Deep Learning Applications**        
        * computer vision
        * speech recognition
        * NLP tasks: 
            - translation, conversation, classification
        * bioinformatics, 
        * drug design, 
        * medical image analysis, 
        * climate change, 
        * gaming or warfare - at times surpassing human expert performance.
        
        ''')

        return md

    @staticmethod
    def GS_AI_job_impact():
        md = dcc.Markdown('''
                ###### **AI Job impacts from Goldman Sachs**        
                
        If generative AI delivers on its promised capabilities, the labor
        market could face significant disruption. Using data on occupational
        tasks in both the US and Europe, we find that roughly two - thirds
        of current jobs are exposed to some degree of AI automation, and that
        generative AI could substitute up to one - fourth of current  work.
        
        Extrapolating our estimates globally suggests that generative AI
        could expose the equivalent of 300 mn full-time jobs to automation.

        The good news is that  worker displacement from automation has  historically
        been offset by creation of new  jobs, and the emergence of new occupations
        following technological innovations accounts for the vast majority 
        of long-run employment growth.The combination of significant labor 
        cost savings, new job creation, and higher productivity for non-displaced 
        workers raises the possibility of a productivity boom that raises economic 
        growth substantially, although the timing of such a boom is hard to predict.

        ''')
        return md

    @staticmethod
    def DataWorldUse():
        md = dcc.Markdown('''
        
            ##### [Source](https://ourworldindata.org/grapher/test-scores-ai-capabilities-relative-human-performance)
                
            Citation:
               
               “Data Page: Test scores of AI systems on various 
                capabilities relative to human performance”, 
                part of the following publication: Charlie Giattino, 
                Edouard Mathieu, Veronika Samborska and 
                Max Roser (2023) - 'Artificial Intelligence'. 
                Data adapted from Kiela et al.. "                
                
                ''')
        return md


    @staticmethod
    def AILaborText():
        md = dcc.Markdown('''
        ## AI and Labor
        
        Workers are at the epicenter of the greatest technological 
        transformation of the modern era—our rights and economic 
        security are at stake. Now more than ever, workers need 
        the collective power of unions.
            
        - Public sentiment echoes this call: overall union favorability 
        is at the highest it’s been in half a century. Working people 
        know giant corporations and tech firms cannot be trusted to 
        self-regulate this revolutionary technology.
        
        - Employers are currently deploying increasingly sophisticated 
        AI-enhanced technologies without workers’ consent in order to 
        hire, monitor, evaluate, discipline and even fire workers. 

        - This is just the beginning: The New York Times reports that 
        nearly half of all jobs will be exposed to some form of AI 
        automation that will disrupt and displace workers in the coming years. 

        - Of those who will see their jobs erased in the next 10 years, 
        nearly 80% could make less than $38,000 annually.  

        - Without protections, working women and people of color will experience 
        the worst social and economic outcomes of this technology.

        - In order to protect workers’ job quality, safety and rights, working 
        people must be included in the design, development and implementation of 
        artificial intelligence. 

        - Labor unions are the most powerful tool workers have to demand inclusion.

        - Labor unions do not oppose AI. AI has the potential to unleash prosperity 
        that improves working conditions and lifts us all up. But if left unchecked 
        in the hands of corporate profiteers, AI will increase economic inequality, 
        curtail our rights and undermine our democracy.
        ''')

        return md








