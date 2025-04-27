from flask import Flask,render_template,request
from model import *

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def results():
      avg_run_test,avg_run_odi,avg_run_t20,\
      avg_sr_test,avg_sr_odi,avg_sr_t20,\
      lst3_test,lst3_odi,lst3_t20,\
      test_performance_chart,odi_performance_chart,t20_performance_chart,pie_test_chart,pie_odi_chart,pie_t20_chart =player_performance_analysis_total()
      chart_test_teamwise,chart_odi_teamwise,chart_t20_teamwise=player_performance_analysis_teamwise("v England")
      predicted_runs = 0
      if request.method == 'POST':
            if request.form.get('BF-input') == None or request.form.get('BF-input')==  "" or request.form.get('BF-input')== "NULL":
                  match_type = ""
                  balls_faced = 0
                  strike_rate = 0
                  inngs_no = 0
                  predicted_runs = 0
                  player_performance_analysis_prediction(match_type,balls_faced,strike_rate,inngs_no)
            else:
                  match_type = request.form['format-input']
                  balls_faced = request.form['BF-input']
                  strike_rate = request.form['SR-input']
                  inngs_no = request.form['Inngs-input']
                  predicted_runs=player_performance_analysis_prediction(match_type,balls_faced,strike_rate,inngs_no)
            test_performance_chart,odi_performance_chart,t20_performance_chart,pie_test_chart,pie_odi_chart,pie_t20_chart =player_performance_analysis_total(player_name)
      opposition_name = ""
      if request.method == 'POST':
            if request.form.get('opposition-input') == None or request.form.get('opposition-input')==  "" or request.form.get('opposition-input')== "NULL":
                  opposition_name = ""
            else:
                  opposition_name = request.form['opposition-input']
            chart_test_teamwise,chart_odi_teamwise,chart_t20_teamwise=player_performance_analysis_teamwise(opposition_name)


      return render_template('index.html',avg_run_test=avg_run_test,avg_run_odi=avg_run_odi,avg_run_t20=avg_run_t20,
      avg_sr_test=avg_sr_test,avg_sr_odi=avg_sr_odi,avg_sr_t20=avg_sr_t20,
      lst3_test=lst3_test,lst3_odi=lst3_odi,lst3_t20=lst3_t20,
      test_performance_chart=test_performance_chart,
      odi_performance_chart=odi_performance_chart,t20_performance_chart=t20_performance_chart,
      pie_test_chart=pie_test_chart,pie_odi_chart=pie_odi_chart,pie_t20_chart=pie_t20_chart,
      chart_test_teamwise=chart_test_teamwise,
      chart_odi_teamwise=chart_odi_teamwise,
      chart_t20_teamwise=chart_t20_teamwise,predicted_runs=predicted_runs)


if __name__ == "__main__":
      app.run(debug=True,port=5000)