# Security Log Analyzer

A Python-based security log analyzer that detects suspicious IP addresses based on repeated failed login attempts.

## Features

- Reads authentication logs from a file
- Detects failed login attempts
- Counts failed attempts for each IP address
- Identifies suspicious IP addresses based on a threshold
- Displays suspicious IPs and their failed attempt counts

## Technologies

- Python
- File Handling
- Lists
- Sets
- Loops and Conditions

## Purpose

This project was created to practice Python fundamentals through a basic cybersecurity log analysis scenario.

## V5 - Risk Analysis and Reporting

- Classifies suspicious IPs by risk level: MEDIUM, HIGH, and CRITICAL
- Generates a security analysis report with failed attempt counts
- Adds a report header for clearer output
- Shows the total number of suspicious IP addresses
- Saves the generated analysis to a report file
