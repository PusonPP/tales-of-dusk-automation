---
artifact_id: QAR-XXXX
artifact_type: qa_report
version: 1.0.0
status: draft
project_id: tales-of-dusk-automation
workflow_thread_id: <thread-id>
author_role: QAValidator
created_at: <UTC ISO 8601 timestamp>
updated_at: <UTC ISO 8601 timestamp>
supersedes: null
related_artifacts:
  - <CTX-XXXX>
---

# QA Report: <qa-report-title>

## Based On

- <Artifact ID and short description>

## Build Under Test

- Build / Commit / Branch: <identifier>
- Runtime Target: <local run / exported build / test harness / etc.>

## Scenarios Tested

### Scenario 1
- Scenario ID: <SCN-001>
- Name: <scenario name>
- Passed: <true|false>
- Notes: <notes>

### Scenario 2
- Scenario ID: <SCN-002>
- Name: <scenario name>
- Passed: <true|false>
- Notes: <notes>

### Scenario 3
- Scenario ID: <SCN-003>
- Name: <scenario name>
- Passed: <true|false>
- Notes: <notes>

## Passes

- <What passed>
- <What passed>
- <What passed>

## Failures

### Failure 1
- Finding ID: <FAIL-001>
- Severity: <low|medium|high|critical>
- Blocking: <true|false>
- Title: <short title>
- Description: <full description>
- Repro Steps: <how to reproduce>

### Failure 2
- Finding ID: <FAIL-002>
- Severity: <low|medium|high|critical>
- Blocking: <true|false>
- Title: <short title>
- Description: <full description>
- Repro Steps: <how to reproduce>

## Regression Notes

- <Regression note 1>
- <Regression note 2>

## QA Summary

<One short paragraph summarizing whether the implementation is ready for acceptance, needs rework, or reveals upstream spec issues.>