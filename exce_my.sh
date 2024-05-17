pynguin --maximum-search-time=600 \
    --assertion-generation=NONE \
    --create-coverage-report=True \
    --project-path=projects/thonny \
    --module-name=thonny.roughparse \
    --output-path=projects/thonny/testgen \
    --report-dir=projects/thonny/coverage_report \
    -v \
    --poor \
    --type_inference_strategy=TYPE_HINTS \