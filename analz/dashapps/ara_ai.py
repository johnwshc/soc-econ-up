from app import server
import dash
from dash import dcc, Dash, html
import dash_bootstrap_components as dbc
from analz.dashapps.aicards import ICard, SharesCard, Shares1910Card
from analz.dashapps.aicards import AIJobImpact1Card, AIOccImmpactGSCard, PublicCard, UnionCard
from analz.dashapps.markdowns import Markdowns as MD
from analz.dashapps.graphs import USGovTotals

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "padding": "2rem 1rem",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


def SideBar() -> html.Div:
    sidebar = html.Div(
        [
            html.H2("AI Slides"),
            html.Hr(),
            html.P(
                "An Introduction To AI", className="lead"
            ),
            dbc.Nav(
                [
                    dbc.NavLink("What Is AI?", href="aip", active="exact"),
                    dbc.NavLink("Machine Learning", href="ml", active="exact"),
                    dbc.NavLink("Workforces From Agg to AI", href="agg2ai", active="exact"),
                    dbc.NavLink("Last Resorts", href="futures", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=SIDEBAR_STYLE,
        className="w-25"

    )
    return sidebar


def AI(pth='/aip/') -> dash.Dash:
    ai_app = dash.Dash(server=server,
                       routes_pathname_prefix=pth,
                       external_stylesheets=[dbc.themes.DARKLY]
                       )

    sidebar = SideBar()

    content = html.Div(id="page-content", style=CONTENT_STYLE, className="w-75")

    ai_app.layout = html.Div([dcc.Location(id="url"), sidebar, content], className="w-100")
    return ai_app


def Agg2AI() -> dbc.Container:
    con = dbc.Container([
        dbc.Tabs(
            [
                dbc.Tab(SharesCard(), label="Occupational Shares, 1860 Forward"),
                dbc.Tab(Shares1910Card(), label="Occupational Shares, 1910 Forward"),
                dbc.Tab(AIJobImpact1Card(), label="AI/Human Task Performance"),
                dbc.Tab(AIOccImmpactGSCard(), label="AI Job Impacts, by Occupation"),

            ]
        ),
    ])
    return con

def Futures() -> dbc.Container:
    tab_content1 = dbc.Tab(
        [
            PublicCard(),
            html.H4("Federal Totals by Year"),
            USGovTotals(),

        ], label="The Employer of Last Resort")
    tab_content2 = dbc.Tab(UnionCard(), label="Union Card")
    con = dbc.Container([
        dbc.Tabs([
            tab_content1,
            tab_content2,
        ])
    ])

    return con


def IntroAI() -> dbc.Container:
    card = ICard()
    introai = html.Div([
        html.H2("Intro to AI"),
        card,])
    definitions = dbc.Card(
        dbc.CardBody(
            [
                MD.AIDefinition(),
                MD.AlgorithmDefinition(),
                html.H5("Want to Learn AI?"),
                MD.LearnAI(),
            ]
        ),
        # className="mt-3",
    )
    con = dbc.Container([
        dbc.Tabs(
                [
                    dbc.Tab(introai, label="AI Intro"),
                    dbc.Tab(definitions, label="Definitions"),

                ]
        ),
    ])

    return con


