# Libra_PBE_B3LYP
# **Understanding B3LYP-TDDFT Limitations in Libra**

## **Overview**
This repository focuses on analyzing the behavior of **B3LYP-TDDFT** calculations in the **Libra library**, specifically examining **step2** and **step3** of the computational workflow. Comparative results from **PBE-TDDFT** are also included to highlight key differences.

---

## **Purpose**
The primary goal is to address two critical issues observed when using **B3LYP-TDDFT** in Libra:
1. **St Matrix Failure:** Inaccuracies arise in the computation of **St matrices** within many-body formalism.
2. **Zero NAC Values:** Non-Adiabatic Coupling (NAC) terms become zero in many-body calculations, affecting the reliability of the results.

These problems hinder the effective use of **B3LYP-TDDFT** in nonadiabatic molecular dynamics simulations.

---

## **Workflow**
The repository focuses on two key steps:
- **Step2:** Computation of time-overlap matrices, KS energy information, and NAC terms.
- **Step3:** Construction of **Slater Determinant (SD)** basis states and generation of **H_vib_sd** and **St_sd** matrices.

Results from both **PBE-TDDFT** and **B3LYP-TDDFT** are compared to identify inconsistencies.

---

## **Objective**
- Diagnose the root cause of **St matrix failures** and **zero NAC values** in B3LYP-TDDFT calculations.
- Compare these results with **PBE-TDDFT** calculations to highlight discrepancies.
- Propose solutions or alternatives for overcoming these limitations in Libra.

---

## **Usage**
1. Clone this repository:
    ```bash
    git clone https://github.com/Pulokesh/Useful_Scripts.git
    cd Useful_Scripts
    ```
2. Follow the step2 and step3 workflows to reproduce the results.
3. Compare PBE and B3LYP outputs to analyze the observed issues.

---

## **Future Directions**
- Detailed comparative analysis reports.
- Suggested fixes or workarounds for Libra's handling of **B3LYP-TDDFT**.
- Additional test cases and validation datasets.

