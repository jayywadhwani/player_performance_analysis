from flask import Flask,render_template,request
from model import *

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def results():
      avg_run_test,avg_run_odi,avg_run_t20,\
      avg_sr_test,avg_sr_odi,avg_sr_t20,\
      lst3_test,lst3_odi,lst3_t20,\
      test_performance_chart,odi_performance_chart,t20_performance_chart,pie_test_chart,pie_odi_chart,pie_t20_chart = player_performance_analysis_total()
      return render_template('index.html',avg_run_test=avg_run_test,avg_run_odi=avg_run_odi,avg_run_t20=avg_run_t20,
      avg_sr_test=avg_sr_test,avg_sr_odi=avg_sr_odi,avg_sr_t20=avg_sr_t20,
      lst3_test=lst3_test,lst3_odi=lst3_odi,lst3_t20=lst3_t20,
      test_performance_chart=test_performance_chart,
      odi_performance_chart=odi_performance_chart,t20_performance_chart=t20_performance_chart,
      pie_test_chart=pie_test_chart,pie_odi_chart=pie_odi_chart,pie_t20_chart=pie_t20_chart)

if __name__ == "__main__":
      app.run(debug=True,port=5000)