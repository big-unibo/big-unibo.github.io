---
title: "BIG - Multistore"
layout: textlay
excerpt: "BIG -- Multistore"
sitemap: false
permalink: /multistore/
---

# Multistore

<!--<p><strong>FULL DOCUMENTATION</strong>: <a href="sabine-readme">sabine-readme</a>
</p>-->

<p>The success of NoSQL DBMSs has pushed the adoption of polyglot storage systems that take advantage of the best characteristics of different technologies and data models. While operational applications take great benefit from this choice, analytical applications suffer the absence of schema consistency, not only between different DBMSs but within a single NoSQL system as well.</p>

<img src="/images/projects/multistore/intro-example.png" width="400px"  />

<p>In this context, the discipline of data science is steering analysts away from traditional data warehousing and towards a more flexible and lightweight approach to data analysis. The idea is to perform OLAP analyses in a <i>pay-as-you-go</i> manner across heterogeneous schemas and data models, where the integration is progressively carried out by the user as the available data is explored.</p>

<p>We propose an approach to support data analysis within a <strong>high-variety multistore</strong>, with heterogeneous schemas and overlapping records. Multistores are data management systems that enable query processing across different and heterogeneous databases; besides the distribution of data, complexity factors like schema heterogeneity and data replication must be resolved through integration and data fusion activities. The multistore solution that we have developed relies on a dataspace to provide the user with an integrated view of the available data.</p>

<img src="/images/projects/multistore/overview.png" width="400px"  />

<p>Our approach supports relational, document, wide-column, and key-value data models by automatically handling both data model and schema heterogeneity through a dataspace layer on top of the underlying DBMSs. The expressiveness we enable corresponds to GPSJ queries, which are the most common class of queries in OLAP applications. We rely on Nested Relational Algebra to define a cross-database execution plan. Different strategies to carry out joins and data fusion are evaluated by means of a self-learning black-box cost model, which estimates execution times and selects the most efficient plan. The system has been prototyped on Apache Spark.</p>


## Downloads

<ul>
<li>Set of queries: <a href="/downloads/multistore/queries.csv">link</a></li>
<li>Dataset (scale factor 1): <a href="/downloads/multistore/sf1.zip">link</a></li>
<li>Dataset (scale factor 10): <a href="/downloads/multistore/sf10.zip">link</a></li>
<li>Dataset (scale factor 100): <a href="/downloads/multistore/sf100.zip">link</a></li>
</ul>

## Publications

<p>Chiara Forresi, Matteo Francia, Enrico Gallinucci, Matteo Golfarelli: <a href="https://doi.org/10.1007/s10796-022-10320-2">Cost-based optimization of multistore query plans</a>. Information Systems Frontiers (2022)</p>
<p>Chiara Forresi, Matteo Francia, Enrico Gallinucci, Matteo Golfarelli: <a href="https://doi.org/10.1007/978-3-030-82472-3_11">Optimizing Execution Plans in a Multistore</a>. ADBIS 2021: 136-151</p>
<p>Chiara Forresi, Enrico Gallinucci, Matteo Golfarelli, Hamdi Ben Hamadou: <a href="https://doi.org/10.1007/s00778-021-00682-5">A dataspace-based framework for OLAP analyses in a high-variety multistore</a>. VLDB J. 30(6): 1017-1040 (2021)</p>
<p>Hamdi Ben Hamadou, Enrico Gallinucci, Matteo Golfarelli: <a href="https://doi.org/10.1007/978-3-030-33223-5_16">Answering GPSJ Queries in a Polystore: A Dataspace-Based Approach</a>. ER 2019: 189-203</p>


<style media="screen" type="text/css">

.note {
  font-size: 0.8em;
}

.logos {
  float: left;
  width: 33%;
  height: 220px;
}

.helper {
  display: inline-block;
  height: 100%;
  vertical-align: middle;
}

img {
  vertical-align: middle;
}

.missing {
  color: red;
}

</style>
