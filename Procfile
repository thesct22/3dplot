
conda: install nodejs

web: bokeh serve \
    --log-level=debug \
    --num-procs=0 \
    --port=$PORT \
    --show \
    --host=my_app.herokuapp.com \
    --host=* --address=0.0.0.0 \
    --use-xheaders sample.py