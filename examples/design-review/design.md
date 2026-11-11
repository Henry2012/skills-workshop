# Offline export design — fixture v1

This is a deliberately flawed, fictional design for a local demonstration. It contains no real system, customer, or performance data.

## 1. Decision and scope

Decision: may implementation of this prototype begin? Stage: pre-implementation.
The decision owner is the prototype maintainer. The scope is a single-user, local-only export of a supplied text file. Payments, authentication, distributed scheduling, and production rollout are excluded. All required design text is present here; there are no external dependencies or missing attachments. Review the document only, without editing or executing it.

## 2. Acceptance response

The local request handler assigns a job ID and returns status code 202 with state QUEUED after recording the request. The client must treat this 202 response as successful completion of the export and show “Export complete,” even if no output file exists yet.

## 3. Job contract

Allowed transitions are QUEUED → RUNNING → SUCCEEDED or FAILED.
SUCCEEDED means the complete output file has been flushed and atomically renamed to its final path. Before that rename, the export is not complete and the client must not show “Export complete.”
The job record is the single authority for state. A local lock allows one worker to own a job. The client polls that record until a terminal state.

## 4. Acceptance and resource limits

Acceptance tests must show that QUEUED and RUNNING never count as completed exports, SUCCEEDED has a complete final file, and FAILED preserves an error record.
Inputs are bounded to 1 MiB. The prototype copies a local supplied file; no remote capacity or performance claim is made. Standard local file operations are sufficient for the scoped design.

## 5. Failure and recovery

On an exception, record FAILED with the error and remove the temporary file.
A restart marks an unfinished RUNNING job FAILED instead of silently replaying it.
The maintainer may submit a new job after inspecting the error. There are no automatic retries.
The old final file is retained until a new file is complete. Canceling a queued job records FAILED with a cancellation reason. The prototype maintainer owns recovery.
