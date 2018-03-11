hadoop fs -rm -r /user/80213526/test/output
hadoop jar hadoop-streaming-0.23.6.jar -file mapper.py -mapper "python mapper.py" \
    -file reducer.py -reducer "python reducer.py" \
    -input /user/80213526/test/datas -output /user/80213526/test/output
