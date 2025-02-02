// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ServiceCatalog::StackSetConstraint
 */
export function getStackSetConstraint(args: GetStackSetConstraintArgs, opts?: pulumi.InvokeOptions): Promise<GetStackSetConstraintResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:servicecatalog:getStackSetConstraint", {
        "id": args.id,
    }, opts);
}

export interface GetStackSetConstraintArgs {
    id: string;
}

export interface GetStackSetConstraintResult {
    readonly acceptLanguage?: string;
    readonly accountList?: string[];
    readonly adminRole?: string;
    readonly description?: string;
    readonly executionRole?: string;
    readonly id?: string;
    readonly regionList?: string[];
    readonly stackInstanceControl?: string;
}
/**
 * Resource Type definition for AWS::ServiceCatalog::StackSetConstraint
 */
export function getStackSetConstraintOutput(args: GetStackSetConstraintOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetStackSetConstraintResult> {
    return pulumi.output(args).apply((a: any) => getStackSetConstraint(a, opts))
}

export interface GetStackSetConstraintOutputArgs {
    id: pulumi.Input<string>;
}
