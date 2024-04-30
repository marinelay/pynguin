pynguin --maximum-search-time=600 \
    --assertion-generation=NONE \
    --create-coverage-report=True \
    --project-path=projects/black/src \
    --module-name=black.__init__ \
    --output-path=projects/black/testgen \
    --report-dir=projects/black/coverage_report \
    -v \
    --poor \
    --type_inference_strategy=TYPE_HINTS \