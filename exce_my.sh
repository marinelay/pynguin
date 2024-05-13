pynguin --maximum-search-time=600 \
    --assertion-generation=NONE \
    --create-coverage-report=True \
    --project-path=projects/codetiming \
    --module-name=codetiming._timer \
    --output-path=projects/codetiming/testgen \
    --report-dir=projects/codetiming/coverage_report \
    -v \
    --poor \
    --type_inference_strategy=TYPE_HINTS \