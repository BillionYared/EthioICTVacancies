from __future__ import annotations

import os

SEARCH_QUERIES = [
    'ICT intern Ethiopia',
    'IT support intern Addis Ababa',
    'network support intern Ethiopia',
    'systems administration intern Ethiopia',
    'infrastructure intern Addis Ababa',
    'Linux support intern Ethiopia',
    'NOC intern Ethiopia',
    'cloud support trainee Ethiopia',
    'junior system administrator Ethiopia',
    'information systems intern Ethiopia',
    'digital technology intern Ethiopia',
    'DevOps trainee Ethiopia',
    'site:careers.un.org Ethiopia ICT internship',
    'site:jobs.au.int internship ICT',
    'site:jobs.unicef.org Ethiopia ICT intern',
    'site:jobs.undp.org Ethiopia ICT intern',
    'site:ilri.org Ethiopia ICT internship',
    'site:ethiongojobs.com ICT intern Ethiopia',
    'site:unjobs.org Ethiopia ICT intern',
]

POSITIVE_TERMS = {
    'ict', 'information technology', 'it support', 'helpdesk', 'service desk',
    'network', 'networking', 'systems administrator', 'system administrator',
    'infrastructure', 'linux', 'server', 'noc', 'cloud support', 'devops',
    'information systems', 'digital technology', 'technical support',
    'cybersecurity', 'security operations', 'data center', 'datacenter',
}

ENTRY_TERMS = {
    'intern', 'internship', 'trainee', 'graduate', 'junior', 'assistant',
    'entry level', 'entry-level', 'apprentice', 'fellowship', 'volunteer',
}

SENIOR_TERMS = {
    'senior', 'lead ', 'manager', 'director', 'head of', 'principal',
    'architect', 'specialist ii', 'specialist iii', '5 years', '7 years',
    '8 years', '10 years',
}

ETHIOPIA_TERMS = {
    'ethiopia', 'addis ababa', 'hawassa', 'bahir dar', 'dire dawa',
    'adama', 'mekelle', 'gambella', 'jijiga', 'seminar',
}

PRIORITY_DOMAINS = {
    'careers.un.org', 'jobs.au.int', 'jobs.unicef.org', 'jobs.undp.org',
    'jobs.unops.org', 'ilri.org', 'iom.int', 'wfp.org', 'giz.de',
    'ethiongojobs.com', 'unjobs.org', 'reliefweb.int', 'ethiojobs.net',
    'linkedin.com', 'afriworket.com',
}

MAX_RESULTS_PER_QUERY = int(os.getenv('MAX_RESULTS_PER_QUERY', '8'))
MAX_ALERTS_PER_RUN = int(os.getenv('MAX_ALERTS_PER_RUN', '12'))
