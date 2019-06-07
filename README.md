# Ansible
Starting point of Ansible development inside GovNS

## Requirements
To run the automated tests some basic requirements are needed

* GitLab instance to run the CI/CD tests on privleged docker containers
* CI/CD runners with access to run RHEL 6/7 based containers
* Access to pull `quay.io/ansible/molecule` image

## Setup
Steps to get this running:

1. Clone this project to a new GitLab project
2. Add the following [protected CI/CD variables](https://docs.gitlab.com/ce/ci/variables/README.html#via-the-ui)

  Environment Variable | Description                                                     
  ---------------------|-----------------------------------------------------------------
  TOWER_USERNAME       | User that can trigger a project refresh on your AWX/Tower server
  TOWER_PASSWORD       | AWX/Tower user password
  TOWER_PROJECT_URL    | The AWX/Tower URL to the project that will sync this repository

## Usage
Write your tests in `molecule/default/tests` to [testinfra](https://testinfra.readthedocs.io) specs.

Confirm the CI/CD fails on the indepth test phase with the expected test failure.

Write a your custom role code in in `roles/` to satisfy your test.
