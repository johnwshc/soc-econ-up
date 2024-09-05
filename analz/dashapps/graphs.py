import plotly.graph_objects as go
from dash import dcc
# from chart_studio import plotly as py
# from plotly.graph_objs import *
from app import usge, cfed
# from analz.dashapps.dataUtils import US_Gov_Employment as USGE
import plotly.express as px
import pandas as pd

# def sGraph():
#
#     py.sign_in('', '')
#     data = Data([
#         Bar(
#             x=['Sivaranjani S', 'Vijayalakshmi C', 'Rajeshwari S', 'Shanthi Priscilla', 'Pandiyaraj G', 'Kamatchi S',
#                'MohanaPriya', 'Madhumitha G', 'Franklin Alphones Raj J', 'Akfaris Almaas', 'Biswajit Champati',
#                'Priya R', 'Rekha Rajasekaran', 'Sarath Kumar B', 'Jegan L', 'Karthick A', 'Mahalakshmi S',
#                'Ragunathan V', 'Anu S', 'Ramkumar KS', 'Uthra R'],
#             y=[1640, 1394, 1390, 1313, 2166, 1521, 1078, 1543, 780, 1202, 1505, 2028, 2032, 1769, 1238, 1491, 1477,
#                1329, 2038, 1339, 1458],
#             text=['Scuti', 'Scuti', 'Cygni', 'Scorpii', 'Scuti', 'Pollux', 'Scorpii', 'Pollux', 'Scuti', 'Pollux',
#                   'Scorpii', 'Scorpii', 'Scuti', 'Cygni', 'Scorpii', 'Scuti', 'Scuti', 'Pollux', 'Scuti', 'Pollux',
#                   'Pollux']
#         )
#     ])
#
#     layout = Layout(
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)',
#         title="1860 to 2015: Occupational Revolutions",
#
#     )
#
#     fig = Figure(data=data, layout=layout)
#
#     # plot_url = py.plot(fig, filename='transparent-background')
#     return dcc.Graph(figure=fig)

def USGovTotals() -> dcc.Graph:
    # usge = USGE()
    df = usge.dff

    dff = df[['total']].copy()
    x = list(dff.index)
    y = dff.total
    fig = px.bar(dff, y='total', x=x, text_auto='.2s',
                 title="Total Federal Employment by Years: 1984 - 2020")
    fig.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )
    g = dcc.Graph(
        id='usgov-total',
        figure=fig
    )
    return g




def USGovGraph() -> dcc.Graph:
    # usge = USGE()
    dfm = usge.dfmelt.copy(deep=True)
    x = list(dfm.index)
    variable = dfm.variable

    y = dfm.value
    figure = px.line(dfm, x=x, y=y, color=variable)
    # figure.update_xaxes(showgrid=False)
    figure.update_yaxes(showgrid=False)
    figure.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    ),


    g = dcc.Graph(
        id='usgov-graph',
        figure=figure
    )
    return g


def SharesGraph():

    # cfed: CFED1 = CFED1.fromCFED()
    top_occs: pd.DataFrame = cfed.topOccs
    xx = top_occs.short_occ_name
    y1 = top_occs.s1860
    y2 = top_occs.s2015

    fig = go.Figure()
    fig.add_trace(go.Bar(

        x=xx,
        y=y1,
        name='1860 % Share',
        marker_color='goldenrod',
        text=y1,
        textposition='outside',
        textfont=dict(
                    size=18,
                ),

        showlegend=True


    ))
    fig.add_trace(go.Bar(
        x=xx,
        #
        y=y2,
        name='2015 % Share',
        marker_color='red',
        text=y2,
        textposition='outside',
        textfont=dict(
            color='black',
            size=18,
        ),
        showlegend=True

    ))

    fig.update_layout(
        barmode='group',
        xaxis_tickangle=-45,
        paper_bgcolor='black',
        plot_bgcolor='black',
        height=500,
        title="1860 to 2015: Occupational Revolutions",
        xaxis=dict(title="Occupation Groups 1860 - 2015"),
        yaxis=dict(title="Percent Share of Workforce"),
        legend=dict(title="Years",
                    bgcolor='darkgrey',
                    font=dict(
                        family="Courier",
                        size=16,
                        color="white",
                        ),
                    ),
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="white",
            # variant="small-caps",
        )
    )
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="cornsilk",
            font_size=16,
            font_family="Rockwell",
            font=dict(color='red'),
        )
    )

    # fig.show()
    return dcc.Graph(figure=fig)
