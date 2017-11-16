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

### Creation of simple URLs

| Library     | OPS (Kops/s)     | Rounds | Iterations |
|-------------|------------------|:------:|------------|
| [URLObject] | 4,321.5118 (1.0) |    5   | 10000000   |
| [url-py]    | 791.4472 (0.18)  |    5   | 1000000    |
| [yarl]      | 48.9380 (0.01)   |    5   | 100000     |
| [furl]      | 4.2583 (0.00)    |    5   | 10000      |

[Interactive SVG](https://vovanbo.github.io/python-urls-benchmark/benchmark-Creation_of_simple_URL.svg)

### Creation of non-ASCII URLs

| Library     | OPS (Kops/s)   | Rounds | Iterations |
|-------------|----------------|:------:|------------|
| [url-py]    | 712.2774 (1.0) |    5   | 1000000    |
| [furl]      | 5.8039 (0.01)  |    5   | 10000      |
| [URLObject] | 4.6441 (0.01)  |    5   | 10000      |
| [yarl]      | 4.5606 (0.01)  |    5   | 10000      |

[Interactive SVG](https://vovanbo.github.io/python-urls-benchmark/benchmark-Creation_of_non-ASCII_URL.svg)

### Conversion of URL to string

| Library     | OPS (Kops/s)      | Rounds | Iterations |
|-------------|-------------------|:------:|------------|
| [URLObject] | 5,927.0871 (1.0)  |    5   | 10000000   |
| [url-py]    | 1,343.2251 (0.23) |    5   | 1363472    |
| [yarl]      | 446.4558 (0.08)   |    5   | 1000000    |
| [furl]      | 2.3551 (0.00)     |    5   | 10000      |

[Interactive SVG](https://vovanbo.github.io/python-urls-benchmark/benchmark-Conversion_of_URL_to_string.svg)

[furl]: https://github.com/gruns/furl
[yarl]: https://github.com/aio-libs/yarl
[URLObject]: https://github.com/zacharyvoase/urlobject
[url-py]: https://github.com/seomoz/url-py
[purl]: https://github.com/codeinthehole/purl
[pytest-benchmark]: http://pytest-benchmark.readthedocs.io/en/stable/index.html
[pipenv]: https://docs.pipenv.org