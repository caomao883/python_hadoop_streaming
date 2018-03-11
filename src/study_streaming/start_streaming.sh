hadoop fs -rm -r /user/80213526/test/study_streaming/output
hadoop jar hadoop-streaming-0.23.6.jar \
-D mapred.job.name="testhadoop" \
-D mapred.job.queue.name=testhadoopqueue \
-D mapred.map.tasks=50 \
-D mapred.min.split.size=1073741824 \
-D mapred.reduce.tasks=10 \
-D stream.num.map.output.key.fields=1 \
-D num.key.fields.for.partition=1 \
-input /user/80213526/test/study_streaming/input \
-output /user/80213526/test/study_streaming/output \
-mapper "python mapper.py" \
-reducer "python reducer.py" \
-file mapper.py \
-file reducer.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner