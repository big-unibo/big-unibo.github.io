---
title: "Precision watering"
layout: textlay
excerpt: "Method and system for soil-moisture monitoring"
sitemap: false
permalink: /watering/
---

# Method and system for soil-moisture monitoring 

Precision farming is a management approach that focuses on (near real-time) observation, measurement, and responses to variability in crops, and fields. 
The main advantages of precision farming are greater efficiency and greater predictability, higher profit margins, soil monitoring, and higher yield.

Current technologies make it possible to assess both the quantity and quality of soil and plants, along with the use of advanced tools to monitor the soil
We need operative solutions able to assess soil-moisture conditions and optimize water resources

Empirical results show that our system:

1. Reduces the usage of water and fertilizers when necessary
2. Reduces the risk of plant asphyxiation
3. Improves the quality and quantity of the harvest
4. Can control water stress

<video width="540" height="310" controls>
  <source src="https://big.csr.unibo.it/resources/watering/video-en.mp4" type="video/mp4">
</video>

## Description

We implement a smart irrigation system capable of maintaining optimal humidity conditions.
In particular, our system:

- Is independent of the soil features (no need for texture analysis) 
- Does not require cold-start training steps (working from day 0)
- Is customizable based on crops and phenological states

![image](https://github.com/big-unibo/big-unibo.github.io/assets/18005592/47ca6610-032d-4ac8-b887-cc8bd0696186)

Our system consists of a 2D (or 3D) sensor grid to detect quantitative soil features (e.g., humidity) with a limited number of sensors.

![image](https://github.com/big-unibo/big-unibo.github.io/assets/18005592/0eb430be-499b-47b2-8515-831448856de0)

Given the sensor data, achieving a soil profile with a precision level in the order of centimeters requires the use of a mapping function to estimate humidity in sensorless spots. 
The profiling function can be implemented with a machine learning algorithm based on neural networks.

We provide two main profiling functions:

- Soil Feature Unaware (SFU): exploiting sensor measurement only. 
- Soil Feature Aware (SFA): exploiting hydrological flux data to consider non-linearities and obtain a more precise estimation.

![image](https://github.com/w4bo/img-dump/assets/18005592/a04abc29-e26e-4b8d-b4ca-4130c06cb396)

The ideal humidity profile is defined by agricultural technicians in the form of a moisture matrix that can be adapted to the irrigation system.

| Single wing | | Double wing |
|-|-|-|
| ![image](https://github.com/w4bo/img-dump/assets/18005592/c62628a9-2739-49b2-b8a2-3b912430e472) | | ![image](https://github.com/w4bo/img-dump/assets/18005592/d16f2cf2-aab1-4c21-ad18-5bb5ea66bf6b) |

Then, the system modulates irrigation to achieve the desired profile.

| Single wing | | Double wing |
|-|-|-|
| ![image](https://github.com/w4bo/img-dump/assets/18005592/4331f0c9-7f0d-4377-9ce9-060e71300c41) | | ![image](https://github.com/w4bo/img-dump/assets/18005592/f69e04d9-155c-493f-a341-6fbebebcd086)|

Tests were conducted on a yellow kiwi farm in Brisighella (RA) in comparison to the farmer's previous performances.

![image](https://github.com/big-unibo/big-unibo.github.io/assets/18005592/d33c848f-5fb0-480e-a7f1-85e05692a19b)

Empirical results show that the system:

- creates 2D and 3D moisture profiles of the field with a level of detail in cubic meters and centimeters
- enables a 40% reduction in irrigation water usage
- reduced fertilizer costs due to decreased soil depletion
- improves the quality and size of the fruits

![image](https://github.com/big-unibo/big-unibo.github.io/assets/18005592/3fa887dc-8160-4c66-ab9b-e9881f880ab3)


## Patented technology

The system is protected by the Patent Cooperation Treaty (PCT/IB2022/058461) from September 8, 2022.

- Title: "Method and system for soil-moisture monitoring" ("Metodo e sistema per il monitoraggio dell'umidità del suolo"), registered as October 18th 2023 N. 102021000023162.
- Owner: Alma Mater Studiorum – Università di Bologna

Research team:

- Matteo Golfarelli, DISI --- University of Bologna
- Matteo Francia, DISI --- University of Bologna
- Enrico Gallinucci, DISI --- University of Bologna
- Joseph Giovanelli, DISI --- University of Bologna

## Contacts 

- Laura Camanzi (laura.camanzi3@unibo.it)
- Andrea Germani (andrea.germani4@unibo.it)
- Alma Mater Studiorum – Università di Bologna, Knowledge Transfer Office – Innovation Area (kto@unibo.it)
