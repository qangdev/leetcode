
def isBadVersion(n, bad_vers):
    return n in bad_vers


def first_bad_version(n, bad_vers):
    # Make a list of version for given n value
    vers = range(1, n+1)
    # Assume first bad version is the first element on the list
    fb_ver = vers[0]

    # Apply binary search to find the target
    while len(vers) > 0:
        mid = int(len(vers)/2)
        is_cur_bad = isBadVersion(n, bad_vers)
        is_prev_bad = False
        
        if len(vers) == 1:
            if is_cur_bad:
                fb_ver = vers[0]
            break
        
        try:
            is_prev_bad = isBadVersion(vers[mid-1], bad_vers)
        except IndexError:
            pass

        if is_prev_bad and is_cur_bad:
            fb_ver = vers[mid-1]
            vers = vers[0:mid]
        else:
            fb_ver = vers[mid]
            vers = vers[mid:]
    return fb_ver

