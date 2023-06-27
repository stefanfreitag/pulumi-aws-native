// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::Personalize::Schema.
 */
export function getSchema(args: GetSchemaArgs, opts?: pulumi.InvokeOptions): Promise<GetSchemaResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:personalize:getSchema", {
        "schemaArn": args.schemaArn,
    }, opts);
}

export interface GetSchemaArgs {
    /**
     * Arn for the schema.
     */
    schemaArn: string;
}

export interface GetSchemaResult {
    /**
     * Arn for the schema.
     */
    readonly schemaArn?: string;
}
/**
 * Resource schema for AWS::Personalize::Schema.
 */
export function getSchemaOutput(args: GetSchemaOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSchemaResult> {
    return pulumi.output(args).apply((a: any) => getSchema(a, opts))
}

export interface GetSchemaOutputArgs {
    /**
     * Arn for the schema.
     */
    schemaArn: pulumi.Input<string>;
}
