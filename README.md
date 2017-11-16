# Benchmark of URL libraries for Python

Libraries in this benchmark:

* [furl]
* [yarl]
* [URLObject]
* [url-py]

Also, [purl] library was excluded due to not properly supported Unicode URLs.

Results was measured with [pytest-benchmark] plugin on the following host:

* Mac OS Sierra 10.12.6
* MacBook Pro (Retina, 13-inch, Early 2015)
* 2,7 GHz Intel Core i5
* 16 GB 1867 MHz DDR3

[pytest-benchmark] preset:

```
timer=time.perf_counter
disable_gc=False
min_rounds=5
min_time=1
max_time=1.0
calibration_precision=10
warmup=False
warmup_iterations=100000
```

## Installation

*Note: [pipenv] should be already installed in your environment.*

```bash
$ git clone https://github.com/vovanbo/python-urls-benchmark.git
$ cd python-urls-benchmark
$ pipenv install
```

## Usage

```bash
$ ./test_performance.py
```

## Results

* [Creation of simple URLs](https://vovanbo.github.io/python-urls-benchmark/benchmark-Creation_of_simple_URL.svg)
* [Creation of non-ASCII URLs](https://vovanbo.github.io/python-urls-benchmark/benchmark-Creation_of_non-ASCII_URL.svg)
* [Conversion of URL to string](https://vovanbo.github.io/python-urls-benchmark/benchmark-Conversion_of_URL_to_string.svg)

[furl]: https://github.com/gruns/furl
[yarl]: https://github.com/aio-libs/yarl
[URLObject]: https://github.com/zacharyvoase/urlobject
[url-py]: https://github.com/seomoz/url-py
[purl]: https://github.com/codeinthehole/purl
[pytest-benchmark]: http://pytest-benchmark.readthedocs.io/en/stable/index.html
[pipenv]: https://docs.pipenv.org