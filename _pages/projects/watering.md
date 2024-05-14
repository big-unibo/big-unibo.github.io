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

Precision farming market value as of 2023: USD 9.7 billion, forecasting USD 21.9 billion in 2031.

![immagine](https://github.com/big-unibo/big-unibo.github.io/assets/18005592/03b5709a-0467-43d2-95e7-39f8f9dcdbe7)

Current technologies make it possible to assess both the quantity and quality of soil and plants, along with the use of advanced tools to monitor the soil
We need operative solutions able to assess soil-moisture conditions and optimize water resources

## Description

Our goal is to implement an irrigation system capable of maintaining optimal humidity conditions.
In particular, our system:

- is independent of the soil features (no need for texture analysis) 
- does not require cold-start training steps (working from day 0)
- is customizable based on crops and phenological states

![immagine](https://github.com/big-unibo/big-unibo.github.io/assets/18005592/47ca6610-032d-4ac8-b887-cc8bd0696186)

Our system consists of a 2D and 3D sensor grid to detect quantitative soil features (e.g., humidity) with a limited number of sensors.

![immagine](https://github.com/big-unibo/big-unibo.github.io/assets/18005592/0eb430be-499b-47b2-8515-831448856de0)

Given the sensor data, the profiling of quantitative values enables the generation of a detailed profile.
Achieving precision levels (in centimeters) requires the use of a mapping function to estimate humidity in sensorless spots. 
This can be implemented in a machine learning algorithm based on a neural network to achieve a vision of humidity profiles within a specified time range.

We provide two main profiling functions:

- Soil Feature Unaware (SFU): exploiting sensor measurement only. 
- Soil Feature Aware (SFA): exploiting hydrological flux data to consider non-linearities and obtain a more precise estimation.

![immagine](https://github.com/big-unibo/big-unibo.github.io/assets/18005592/6ee8e55f-7cac-4a4b-ac78-bc4f67e41405)

The ideal humidity profile is defined by agricultural technicians in the form of a moisture matrix.

![immagine](https://github.com/big-unibo/big-unibo.github.io/assets/18005592/d263892d-1ec6-4d72-a22d-9f13e1d2192c)

The system modulates irrigation to achieve the desired profile.

![immagine](https://github.com/big-unibo/big-unibo.github.io/assets/18005592/9cdeca22-509c-4d4d-af06-328d4d035692)

Tests were conducted on a yellow kiwi farm in Brisighella (RA) in comparison to the farmer's previous performances.
Empirical results show that the system:

- creates 2D and 3D moisture profiles of the field with a level of detail in cubic meters and centimeters
- enables a 40% reduction in irrigation water usage
- reduced fertilizer costs due to decreased soil depletion
- improves the quality and size of the fruits

![immagine](https://github.com/big-unibo/big-unibo.github.io/assets/18005592/d33c848f-5fb0-480e-a7f1-85e05692a19b)

![immagine](https://github.com/big-unibo/big-unibo.github.io/assets/18005592/3fa887dc-8160-4c66-ab9b-e9881f880ab3)


## Patented technology

- Title: "Method and system for soil-moisture monitoring" ("Metodo e sistema per il monitoraggio dell'umidità del suolo"), registered as October 18th 2023 N. 102021000023162.
- Owner: Alma Mater Studiorum – Università di Bologna

The system is protected by the Patent Cooperation Treaty (PCT/IB2022/058461) from September 8, 2022.

## Contacts 

Research team:

- Matteo Golfarelli, DISI --- University of Bologna
- Matteo Francia, DISI --- University of Bologna
- Enrico Gallinucci, DISI --- University of Bologna
- Joseph Giovanelli, DISI --- University of Bologna

Contacts:

- Laura Camanzi (laura.camanzi3@unibo.it)
- Andrea Germani (andrea.germani4@unibo.it)
- Alma Mater Studiorum – Università di Bologna, Knowledge Transfer Office – Innovation Area (kto@unibo.it)
