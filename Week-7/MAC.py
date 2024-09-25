"""MAC"""
def check_mac_address(mac):
    """burger king"""
    if len(mac) != 17 and len(mac) != 14:
        return "ERROR"
    parts = mac.split('-') if '-' in mac else mac.split(':') if ':' in mac else mac.split('.')
    if len(parts) == 6 and all(len(part) == 2 for part in parts):
        if '-' in mac:
            return "VALID 1" if all(c in '0123456789ABCDEFabcdef' for c in mac.replace('-', '')) \
                else "ERROR"
        if ':' in mac:
            return "VALID 2" if all(c in '0123456789ABCDEFabcdef' for c in mac.replace(':', '')) \
                else "ERROR"
    elif len(parts) == 3 and all(len(part) == 4 for part in parts):
        return "VALID 3" if all(c in '0123456789ABCDEFabcdef' for c in mac.replace('.', '')) \
            else "ERROR"
    return "ERROR"
mac_address = input().strip()
RESULT = check_mac_address(mac_address)
print(RESULT)
