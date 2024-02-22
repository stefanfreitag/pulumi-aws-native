// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Connect::UserHierarchyGroup
 */
export function getUserHierarchyGroup(args: GetUserHierarchyGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetUserHierarchyGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:connect:getUserHierarchyGroup", {
        "userHierarchyGroupArn": args.userHierarchyGroupArn,
    }, opts);
}

export interface GetUserHierarchyGroupArgs {
    /**
     * The Amazon Resource Name (ARN) for the user hierarchy group.
     */
    userHierarchyGroupArn: string;
}

export interface GetUserHierarchyGroupResult {
    /**
     * The identifier of the Amazon Connect instance.
     */
    readonly instanceArn?: string;
    /**
     * The name of the user hierarchy group.
     */
    readonly name?: string;
    /**
     * One or more tags.
     */
    readonly tags?: outputs.Tag[];
    /**
     * The Amazon Resource Name (ARN) for the user hierarchy group.
     */
    readonly userHierarchyGroupArn?: string;
}
/**
 * Resource Type definition for AWS::Connect::UserHierarchyGroup
 */
export function getUserHierarchyGroupOutput(args: GetUserHierarchyGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetUserHierarchyGroupResult> {
    return pulumi.output(args).apply((a: any) => getUserHierarchyGroup(a, opts))
}

export interface GetUserHierarchyGroupOutputArgs {
    /**
     * The Amazon Resource Name (ARN) for the user hierarchy group.
     */
    userHierarchyGroupArn: pulumi.Input<string>;
}
