# Security Standard

**Version:** 1.0.0  
**Effective:** 2026-05-29  
**Applies to:** All Software Factory projects

---

## 1. Purpose

This standard defines the minimum security requirements for all Software Factory projects.
Security is not a phase or a feature — it is a baseline requirement present from the first
commit to production operation.

---

## 2. Credential and Secret Management

### 2.1 No Secrets in Repositories
Credentials, API keys, passwords, tokens, private keys, or any secret material must
**never** be committed to any repository — including private repositories.

This applies to:
- Database passwords
- Odoo master passwords
- API keys for external services
- SSH private keys
- SSL/TLS certificates and private keys
- SMTP credentials
- Cloud provider access keys

### 2.2 Secret Storage
All secrets must be stored in:
- Environment variables (injected at runtime, never stored in files committed to git).
- A secret management service appropriate to the deployment environment.
- Encrypted configuration files that are explicitly excluded from version control via `.gitignore`.

### 2.3 .gitignore Requirements
Every project repository must have a `.gitignore` file that excludes:
- `.env` and all `.env.*` variants
- `*.key`, `*.pem`, `*.p12`, `*.pfx`
- `config/odoo.conf` if it contains passwords
- Any file that may contain runtime secrets

### 2.4 Secret Rotation
If a secret is accidentally committed:
1. Immediately revoke and rotate the secret — assume it is compromised.
2. Remove it from git history using appropriate tooling.
3. Log a `SECURITY` decision in `DECISION_LOG.md` recording the incident and response.
4. Notify the Software Factory lead.

---

## 3. Access Control

### 3.1 Principle of Least Privilege
Every user, role, and system account must have the minimum permissions needed to
perform its function. Excess permissions must not be granted for convenience.

### 3.2 Access Control Decisions Must Be Logged
Every significant access control decision must be recorded in `DECISION_LOG.md` with
type `SECURITY`. This includes:
- Which user groups can see which records or menus.
- Portal user access scope.
- API user permissions.
- Admin or manager role definitions.
- Any departure from default platform access control.

### 3.3 Record Rules and Domain Filters
Custom record rules and domain filters that restrict data visibility must be:
- Tested to confirm they work as intended.
- Documented in `MODULE_REGISTRY.md` if implemented as a custom component.
- Logged in `DECISION_LOG.md` if they represent a deliberate access control decision.

### 3.4 Multi-Company Access
In multi-company Odoo deployments, cross-company data access must be explicitly
designed and documented. Default multi-company isolation must not be weakened
without a logged security decision.

---

## 4. External Integrations

### 4.1 Authentication
All external integrations must use authenticated connections. Unauthenticated
integrations (e.g., open webhooks) are not permitted without a logged governance
exception.

### 4.2 TLS/HTTPS
All external API calls must use HTTPS. HTTP-only integrations are not permitted
without a logged governance exception stating the specific constraint.

### 4.3 Integration Credentials
Credentials used for external integrations must follow the secret management
rules in section 2.

### 4.4 Inbound Webhooks
Inbound webhooks must validate the source (e.g., HMAC signature, bearer token,
IP allowlist). Unsigned, unauthenticated inbound webhooks are a security defect.

---

## 5. Data Protection

### 5.1 Personal Data
Any system that handles personal data (names, contact information, national IDs,
financial data, health data) must:
- Identify the personal data fields in `MODULE_REGISTRY.md`.
- Apply appropriate access controls.
- Not expose personal data to portal users beyond what is needed.
- Consider data retention requirements.

### 5.2 Financial Data
Financial records (invoices, payments, bank accounts) must be restricted to
authorized finance users. Non-finance staff must not have write access to
financial records without a logged security decision.

### 5.3 Backups
Backup files may contain sensitive data and must be:
- Stored in access-controlled locations.
- Encrypted at rest where feasible.
- Subject to the same retention policies as live data.

---

## 6. Deployment Security

### 6.1 Server Access
Production server access (SSH, web admin) must be:
- Restricted to named individuals.
- Using key-based authentication where possible.
- Logged in the `DECISION_LOG.md` when access policy is set.

### 6.2 Odoo Admin Password
The Odoo master admin password must:
- Be a strong, randomly generated password.
- Not be the same as any other credential.
- Be stored in the secret management system.
- Never be committed to any configuration file in version control.

### 6.3 Database Access
Direct database access must be:
- Restricted to the application user and named DBAs.
- Not permitted from the application server's application user using superuser credentials.
- Logged as an access control decision.

---

## 7. Security Review in PRs

Any PR that touches authentication, authorization, access control, external APIs,
user data, or deployment configuration must include an explicit security review
section in the PR description addressing:

1. What data or access is affected by this change.
2. Whether access control has been verified.
3. Whether secrets are handled correctly.
4. Whether this change could expose data to unauthorized users.

---

*This standard is owned by the Software Factory. Changes require a PR with a security decision log entry.*
