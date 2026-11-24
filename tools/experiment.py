import json

def run(root,output):
    source=json.loads((root/"fixtures/source-evidence.json").read_text())
    assert source["cases"]==8 and source["baseline_unsafe_allows"]==6 and source["corrected_unsafe_allows"]==0
    body=(root/"contributions/001-authorization-investment.md").read_text()
    return {"scope":"executive document and linked owned-lab source-evidence review only; no financial/customer outcomes or new technical experiment","document_words":len(body.split()),"linked_lab_case_count":source["cases"],"source_scope":source["scope"],"production_ROI_measured":False,"new_regression_tests_expected":0}
