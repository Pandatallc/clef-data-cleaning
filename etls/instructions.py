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
        "Chronic kidney disease ICD9Code before FirstDXDate": {
            "format": "string",
            "string_intention": "split",
        },
        "Chronic kidney disease ICD10Code before FirstDXDate": {
            "format": "string",
            "string_intention": "split",
        },
        "Hyperlipidemia ICD9Code before FirstDXDated": {
            "format": "string",
            "string_intention": "split",
        },
        "Hyperlipidemia ICD10Code before FirstDXDate": {
            "format": "string",
            "string_intention": "split",
        },
        "Hypertension ICD9Code before FirstDXDate": {
            "format": "string",
            "string_intention": "split",
        },
        "Hypertension ICD10Code before FirstDXDate": {
            "format": "string",
            "string_intention": "split",
        },
        "VA_Right_Distance_SC": {
            "format": "string",
            "string_intention": "map",
            "args": {
                "sheet_name": "PAT_POP_VA_Right_Distance_SC",
                "str_head": 3,
                "str_tail": 61,
                "str_cols": "A:C",
            },
        },
        "VA_Left_Distance_SC": {
            "format": "string",
            "string_intention": "map",
            "args": {
                "sheet_name": "PAT_POP_VA_Left_Distance_SC",
                "str_head": 3,
                "str_tail": 61,
                "str_cols": "A:C",
            },
        },
        "VA_Right_Distance_CC": {
            "format": "string",
            "string_intention": "map",
            "args": {
                "sheet_name": "PAT_POP_VA_Right_Distance_CC",
                "str_head": 3,
                "str_tail": 87,
                "str_cols": "A:C",
            },
        },
        "VA_Left_Distance_CC": {
            "format": "string",
            "string_intention": "map",
            "args": {
                "sheet_name": "PAT_POP_VA_Left_Distance_CC",
                "str_head": 3,
                "str_tail": 108,
                "str_cols": "A:C",
            },
        },
        "VA_Right_Pressure": {"format": "numeric", "string_intention": "blank"},
        "VA_Left_Pressure": {"format": "numeric", "string_intention": "blank"},
        "C-reactive protein result 30 days after FirstDxDate": {
            "format": "string",
            "string_intention": "impute",
            "args": {
                "sheet_name": "PAT_POP_C-reactive protein resu",
                "str_head": 3,
                "str_tail": 19,
                "str_cols": "A:D",
            },
        },
        "Chloride result 30 days after FirstDxDate": {
            "format": "numeric",
            "string_intention": "blank",
        },  # we are double checking
        "Estimated GFR result 30 days after FirstDxDate": {
            "format": "string",
            "string_intention": "impute",
            "args": {
                "sheet_name": "PAT_POP_Estimated GFR result 30",
                "str_head": 3,
                "str_tail": 42,
                "str_cols": "A:D",
            },
        },  # impute
        "Glucose result 30 days after FirstDxDate": {
            "format": "numeric",
            "string_intention": "blank",
        },
        "Potassium result 30 days after FirstDxDate": {
            "format": "numeric",
            "string_intention": "blank",
        },
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
            "format": "string",
            "string_intention": "impute",
            "args": {
                "sheet_name": "ophth after DXDate_21",
                "str_head": 31,
                "str_tail": 31,
                "str_cols": "A:D",
            },
        },
        "Serum Creatinine result 30 days after Contact_DATE": {
            "format": "numeric",
            "string_intention": "blank",
        },
        "Estimated GFR result 30 days after Contact_DATE": {
            "format": "string",
            "string_intention": "impute",
            "args": {
                "sheet_name": "ophth after DXDate_20",
                "str_head": 31,
                "str_tail": 9,
                "str_cols": "A:D",
            },
        },
        "C-reactive protein result 30 days after Contact_DATE": {
            "format": "string",
            "string_intention": "impute",
            "args": {
                "sheet_name": "ophth after DXDate_18",
                "str_head": 31,
                "str_tail": 3,
                "str_cols": "A:D",
            },
        },
        "cst_OS": {"format": "numeric", "string_intention": "blank"},
        "dist_fovea OS": {"format": "numeric", "string_intention": "blank"},
        "Sub-RPE 5mm OS": {"format": "numeric", "string_intention": "notes"},
        "dist_fovea OD": {"format": "numeric", "string_intention": "blank"},
        "Sub-RPE 5mm OD": {"format": "numeric", "string_intention": "notes"},
        "Hemoglobin a1c result 30 days after Contact_DATE": {
            "format": "numeric",
            "string_intention": "blank",
        },
        "Chloride result 30 days after Contact_DATE": {
            "format": "numeric",
            "string_intention": "map",
            "args": {
                "sheet_name": "ophth after DXDate_19",
                "str_head": 31,
                "str_tail": 3,
                "str_cols": "A:C",
            },
        },
        "Potassium result 30 days after Contact_DATE": {
            "format": "numeric",
            "string_intention": "map",
            "args": {
                "sheet_name": "ophth after DXDate_24",
                "str_head": 31,
                "str_tail": 7,
                "str_cols": "A:C",
            },
        },
        "Sodium result 30 days after Contact_DATE": {
            "format": "numeric",
            "string_intention": "map",
            "args": {
                "sheet_name": "ophth after DXDate_26",
                "str_head": 31,
                "str_tail": 4,
                "str_cols": "A:C",
            },
        },
        "VA_Left_Distance_CC": {
            "format": "string",
            "string_intention": "map",
            "args": {
                "sheet_name": "ophth after DXDate_14",
                "num_head": 15,
                "num_tail": 16,
                "num_cols": "A:C",
                "str_head": 39,
                "str_tail": 1045,
                "str_cols": "A:C",
            },
        },
        "VA_Right_Distance_SC": {
            "format": "string",
            "string_intention": "map",
            "args": {
                "sheet_name": "ophth after DXDate_11",
                "num_head": 15,
                "num_tail": 4,
                "num_cols": "A:C",
                "str_head": 30,
                "str_tail": 566,
                "str_cols": "A:C",
            },
        },
        "VA_Left_Distance_SC": {
            "format": "string",
            "string_intention": "map",
            "args": {
                "sheet_name": "ophth after DXDate_12",
                "num_head": 15,
                "num_tail": 3,
                "num_cols": "A:C",
                "str_head": 31,
                "str_tail": 659,
                "str_cols": "A:C",
            },
        },
        "VA_Right_Distance_CC": {
            "format": "string",
            "string_intention": "map",
            "args": {
                "sheet_name": "ophth after DXDate_13",
                "num_head": 15,
                "num_tail": 18,
                "num_cols": "A:C",
                "str_head": 41,
                "str_tail": 891,
                "str_cols": "A:C",
            },
        },
        "VA_Right_Pressure": {
            "format": "numeric",
            "string_intention": "map",
            "args": {
                "sheet_name": "ophth after DXDate_15",
                "str_head": 31,
                "str_tail": 37,
                "str_cols": "A:C",
            },
        },
        "VA_Left_Pressure": {
            "format": "numeric",
            "string_intention": "map",
            "args": {
                "sheet_name": "ophth after DXDate_16",
                "str_head": 31,
                "str_tail": 40,
                "str_cols": "A:C",
            },
        },
    },
    "alldxatfirstdxdate": {
        "CURRENT_ICD9_LIST": {"format": "string", "string_intention": "split"},
        "CURRENT_ICD10_LIST": {"format": "string", "string_intention": "split"},
    },
}
