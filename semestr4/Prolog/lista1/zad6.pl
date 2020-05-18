prime(D�, G�ra, N) :- between(D�, G�ra, N), N > 1, is_prime(N).

is_prime(X) :-  not((
                      MAX is floor(sqrt(X)),
                      between(2, MAX, N),
                      0 is mod(X, N)
                    )),
                X >= 2.
