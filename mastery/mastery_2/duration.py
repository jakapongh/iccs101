from __future__ import annotations

class Duration:
    def __init__(self):
        self.weeks = 0
        self.days = 0
        self.hours = 0

    def __repr__(self):
        return f'Duration(weeks={self.weeks}, days={self.days}, hours={self.hours})'

    def __str__(self):
        return f'{self.weeks} weeks {self.days} days {self.hours} hours'

    def hours_to_more_significant(self, hours) -> tuple[int, int, int]:
        weeks = hours // 168
        weeks_remainder_hours = ((hours / 168) - weeks) * 168

        # Convert hours into days
        days = weeks_remainder_hours // 24
        days_remainder_hours = ((weeks_remainder_hours / 24) - days) * 24

        weeks = round(weeks)
        days = round(days)
        hours = round(days_remainder_hours)

        return weeks, days, hours


    def extendBy(self, hours: int) -> None:
        """
        Extends the current time duration by hr hours
        May lead to days and weeks being updated as well
        """
        # Get current hour duration
        current_hours = self.toHours()

        # Hours that has been extended
        summed_hours = current_hours + hours
        weeks, days, hours = self.hours_to_more_significant(summed_hours)

        self.weeks = weeks
        self.days = days
        self.hours = hours

    def toHours(self) -> int:
        total_hours = self.hours

        # Convert weeks into hours
        total_hours += self.weeks * 168

        # Convert days into hours
        total_hours += self.days * 24

        return total_hours

    def isShorterThan(self, other: Duration) -> bool:
        """
        Returns true if current duration shorter than other duration
        """
        return self.toHours() < other.toHours()


if __name__ == '__main__':
    a = Duration()
    a.extendBy(25)
    assert (a.weeks == 0 and a.days == 1 and a.hours == 1)
    a.extendBy(24)
    assert (a.weeks == 0 and a.days == 2 and a.hours == 1)
    a.extendBy(7 * 24)
    assert (a.weeks == 1 and a.days == 2 and a.hours == 1)

    b = Duration()
    b.extendBy(2 * 7 * 24 + 3)
    assert (b.weeks == 2 and b.days == 0 and b.hours == 3)
    b.extendBy(74)
    assert (b.weeks == 2 and b.days == 3 and b.hours == 5)
    assert b.isShorterThan(a) is False
    assert b.isShorterThan(b) is False
    assert a.isShorterThan(b) is True

    """
    Provided test cases
    """
    ### duration ###
    eoyfmln = Duration()
    qdrycoi = Duration()
    bvugkhj = Duration()
    eoyfmln.extendBy(145)
    assert (eoyfmln.weeks == 0 and eoyfmln.days == 6 and eoyfmln.hours == 1)
    assert (eoyfmln.isShorterThan(eoyfmln) == False)
    qdrycoi.extendBy(642)
    assert (qdrycoi.weeks == 3 and qdrycoi.days == 5 and qdrycoi.hours == 18)
    assert (qdrycoi.isShorterThan(qdrycoi) == False)
    eoyfmln.extendBy(980)
    assert (eoyfmln.weeks == 6 and eoyfmln.days == 4 and eoyfmln.hours == 21)
    assert (qdrycoi.isShorterThan(eoyfmln) == True)
    qdrycoi.extendBy(165)
    assert (qdrycoi.weeks == 4 and qdrycoi.days == 5 and qdrycoi.hours == 15)
    assert (qdrycoi.isShorterThan(qdrycoi) == False)
    bvugkhj.extendBy(185)
    assert (bvugkhj.weeks == 1 and bvugkhj.days == 0 and bvugkhj.hours == 17)
    assert (eoyfmln.isShorterThan(bvugkhj) == False)
    qdrycoi.extendBy(793)
    assert (qdrycoi.weeks == 9 and qdrycoi.days == 3 and qdrycoi.hours == 16)
    assert (qdrycoi.isShorterThan(eoyfmln) == False)
    eoyfmln.extendBy(172)
    assert (eoyfmln.weeks == 7 and eoyfmln.days == 5 and eoyfmln.hours == 1)
    assert (eoyfmln.isShorterThan(eoyfmln) == False)
    bvugkhj.extendBy(994)
    assert (bvugkhj.weeks == 7 and bvugkhj.days == 0 and bvugkhj.hours == 3)
    assert (eoyfmln.isShorterThan(bvugkhj) == False)
    bvugkhj.extendBy(130)
    assert (bvugkhj.weeks == 7 and bvugkhj.days == 5 and bvugkhj.hours == 13)
    assert (bvugkhj.isShorterThan(qdrycoi) == True)
    eoyfmln.extendBy(254)
    assert (eoyfmln.weeks == 9 and eoyfmln.days == 1 and eoyfmln.hours == 15)
    assert (eoyfmln.isShorterThan(bvugkhj) == False)
    bvugkhj.extendBy(297)
    assert (bvugkhj.weeks == 9 and bvugkhj.days == 3 and bvugkhj.hours == 22)
    assert (bvugkhj.isShorterThan(bvugkhj) == False)
    qdrycoi.extendBy(699)
    assert (qdrycoi.weeks == 13 and qdrycoi.days == 4 and qdrycoi.hours == 19)
    assert (bvugkhj.isShorterThan(qdrycoi) == True)
    qdrycoi.extendBy(412)
    assert (qdrycoi.weeks == 16 and qdrycoi.days == 0 and qdrycoi.hours == 23)
    assert (qdrycoi.isShorterThan(qdrycoi) == False)
    eoyfmln.extendBy(668)
    assert (eoyfmln.weeks == 13 and eoyfmln.days == 1 and eoyfmln.hours == 11)
    assert (qdrycoi.isShorterThan(eoyfmln) == False)
    eoyfmln.extendBy(732)
    assert (eoyfmln.weeks == 17 and eoyfmln.days == 3 and eoyfmln.hours == 23)
    assert (bvugkhj.isShorterThan(eoyfmln) == True)
