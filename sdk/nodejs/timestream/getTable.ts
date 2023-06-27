// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::Timestream::Table resource creates a Timestream Table.
 */
export function getTable(args: GetTableArgs, opts?: pulumi.InvokeOptions): Promise<GetTableResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:timestream:getTable", {
        "databaseName": args.databaseName,
        "tableName": args.tableName,
    }, opts);
}

export interface GetTableArgs {
    /**
     * The name for the database which the table to be created belongs to.
     */
    databaseName: string;
    /**
     * The name for the table. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the table name.
     */
    tableName: string;
}

export interface GetTableResult {
    readonly arn?: string;
    /**
     * The properties that determine whether magnetic store writes are enabled.
     */
    readonly magneticStoreWriteProperties?: outputs.timestream.MagneticStoreWritePropertiesProperties;
    /**
     * The table name exposed as a read-only attribute.
     */
    readonly name?: string;
    /**
     * The retention duration of the memory store and the magnetic store.
     */
    readonly retentionProperties?: outputs.timestream.RetentionPropertiesProperties;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.timestream.TableTag[];
}
/**
 * The AWS::Timestream::Table resource creates a Timestream Table.
 */
export function getTableOutput(args: GetTableOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTableResult> {
    return pulumi.output(args).apply((a: any) => getTable(a, opts))
}

export interface GetTableOutputArgs {
    /**
     * The name for the database which the table to be created belongs to.
     */
    databaseName: pulumi.Input<string>;
    /**
     * The name for the table. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the table name.
     */
    tableName: pulumi.Input<string>;
}
