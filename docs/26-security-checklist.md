# Security Checklist

## Version 1.0

---

## Philosophy
Security is not an afterthought. Every website we build must follow basic security practices to protect both the client and their visitors.

---

## Hosting Security
- [ ] HTTPS enabled (Let's Encrypt or hosting SSL)
- [ ] Automatic HTTPS redirect (HTTP → HTTPS)
- [ ] Hosting account has strong unique password
- [ ] 2FA enabled on hosting account
- [ ] Regular automatic backups enabled

## Form Security
- [ ] Form inputs sanitized (no raw HTML/JS submission)
- [ ] CSRF protection implemented
- [ ] Rate limiting on form submissions
- [ ] Honeypot field for bot detection
- [ ] Email injection prevention
- [ ] Form submissions logged with timestamp + IP

## Third-Party Security
- [ ] Only necessary CDN scripts loaded
- [ ] All scripts loaded over HTTPS
- [ ] Analytics configured to not share data with third parties
- [ ] Google Maps API key restricted to domain
- [ ] No hardcoded API keys in frontend code

## Admin / CMS Security (if applicable)
- [ ] Unique admin URL (not /admin)
- [ ] Strong password policy
- [ ] 2FA enabled
- [ ] Session timeout configured
- [ ] Login attempts limited (rate limiting)
- [ ] Regular security updates applied

## Code Security
- [ ] No sensitive data in comments
- [ ] No exposed .env or config files
- [ ] .gitignore configured for sensitive files
- [ ] No debug/console output in production

## Maintenance Security
- [ ] Regular security scan (monthly)
- [ ] SSL certificate renewal reminder
- [ ] Domain renewal reminder
- [ ] Backup restoration test (quarterly)

## Anti-Patterns

| Anti-Pattern | Risk |
|---|---|
| Hardcoded email in form action | Spam harvesting |
| No form validation | Injection attacks |
| Shared hosting with outdated PHP | Site compromise |
| No backup | Data loss |
| Default CMS credentials | Brute force attack |
| jQuery from unknown CDN | Supply chain attack |
