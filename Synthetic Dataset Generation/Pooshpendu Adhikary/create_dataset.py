#!/usr/bin/env python
from SyntheticDataGenerator import SyntheticDataGenerator

sdg = SyntheticDataGenerator("E:/ASU/CSE-576/Project/synthetic-dataset-creation/train.tsv", "E:/synthetic_data.csv");

sdg.create_synthetic_data();