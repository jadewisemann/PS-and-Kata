# Linear Sieve

> also called, Sieve of Euler.
> but acronym of sieve of euler is same with sieve of eratosthenes as SOE.
> So, It called as Linear Sieve more often, from the time complexity of its.

에라스토테네스의 체(Sieve of Eratosthenes, 이하 **SoE**)와 동일한 방식이다.
다만 SoE의 경우 중복해서 판별하는 경우가 있다.
6의 경우만 해도, 2의 배수로 걸러지고, 3의 배수로 두번 걸러진다.
합성수의 경우, `소인수 - 2(1과 자시자신)`번 만큼 걸러진다.
시간 복잡도는 $O(NloglogN)$ 이다.

오일레의 체는 SoE에서 중복을 제거하여, **모든수를 딱 한번만 판정**하도록 최적화 하였다.
때문에 시간복잡도는 $O(N)$ 이 된다.
