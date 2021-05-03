class Solution(object):
    """
    1604. Alert Using Same Key-Card Three or More Times in a One Hour Period

    LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card,
    the security system saves the worker's name and the time when it was used. The system emits an alert if
    any worker uses the key-card three or more times in a one-hour period.
    You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a
    person's name and the time when their key-card was used in a single day.
    Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".
    Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in
    ascending order alphabetically.
    Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not
    considered to be within a one-hour period.
    """

    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """

        res = []

        dict = {}

        for name, time in zip(keyName, keyTime):
            hour, minute = map(int, time.split(":"))
            time_in_min = 60 * hour + minute

            if name not in dict:
                dict[name] = [time_in_min]
            else:
                dict[name].append(time_in_min)

        for name, times in dict.items():
            if self.issue_alert(times):
                res.append(name)
        
        return sorted(res)

    def issue_alert(self, times):
        n = len(times)
        times = sorted(times)
        for i in range(n-2):
            counter = 1
            while i + counter < n and times[i + counter] - times[i] <= 60:
                counter += 1

                if counter >= 3:
                    return True
        return False


    
sol = Solution()
print(sol.alertNames(["john","john","john"], ["23:58","23:59","00:01"]))
