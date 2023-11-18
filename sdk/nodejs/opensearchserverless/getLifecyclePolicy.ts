// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Amazon OpenSearchServerless lifecycle policy resource
 */
export function getLifecyclePolicy(args: GetLifecyclePolicyArgs, opts?: pulumi.InvokeOptions): Promise<GetLifecyclePolicyResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:opensearchserverless:getLifecyclePolicy", {
        "name": args.name,
        "type": args.type,
    }, opts);
}

export interface GetLifecyclePolicyArgs {
    /**
     * The name of the policy
     */
    name: string;
    type: enums.opensearchserverless.LifecyclePolicyType;
}

export interface GetLifecyclePolicyResult {
    /**
     * The description of the policy
     */
    readonly description?: string;
    /**
     * The JSON policy document that is the content for the policy
     */
    readonly policy?: string;
}
/**
 * Amazon OpenSearchServerless lifecycle policy resource
 */
export function getLifecyclePolicyOutput(args: GetLifecyclePolicyOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetLifecyclePolicyResult> {
    return pulumi.output(args).apply((a: any) => getLifecyclePolicy(a, opts))
}

export interface GetLifecyclePolicyOutputArgs {
    /**
     * The name of the policy
     */
    name: pulumi.Input<string>;
    type: pulumi.Input<enums.opensearchserverless.LifecyclePolicyType>;
}
