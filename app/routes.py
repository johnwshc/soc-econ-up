from app import server, usge, cfed
from flask import  render_template, redirect, make_response, request
from analz.dashapps.ara_ai import IntroAI, AI, Agg2AI, Futures
from analz.dashapps.aicards import MLCardContent, SLCard, MLCards
from dash.dependencies import Input, Output
from dash import html


#
#
#
#  AI Report for ARA Converntion
########################################

ai_ara = AI()


@ai_ara.callback(
    Output("page-content", "children"),
    Input("url", "pathname"))
def render_page_content(pathname):
    print(f'pathname is: {pathname}')
    if pathname == "/aip/aip":
        # return html.P("This is the content of the home page!")
        return IntroAI()
    elif pathname == "/aip/ml":
        # return html.P("This is the content of page 1. Yay!")
        return MLCards()
    elif pathname == "/aip/agg2ai":
        return Agg2AI()
    elif pathname == "/aip/futures":

        return Futures()
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

if __name__ == "__main__":
    ai_ara.run(debug=True)

# ###############   ER HOME   #################


@server.route('/', methods=['GET'])
@server.route('/home', methods=['GET'])
def home():
    msg = "hello Reporters logger"
    # slog.log(msg)
    print(msg)

    return render_template("er.html")


# # ##############  Whats Playing  ##############
# @app.route('/whats_playing', methods=['GET', 'POST'])
# def whats_playing():
#     if request.method == 'POST':
#         content_type = request.headers.get('Content-Type')
#         if content_type == 'application/json':
#             d = json.loads(request.get_data())
#             txt = d['wp']
#             print(f"wp txt: {txt}")
#             with open(Config.ER_WP_P, "w" ) as f:
#                 f.write(txt)
#             return "success"
#         else:
#             return "invalid content-type"

#     with open(Config.ER_WP_P) as f:
#         txt = f.read()
#     ds = datetime.now().date().strftime('%A')[0:3].lower()
#     menu_props = stage.pattern_to_html(ds)
#     return render_template('wp.html', wp_txt=txt, menu=menu_props)

# ##### Reporter Gateway  ###################

@server.route('/reporter')
def reporter():
    return render_template('reporter.html', title='reporter')

@server.route('/analytics')
def analytics():  # put application's code here
    # hosts = {'whats_playing':}
    return render_template('rc_analytics.html', title='Red Caboose Analytics')



