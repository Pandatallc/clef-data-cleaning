instructions = {
    "pat_pop": {
        "OCT_DATE": {
            "format": "date",
            "string_intention": "mixed",
            "vals_to_notes": ["NO ATROPHY", "OD CONVERTS TO WET"],
        },
        "Sub-RPE 5mm OD": {"format": "numeric", "string_intention": "notes"},
        "dist_fovea_OD": {"format": "numeric", "string_intention": "blank"},
        "cst_OD": {"format": "numeric", "string_intention": "notes"},
        "Sub-RPE 5mm OS": {"format": "numeric", "string_intention": "notes"},
        "questionable_OS": {"format": "numeric", "string_intention": "blank"},
    },
    "dxafterdxdate": {
        "CURRENT_ICD9_LIST": {"format": "string", "string_intention": "split"}
    },
    "ophthafterdxdate": {
        "BUN result 30 days after Contact_DATE": {
            "format": "numeric",
            "string_intention": "blank",
        },
        "LDL result 30 days after Contact_DATE": {
            "format": "numeric",
            "string_intention": "blank",
        },
        "Glucose result 30 days after Contact_DATE": {
            "format": "numeric",
            "string_intention": "blank",
        },
        "cst_OS": {"format": "numeric", "string_intention": "blank"},
        "dist_fovea OS": {"format": "numeric", "string_intention": "blank"},
        "Sub-RPE 5mm OS": {"format": "numeric", "string_intention": "notes"},
        "dist_fovea OD": {"format": "numeric", "string_intention": "blank"},
        "Sub-RPE 5mm OD": {"format": "numeric", "string_intention": "notes"},
        "column_name": {"format": "string", "string_intention": "fix", "lookup_table": {"bad_val": "good_val"}}
    },
}
