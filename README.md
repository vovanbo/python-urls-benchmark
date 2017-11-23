# Benchmark of URL libraries for Python

Libraries in this benchmark:

* [furl]
* [yarl]
* [URLObject]
* [url-py]
* [hyperlink]

Also, [purl] and [YURL] libraries was excluded due to not properly 
supported Unicode URLs.

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
| [URLObject] | 4,639.7060 (1.0) |    5   | 10000000   |
| [url-py]    | 821.4608 (0.18)  |    5   | 1000000    |
| [yarl]      | 48.9879 (0.01)   |    5   | 100000     |
| [hyperlink] | 38.0768 (0.01)   |    5   | 100000     |
| [furl]      | 4.3951 (0.00)    |    5   | 10000      |

[Interactive SVG](https://vovanbo.github.io/python-urls-benchmark/benchmark-Creation_of_simple_URL.svg)

### Creation of non-ASCII URLs

| Library     | OPS (Kops/s)   | Rounds | Iterations |
|-------------|----------------|:------:|------------|
| [url-py]    | 723.1370 (1.0) |    5   | 1000000    |
| [hyperlink] | 47.9041 (0.07) |    5   | 100000     |
| [furl]      | 5.7790 (0.01)  |    5   | 10000      |
| [URLObject] | 4.7849 (0.01)  |    5   | 10000      |
| [yarl]      | 4.7252 (0.01)  |    5   | 10000      |

[Interactive SVG](https://vovanbo.github.io/python-urls-benchmark/benchmark-Creation_of_non-ASCII_URL.svg)

### Conversion of URL to string

| Library     | OPS (Kops/s)      | Rounds | Iterations |
|-------------|-------------------|:------:|------------|
| [URLObject] | 6,161.5267 (1.0)  |    5   | 10000000   |
| [url-py]    | 1,366.2313 (0.22) |    5   | 1390781    |
| [yarl]      | 444.8349 (0.07)   |    5   | 1000000    |
| [hyperlink] | 4.1737 (0.00)     |    5   | 10000      |
| [furl]      | 2.3741 (0.00)     |    5   | 10000      |

[Interactive SVG](https://vovanbo.github.io/python-urls-benchmark/benchmark-Conversion_of_URL_to_string.svg)

[furl]: https://github.com/gruns/furl
[yarl]: https://github.com/aio-libs/yarl
[URLObject]: https://github.com/zacharyvoase/urlobject
[url-py]: https://github.com/seomoz/url-py
[purl]: https://github.com/codeinthehole/purl
[pytest-benchmark]: http://pytest-benchmark.readthedocs.io/en/stable/index.html
[pipenv]: https://docs.pipenv.org
[hyperlink]: https://github.com/python-hyper/hyperlink
[YURL]: https://github.com/homm/yurl