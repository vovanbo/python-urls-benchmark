# Benchmark of URL libraries for Python

Libraries in this benchmark:

* [furl]
* [yarl]
* [URLObject]
* [hyperlink]

Python version is **3.10.4**.

Also, [purl] and [YURL] libraries was excluded due to not properly 
supported Unicode URLs. [url-py] was excluded due to no support of Python 3.10.

Results was measured with [pytest-benchmark] plugin on the following host:

* MacBook Air (M1, 2020)
* OS: Mac OS Monterey 12.4
* Chip: Apple M1
* Memory: 16 GB

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

| Library     | OPS (Kops/s)      | Rounds | Iterations |
|-------------|-------------------|:------:|------------|
| [URLObject] | 11,634.4655 (1.0) |    5   | 11647268   |
| [yarl]      | 164.2184 (0.01)   |    5   | 165130     |
| [hyperlink] | 119.3448 (0.01)   |    5   | 120371     |
| [furl]      | 11.5602 (0.00)    |    5   | 11701      |

[Interactive SVG](https://vovanbo.github.io/python-urls-benchmark/benchmark-Creation_of_simple_URL.svg)

### Creation of non-ASCII URLs

| Library     | OPS (Kops/s)    | Rounds | Iterations |
|-------------|-----------------|:------:|------------|
| [yarl]      | 154.5179 (1.0)  |    5   | 154462     |
| [hyperlink] | 152.6398 (0.99) |    5   | 153125     |
| [URLObject] | 15.0344 (0.10)  |    5   | 15023      |
| [furl]      | 3.8075 (0.02)   |    5   | 10000      |

[Interactive SVG](https://vovanbo.github.io/python-urls-benchmark/benchmark-Creation_of_non-ASCII_URL.svg)

### Conversion of URL to string

| Library     | OPS (Kops/s)      | Rounds | Iterations |
|-------------|-------------------|:------:|------------|
| [URLObject] | 16,166.8971 (1.0) |    5   | 16181124   |
| [yarl]      | 1,413.2480 (0.09) |    5   | 1408450    |
| [hyperlink] | 15.2360 (0.00)    |    5   | 15276      |
| [furl]      | 5.0420 (0.00)     |    5   | 10000      |

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