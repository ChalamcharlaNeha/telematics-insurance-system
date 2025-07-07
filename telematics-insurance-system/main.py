from src import collect_data, analyze_behavior, risk_score, pricing, feedback

def run_pipeline():
    data = collect_data.simulate()
    behavior = analyze_behavior.detect(data)
    score = risk_score.calculate(behavior)
    premium = pricing.adjust(score)
    tips = feedback.generate(behavior)

    print("Risk Score:", score)
    print("Adjusted Premium:", premium)
    print("Feedback:", tips)

if __name__ == "__main__":
    run_pipeline()
