def https_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found!"
        case 500:
            return "Internal Server ERORR"
        case _:
            return "UnKnown Status"

print(https_status(200)) # OK
print(https_status(404)) # Not Found!
print(https_status(500)) # Internal Server ERORR
print(https_status(505)) # UnKnown Status
