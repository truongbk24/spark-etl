# DBT project

This project is used to do the transformation from the Minio storage to different layers of the Clickhouse Analytics Platform

## Structure of the project

We splitted the project into different layer as below

### Models

In this folder will hold all the models for transformations:

- Raw: Read the data from Minio storage as view
- Datamart: Read the data from raw view and populate to table datamart

### Configuration file

- dbt_project.yml: The configuration for path and the materialized, engine for each model folders
- packages.yml: The list of the package for dbt
- profiles.yml: The target configuration for target databases




