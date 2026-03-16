from transformers import pipeline

verifier = pipeline(
    "text-classification",
    model="facebook/bart-large-mnli"
)

def verify_claim(claim, evidence):

    result = verifier({
        "text": evidence,
        "text_pair": claim
    })

    # handle both dict and list outputs
    if isinstance(result, list):
        label = result[0]["label"]
    else:
        label = result["label"]

    return label