// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of AWS::IoTFleetWise::SignalCatalog Resource Type
 */
export function getSignalCatalog(args: GetSignalCatalogArgs, opts?: pulumi.InvokeOptions): Promise<GetSignalCatalogResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:iotfleetwise:getSignalCatalog", {
        "name": args.name,
    }, opts);
}

export interface GetSignalCatalogArgs {
    name: string;
}

export interface GetSignalCatalogResult {
    readonly arn?: string;
    readonly creationTime?: string;
    readonly description?: string;
    readonly lastModificationTime?: string;
    readonly nodeCounts?: outputs.iotfleetwise.SignalCatalogNodeCounts;
    readonly nodes?: outputs.iotfleetwise.SignalCatalogNode[];
    readonly tags?: outputs.iotfleetwise.SignalCatalogTag[];
}
/**
 * Definition of AWS::IoTFleetWise::SignalCatalog Resource Type
 */
export function getSignalCatalogOutput(args: GetSignalCatalogOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSignalCatalogResult> {
    return pulumi.output(args).apply((a: any) => getSignalCatalog(a, opts))
}

export interface GetSignalCatalogOutputArgs {
    name: pulumi.Input<string>;
}
