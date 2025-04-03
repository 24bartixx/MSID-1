# Raport

## Data overview

# Heatmap

<img src="https://github.com/user-attachments/assets/c32f32f2-9558-4033-8e00-80d2501b7327" alt="Data heatmap" width="800">

* It is no surprise that curricular units' params in the 1st sem (credited, enrolled, evaluations, approved, grade) are correlated
* There is a high correlation between the admission grade and the previous qualification grade
* Small negative correlation between age at enrollment and grades
* Negative correlation between GDP and unemployment rate
* The inflation rate isn't significantly correlated with GDP and unemployment (surprising)

# PCA

<img src="https://github.com/user-attachments/assets/8b0bf288-86dc-4648-91af-0fcf7ac9993b" alt="PCA" width="700">

We can see that the different categories on the PCA chart are clustered
* The dropout students category appears more towards the left side of the chart
* The graduate students category appears more towards the upper and left sides of the chart
* The enrolled students category is spread across the chart but is often situated between the dropout students and graduate students categories

# Numeric statistics

![Numeric statistics](https://github.com/user-attachments/assets/ea7a104f-1c25-4b42-bdd8-475c7472bc34)

# Categorical statistics
Most common categories:
* Application mode -> 1st phase - general contingent (38.61%)
* Application order -> 2nd choice (68.40%)
* Course -> Nursing (17.31%)
* Daytime evening attendance -> Daytime (89.08%)
* Deptor -> No (88.63%)
* Displaced -> Yes (54.84%)
* Educational special needs -> No (98.85%)
* Father's occupation -> Unskilled Workers (22.83%)
* Father's qualification -> Basic Ed 1st Cycle (4th/5th) (27.33%)
* Gender -> Female (64.83%)
* International -> No (97.51%)
* Maritial status -> single (88.58%)
* Mother's occupation -> Unskilled Workers (35.65%)
* Mother's qualification -> Secondary Education (24.16%)
* Nacionality -> Portuguese (97.51%)
* Previous qualification -> Secondary education (84.02%)
* Scholarship holder -> No (75.16%)
* Target -> Graduate (49.93%)
* Tuition fees up to date -> Yes (88.07%)

## Correlation detected

### Gender

<img src="https://github.com/user-attachments/assets/82fdd504-cbe6-442d-9c67-004d1f8078e2" alt="Gender histogram" width="600">
<img src="https://github.com/user-attachments/assets/89613c23-a14d-41b0-83c1-4378eb0db0a6" alt="Gender histogram" width="600">

* More female students

### Admission and previous qualification grades

<img src="https://github.com/user-attachments/assets/ecc74a0f-d359-40c5-bcda-e51137ec2e95" alt="Admission and previous qualification grades histogram" width="1000">

* Dropout students score worse grades as an admission grade than enrolled students and graduates

<img src="https://github.com/user-attachments/assets/03529ac1-a953-4d8e-aca0-9f9f3c4945b9" alt="boxplot_admission_grade_vs_course" width="700">

* Biofuel Production Technologies students tend to score worse on admission grade for some reason...
* The best scores were from Animation and Multimedia Design students

### Age at enrollment

<img src="https://github.com/user-attachments/assets/f21e5e47-5596-4890-bc58-45f2e20ca05c" alt="Age errorploT" width="600">

<img src="https://github.com/user-attachments/assets/8df2ade1-c035-4e6a-9133-d4881674dc99" alt="Admission grade vs age regression" width="600">

* Students' admission grades get slightly worse if they get older

<img src="https://github.com/user-attachments/assets/79ac0202-4795-46ab-b100-63c30ac7553d" alt="regression params 1st vs age regression" width="600">

* The older students are, the more classes and evaluations they take, but they score worse and fail more frequently

<img src="https://github.com/user-attachments/assets/124fb07a-d0d0-4422-a476-6b88f6d7edcc" alt="Age at enrollment vs target violinplot" width="600">
<img src="https://github.com/user-attachments/assets/4ff42621-df9e-4c7e-bb7a-534fc8926df6" alt="Age at enrollment vs target boxplot" width="600">

* The older students are more likely they are to dropout
* dropout males are on average older than dropout females

<img src="https://github.com/user-attachments/assets/b2b21e4b-bc10-4df6-afef-8fe43f16736e" alt="Age at enrollment vs target boxplot" width="700">

* Most middle-aged and elderly students are from Portugal
* Brazilian, Spanish, Angolan, and Moldovan students tend to enroll later

### 1st sem


<img src="https://github.com/user-attachments/assets/53002b50-3b3e-4ca5-b8e7-73f9327f5ae7" alt="evaluations 1st sem vs target violinplot" width="600">
<img src="https://github.com/user-attachments/assets/4dd0278c-1c5a-4ca5-9315-02e098bf7783" alt="evaluations 1st sem histogram (target)" width="600">

* Students who drop out often don't take evaluations at all during 1st sem
* Students who are debtors try to take more evaluations than students without debt because of liability

<img src="https://github.com/user-attachments/assets/97bd85ee-1ab2-4616-ab24-5aebe517569a" alt="Grades 1st sem vs target violinplot (scholarships)" width="600">
<img src="https://github.com/user-attachments/assets/f24b0baf-92b3-48a2-a157-cb366b85ab23" alt="grades 1st sem vs target violinplot (deptors)" width="600">
<img src="https://github.com/user-attachments/assets/bc100be9-a255-4ee6-a046-3358e166e938" alt="grades 1st sem histogram (target)" width="600">

* Many dropouts receive terrible grades in the 1st semester
* If they are debtors or scholarship holders, they are less likely to receive such bad grades (probably they care more because of liability)

<img src="https://github.com/user-attachments/assets/21021106-1057-4066-816b-1f788ee7b62d" alt="approved 1st sem vs target violinplot (scholarship)" width="600">
<img src="https://github.com/user-attachments/assets/c08ed536-6c0e-47ff-a8b9-d6cbae182d03" alt="approved 1st sem vs target violinplot (debtor)" width="600">
<img src="https://github.com/user-attachments/assets/b764c76d-5a5e-4aea-a0be-4eaf85537b3c" alt="approved 1st sem histogram (target)" width="600">

* Most dropouts pass 0-2 units in the first semester - incredibly low number
* Most of them don't have scholarships (debt doesn't matter here)
* Graduates pass most units in the 1st semester

### Economic

<img src="https://github.com/user-attachments/assets/aad68b9e-5fe6-4869-b53b-1f1c38067204" alt="GDP and unemployment vs age regressions" width="700">

* Middle-aged and elderly students are more likely to enroll in bad times

<img src="https://github.com/user-attachments/assets/5ddfb00f-c46a-4886-8066-f184f5d0f401" alt="Grade 1st vs GDP regression" width="600">

* Growing economy -> students get better grades in the 1st semester

<img src="https://github.com/user-attachments/assets/7a926890-f904-43dd-80bd-1a03c9826fb6" alt="unemploymenet rate vs target (deptor)" width="600">
<img src="https://github.com/user-attachments/assets/730c9d2e-6889-4fee-b8df-e10e8127cbba" alt="inflation rate vs target (deptor)" width="600">
<img src="https://github.com/user-attachments/assets/6339aa27-6771-4604-acd8-f830f4d5c8c0" alt="GDP rate vs target (deptor)" width="600">

* Increasing GDP + low unemployment and inflation rates --> more students become deptors

## No correlation (weird)

### Admission grade and age don't correlate

<img src="https://github.com/user-attachments/assets/b385371c-3a20-474f-9338-22982071c5fa" alt="Admission grade vs age boxplot" width="1000">
