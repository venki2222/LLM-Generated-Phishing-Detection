# LLM-Generated Phishing Email Detection Using Machine Learning

**Student:** Mungara Venkateshwara Rao  
**USN:** 23BTRCO021

## Objective
Evaluate machine-learning detection of LLM-generated phishing emails using the 17 stylometric/linguistic features in the selected 2026 research dataset.

## Dataset
Cross-model evaluation of phishing detectors against LLM-generated emails.

- 9,986 phishing emails
- 5,000 human-written
- 4,986 LLM-generated
- LLM sources: GPT-4.1, DeepSeek 3.2, LLaMA 3.3 70B
- 17 stylometric/linguistic features

Source: Zenodo DOI 10.5281/zenodo.20250116

## Models
- Logistic Regression
- XGBoost

## Experiments
The implementation reproduces the supplied research pipeline's main evaluations:
- Task A: 5-fold intra-model evaluation
- Task B: cross-model transferability
- Task B': threshold-recalibrated cross-model evaluation
- Task C: cross-dataset human verification
- Task D: aggregated-pool detector
- SHAP feature importance

## Reproduction
1. Install Python 3.11 or a compatible Python version.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Put `corpus_features.csv` at `data/corpus_features.csv`.
4. Run:
   `python src/run_experiment.py`

## Results
The `results/` folder contains the actual outputs generated during this implementation, including CSV metrics and figures.

## Research comparison
The original supplied repository reports:
- XGBoost intra-model F1 around 0.955–0.968
- default-threshold cross-model transferability gap around 28.1 percentage points
- recalibration reducing the gap to about 4 percentage points
- pooled detector F1 around 0.997

This implementation was executed independently using the supplied dataset and methodology. Small numerical differences can occur because of software/library versions and execution environment.

## References
Gutierrez, R., Villegas-Ch, W., & Govea, J. (2026). Cross-model evaluation of phishing detectors against LLM-generated emails.

Zenodo dataset: 10.5281/zenodo.20250116
