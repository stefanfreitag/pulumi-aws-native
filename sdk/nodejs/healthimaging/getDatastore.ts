// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of AWS::HealthImaging::Datastore Resource Type
 */
export function getDatastore(args: GetDatastoreArgs, opts?: pulumi.InvokeOptions): Promise<GetDatastoreResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:healthimaging:getDatastore", {
        "datastoreId": args.datastoreId,
    }, opts);
}

export interface GetDatastoreArgs {
    datastoreId: string;
}

export interface GetDatastoreResult {
    readonly createdAt?: string;
    readonly datastoreArn?: string;
    readonly datastoreId?: string;
    readonly datastoreStatus?: enums.healthimaging.DatastoreStatus;
    readonly updatedAt?: string;
}
/**
 * Definition of AWS::HealthImaging::Datastore Resource Type
 */
export function getDatastoreOutput(args: GetDatastoreOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDatastoreResult> {
    return pulumi.output(args).apply((a: any) => getDatastore(a, opts))
}

export interface GetDatastoreOutputArgs {
    datastoreId: pulumi.Input<string>;
}
