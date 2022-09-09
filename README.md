# Hello world docker action

This action a small Github Actions to send metrics in pipelines to [Prometheus](https://github.com/prometheus/prometheus) through [Pushgateway](https://github.com/prometheus/pushgateway).

## Inputs

## `pushgateway_url`

**Required** URL of your Pushgateway. Default `"http://localhost:9091/"`.

## `job`

**Required** Job Name. Default `"JobA"`.

## `metric_name`

**Required** The name of the metric you want to create/update. Default `"new_metric"`.

## `metric_description`

**Required** The description of the metric you want to create/update. Default `"metric description"`.

## `metric_labels`

**Required** he list of labels for your metric. Default `"{'version': '1.0'}"`.

## Example usage

```
uses: cirolini/hello-world-docker-action@v1
with:
  pushgateway_url: 'https://31dd-189-6-240-216.sa.ngrok.io/'
  job: "JobB"
  metric_name: "github_action_pushgateway"
  metric_description: "Test on github actions push metrics to Prometheus Pushgateway"
  metric_labels: "{'version': '1.0'}"
```
