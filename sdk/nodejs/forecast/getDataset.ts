// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type Definition for AWS::Forecast::Dataset
 */
export function getDataset(args: GetDatasetArgs, opts?: pulumi.InvokeOptions): Promise<GetDatasetResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:forecast:getDataset", {
        "arn": args.arn,
    }, opts);
}

export interface GetDatasetArgs {
    arn: string;
}

export interface GetDatasetResult {
    readonly arn?: string;
    /**
     * Frequency of data collection. This parameter is required for RELATED_TIME_SERIES
     */
    readonly dataFrequency?: string;
    /**
     * The dataset type
     */
    readonly datasetType?: enums.forecast.DatasetType;
    /**
     * The domain associated with the dataset
     */
    readonly domain?: enums.forecast.DatasetDomain;
    readonly encryptionConfig?: outputs.forecast.EncryptionConfigProperties;
    readonly schema?: outputs.forecast.SchemaProperties;
    readonly tags?: outputs.Tag[];
}
/**
 * Resource Type Definition for AWS::Forecast::Dataset
 */
export function getDatasetOutput(args: GetDatasetOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDatasetResult> {
    return pulumi.output(args).apply((a: any) => getDataset(a, opts))
}

export interface GetDatasetOutputArgs {
    arn: pulumi.Input<string>;
}
