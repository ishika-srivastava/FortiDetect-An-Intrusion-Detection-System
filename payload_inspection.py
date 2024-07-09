import re
def isSuspiciousPayload(payload):
    # regex pttern to detect SQLI
    sqlInjectionPattern = re.compiler(r"(\%27)|(\')|(\-\-)|(\%23)|(#)")

    # regex pattern to detect XSS Attacks
    xssPattern = re.compile(r"(<script>.*<\/script>)")

    if (sqlInjectionPattern.search(payload) or xssPattern.search(payload)):
        return True
    return False