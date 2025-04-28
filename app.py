from flask import Flask,render_template,request
from model import *

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def results():
      avg_run_test,avg_run_odi,avg_run_t20,\
      avg_sr_test,avg_sr_odi,avg_sr_t20,\
      lst3_test,lst3_odi,lst3_t20,\
      test_performance_chart,odi_performance_chart,t20_performance_chart,\
      pie_test_chart,pie_odi_chart,pie_t20_chart = player_performance_analysis_total()

      # opposition_name = ""
      # if request.method == 'GET':
            # if request.form.get('opposition-input') == None or request.form.get('opposition-input')==  "" or request.form.get('opposition-input')== "NULL":
      opposition_name = ""
      chart_test_teamwise,chart_odi_teamwise,\
      chart_t20_teamwise=player_performance_analysis_teamwise(opposition_name)
      if request.form.get('opposition-input') != '':
            opposition_name = request.form.get('opposition-input')
            chart_test_teamwise,chart_odi_teamwise,\
            chart_t20_teamwise=player_performance_analysis_teamwise(opposition_name)
      else:
            opposition_name = ""
            chart_test_teamwise,chart_odi_teamwise,\
            chart_t20_teamwise=player_performance_analysis_teamwise(opposition_name)

      # predicted_runs = 0
            # if request.form.get('BF-input') == None or request.form.get('BF-input')==  "" or request.form.get('BF-input')== "NULL":
      match_type = "Odi"
      balls_faced ,strike_rate,inngs_no,predicted_runs,mse,r2,mae = 0,0,0,0,0,0,0
      if request.form.get('format-input') != '':
            match_type = request.form.get('format-input')
            balls_faced = request.form.get('BF-input',type=int)
            strike_rate = request.form.get('SR-input',type=float)
            inngs_no = request.form.get('Inngs-input',type=int)
            predicted_runs,mse,r2,mae=player_performance_analysis_prediction(match_type,balls_faced,strike_rate,inngs_no)
      else:
            match_type = ""
            balls_faced ,strike_rate,inngs_no,predicted_runs,mse,r2,mae = 0,0,0,0,0,0,0

      return render_template('index.html',avg_run_test=avg_run_test,avg_run_odi=avg_run_odi,avg_run_t20=avg_run_t20,
      avg_sr_test=avg_sr_test,avg_sr_odi=avg_sr_odi,avg_sr_t20=avg_sr_t20,
      lst3_test=lst3_test,lst3_odi=lst3_odi,lst3_t20=lst3_t20,
      test_performance_chart=test_performance_chart,
      odi_performance_chart=odi_performance_chart,t20_performance_chart=t20_performance_chart,
      pie_test_chart=pie_test_chart,pie_odi_chart=pie_odi_chart,pie_t20_chart=pie_t20_chart,
      chart_test_teamwise=chart_test_teamwise,
      chart_odi_teamwise=chart_odi_teamwise,
      chart_t20_teamwise=chart_t20_teamwise,predicted_runs=predicted_runs,
      mse=mse,r2=r2,mae=mae)


if __name__ == "__main__":
      app.run(debug=True,port=5000)