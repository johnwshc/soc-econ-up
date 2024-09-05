from dash import dcc, html
import dash_bootstrap_components as dbc
from analz.dashapps.markdowns import Markdowns as MD, HTMs
from analz.dashapps.graphs import SharesGraph, USGovGraph
# from analz.dashapps.dataUtils import US_Gov_Employment as USGE
from app import usge


def UnionCard():
    simg = {
        'width': '500px',
        'height': '400px',
    }
    websrc = 'https://aflcio.org/issues/future-work/ai'
    ifr = html.Iframe(src=websrc)
    card = dbc.Card([
        dbc.CardHeader("AFL-CIO on AI"),
        dbc.CardImg(src="/static/img/AI_labor.jpg", top=True, style=simg),
        dbc.CardBody(html.Div([
          MD.AILaborText(),
        ],id='ai-labor-text')),
        ])

    return card


def PublicCard() -> dbc.Card:

    # usge = USGE()
    dfm = usge.dfmelt
    total_2020 =  usge.str_total_2020


    card = dbc.Card([
        dbc.CardHeader("Public Sector Employment"),
        USGovGraph(),
        dbc.CardBody(
            [


                html.H4(f"""2020 US Federal Public Employment"""),

                html.P(f"""including civilian, 
                    military, contract, and postal: {total_2020}"""),

                #
                dcc.Markdown('''
                Data From [Statistia](https://www.statista.com/): Estimated total public employment including
                state, county and municipal public employment: 20.2 Million, 14.5 % of the workforce .
                
                Other than government there is no obvious "employer of last resort" beyond volunteer or 
                other non-commercial work. However -- where is the tax base to either support or employ
                 those left behind after the AI hurricanes? Perhaps more to the point for corporations, especially
                 productive ones --- where will profit, or customers, come from if there is no wage or salary labor?
                
                '''),


            ])
       ])

    return card




#
# def US_gov_jobs1_card():
#
#     card = dbc.Card([
#         dbc.CardHeader("US Government Civiian Employment, by Year"),
#         dbc.CardImg(src="/static/img/occ_ai_impact_gs.png", top=True),
#         dbc.CardBody(
#             [
#                 html.H4("Goldman Sachs: Deep Impact on Service and Production", className="card-title"),
#                 html.P(
#                     "Some quick example text to build on the card title and "
#                     "make up the bulk of the card's content.",
#                     className="card-text",
#                 ),
#                 dbc.Button("Go somewhere", color="primary"),
#             ]
#         ),
#
#     ])
#     return card


def AIOccImmpactGSCard():
    card = dbc.Card([
        dbc.CardHeader("AI Impact, by Occupation"),

        dbc.CardImg(src="/static/img/occ_ai_impact_gs.png", top=True),
        dbc.CardBody(
            [
                html.H4("Goldman Sachs: Deep AI Impact on Service and Production", className="card-title"),
                dcc.Markdown('''
                Goldman Sachs has a powerful interest in the accuracy of its economic forecasting. That interest
                 arises out of the inherent risk associated with investing in the future. Investment firms also have 
                 an interest in biasing the regulatory  and international investment environment in any way 
                 that reduces risks and their inevitable costs to the profitability of the investments.
                 
                 The projections from Goldman Sachs are data driven, but also still speculative. The rate of
                 AI deployment and acceleration is not yet known. There are many variables: jobs,
                  security, privacy, property, government, politics, war, or peace. 
                  
                  The overwhelming impact on services does give one pause however.
                 
                 #### What is going to absorb the losses to Services?
                '''),

                # dbc.Button("Last Resorts", color="primary"),
                html.Div([
                    dbc.Button('Last Resorts', href='futures'),
                ]),

                # html.Div([
                #     html.Div([], style={'display': "block", 'height': "2000px"}),
                #     html.Div([
                #         html.H3('Record Information', id='record-info')
                #     ])
                # ])
            ]
        ),

    ])
    return card



def AIJobImpact1Card():
    simg = {
        'width': '500px',
        'height': '500px',
    }
    card = dbc.Card([
        dbc.CardHeader("AI Performance"),
        html.Center([
            dbc.CardImg(src="/static/img/AI_performance.png", top=True, style=simg),
        ]),

        dbc.CardBody(
            [
                html.H4("AI Performance Rapid Rise: ", className="card-title"),
                HTMs.AIPerformanceText(),
            ]
        ),

    ])
    return card
def Shares1910Card()-> dbc.Card:
    simg = {
        'width': '700px',
        'height': '800px',
    }
    card = dbc.Card([
        dbc.CardHeader("Industrialization Accelerates New Workforce"),

        dbc.CardImg(src="/static/img/proportional_occs_1910-1000.JPG", top=True, style=simg),
        dbc.CardBody(
            [
                html.H4("Occupational Group Employment Shares in the US: 1910--2000", className="card-title"),
                HTMs.Shares1910Text(),
            ]
        ),

    ])
    return card


def SharesCard() -> dbc.Card:
    card = dbc.Card([
        dbc.CardHeader("Technology and the Division of Labor"),
        dbc.CardBody(
            [
                SharesGraph(),
                # html.H4("1860 to 2015: Occupational Revolutions", className="card-title"),
                html.H6("Changes in Occupational Group Shares of US Workforce", className="card-subtitle"),

                dbc.CardLink("Source: The Cleveland Fed",
                             href="https://www.clevelandfed.org/publications/economic-commentary/2019/ec-201909-changes-in-us-occupational-structure"),
                HTMs.SharesText(),

            ]
        )
        ]
    )

    return card


def ICard() -> dbc.Card:

    sty1 = {
        'height': '500px'
    }

    simg = {
      'width': '500px',
      'height': '500px',
    }
    card = dbc.Card(
        [

            html.Center([
                dbc.CardImg(src="/static/img/ai-machine-relation.png", top=True, style=simg),
            ]),

            dbc.CardBody(
                [
                    html.H2("What is Artificial Intelligence?", className="card-title"),
                    dcc.Markdown('''
                        #### **The development of Machine Learning technologies is at the heart of recent breakthroughs in Artificial Intelligence.**
                        
                        ''')



                ]
            ),
        ],
        className="w-75"
        # style={"width": "18rem"},
    )
    return card

def IntroCard() -> dbc.Card:

        return ICard()


def MLCardContent() -> list:
    simg = {
        'width': '400px',
        'height': '300px',
    }
    card_content = [
        html.Center(
            [
                dbc.CardImg(src='/static/img/ml1.jpg', top=True, style=simg),
            ]
        ),
        dbc.CardHeader('What is Machine Learning?', className="card-title"),
        dbc.CardBody(
            [
                # html.H5("What is Machine Learning?", className="card-title"),
                # html.P(
                #     "This is some card content that we'll reuse",
                #     className="card-text",
                # ),
                MD.MachineLearningDefinition()



            ]
        ),
    ]
    return card_content


def SLCard():
    simg = {
        'width': '600px',
        'height': '400px',
    }
    card_content = [

        html.Center(
            [
                dbc.CardImg(src='/static/img/isit_cat.png', top=True, style=simg),
            ]
        ),
        dbc.CardHeader(
            [html.H3("What is Supervised Learning?")], className="card-title"),
        dbc.CardBody(
            [
                # html.H5("What is Supervised Learning?", className="card-title"),
                # html.P(
                #     "This is some card content that we'll reuse",
                #     className="card-text",
                # ),
                MD.SupervisedLearningDefinition(),
                MD.SupervisedLearningApps()

            ]
        ),
    ]
    return card_content


def ULCard():
    simg = {
        'width': '500px',
        'height': '400px',
    }
    card_content = [

        html.Center(
            [
                dbc.CardImg(src='/static/img/unsuper.webp', top=True, style=simg),
            ]
        ),
        dbc.CardHeader('What is Unsupervised Learning?', className="card-title"),
        dbc.CardBody(
            [
                # html.H5("What is Unsupervised Learning?", className="card-title"),
                # html.P(
                #     "This is some card content that we'll reuse",
                #     className="card-text",
                # ),
                MD.UnsupervisedLearningDefinition(),
                MD.UnsupervisedLearningApps(),

            ]
        ),
    ]
    return card_content


def DLCardContent() -> list:
    simg = {
        'width': '540px',
        'height': '300px',
    }
    card_content = [
        html.Center(
            [
            dbc.CardImg(src='/static/img/deep_learning_model.png', top=True, style=simg),
            ]
        ),
        dbc.CardHeader('What is Deep Learning?', className="card-title"),
        dbc.CardBody(
            [
                # html.H5("What is Deep Learning?", className="card-title"),
                # html.P(
                #     "This is some card content that we'll reuse",
                #     className="card-text",
                # ),
                MD.DeepLearningDefinition(),
                MD.DeepLearningApps(),

            ]
        ),
    ]
    return card_content


def MLCards():

    stabs = dbc.Tabs(
                    [
                        dbc.Tab(dbc.Card(MLCardContent(), color="primary", inverse=True),
                                label='What is Machine Learning?'),
                        dbc.Tab(dbc.Card(SLCard(), color="warning", inverse=True),
                                label='Supervised Machine Learning'),
                        dbc.Tab(dbc.Card(ULCard(), color="info", inverse=True),
                                label='Unsupervised Learning'),
                        dbc.Tab(dbc.Card(DLCardContent(), color="danger", inverse=True),
                                label="Deep Learning"),

                    ])
    return stabs

