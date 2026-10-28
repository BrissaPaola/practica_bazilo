Hanoi n src dst aux |:
    if n > 0 |:
        Hanoi (n - 1) src aux dst
        note <- src[#src]
        8< src[#src]
        dst << note
        (:) note
        Hanoi (n - 1) aux dst src
    :|
:|

Main |:
    ori <- {C D E F G}
    dst <- {}
    aux <- {}
    Hanoi 5 ori dst aux
:|