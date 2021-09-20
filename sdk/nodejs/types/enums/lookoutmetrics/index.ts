// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const AnomalyDetectorAnomalyDetectorFrequency = {
    Pt5m: "PT5M",
    Pt10m: "PT10M",
    Pt1h: "PT1H",
    P1d: "P1D",
} as const;

/**
 * Frequency of anomaly detection
 */
export type AnomalyDetectorAnomalyDetectorFrequency = (typeof AnomalyDetectorAnomalyDetectorFrequency)[keyof typeof AnomalyDetectorAnomalyDetectorFrequency];

export const AnomalyDetectorCsvFormatDescriptorFileCompression = {
    None: "NONE",
    Gzip: "GZIP",
} as const;

export type AnomalyDetectorCsvFormatDescriptorFileCompression = (typeof AnomalyDetectorCsvFormatDescriptorFileCompression)[keyof typeof AnomalyDetectorCsvFormatDescriptorFileCompression];

export const AnomalyDetectorJsonFormatDescriptorFileCompression = {
    None: "NONE",
    Gzip: "GZIP",
} as const;

export type AnomalyDetectorJsonFormatDescriptorFileCompression = (typeof AnomalyDetectorJsonFormatDescriptorFileCompression)[keyof typeof AnomalyDetectorJsonFormatDescriptorFileCompression];

export const AnomalyDetectorMetricAggregationFunction = {
    Avg: "AVG",
    Sum: "SUM",
} as const;

/**
 * Operator used to aggregate metric values
 */
export type AnomalyDetectorMetricAggregationFunction = (typeof AnomalyDetectorMetricAggregationFunction)[keyof typeof AnomalyDetectorMetricAggregationFunction];

export const AnomalyDetectorMetricSetMetricSetFrequency = {
    Pt5m: "PT5M",
    Pt10m: "PT10M",
    Pt1h: "PT1H",
    P1d: "P1D",
} as const;

/**
 * A frequency period to aggregate the data
 */
export type AnomalyDetectorMetricSetMetricSetFrequency = (typeof AnomalyDetectorMetricSetMetricSetFrequency)[keyof typeof AnomalyDetectorMetricSetMetricSetFrequency];
