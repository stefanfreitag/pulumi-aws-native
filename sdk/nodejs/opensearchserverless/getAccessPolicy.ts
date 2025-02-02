// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Amazon OpenSearchServerless access policy resource
 */
export function getAccessPolicy(args: GetAccessPolicyArgs, opts?: pulumi.InvokeOptions): Promise<GetAccessPolicyResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:opensearchserverless:getAccessPolicy", {
        "name": args.name,
        "type": args.type,
    }, opts);
}

export interface GetAccessPolicyArgs {
    /**
     * The name of the policy
     */
    name: string;
    type: enums.opensearchserverless.AccessPolicyType;
}

export interface GetAccessPolicyResult {
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
 * Amazon OpenSearchServerless access policy resource
 */
export function getAccessPolicyOutput(args: GetAccessPolicyOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAccessPolicyResult> {
    return pulumi.output(args).apply((a: any) => getAccessPolicy(a, opts))
}

export interface GetAccessPolicyOutputArgs {
    /**
     * The name of the policy
     */
    name: pulumi.Input<string>;
    type: pulumi.Input<enums.opensearchserverless.AccessPolicyType>;
}
