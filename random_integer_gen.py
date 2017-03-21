import urllib2


class RandomIntGen(object):
    """
    Modified from the example code "pyrandomdotorg" and "randomwrapy" provided on random.org.

    """
    def __init__(self, emailaddr):
        self.max_num = 1e4
        self.min_num = 1
        self.num_min = -1e9
        self.num_max = 1e9
        self.min_col = 1
        self.max_col = 1e9
        self.base = [2, 8, 10, 16]
        self.email = emailaddr

    def generate(self, num, nmin, nmax, col=1, base=10, rnd="new", ipaddr=None):
        if self.QuotaChecker(ipaddr) < 0:
            raise Exception("Quota of %s has run out." % ipaddr)
        if num < self.min_num or num > self.max_num:
            raise Exception("Too many or too few Ints requested.")
        if nmin < self.num_min:
            raise Exception("The requested int is less than the lower bound.")
        if nmax > self.num_max:
            raise Exception("The requested int exceeds the upper bound.")
        if nmin > nmax:
            raise Exception("Wrong positioning of num_min and num_max.")
        if col < self.min_col or col > self.max_col:
            raise Exception("Too many or too few columns requested")
        if base not in self.base:
            raise Exception("Wrong number base.")

        url = "http://www.random.org/integers/?num=%d&min=%d&max=%d&col=%d&base=%d&format=plain&rnd=%s" \
            % (num, nmin, nmax, col, base, rnd)
        req = urllib2.Request(url)
        req.add_header('User-Agent', self.email)
        opener = urllib2.build_opener()
        u = opener.open(req)
        return [int(i) for i in u.readlines()]

    def QuotaChecker(self, ipaddr=None):
        url = "http://www.random.org/quota/?format=plain"
        url += "&ip=" + ipaddr if ipaddr else ""
        req = urllib2.Request(url)
        req.add_header('User-Agent', self.email)
        opener = urllib2.build_opener()
        u = opener.open(req)
        return u.readlines()

if __name__ == "__main__":
    randomInt = RandomIntGen("myemail@gmail.com").generate(1, 1, 1e9, 1, 10)
    print(randomInt)
