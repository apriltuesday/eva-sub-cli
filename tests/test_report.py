# Function to generate HTML report from validation results
import os
from unittest import TestCase

from cli.report import generate_html_report
validation_results = {
    "assembly_check": {
        "input_passed.vcf": {
            "error_list": [],
            "match": 247,
            "mismatch_list": [],
            "nb_error": 0,
            "nb_mismatch": 0,
            "total": 247,
        },
        "input_fail.vcf": {
            "error_list": [],
            "match": 26,
            "mismatch_list": [
                "Chromosome 1, position 35549, reference allele 'G' does not match the reference sequence, expected 'c'",
                "Chromosome 1, position 35595, reference allele 'G' does not match the reference sequence, expected 'a'",
                "Chromosome 1, position 35618, reference allele 'G' does not match the reference sequence, expected 'c'",
                "Chromosome 1, position 35626, reference allele 'A' does not match the reference sequence, expected 'g'",
                "Chromosome 1, position 35639, reference allele 'T' does not match the reference sequence, expected 'c'",
                "Chromosome 1, position 35643, reference allele 'T' does not match the reference sequence, expected 'g'",
                "Chromosome 1, position 35717, reference allele 'T' does not match the reference sequence, expected 'g'",
                "Chromosome 1, position 35819, reference allele 'T' does not match the reference sequence, expected 'a'",
                "Chromosome 1, position 35822, reference allele 'T' does not match the reference sequence, expected 'c'",
            ],
            "nb_error": 0,
            "nb_mismatch": 10,
            "total": 36,
        },
    },
    "vcf_check": {
        "input_passed.vcf": {
            "error_count": 0,
            "error_list": [],
            "valid": True,
            "warning_count": 0,
        },
        "input_fail.vcf": {
            "critical_count": 1,
            "critical_list": ["Line 4: Error in meta-data section."],
            "error_count": 1,
            "error_list": ["Sample #11, field AD does not match the meta specification Number=R (expected 2 value(s)). AD=.."],
            "valid": False,
            "warning_count": 0,
        },
    },
    "sample_check": {
        'overall_differences': True,
        'results_per_analysis': {
            'AA': {
                'difference': True,
                'more_metadata_submitted_files': ['Sample1'],
                'more_per_submitted_files_metadata': {},
                'more_submitted_files_metadata': ['1Sample']
            }
        }
    },
    'metadata_check': {'json_errors': [
        {'property': '.files', 'description': "should have required property 'files'"},
        {'property': '/project.title', 'description': "should have required property 'title'"},
        {'property': '/project.description', 'description': "should have required property 'description'"},
        {'property': '/project.taxId', 'description': "should have required property 'taxId'"},
        {'property': '/project.centre', 'description': "should have required property 'centre'"},
        {'property': '/analysis/0.analysisTitle', 'description': "should have required property 'analysisTitle'"},
        {'property': '/analysis/0.description', 'description': "should have required property 'description'"},
        {'property': '/analysis/0.experimentType', 'description': "should have required property 'experimentType'"},
        {'property': '/analysis/0.referenceGenome', 'description': "should have required property 'referenceGenome'"},
        {'property': '/sample/0.bioSampleAccession', 'description': "should have required property 'bioSampleAccession'"},
        {'property': '/sample/0.bioSampleObject', 'description': "should have required property 'bioSampleObject'"},
        {'property': '/sample/0', 'description': 'should match exactly one schema in oneOf'}
    ]}
}


class TestReport(TestCase):
    resource_dir = os.path.join(os.path.dirname(__file__), 'resources')
    expected_report = os.path.join(resource_dir, 'validation_reports', 'expected_report.html')

    def test_generate_html_report(self):
        report = generate_html_report(validation_results)
        with open(self.expected_report) as open_html:
            assert report == open_html.read()

